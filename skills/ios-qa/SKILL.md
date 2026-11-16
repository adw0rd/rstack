---
name: ios-qa
description: "Пройти реальный iOS-сценарий через существующий device bridge и собрать состояние и screenshots."
---

# Проверить iOS-приложение на устройстве

Результат: Подтверждённое поведение выбранного устройства и воспроизводимые findings.

## Runtime rcode

Инструменты: `read_file`, `search`, `list_files`; запись — `write_file` (в разрешённом корне создаёт подкаталоги при поддержке в схеме `write_file`) и `edit_file` (без `N\t`; крупные замены — `write_file` после `read_file`; обе записи обновляют снимок без перечитывания), shell — `run_command`/`start_command`, план — `update_plan`. В `/plan` и `explorer`/`reviewer` нет shell/записи; субагенты (`explorer`/`reviewer`/`worker`) без `ask_user`, памяти и `load_skill` (`wait_agent`).

Скилл не даёт прав: соблюдай approvals, mid-turn уточнения (не дают прав; `/btw` вне истории) и ОС-песочницу (`--sandbox`, `/sandbox`; в `--sandbox read-only` shell пишет лишь в `TMPDIR`), hooks нет. Публикация и внешний LLM/API — по выбору без fallback. Ключи не в args/логи/память/shell; на `localhost`/`127.0.0.1`/`[::1]` — заглушки без секретов, PEM, `sk-`/`ghp_` и `user:pass@`.

Поиск/HTTP — `web_search`/`web_fetch` (не браузер). Развилки в интерактиве — `ask_user` (1–3 вопроса, 2–4 варианта, 1-й рек., без повтора, не права/секреты), иначе текстом. `<rcode_compaction>` и `read_memory` — историческая справка (сверяй с файлами); `write_memory` — только интерактивному основному агенту вне `/plan` для `[stated]` без секретов (иначе текстом).

## Условия

Нужны macOS, Xcode, исходники приложения, выбранное доверенное iOS-устройство и уже установленный companion bridge/daemon. Проверяй фактический CLI help, подключение и Debug-конфигурацию до изменения приложения; без них не объявляй device-проверку выполненной.

- macOS, Xcode/devicectl, доверенное устройство и установленный gstack-ios-qa-daemon; для codegen — gstack-ios-qa-regen.

## Порядок работы

1. Определи app source, bundle ID, устройство и сценарий; при нескольких устройствах выбери конкретное.
2. Проверь macOS/Xcode, xcrun devicectl list devices, Swift и существующие gstack-ios-qa-daemon/regen companions по help.
3. При уже установленном bridge проверь schema/device identity и состояние приложения; debug StateServer не выставляй на публичный интерфейс.
4. Добавление или регенерацию DebugBridge выполняй только при разрешённой записи в app source и через подтверждённый companion.
5. Пройди flow: screenshot → состояние/действие → новая проверка. Не выдавай API-state за фактический tap/screenshot.
6. Проверь разрешённые tiers удалённого доступа отдельно; токены передаются только механизмом companion, без model transcript.
7. Запиши repro и cleanup; без device runtime выполни доступный source review и обозначь, какие live-device проверки заблокированы.

## Обязательный чеклист результата

- Сценарий выполнен на указанном UDID/bundle/revision.
- Bridge остаётся Debug-only; device/tunnel exposure не расширены самовольно.

## Материалы и завершение

Вход самодостаточен. Supporting files открывай только по точным путям из `resources` ответа `load_skill`; не придумывай имена и не ищи `../` вне скилла. При усечении продолжай по `next_line` с тем же `sha256`.

Обязательный чеклист приведён выше; [развёрнутые критерии и сценарии](references/acceptance.md) — дополнительная справка. [Происхождение](references/upstream.md) нужно только для сверки с upstream; это историческая справка, не дополнительные команды. Не загружай все материалы без причины.

Укажи выполненное, доказательства, оставшееся и блокеры. Для блокера назови недостающее предусловие и один выполнимый следующий шаг; не повторяй одинаковый preflight. Отделяй проверенное от `blocked`/`untested`.
