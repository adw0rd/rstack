# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/skillify/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `skillify/SKILL.md`; SHA-256: `9b250b0d29164facc978c87247f7c9cc4301c45ed57c19955e0102b3471a8b85`.
- Семейство runtime: `browser`.

## Индекс этапов исходного workflow

- Iron contract — never write a half-broken skill to disk
- Step 1 — Provenance guard (D1)
- Step 2 — Propose name + triggers
- Step 3 — Synthesize `script.ts` (D2)
- Step 4 — Capture the fixture
- Step 5 — Write `script.test.ts`
- Step 6 — Resolve the canonical SDK path + read it
- Step 7 — Stage the skill (D3 atomic write)
- Step 8 — Run `$B skill test` against the staged dir
- Step 9 — Approval gate
- Step 10 — Commit (atomic) or discard
- Step 11 — Confirm + verify
- Capture Learnings

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
