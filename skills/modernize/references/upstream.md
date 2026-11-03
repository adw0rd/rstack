# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/modernize/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `modernize/SKILL.md`; SHA-256: `e410389ac99242c47d36fd7d82880192ecb64c3a9ae779bb760b55158dc0d82c`.
- Семейство runtime: `release`.

## Индекс этапов исходного workflow

- /modernize — Is this PR still worth landing?
- Step 1: Read the PR as a claim
- Step 2: What moved under it
- Step 3: The disposition
- Step 4 (MODERNIZE only): Rebase and prove intent survived
- Step 5 (MODERNIZE only): Push with a lease pinned to what you saw
- Step 6: Report

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
