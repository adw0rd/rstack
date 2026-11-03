# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/context-save/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `context-save/SKILL.md`; SHA-256: `8c9a48775c1dc0a2c6be3b2bc74e6d70b795019c8fb1852e877bfb2a3315fc7a`.
- Семейство runtime: `context`.

## Индекс этапов исходного workflow

- Step 1: Gather state
- Step 2: Summarize context
- Step 4: Write saved-context file
- Step 1: Gather saved contexts
- Step 2: Display table

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
