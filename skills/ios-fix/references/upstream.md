# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/ios-fix/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `ios-fix/SKILL.md`; SHA-256: `bffd31d8797f855e762398bb0ae485fdea709bb824a7012547fecf2302279951`.
- Семейство runtime: `ios`.

## Индекс этапов исходного workflow

- Phase 1: Reproduce the bug
- Phase 2: Locate root cause
- Phase 3: Apply fix
- Phase 4: Verify
- Phase 5: Add regression test
- Failure modes

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
