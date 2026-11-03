# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/gstack-upgrade/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `gstack-upgrade/SKILL.md`; SHA-256: `a2c7925b29b5cd659c8c208272aa7f60298ae0d77a37baffe9cb9aa1a9c97c32`.
- Семейство runtime: `release`.

## Индекс этапов исходного workflow

- Step 1: Ask the user (or auto-upgrade)
- Step 2: Detect install type
- Step 3: Save old version
- Step 4: Upgrade
- Step 4.5: Handle local vendored copy
- Step 4.75: Run version migrations
- Step 4.8: Stop any stale daemon (unconditional)
- Step 5: Write marker + clear cache
- Step 6: Show What's New
- Step 7: Continue

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
