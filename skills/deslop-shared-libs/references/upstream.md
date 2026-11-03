# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/deslop-shared-libs/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `deslop-shared-libs/SKILL.md`; SHA-256: `13298bd1becd17b16b859775fad952754c3e870f4c0f44a2f39d05cd70af30b4`.
- Семейство runtime: `review`.

## Индекс этапов исходного workflow

- Scope and read-only boundary
- Establish the reviewed source
- Check work already underway
- Output

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
