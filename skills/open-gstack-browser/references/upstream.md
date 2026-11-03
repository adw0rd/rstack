# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/open-gstack-browser/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `open-gstack-browser/SKILL.md`; SHA-256: `2dd3227c8a8534415d5b4161bd9cf6ef5b542540e37d5d0e50dbb09b7eecbc10`.
- Семейство runtime: `browser`.

## Индекс этапов исходного workflow

- Plan Mode Safe Operations
- SETUP (run this check BEFORE any browse command)
- Step 0: Check for a running browse daemon
- Step 1: Connect
- Step 2: Verify
- Step 3: Guide the user to the Side Panel
- Step 4: Demo
- Step 5: Sidebar chat
- Step 6: What's next

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
