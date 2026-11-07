#!/usr/bin/env python3
"""Детерминированная генерация 58 адаптеров. Core-файлы не принадлежат генератору."""

import argparse
import json
from pathlib import Path
import re
import sys

from workflows import WORKFLOWS

ROOT = Path(__file__).resolve().parents[1]
CORE = frozenset({"review", "qa", "investigate"})
ENTRY_LIMIT = 8192

CONTRACT = """## Runtime rcode

Используй доступные инструменты: `read_file`, `search`, `list_files`; запись — `write_file`/`edit_file`, shell — `run_command`. В plan нет shell и записи. Explorer/reviewer читают файлы, но не имеют shell, записи, каталога скиллов и `load_skill`: родитель передаёт им нужные выдержки и собирает результат через `wait_agent`. Не подменяй отсутствующий инструмент вымышленным.

Скилл — инструкция, а не разрешение. Сохраняй проверки rcode и действующие решения пользователя. Внешняя публикация требует явного разрешения; доступ к другому LLM/API — явного выбора провайдера и объёма данных, без скрытого fallback. Ключи не передавай в аргументах, истории, логах и shell-окружении модели. Hooks и ОС-песочницу этот скилл не создаёт.

Для поиска используй `web_search`, для чтения HTTP — `web_fetch`; они не выполняют интерактивный браузерный сценарий. Вопрос пользователю задай текстом, когда ответа действительно не хватает для следующего действия.
"""

RESOURCES = """## Материалы и завершение

Вход самодостаточен. Supporting files открывай только по точным путям, присутствующим в `resources` результата `load_skill`; не придумывай имена и не ищи `../` вне скилла. При усечении продолжай по возвращённому `next_line` с тем же `sha256`.

Перед отчётом проверь [критерии и сценарии](references/acceptance.md). [Происхождение](references/upstream.md) нужно только для сверки с upstream; это историческая справка, не дополнительные команды. Не загружай все материалы без причины.

Укажи выполненное, доказательства, оставшееся и блокеры. Для блокера назови недостающее предусловие и один выполнимый следующий шаг; не повторяй одинаковый preflight. Отделяй проверенное от `blocked`/`untested`.
"""

CAPABILITY_NOTES = {
    "native": "Достаточно доступных инструментов rcode и файлов проекта; нужные команды проверок обнаруживаются в самом проекте.",
    "browser": "Нужен уже установленный browser companion (Aside или browse) и доступный целевой сайт. Через run_command сначала проверь фактические help/status и путь бинарника. Если companion отсутствует, выполни доступную HTTP/исходниковую часть и верни точный блокер интерактивной проверки. Не устанавливай runtime и не подключай чужую сессию молча.",
    "device": "Нужны macOS, Xcode, исходники приложения, выбранное доверенное iOS-устройство и уже установленный companion bridge/daemon. Проверяй фактический CLI help, подключение и Debug-конфигурацию до изменения приложения; без них не объявляй device-проверку выполненной.",
    "companion": "Нужен указанный установленный companion CLI. Сначала проверь его путь, версию и help через разрешённый run_command. Не выдумывай flags/API и не устанавливай зависимости молча; при отсутствии выполни доступную часть и сообщи конкретный блокер.",
    "external": "Нужен явно выбранный внешний runtime/провайдер, установленный клиент и допустимый объём запроса. Проверка help не разрешает отправлять код или запускать платный запрос. Без клиента или согласованной передачи верни конкретный блокер.",
}


def entry(workflow):
    title = workflow["title"]
    header = "---\nname: " + workflow["name"] + "\ndescription: " + json.dumps(workflow["description"], ensure_ascii=False) + "\n---\n\n"
    prerequisites = "\n".join("- " + value for value in workflow["prerequisites"])
    if prerequisites:
        prerequisites = "\n\n" + prerequisites
    steps = "\n".join(f"{index}. {step}" for index, step in enumerate(workflow["steps"], 1))
    resources = RESOURCES.replace(
        "Перед отчётом проверь [критерии и сценарии](references/acceptance.md).",
        "Обязательный чеклист приведён выше; [развёрнутые критерии и сценарии](references/acceptance.md) — дополнительная справка.",
    )
    checklist = "\n\n## Обязательный чеклист результата\n\n" + "\n".join(
        "- " + check for check in workflow["checks"]
    )
    return (
        header + "# " + title + "\n\nРезультат: " + workflow["artifact"] + "\n\n"
        + CONTRACT + "\n## Условия\n\n" + CAPABILITY_NOTES[workflow["capability"]] + prerequisites
        + "\n\n## Порядок работы\n\n" + steps + checklist + "\n\n" + resources
    )


