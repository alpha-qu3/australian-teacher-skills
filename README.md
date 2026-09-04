# Agent Skills for Australian F–12 Teachers
Source code and evaluation framework for the agent skills that are included with [Claude for Teachers](https://claude.com/solutions/teachers).

Included are four skills:
- `australian-lesson-plan-creation`: Builds classroom-ready lesson plans, student materials, and observation templates aligned to the Australian Curriculum v9.0 (F–10, ACARA) or QCAA senior syllabuses (Years 11–12)
- `australian-lesson-differentiation`: Adapts an existing lesson into tiered versions (below / at / above proficiency level) and for specific student needs, keeping core content consistent across tiers
- `australian-lesson-preparation`: A prep partner for a lesson the teacher already has; works through the key student task with them and leaves a short teacher-only prep note
- `australian-check-for-understanding`: Builds a 1–3 item formative check for a Mathematics topic, with distractors drawn from documented student misconceptions (where authority-verified sources exist) and a teacher guide routing each response to a next instructional step

Where noted, materials in this repo were co-developed between Anthropic and Learning Commons, who collaborated to help Claude create classroom materials that are grounded in Australian curriculum standards and follow best practices from learning science research.

The skills use a curriculum lookup adapter that reads offline, versioned, authority-verified manifests covering the Australian Curriculum v9.0 (F–10, ACARA) and QCAA General Senior Syllabuses (Years 11–12). No external connector is required; safe not-found behaviour is documented in `docs/localisation/tooling-contract.md` and `docs/localisation/source-and-version-policy.md`.

## Quick start
There are two options to use these skills:

**In Claude for Teachers:**
If you have a Claude for Teachers account, there is no extra install needed. These skills are already installed for you.

**In other places:**
Load the plugin or skills manually. For instance, in Claude Code:

```
git clone https://github.com/anthropics/australian-teacher-skills
claude plugin marketplace add ./australian-teacher-skills
claude plugin install australian-education@australian-teacher-skills
```

## Layout

- `plugin/` - Main skill content bundled as a plugin; also includes teacher-focused 3rd party MCP servers that are available for users to enable
- `docs/localisation/` - Source registers, authority verification records, mapping matrices, tooling contract, migration guide, and source/version policy
- `evals/` - Contains our evaluation framework and how to adapt them for your use case
