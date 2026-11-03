# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/context-restore/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `context-restore/SKILL.md`; SHA-256: `c25a8b2b045f968ebaa53b8b9bfcdaf847a1d3f4c612559aec8d7ea312732e26`.
- Семейство runtime: `context`.

## Индекс этапов исходного workflow

- Step 1: Find saved contexts
- Step 2: Load the right file
- Step 3: Offer next steps

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
