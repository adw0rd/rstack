# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/canary/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `canary/SKILL.md`; SHA-256: `44ac3d43728b022c6d0eced562405ed1d2f11f895ecf5a6f52620b08c593f590`.
- Семейство runtime: `qa`.

## Индекс этапов исходного workflow

- BROWSER SETUP (Aside — run this check BEFORE any browser step)
- Translate the Aside scripts step by step
- Step 0: Detect platform and base branch
- Phase 1: Setup
- Phase 2: Baseline Capture (--baseline mode)
- Phase 3: Page Discovery
- Phase 4: Pre-Deploy Snapshot (if no baseline exists)
- Phase 5: Continuous Monitoring Loop
- Phase 6: Health Report
- Phase 7: Baseline Update

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
