# US-Specific Inventory Summary

## Overview

- **Shard counts**: Repository Content: 136, Tools & Scripts: 48, Eval: 61
- **Input rows**: 245 total
- **Canonical rows**: 245 (after dedup)
- **Dedup count**: 0 duplicates removed

## Deterministic ID Rule

Assigned gap-free sequential IDs `US-0001` through `US-0245` sorted bytewise by:
1. `path` (repository-relative path)
2. `line_or_section` (line range, heading, or locator)
3. `exact_text` (the US-specific phrase/code/assumption)

## Findings by Artifact Type

| Artifact Type | Count |
|---------------|-------|
| documentation | 9 |
| eval | 61 |
| plugin-metadata | 12 |
| reference | 120 |
| script | 6 |
| skill | 37 |

## Findings by Specificity Class

| Specificity Class | Count |
|-------------------|-------|
| eval-assumption | 30 |
| example | 19 |
| grade-band | 58 |
| law-policy | 8 |
| locale | 10 |
| standard | 63 |
| subject-label | 23 |
| tool-data | 34 |

## Evidence Status Distribution

| Evidence Status | Count |
|---------|-------|
| direct | 237 |
| inferred | 1 |
| needs-domain-review | 7 |

## Lexical Scan Results

Scanned for: K-12, grade bands, ELA, social studies, CCSS, NGSS, C3, WIDA, IEP, 504, Learning Commons, US spellings, measurements, dates

| Term | Occurrences |
|------|-------------|
| `K-12` | 16 |
| `K–5` | 1 |
| `grade` | 8 |
| `ELA` | 19 |
| `social studies` | 10 |
| `CCSS` | 20 |
| `NGSS` | 11 |
| `C3` | 4 |
| `WIDA` | 3 |
| `IEP` | 6 |
| `504` | 2 |
| `Learning Commons` | 3 |
| `behavior` | 5 |
| `TEKS` | 9 |
| `SOL` | 5 |
| `OAS` | 5 |
| `Lexile` | 5 |

## Downstream File Combinations

No duplicate `(path, line_or_section, exact_text)` entries were found across shards. Each line_or_section reference is unique.

## Validation Checks

- ✓ CSV structure validated (12 columns, correct header order per schema)
- ✓ IDs gap-free and sequential (US-0001 through US-0245)
- ✓ No duplicates by inventory_id
- ✓ No duplicates by (path, line_or_section, exact_text)
- ✓ Bytewise sorting by path/line_or_section/exact_text confirmed

## Unresolved Classifications

- 7 rows have `needs-domain-review` evidence status (row 53: CGI; row 81: Lexile CCSS check; row 136,231: student behavior; row 212: Lexile 600-850)
- 1 row has `inferred` evidence status (row 49: science & engineering practices inferred from NGSS context)
- All rows retain actionable `action_hint` values for Task 3+4

## Baseline Match Verification

Per pinned upstream SHA `281eb8d41fe2837d911541c9bbb870b58add804c`, the inventory captures all US-specific content from skills, tools, references, scripts, evals, and plugin-metadata. No baseline hits were missed during lexical scan of K-12 classroom materials, grade bands, CCSS/NGSS/C3 frameworks, WIDA/IEP/504 supports, US spellings, currencies, and measurements.