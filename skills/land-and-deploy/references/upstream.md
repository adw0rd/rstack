# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/land-and-deploy/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `land-and-deploy/SKILL.md`; SHA-256: `224077c3b976ceea0046929dbc0c6c61ba591380ed3c7547262edbac148a51b8`.
- Семейство runtime: `release`.

## Индекс этапов исходного workflow

- BROWSER SETUP (Aside — run this check BEFORE any browser step)
- Translate the Aside scripts step by step
- Step 0: Detect platform and base branch
- Step 1: Pre-flight
- Step 1.5: First-run dry-run validation
- Step 2: Pre-merge checks
- Step 3: Wait for CI (if pending)
- Step 3.4: VERSION drift detection (workspace-aware ship)
- Step 6: Wait for deploy (if applicable)
- Strategy A: GitHub Actions workflow
- Common: Timing and failure handling
- Step 7: Canary verification (conditional depth)
- Step 8: Revert (if needed)
- Step 9: Deploy report
- Step 10: Suggest follow-ups
- Section self-check (before you finish)

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
