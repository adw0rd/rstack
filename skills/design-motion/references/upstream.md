# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/design-motion/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `design-motion/SKILL.md`; SHA-256: `d56b42c14108f00e2455ef4f2e4e1967d49d8e8bfc29e69cd1d1b052be611f84`.
- Семейство runtime: `design`.

## Индекс этапов исходного workflow

- Step 0: Setup and source detection
- Step 1: Intake and the motion plan
- Step 2: Rebuild the exact frame
- Step 3: Verify the still
- Step 4: Motion
- Step 5: Capture
- Step 6: Motion checks (before any export)
- Step 7: Export and report

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
