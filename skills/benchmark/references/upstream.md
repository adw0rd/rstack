# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/benchmark/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `benchmark/SKILL.md`; SHA-256: `15ac49f4a6b948fac2c9af6b5cda9f688ddc1f2ca7d77143c0e3cf36ffcd5026`.
- Семейство runtime: `qa`.

## Индекс этапов исходного workflow

- Plan Mode Safe Operations
- BROWSER SETUP (Aside — run this check BEFORE any browser step)
- Translate the Aside scripts step by step
- Phase 1: Setup
- Phase 2: Page Discovery
- Phase 3: Performance Data Collection
- Phase 4: Baseline Capture (--baseline mode)
- Phase 5: Comparison
- Phase 6: Slowest Resources
- Phase 7: Performance Budget
- Phase 8: Trend Analysis (--trend mode)
- Phase 9: Save Report

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
