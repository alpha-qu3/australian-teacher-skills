# Agent Skills for Australian F–12 Teachers

> **Australian adaptation:** This repository was forked from [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) and adapted for the Australian Curriculum Version 9.0 and Queensland senior syllabuses.

Source code and evaluation framework for agent skills designed for Australian and Queensland teaching contexts. This fork is not a Claude for Teachers package.

Included are four skills:
- `australian-lesson-plan-creation`: Builds classroom-ready lesson plans, student materials, and observation templates aligned to the Australian Curriculum v9.0 (F–10, ACARA) or QCAA senior syllabuses (Years 11–12)
- `australian-lesson-differentiation`: Adapts an existing lesson into tiered versions (below / at / above proficiency level) and for specific student needs, keeping core content consistent across tiers
- `australian-lesson-preparation`: A prep partner for a lesson the teacher already has; works through the key student task with them and leaves a short teacher-only prep note
- `australian-check-for-understanding`: Builds a 1–3 item formative check for a Mathematics topic, with distractors drawn from documented student misconceptions (where authority-verified sources exist) and a teacher guide routing each response to a next instructional step

Where noted, materials in this repo retain upstream attribution. The Australian adaptation adds authority-verified curriculum sources and preserves the upstream curriculum-neutral teaching practices and learning-science guardrails.

The skills use a curriculum lookup adapter that reads offline, versioned, authority-verified manifests covering the Australian Curriculum v9.0 (F–10, ACARA) and QCAA General Senior Syllabuses (Years 11–12). No external connector is required; safe not-found behaviour is documented in `docs/localisation/tooling-contract.md` and `docs/localisation/source-and-version-policy.md`.

## Quick start
Load the plugin or skills manually in a compatible agent environment. For instance, in Claude Code:

```
git clone git@github.com:alpha-qu3/australian-teacher-skills.git
claude plugin marketplace add ./australian-teacher-skills
claude plugin install australian-education@australian-teacher-skills
```

## Layout

- `plugin/` - Main skill content bundled as a plugin; also includes teacher-focused 3rd party MCP servers that are available for users to enable
- `docs/localisation/` - Source registers, authority verification records, mapping matrices, tooling contract, migration guide, and source/version policy
- `evals/` - Contains our evaluation framework and how to adapt them for your use case
