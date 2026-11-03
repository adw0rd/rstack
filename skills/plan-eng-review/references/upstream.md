# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/plan-eng-review/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `plan-eng-review/SKILL.md`; SHA-256: `45013d684e82a92c65906eb40cf24084faf8c45cd403918d80e2a5764f226559`.
- Семейство runtime: `planning`.

## Индекс этапов исходного workflow

- Plan Review Mode
- Scope gate (FIRST — overrides everything below). This is a hard STOP.
- Self-check before emitting
- Design Doc Check
- Prerequisite Skill Offer
- Engineering review
- Step 0: Scope Challenge
- Section self-check (before you finish)

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
