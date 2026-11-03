# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/browse/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `browse/SKILL.md`; SHA-256: `ae6707dbc37d2a4638f8d8021800a486b2e1edd09909b85ebc189dc5d1466105`.
- Семейство runtime: `browser`.

## Индекс этапов исходного workflow

- Plan Mode Safe Operations
- BROWSER SETUP (Aside — run this check BEFORE any browser step)
- Translate the Aside scripts step by step
- Pick the mode
- Report

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
