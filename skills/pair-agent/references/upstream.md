# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/pair-agent/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `pair-agent/SKILL.md`; SHA-256: `81bc6ef65aac67ab8e963c55599b447cf860a562a0f664e3218963c5f6742404`.
- Семейство runtime: `browser`.

## Индекс этапов исходного workflow

- SETUP (run this check BEFORE any browse command)
- Step 1: Check prerequisites
- Step 2: Ask what they want
- Step 3: Local or remote?
- Step 4: Execute pairing
- Step 5: Verify connection

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
