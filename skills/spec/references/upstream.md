# Происхождение адаптера

Производная адаптация gstack для runtime rcode. MIT, Copyright (c) 2026 Garry Tan; полный LICENSE находится в корне набора.

- Upstream: https://github.com/garrytan/gstack/blob/219f7488/spec/SKILL.md
- Версия: 1.91.292; commit: 219f7488.
- Исходный файл: `spec/SKILL.md`; SHA-256: `5df8c5e820729eca80266e4ca84966bf8d1e53dc6d8c6f00c935e764f7b83625`.
- Семейство runtime: `planning`.

## Индекс этапов исходного workflow

- Process (STRICT — do not skip or combine phases)
- Phase 1: Understand the "Why" (+ optional --dedupe)
- Phase 2: Scope and Boundaries
- Phase 3: Technical Interrogation (read code first)
- Phase 4: Draft Review
- Phases 4.5 and 5: Quality Gate, then File the Spec (sequencing summary)
- 8. Schema, API Shapes, and Data Models
- 10. Testable Acceptance Criteria
- 11. Testing Pyramid
- Audit / Cleanup Issues (routed via `--audit` flag)
- Section self-check (before you finish)

Индекс описывает происхождение и не является командой загрузить другие файлы. Сохранена задача и содержательные этапы; универсальные preamble, телеметрия, обязательное onboarding, host-specific hooks и дополнительные permissions не переносились. Конкретные runtime-действия задаёт локальный SKILL.md и доступный CLI help.
