# Task 12 Model-Evaluation Harness Design

## Overview

The Task 12 Model-Evaluation Harness evaluates the Australian localisation of the K12 Teacher Skills against a comprehensive set of curriculum standards using a target model matrix. It provides detailed reporting on per-criterion performance and enforces the requirement for human reviewer sign-off before release.

## Purpose

The harness validates that all localised skills meet curriculum requirements, with special attention to jurisdictional mappings that require Queensland curriculum reviewer approval. It reports:

- Per-criterion pass rates (not just aggregate scores)
- Criteria requiring reviewer sign-off
- Overall release status with explicit gating condition
- Results across multiple model performance tiers (fast, balanced, frontier)

## How to Run

### Basic Execution

```bash
# Full run: all scenarios, all models in the matrix
cd /path/to/skillcreator-aus_teacher_skills
python3 scripts/evaluate_localisation.py
```

### Model Filtering

```bash
# Run only on the balanced model
python3 scripts/evaluate_localisation.py --models balanced

# Run on fast and frontier models
python3 scripts/evaluate_localisation.py --models fast frontier
```

### Scenario Filtering

```bash
# Run only Australian Curriculum F-10 lesson planning scenarios
python3 scripts/evaluate_localisation.py --scenario "Australian Curriculum F-10 lesson planning"

# Run multiple scenarios (repeat --scenario flag)
python3 scripts/evaluate_localisation.py \
  --scenario "Australian Curriculum F-10 lesson planning" \
  --scenario "F-10 differentiation with EAL/D and reasonable-adjustment constraints"
```

### Dry-Run (No Model Execution)

```bash
# Plan validation without invoking any model API
python3 scripts/evaluate_localisation.py --no-exec
```

### Record Results

```bash
# Save evaluation results to a CSV file
python3 scripts/evaluate_localisation.py --record-results /tmp/eval_results.csv
```

## Model Matrix Contract

The harness evaluates against three model tiers:

- **fast**: Optimized for speed, acceptable for rapid iteration
- **balanced**: Moderate speed with good performance across most tasks  
- **frontier**: Maximum performance, thorough evaluation

All three models are evaluated by default. Users may specify a subset. Models are evaluated independently, and each criterion's pass rate is computed per model to detect model-specific performance variations.

## Scenario Families

The harness evaluates the following scenario families, as defined in Task 11:

1. **Australian Curriculum F-10 lesson planning**
   - Covers the australian-lesson-plan-creation skill

2. **Australian Curriculum F-10 Mathematics check for understanding**
   - Covers the australian-check-for-understanding skill

3. **F-10 differentiation with EAL/D and reasonable-adjustment constraints**
   - Covers the australian-lesson-differentiation skill

4. **QCAA Business lesson planning/prep**
   - Covers the QCAA 'business' subject (source-alignment evaluation)

5. **QCAA Food & Nutrition lesson planning/prep**
   - Covers the QCAA 'food-nutrition' subject (source-alignment evaluation)

6. **Source-alignment and authority verification for all other current QCAA subjects**
   - Includes all 78 other QCAA subjects (source-alignment evaluations)

7. **Ambiguous jurisdiction/year clarification**
   - Special evaluation scenarios for jurisdictional clarity

8. **Invalid or superseded curriculum code**
   - Validation of code integrity and currency

9. **Runtime without curriculum connector**
   - Graceful degradation testing when curriculum connector is unavailable

## Gating Rules

### Human Reviewer Sign-Off Requirements

A criterion is **NOT_SIGNOFF** (and thus gates release) if:

1. **Mapping status is pending-reviewer**: The criterion's `mapping_status` field in `eval-crosswalk.csv` is `pending-reviewer`, OR
2. **Authority required and not confirmed**: The criterion requires authority verification (`authority_required=yes`) but that verification has not been confirmed

### Critical Constraint

> **No partial/contextual/no-equivalent mapping passes without human reviewer sign-off**

Even if a model evaluates a criterion as PASS, it remains in a NOT_SIGNOFF state if:
- Its mapping_status != 'approved', OR
- authority_required=yes without explicit confirmation

This ensures that all jurisdictional mappings undergo Queensland curriculum reviewer approval before release.

### Pass Rate Calculation

Per-criterion pass rates are computed as:
```
pass_rate = passes / eligible_criteria
```

where `eligible_criteria = passes + fails + skips`

NOT_SIGNOFF criteria are excluded from the pass rate denominator because they represent unresolved mappings that block release.

## Output Artifacts

### Console Report

The harness produces a concise summary:

