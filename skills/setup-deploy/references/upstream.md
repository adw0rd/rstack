# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/setup-deploy/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `setup-deploy/SKILL.md`; SHA-256: `aefb84d754d8ccc19f1ee6b298b6e99e329af676c963f5847f80794209f05140`.
- Семейство runtime: `release`.

## Индекс этапов исходного workflow

- Step 1: Check existing configuration
- Step 2: Detect platform
- Step 3: Platform-specific setup
- Step 4: Write configuration
- Step 5: Verify
- Step 6: Summary

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
