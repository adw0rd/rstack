# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/design-review/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `design-review/SKILL.md`; SHA-256: `49e3d7b60a36a2a89b82e57a7f1bc8ba3db2e47fe5c2895da668fdf767fc6ba9`.
- Семейство runtime: `design`.

## Индекс этапов исходного workflow

- /design-review: Design Audit → Fix → Verify
- BROWSER SETUP (Aside — run this check BEFORE any browser step)
- Translate the Aside scripts step by step
- DESIGN SETUP (run this check BEFORE any design mockup command)
- Phases 1-6: Design Audit Baseline
- Modes
- Regression (`--regression` or previous `design-baseline.json` found)
- Phase 1: First Impression
- Phase 2: Design System Extraction
- Phase 3: Page-by-Page Visual Audit
- DOM dump (DOM mode only: Setup printed `IMPECCABLE_READY` and the target is a URL)
- Trunk Test (run on every page)
- Design Audit Checklist (10 categories, ~80 items)
- Phase 4: Interaction Flow Review
- Phase 5: Cross-Page Consistency
- Phase 6: Compile Report
- Baseline
- Regression Output

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
