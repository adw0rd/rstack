# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/scrape/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `scrape/SKILL.md`; SHA-256: `79fd2bc6d9ba1f816f9200a747bbecd3c3a00abad59420e8b217f6d678c15b8f`.
- Семейство runtime: `browser`.

## Индекс этапов исходного workflow

- Plan Mode Safe Operations
- BROWSER SETUP (Aside — run this check BEFORE any browser step)
- Translate the Aside scripts step by step
- Step 1 — Determine intent
- Step 2 — Refuse mutating intents
- Step 3 — Read the page
- Output discipline
- Capture Learnings

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
