# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/ios-sync/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `ios-sync/SKILL.md`; SHA-256: `70b38c465123646b2a4bbf019a1e064a70992de257bddb7e90684c0c1f91605d`.
- Семейство runtime: `ios`.

## Индекс этапов исходного workflow

- Phase 1: Detect installed version
- Phase 2: Regenerate codegen output
- Phase 3: Review the generated diff
- Phase 4: Verify
- Failure modes

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