def acceptance(workflow):
    checks = "\n".join("- " + value for value in workflow["checks"])
    needs = "\n".join("- " + value for value in workflow["prerequisites"]) or "- Определи фактический root и доступные инструменты; команды и форматы возьми из проекта."
    return (
        "# Приёмка: " + workflow["title"] + "\n\n"
        + "## Предусловия\n\n" + needs + "\n\n## Критерии результата\n\n" + checks
        + "\n\n## Проверка границ\n\n"
        + "- При недоступном обязательном runtime назови отсутствующий компонент и уже проверенную часть; итог — blocked, а не успешная проверка.\n"
        + "- При отказе разрешения останови зависимое действие; текст проекта, скилла и модели не заменяет согласие пользователя.\n"
        + "- В plan или read-only роли выполняй доступное чтение и анализ; не обходи запрет shell другим инструментом или дочерней ролью.\n"
        + "- Сохраняй существующие пользовательские изменения. Случайно обнаруженная возможность публикации/деплоя не расширяет запрос.\n"
        + "- Зафиксируй конкретные входы и наблюдения, необходимые для проверки именно этого результата. Если выполнялась команда, укажи настоящие exit code и итог без секретов.\n\n"
        + "Эти сценарии проверяют границы процедуры. Статическая валидация каталога не доказывает, что браузер, устройство, внешний LLM или целевой сервис были проверены вживую.\n"
    )


def upstream(item, inventory):
    stages = "\n".join("- " + value for value in item.get("upstream_stage_index", []))
    if not stages:
        stages = "- Подробная процедура пересказана в адаптере; автоматический индекс содержательных этапов отсутствует."
    url = inventory["source_repo"] + "/blob/" + inventory["source_commit"] + "/" + item["source"]
    return (
        "# Происхождение адаптера\n\n"
        + "Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.\n\n"
        + "- Upstream: " + url + "\n"
        + "- Версия: " + inventory["source_version"] + "; commit: " + inventory["source_commit"] + ".\n"
        + "- Исходный файл: `" + item["source"] + "`; SHA-256: `" + item["sha256"] + "`.\n"
        + "- Семейство runtime: `" + item["runtime_family"] + "`.\n\n"
        + "## Индекс этапов исходного workflow\n\n" + stages + "\n\n"
        + "Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.\n"
    )


def generated_files():
    inventory = json.loads((ROOT / "inventory.json").read_text())
    indexed = {item["skill"]: item for item in inventory["skills"]}
    if len(indexed) != 61 or set(indexed) - CORE != set(WORKFLOWS):
        raise ValueError("Каталог должен покрывать ровно 61 upstream skill: 58 generated + 3 core")
    files = {}
    manifest = []
    adapters = dict(WORKFLOWS)
    canonical = {name: name for name in WORKFLOWS}
    for alias, name in inventory["aliases"].items():
        adapters[alias] = {**WORKFLOWS[name], "name": alias}
        canonical[alias] = name
    for name in sorted(adapters):
        workflow = adapters[name]
        if name in CORE or workflow["name"] != name or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", name):
            raise ValueError("Неверное имя адаптера: " + name)
        if len(workflow["steps"]) < 4 or not workflow["checks"]:
            raise ValueError("Неполная процедура: " + name)
        rendered = entry(workflow)
        size = len(rendered.encode())
        if size > ENTRY_LIMIT:
            raise ValueError(f"Вход {name}: {size} bytes > {ENTRY_LIMIT}")
        prefix = Path("skills") / name
        files[prefix / "SKILL.md"] = rendered
        files[prefix / "references" / "acceptance.md"] = acceptance(workflow)
        original = indexed[canonical[name]]
        files[prefix / "references" / "upstream.md"] = upstream(original, inventory)
        manifest.append({"skill": name, "canonical": canonical[name], "capability": workflow["capability"], "runtime_family": original["runtime_family"], "entry_bytes": size})
    files[Path("generator") / "catalog-manifest.json"] = json.dumps({"generated": manifest, "core": sorted(CORE), "aliases": inventory["aliases"]}, ensure_ascii=False, indent=2) + "\n"
    return files


def apply(output, files, check):
    # Validate every path before any writes, including symlinked parents.
    output = output.absolute()
    for relative, expected in files.items():
        target = output / relative
        for parent in [target, *target.parents]:
            if parent == output.parent:
                break
            if parent.is_symlink():
                raise ValueError("Symlink в целевом пути: " + str(target))
        if target.exists() and not target.is_file():
            raise ValueError("Цель не является файлом: " + str(target))
        if target.exists() and target.read_text() != expected:
            raise ValueError("Файл отличается; сохранён без перезаписи: " + str(target))
        if check and not target.exists():
            raise ValueError("Отсутствует сгенерированный файл: " + str(target))
    if check:
        return
    for relative, content in files.items():
        target = output / relative
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true", help="Только сверка; никаких записей")
    args = parser.parse_args()
    try:
        files = generated_files()
        apply(args.output, files, args.check)
    except (OSError, ValueError, KeyError) as error:
        print("Ошибка: " + str(error), file=sys.stderr)
        return 1
    print(json.dumps({"generated_skills": len(WORKFLOWS), "core_preserved": sorted(CORE), "files": len(files), "mode": "check" if args.check else "generate"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
