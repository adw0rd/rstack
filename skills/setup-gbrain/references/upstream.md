# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/setup-gbrain/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `setup-gbrain/SKILL.md`; SHA-256: `93a7a9a5f35eaf847688dd9740cbfbc24ef1e5c66109464a5e7eacbd51e1b83d`.
- Семейство runtime: `context`.

## Индекс этапов исходного workflow

- Step 1: Detect current state
- Step 1.5: Broken-local-engine remediation
- Step 1.7: Code-intelligence provider choice (Step 0 of indexing)
- Step 6: Per-remote policy (gated repo-import)
- Step 7.5: Transcript ingest consent
- Step 9: Smoke test
- Step 10: GREEN/YELLOW/RED verdict block (idempotent doctor output)

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
