# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/make-pdf/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `make-pdf/SKILL.md`; SHA-256: `7378d92b5142de4f05ff3b40b4766116194a3c0bea43e12cf8a44416baf356c9`.
- Семейство runtime: `docs`.

## Индекс этапов исходного workflow

- MAKE-PDF SETUP (run this check BEFORE any make-pdf command)
- Plan Mode Safe Operations
- Publication mode — cover + TOC + chapter breaks
- Fast iteration via preview
- CI mode — fail loud on missing assets
- Output contract

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
