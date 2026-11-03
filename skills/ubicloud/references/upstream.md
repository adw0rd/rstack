# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/ubicloud/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `ubicloud/SKILL.md`; SHA-256: `e1cff691e87b18023700706f9cf6f0781e849c4e3be72f9cfb5c49dd36cf32df`.
- Семейство runtime: `external`.

## Индекс этапов исходного workflow

- Step 0: Prerequisites (set/unset only)
- Step 1: Preflight the project
- Step 2: Launch watched, with a TTL that covers the run
- Step 3: One committed verify per repository
- Step 4: Read the result
- Resume checklist after a wake or a machine swap

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
