# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/autoplan/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `autoplan/SKILL.md`; SHA-256: `c3148676e5fc378bd6b10a54c9227b0c4ed94732bee9ae6d4e2eb78b4a045d1e`.
- Семейство runtime: `planning`.

## Индекс этапов исходного workflow

- Step 0: Detect platform and base branch
- Design Doc Check
- Prerequisite Skill Offer
- /autoplan — Auto-Review Pipeline
- Phase 0: Intake + Restore Point
- Step 1: Capture restore point
- Step 2: Read context
- Step 3: Locate review skills; load each at phase entry
- Phase 0.5: Outside reviewer preflight
- Phase 1: CEO Review (Strategy & Scope)
- Phase 2: Design Review (conditional — skip if no UI scope)
- Phase 2.5: DX Review (conditional — skip if no developer-facing scope)
- Phase 4: Final Approval Gate
- Completion: Write Review Logs

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
