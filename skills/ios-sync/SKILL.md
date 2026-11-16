---
name: ios-sync
description: "Проверить и регенерировать DebugBridge существующим companion при изменении observable state или версии."
---

# Синхронизировать iOS DebugBridge

Результат: Согласованные generated accessors/schema без изменения business state.

## Runtime rcode

Инструменты: `read_file`, `search`, `list_files`; запись — `write_file` (в разрешённом корне создаёт подкаталоги при поддержке в схеме `write_file`) и `edit_file` (без `N\t`; крупные замены — `write_file` после `read_file`; обе записи обновляют снимок без перечитывания), shell — `run_command`/`start_command`, план — `update_plan`. В `/plan` и `explorer`/`reviewer` нет shell/записи; субагенты (`explorer`/`reviewer`/`worker`) без `ask_user`, памяти и `load_skill` (`wait_agent`).

Скилл не даёт прав: соблюдай approvals, mid-turn уточнения (не дают прав; `/btw` вне истории) и ОС-песочницу (`--sandbox`, `/sandbox`; в `--sandbox read-only` shell пишет лишь в `TMPDIR`), hooks нет. Публикация и внешний LLM/API — по выбору без fallback. Ключи не в args/логи/память/shell; на `localhost`/`127.0.0.1`/`[::1]` — заглушки без секретов, PEM, `sk-`/`ghp_` и `user:pass@`.

Поиск/HTTP — `web_search`/`web_fetch` (не браузер). Развилки в интерактиве — `ask_user` (1–3 вопроса, 2–4 варианта, 1-й рек., без повтора, не права/секреты), иначе текстом. `<rcode_compaction>` и `read_memory` — историческая справка (сверяй с файлами); `write_memory` — только интерактивному основному агенту вне `/plan` для `[stated]` без секретов (иначе текстом).

## Условия

Нужны macOS, Xcode, исходники приложения, выбранное доверенное iOS-устройство и уже установленный companion bridge/daemon. Проверяй фактический CLI help, подключение и Debug-конфигурацию до изменения приложения; без них не объявляй device-проверку выполненной.

- Установленный gstack-ios-qa-regen, app source и Swift toolchain проекта.

## Порядок работы

1. Прочитай app source и текущую метку/manifest установленного DebugBridge; проверь Swift/runtime/tool versions.
2. Найди установленный gstack-ios-qa-regen и прочитай его help; отсутствие генератора — конкретный blocker, а не повод писать несовместимый bridge вручную.
3. Определи app-source и bridge-dir; сохрани пользовательские изменения и убедись, что обновляется только известный generated output.
4. Запусти подтверждённую команду regen в разрешённом scope; не удаляй произвольные похожие файлы.
5. Проверь generated diff, schema/hash и source build.
6. Переподключи daemon и получи новый snapshot; при schema mismatch не восстанавливай старое состояние.
7. Отчитайся, был ли это cache no-op, реальная регенерация или blocked step.

## Обязательный чеклист результата

- Generated diff соответствует текущим observable классам и версии генератора.
- Business fields и пользовательский исходный код не изменены как побочный эффект.

## Материалы и завершение

Вход самодостаточен. Supporting files открывай только по точным путям из `resources` ответа `load_skill`; не придумывай имена и не ищи `../` вне скилла. При усечении продолжай по `next_line` с тем же `sha256`.

Обязательный чеклист приведён выше; [развёрнутые критерии и сценарии](references/acceptance.md) — дополнительная справка. [Происхождение](references/upstream.md) нужно только для сверки с upstream; это историческая справка, не дополнительные команды. Не загружай все материалы без причины.

Укажи выполненное, доказательства, оставшееся и блокеры. Для блокера назови недостающее предусловие и один выполнимый следующий шаг; не повторяй одинаковый preflight. Отделяй проверенное от `blocked`/`untested`.