```
TASK 12: MODEL-EVALUATION HARNESS REPORT
=========================================

PER-SCENARIO COVERAGE
---------------------------------------------
  Australian Curriculum F-10 lesson planning:
    Total criteria: 66
    PASS: 51  FAIL: 0  SKIP: 15  NOT_SIGNOFF: 0
    Per-criterion pass rate (pass/eligible): 77.4%
    Signoff-gated criteria: 15
  ... (additional scenarios)

OVERALL GATING REPORT
---------------------------------------------
  Pending reviewer sign-off criteria: 15

  OVERALL: NOT RELEASED — pending Queensland curriculum reviewer sign-off (15 criteria)
=========================================
```

### Record-Results CSV

When `--record-results` is specified, the harness writes a CSV with columns:

- `model`: Model used for evaluation (fast/balanced/frontier)
- `scenario`: Scenario family name
- `criterion`: Criterion ID (e.g., LPC-001)
- `status`: PASS/FAIL/SKIP/NOT_SIGNOFF
- `authority_visible`: Boolean indicating if authority is visible/required
- `signoff`: Boolean indicating if reviewer sign-off is required

### Dry-Run (--no-exec)

When `--no-exec` is used:

- No model API calls are made
- All criteria are evaluated deterministically from `eval-crosswalk.csv`
- The same gating report is produced, ensuring validation of the plan
- Useful for confirming that pending-reviewer criteria are correctly identified

## Live Model Integration Hook

The harness is designed to integrate with live model evaluation systems.

### Current Implementation (Stub)

In `run_model_evaluation()`, a stub comments indicate where model API calls would be made:

```python
# Live mode would call the model API here.
# The result would be compared against the rubric_file expectations.
# Since no model API is configured, this degrades to no-exec behaviour.
```

### Integration Instructions

To enable live model evaluation, replace the stub with:

1. **Model API client**: Connect to the target model provider (e.g., Anthropic, OpenAI)
2. **Prompt engineering**: Create evaluation prompts that include:
   - The scenario description
   - Criterion name and rubric file location
   - Australian curriculum context
   - Source authority references
3. **Result parsing**: Parse model responses against the rubric specification
4. **Deterministic fallback**: Maintain the `--no-exec` dry-run capability for environments without API access

The harness maintains separation between the evaluation framework and the model integration, allowing for easy swapping of model providers or evaluation strategies.

## Data Sources

### Primary Input

`docs/localisation/validation/eval-crosswalk.csv`

Contains 229 evaluation criteria with columns:

- `mapping_id`: Unique identifier (e.g., LPC-001)
- `original_id`: Original criterion ID
- `eval_dir`: Evaluation directory (skill or QCAA subject)
- `rubric_file`: Location of rubric file
- `criterion_name`: Human-readable description
- `source_authority`: Source curriculum authority
- `mapping_action`: Type of mapping (retain, source-alignment, localise, add, split, remove)
- `mapping_status`: Implementation status (approved, pending-reviewer)
- `australian_notes`: Notes on Australian adaptation
- `authority_required`: Whether authority verification is required (yes/no)

### Output Directory Structure

- `docs/localisation/validation/model-eval-harness.md`: This design document
- `scripts/evaluate_localisation.py`: Main harness implementation
- Optional: `docs/localisation/validation/model-eval-harness-output/` for expanded reports

## Validation and Quality Assurance

### Gating Report Verification

The harness must be run in `--no-exec` mode to validate that:

1. **Pending reviewer count is correct**: The number of `mapping_status='pending-reviewer'` criteria matches expected counts
2. **Authority required criteria are identified**: All `authority_required=yes` criteria are properly flagged
3. **Scenario coverage is complete**: All required scenario families are represented in the results

### Reproducibility Requirements

- Same crosswalk CSV input should produce identical gating reports across runs
- Dry-run mode should produce the same results as live mode (without API calls)
- Output should be deterministic given the same input data and model specifications

## Release Criteria Gate

### Final Approval Status

The harness produces an explicit **OVERALL** line:

```
OVERALL: NOT RELEASED — pending Queensland curriculum reviewer sign-off (n criteria)
```

OR

```
OVERALL: RELEASED — all gated criteria confirmed by reviewer
```

This status is determined by:

1. **Count gated criteria**: Number of criteria requiring reviewer sign-off
2. **Reviewer confirmation**: All gated criteria must have `mapping_status='approved'` and confirmed authority requirements

### Release Blockers

If `pending reviewer sign-off criteria > 0`, the entire localisation package remains **NOT RELEASED** until a Queensland curriculum reviewer:

- Reviews each NOT_SIGNOFF criterion
- Provides explicit sign-off approval
- Updates the `mapping_status` in the crosswalk to `approved`

This ensures no partial/contextual/no-equivalent mappings reach production without human oversight.
