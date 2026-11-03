# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/benchmark-models/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `benchmark-models/SKILL.md`; SHA-256: `1e6e984507b3d12aeb8542446f08889f9576fdeff79694725e43c5d29db1f32d`.
- Семейство runtime: `external`.

## Индекс этапов исходного workflow

- Plan Mode Safe Operations
- /benchmark-models — Cross-Model Skill Benchmark
- Step 0: Locate the binary
- Step 1: Choose a prompt
- Step 2: Choose providers
- Step 3: Decide on judge
- Step 4: Run the benchmark
- Step 5: Interpret results
- Step 6: Offer to save results

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
