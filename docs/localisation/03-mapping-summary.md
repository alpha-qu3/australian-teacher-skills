# Task 6 Mapping Summary (Draft)

**Status:** Scaffold for Queensland curriculum reviewer completion. No `partial`/`contextual`/`no-equivalent` mapping is approved for shipped behaviour until the Queensland curriculum-qualified human reviewer signs off.

## Inputs
- `01-us-specific-inventory.csv`: 245 US-specific inventory rows (US-0001..US-0245).
- `02-source-register.csv`: 390 authority-verified source records (377 QCAA + 14 ACARA) with stable `SRC-####` IDs.
- `02-rejected-sources.csv`: 1 rejected record (French MP3 audio stimulus, placeholder hash).
- `04-gap-register.csv`: unmatched curriculum functions (misconception library, progressions, HQIM, curriculum search, adjustment/EAL-D).

## Approach
- Apply the plan's default terminology rules only where context supports them:
  - `K-12` → `F-12`; `K-5` → `F-6`
  - `kindergarten` → `Prep` (Queensland)
  - `ELA` → `English`
  - `social studies` → `HASS` (F-10) or named QCAA senior subject
  - `math` → `Mathematics`
  - `grade` → `year level`
- Rows to which no default applies are marked `pending` and require an authority-verified mapping against `02-source-register` before use.

## Reviewer gate
- Human gate (gate cannot be self-signed on `partial/contextual/no-equivalent` rows or the release).
- Reviewer decision column is `pending` until sign-off.

## Status
- Source register: built, schema-validated.
- Matrix scaffold: 245 rows; a subset auto-classified `contextual` via the default rules; remainder `pending`.
- Pending rows intentionally have empty `source_ids` until a human mapping review assigns actual `SRC-####` references from the source register.
