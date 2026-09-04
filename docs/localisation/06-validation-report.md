# Localisation Validation Report

**Date:** 2026-09-04
**Branch:** `australian-localisation`
**Scope:** Deterministic Tasks 7-11 validation after Australian/Queensland localisation.

## Deterministic Results

| Check | Result | Evidence |
| --- | --- | --- |
| Localisation pytest suite | PASS | `python3 -m pytest tests/localisation -q` → `18 passed` |
| Contract validator | PASS | `python3 scripts/validate_localisation.py` → `Total failing checks: 0` |
| Offline curriculum lookup | PASS | F-10 Mathematics found; QCAA Legal Studies found; unknown subject returns explicit `not-found` |
| Old skill directories | PASS | No `plugin/skills/k12-*` directories |
| Old eval directories | PASS | No `evals/k12-*` directories |
| QCAA eval coverage | PASS | 78 `evals/fixtures/qcaa/**/source-fixture.json` files |
| Replacement matrix coverage | PASS (draft) | 245 `US-####` rows |
| Accepted source register | PASS | 390 authority-verified records; 1 unsupported French MP3 record rejected |

## Implemented Work

- Task 7: deterministic localisation contract tests, preserved historical RED report and current green report.
- Task 8: portable offline curriculum lookup adapter; uncited/fabricated codes return `not-found` rather than a synthetic identifier.
- Task 9: breaking renames and localisation of all four skills.
- Task 10: Australian plugin metadata, migration guide, and source/version policy.
- Task 11: Australian eval directory renames, crosswalk, F-10 fixtures, and one QCAA source-alignment fixture per current subject.
- Task 13: ranked proposal-only new-skill opportunities.

## Remaining Human Gates

The user authorised reduced human-gate strictness for deterministic Tasks 7-11. That does not remove release review requirements:

1. A Queensland curriculum-qualified reviewer must complete and approve the pending replacement-matrix mappings, especially `partial`, `contextual`, and `no-equivalent` entries.
2. A Queensland curriculum-qualified reviewer must review terminology and jurisdictional source use in shipped behaviour, including an F-10 case and the QCAA Business/Food & Nutrition cases.
3. Model-matrix behavioural evaluations, renderer smoke tests, and visual HTML/DOCX inspection remain release tasks.
4. Task 13 recommendations are proposal-only and require reviewer approval before a separate skill-creation project.

## Task 12 Verification Harnesses (added 2026-09-04)

- `scripts/render_smoke.sh` + `tests/localisation/test_render_smoke.py`: deterministic render smoke for F-10 Maths, QCAA Business, QCAA Food & Nutrition. HTML outputs verified; `.docx` produced when `python-docx` is available, otherwise recorded as a documented fallback rather than a hard failure. `6 passed`.
- `scripts/evaluate_localisation.py` + `docs/localisation/validation/model-eval-harness.md`: model-matrix evaluation harness. Reads `eval-crosswalk.csv`, covers all required scenario families (F-10, Mathematics CFU, EAL/D differentiation, Business, Food & Nutrition, 78-subject source alignment, ambiguity, invalid/superseded code, no connector), reports per-criterion pass rates, and drives gating from the crosswalk.
  - **Gating rule:** no criterion with `mapping_status != approved` or unconfirmed required authority may pass. Currently **102 criteria are gated pending the Queensland curriculum reviewer sign-off**.
  - Dry-run `--no-exec` result:
    ```
    OVERALL: NOT RELEASED — pending Queensland curriculum reviewer sign-off (102 criteria)
    ```
  - Live model inference is wired via the documented `run_model_evaluation()` stub hook.

## Known Limits

- The replacement matrix is an authority-source-backed draft scaffold. Pending mapping rows deliberately have no synthetic source IDs.
- The offline lookup adapter only resolves bundled ACARA/QCAA manifests. Missing subjects return explicit `not-found` and require a teacher-provided official code/URL or direct official-source citation.
- Historical RED evidence remains at `docs/localisation/validation/baseline-red.md`; current green output is `docs/localisation/validation/current-validation.md`.
