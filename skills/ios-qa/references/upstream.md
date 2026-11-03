# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/ios-qa/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `ios-qa/SKILL.md`; SHA-256: `f8df2f01eac150b8b0446dccc344ca0e1e8e401550f974986311ee52d548eb00`.
- Семейство runtime: `ios`.

## Индекс этапов исходного workflow

- Architecture
- Prerequisites
- Phase 1: Read source, plan codegen
- Phase 2: Bootstrap the device bridge
- Phase 3: Vision-driven agent loop
- Modes
- Demo mode
- Failure modes + recovery
- Cleanup

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
