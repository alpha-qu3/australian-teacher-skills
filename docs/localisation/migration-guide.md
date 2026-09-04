# Migration Guide — Australian Localisation

This guide documents the breaking changes introduced by the Australian localisation of this
plugin and how to migrate an existing install. It is authoritative for anything not stated in
`README.md`, `plugin/.claude-plugin/plugin.json`, or `.claude-plugin/marketplace.json`.

## 1. Breaking rename — no compatibility aliases

The plugin identifier and every user-facing skill name changed. There are **no compatibility
aliases** and no shim that maps the old names to the new ones. Anything still referencing the
old names will fail to resolve.

| Old identifier | New identifier | Type |
|---|---|---|
| `k12-education` | `australian-education` | Plugin name (plugin.json, marketplace.json) |
| `k12-teacher-skills` | `australian-teacher-skills` | Marketplace/repository name |
| `k12-lesson-plan-creation` | `australian-lesson-plan-creation` | Skill directory + frontmatter `name` |
| `k12-lesson-differentiation` | `australian-lesson-differentiation` | Skill directory + frontmatter `name` |
| `k12-lesson-prep` | `australian-lesson-preparation` | Skill directory + frontmatter `name` |
| `k12-check-for-understanding` | `australian-check-for-understanding` | Skill directory + frontmatter `name` |

The repository URL also changed: `https://github.com/anthropics/k12-teacher-skills` is now
`https://github.com/anthropics/australian-teacher-skills`.

### What to do

1. Uninstall any previously installed `k12-education` plugin or `k12-*` skills.
2. Reinstall from the new repository and plugin name:

   ```
   claude plugin marketplace add ./australian-teacher-skills
   claude plugin install australian-education@australian-teacher-skills
   ```

3. Update any automation, scripts, or documentation that hard-codes the old names or the old
   clone URL.
4. Skill frontmatter and SKILL.md bodies that previously self-referenced the old skill names
   (e.g. "do not also invoke `k12-lesson-differentiation`") now use the approved Australian
   names. If you have patched or forked these skills, re-apply your changes against the new
   names — the old names are not recognised anywhere in the shipped code.

## 2. Terminology changes

User-facing descriptions and documentation now use Australian/F-12 terminology:

- `K-12` → `F-12` (Foundation to Year 12)
- `K-5` → `F-6`
- `kindergarten` → `Prep` (Queensland)
- `ELA` → `English`
- `social studies` → `HASS` (F-10) or named QCAA senior subject
- `math` → `Mathematics`
- `grade` → `year level`
- `grade level` → `year level`

`K-12` and `grade` are no longer approved in shipped behaviour; see
`docs/localisation/source-and-version-policy.md` for the approved vocabulary list and the
procedure for requesting an exception.

## 3. Curriculum authority selection

The skills branch on school phase, not on a single global standard. The approved split is:

| Phase | Years | Authority | Content used |
|---|---|---|---|
| Foundation–Year 10 | F–10 | Australian Curriculum v9.0 (ACARA) | Content descriptions and achievement standards |
| Senior secondary | Years 11–12 | QCAA General Senior Syllabuses (Queensland) | Syllabus objectives and subject matter |

- For F–10, the curriculum lookup adapter is called with `jurisdiction="Australia"`,
  `school_phase="F-10"`.
- For Years 11–12, it is called with `jurisdiction="Queensland"`,
  `school_phase="Years 11-12"`.
- If the year level is unknown or straddles the F–10 / Years 11–12 boundary, the skill asks the
  teacher before routing. It never guesses the authority.

### Supported versions

- **Australian Curriculum**: Version 9.0 (V9), effective for F–10. This is the only ACARA version
  bundled in `data/curriculum/source-manifest.australian.json`. Earlier versions (e.g. V8.4) are
  **not** supported; do not cite them.
- **QCAA senior syllabuses**: current General Senior Syllabuses for Years 11–12, as bundled in
  `data/curriculum/qcaa/*.json`. QCAA revises syllabuses on a published cycle; the bundled set is
  the supported set, and subjects without a bundled manifest return `not-found` rather than a
  guess (see §4).

The version and effective year returned by the lookup adapter must be cited in any
user-facing alignment claim. Do not present an uncited or fabricated curriculum code.

## 4. Connector and tool requirements — safe no-lookup behaviour

The skills no longer assume the Learning Commons Knowledge Graph connector covers Australian
curricula. The connector upstream was US-standards-focused (CCSS/NGSS/C3/common-core and US
state-standard code patterns) and does **not** cover ACARA V9 or QCAA senior syllabuses.

- The curriculum lookup adapter is **offline**: it reads versioned, bundled manifests only
  (`data/curriculum/source-manifest.australian.json` and `data/curriculum/qcaa/*.json`). It makes
  **no network call** and does **not** query the Learning Commons Graph.
- When the requested subject is not in the bundled set, the adapter returns an explicit
  `status: "not-found"` result with a message naming the missing subject. It **never** guesses a
  code, **never** synthesises an identifier, and **never** maps a US code onto an Australian
  identifier.
- A skill that receives `not-found` works from general best practice and adds a footer to the
  teacher guide stating that the curriculum focus reflects general best practice, with nothing
  about what was or was not retrieved. It never invents a curriculum citation.
- The full interface contract, coverage limitations, and CLI self-check commands are documented in
  `docs/localisation/tooling-contract.md`.

## 5. Review status

The breaking rename and the terminology changes in this guide are **shipped as-is**. The
authority selection rules in §3 are implemented against the bundled manifests and are
authority-verified for the subjects present in `data/curriculum/`. Subject mappings marked
`pending-reviewer` in `docs/localisation/03-mapping-summary.md` have **not** been approved by a
Queensland curriculum-qualified human reviewer and must not be presented as approved.

## 6. Rollback

Because there are no aliases, rollback means reinstalling the previous `k12-*` artefacts from
the upstream `k12-teacher-skills` repository at its last pre-localisation commit. The localisation
is not reversible in place.