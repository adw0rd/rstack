# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/plan-design-review/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `plan-design-review/SKILL.md`; SHA-256: `fc2ff2246d4c38ceb6886aa2165c49a54097d59041a34d7e5c668007a8b86d72`.
- Семейство runtime: `planning`.

## Индекс этапов исходного workflow

- /plan-design-review: Designer's Eye Plan Review
- Scope gate (FIRST — overrides everything below). This is a hard STOP.
- Self-check before emitting
- Step 0: Detect platform and base branch
- PRE-REVIEW SYSTEM AUDIT (before Step 0)
- Retrospective Check
- UI Scope Detection
- DESIGN SETUP (run this check BEFORE any design mockup command)
- Step 0: Design Scope Assessment
- Step 0.5: Visual Mockups (DEFAULT when DESIGN_READY)
- Section self-check (before you finish)

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
