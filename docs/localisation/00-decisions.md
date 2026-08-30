# Confirmed Execution Decisions

This file records the confirmed requirements from the localisation execution specification verbatim.

| Decision | Confirmed requirement | Execution effect |
|---|---|---|
| QCAA senior scope | Cover all current senior subjects, with every subject completed separately | The catalogue agent creates one work order per subject. A dedicated subject agent owns exactly one subject work order and produces an independently reviewable result. Business and Food & Nutrition remain separate deep-validation tasks. |
| Package naming | Rename the existing skills outright to Australian names | Rename directories, frontmatter names, plugin metadata, documentation and eval directories. Do not create aliases or retain old `k12-*` triggers. |
| Approved supplementary sources | ACARA, NCCD and Queensland Education resources may be used | These sources may support EAL/D, inclusion and reasonable-adjustment mappings when curriculum pages are insufficient. |
| Source authority | Agents must verify that every information source is published by an Authority | Each source record requires authority identity, authority type and verification evidence. Unverified and non-authority sources are excluded from mappings and eval truth data. |
| Runtime | Keep the Claude plugin format but make curriculum lookup portable and degrade safely when no curriculum connector exists | The upstream skills currently assume a Learning Commons connector focused on US standards. |
| New-skill outcome | Produce a ranked proposal only; do not implement new skills in this localisation pass | Keeps localisation reviewable and prevents scope creep. |
| Target model matrix | Test at least one fast, one balanced and one frontier model supported by the execution environment | Skill discoverability and compliance can differ by model. |

## Approved Australian Skill Names

| Upstream name | Australian replacement |
|---|---|
| `k12-lesson-plan-creation` | `australian-lesson-plan-creation` |
| `k12-lesson-differentiation` | `australian-lesson-differentiation` |
| `k12-check-for-understanding` | `australian-check-for-understanding` |
| `k12-lesson-prep` | `australian-lesson-preparation` |

## Authority Verification Rule

A source can enter the replacement matrix or an evaluation fixture only when all of the following are recorded:

1. `authority_name`: ACARA, QCAA, NCCD, Queensland Department of Education or the relevant Queensland Government education authority.
2. `authority_type`: statutory curriculum authority, government department/agency, or official national education program.
3. `authority_evidence_url`: an official About, governance, legislation, departmental ownership or equivalent page that establishes who publishes the source.
4. `publication_owner`: the named organisation on the page or document.
5. `authority_verification_status`: `verified` after the agent confirms the domain, publisher and authority evidence agree.

Search snippets, commercial education sites, teacher blogs, social media, AI summaries and resources that merely link to an authority are not evidence sources. Record useful but rejected candidates in `docs/localisation/02-rejected-sources.csv` with the rejection reason.
