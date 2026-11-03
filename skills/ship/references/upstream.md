# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/ship/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `ship/SKILL.md`; SHA-256: `ce360870f69502c524a028958c75c30dac989ba2789b0dbbe48a5e0d13c5a0ea`.
- Семейство runtime: `release`.

## Индекс этапов исходного workflow

- Ship: Fully Automated Ship Workflow
- Keep state between steps
- Step 0: Detect platform and base branch
- Step 0.9: Apple target detection
- Step 1: Pre-flight
- Review Readiness Dashboard
- Step 2: Distribution Pipeline Check
- Step 3: Merge the base branch (BEFORE tests)
- Step 11.5: Bind the reviews
- Step 12: Version bump (auto-decide)
- Step 14: TODOS.md (auto-update)
- Step 14.5: Documentation audit (every ship)
- Step 15: Commit (bisectable chunks)
- Step 16: Verification Gate
- 1. Finish writers and prepare outputs
- 5. Report, then push
- Step 17: Push
- Step 18: Prepare publication metadata

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
