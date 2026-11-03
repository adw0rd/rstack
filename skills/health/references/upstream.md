# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/health/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `health/SKILL.md`; SHA-256: `dc18a0ae204f2c80e3d61f07bc202ec60acef3697b8cd4394c8145965884e19c`.
- Семейство runtime: `review`.

## Индекс этапов исходного workflow

- Step 1: Detect Health Stack
- Step 2: Run Tools
- Step 3: Score Each Category
- Step 4: Present Dashboard
- Step 5: Persist to Health History
- Step 6: Trend Analysis + Recommendations

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
