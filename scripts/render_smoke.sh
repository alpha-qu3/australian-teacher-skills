#!/usr/bin/env bash
# Render smoke test harness - validates HTML outputs for F-10 Maths, QCAA Business, and QCAA Food & Nutrition
# Output is a render smoke (not a curriculum-alignment model evaluation)
# Usage: scripts/render_smoke.sh
# Exit codes:
#   0 - All required HTML outputs produced
#   1 - Missing required HTML outputs

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.."
PLAN_SKILL_DIR="$REPO_ROOT/plugin/skills/australian-lesson-plan-creation"
DATA_DIR="$REPO_ROOT/data"

# Track scenario results
declare -a scenario_results=()
overall_success=true

check_docx_available() {
    python3 -c "import docx" 2>/dev/null
}

run_scenario() {
    local scenario_name="$1"
    local json_path="$2"
    local outdir="$3"
    local use_render_all="${4:-true}"

    echo ""
    echo "=== Scenario: $scenario_name ==="
    echo "Source JSON: $json_path"
    echo "Output dir: $outdir"

    mkdir -p "$outdir"

    local docx_status="unknown"
    if check_docx_available; then
        docx_status="available"
    else
        docx_status="not_available"
    fi

    # Run the renderer
    local render_rc=0
    if [ "$use_render_all" = true ]; then
        if ! bash "$PLAN_SKILL_DIR/scripts/render_all.sh" "$json_path" "$outdir" 2>&1; then
            render_rc=$?
        fi
    else
        if ! python3 "$PLAN_SKILL_DIR/scripts/render_documents.py" "$json_path" --format html --outdir "$outdir" 2>&1; then
            render_rc=$?
        fi
    fi

    if [ $render_rc -ne 0 ]; then
        echo "✗ FAIL: Render pipeline failed for $scenario_name"
        scenario_results+=("$scenario_name:FAIL_RENDER_ERROR")
        overall_success=false
        return 1
    fi

    # Check HTML outputs
    local html_count=0
    local html_files
    html_files=$(find "$outdir" -maxdepth 1 -type f -name "*.html" 2>/dev/null | sort)
    if [ -n "$html_files" ]; then
        html_count=$(echo "$html_files" | wc -l)
    fi

    if [ $html_count -eq 0 ]; then
        echo "✗ FAIL: No .html outputs produced for $scenario_name"
        scenario_results+=("$scenario_name:FAIL_NO_HTML")
        overall_success=false
        return 1
    fi

    echo "✓ PASS: $scenario_name produced $html_count .html output(s)"

    # Validate each HTML file is non-empty
    local all_html_valid=true
    for f in $html_files; do
        if [ ! -s "$f" ]; then
            echo "  ✗ Empty HTML file: $(basename "$f")"
            all_html_valid=false
        fi
    done

    if [ "$all_html_valid" = false ]; then
        echo "✗ FAIL: Some HTML files are empty for $scenario_name"
        scenario_results+=("$scenario_name:FAIL_EMPTY_HTML")
        overall_success=false
        return 1
    fi

    # Check docx status
    local docx_count=0
    if [ "$docx_status" = "available" ]; then
        local docx_files
        docx_files=$(find "$outdir" -maxdepth 1 -type f -name "*.docx" 2>/dev/null | sort)
        if [ -n "$docx_files" ]; then
            docx_count=$(echo "$docx_files" | wc -l)
        fi
        if [ $docx_count -gt 0 ]; then
            echo "  DOCX: produced ($docx_count file(s))"
            scenario_results+=("$scenario_name:DOCX_PRODUCED")
        else
            echo "  DOCX: SKIPPED (python-docx available but no .docx output — render_all.sh fell back to HTML)"
            scenario_results+=("$scenario_name:SKIP_DOCX_FALLBACK")
        fi
    else
        echo "  DOCX: SKIPPED (python-docx not installed)"
        scenario_results+=("$scenario_name:SKIP_DOCX_NOT_INSTALLED")
    fi

    # Verify at least one HTML output exists and is non-empty
    if [ $html_count -gt 0 ]; then
        echo "✓ PASS: $scenario_name — HTML validated ($html_count files)"
    fi
}

build_minimal_lesson_json() {
    local curriculum_path="$1"
    local subject_name="$2"
    local output_path="$3"

    python3 -c "
import json
from pathlib import Path

with open('$curriculum_path', 'r', encoding='utf-8') as f:
    curriculum = json.load(f)

# Extract objectives - handle both array of strings and array of dicts
objectives = curriculum.get('objectives', [])
assessment = curriculum.get('assessment_model', {})
subject_matter = curriculum.get('subject_matter', {})

# Extract a sample objective text
objective_text = '$subject_name learning objectives'
if isinstance(objectives, list) and objectives:
    if isinstance(objectives[0], dict):
        objective_text = objectives[0].get('text', objective_text)
    else:
        objective_text = objectives[0]
elif isinstance(subject_matter, dict) and 'units' in subject_matter:
    objective_text = 'Business studies unit content'

# Build minimal lesson.json shape compatible with render_documents.py
result = {
    'shared': {
        'subject': '$subject_name',
        'grade': 'Grade 11',
        'duration': 50,
        'standard_code': 'QCAA-BUSINESS',
        'standard_text': objective_text,
        'curriculum': 'QCAA',
    },
    'theme': {
        'primary': '#0E7A4D',
    },
    'documents': [
        {
            'id': 'lesson_plan',
            'audience': 'teacher',
            'eyebrow': '$subject_name · Senior Curriculum',
            'title': '$subject_name Lesson Plan',
            'meta': 'Grade 11 · 50 minutes · QCAA',
            'sections': [
                {
                    'heading': 'Learning goal',
                    'blocks': [
                        {
                            'type': 'labeled',
                            'label': 'Students will be able to',
                            'text': objective_text
                        }
                    ]
                },
                {
                    'heading': 'Assessment',
                    'blocks': [
                        {
                            'type': 'labeled',
                            'label': 'Assessment approach',
                            'text': 'Combination response examination (25%)'
                        }
                    ]
                }
            ]
        },
        {
            'id': 'student_materials',
            'audience': 'student',
            'eyebrow': '$subject_name · Student Materials',
            'title': '$subject_name Lesson Activities',
            'meta': 'Name: ____________________    Date: ____________',
            'sections': [
                {
                    'heading': 'Practice',
                    'blocks': [
                        {
                            'type': 'workspace',
                            'size': 'large',
                            'height_pt': 80
                        }
                    ]
                }
            ]
        }
    ]
}

with open('$output_path', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print('Built minimal lesson.json at $output_path')
"
}

main() {
    echo "============================================================"
    echo " RENDER SMOKE TEST HARNESS (Task 12)"
    echo " Testing HTML output generation — deterministic plumbing"
    echo " NOT a curriculum-alignment model evaluation"
    echo "============================================================"

    test_outdir="$(mktemp -d -t render-smoke-test-XXXXXX)"
    echo "Temporary output directory: $test_outdir"

    # Scenario 1: F-10 Australian Mathematics (using example_lesson.json)
    scenario1_json="$PLAN_SKILL_DIR/references/example_lesson.json"
    scenario1_outdir="$test_outdir/scenario1_mathematics"
    if [ -f "$scenario1_json" ]; then
        run_scenario "F-10 Australian Mathematics" "$scenario1_json" "$scenario1_outdir" true
    else
        echo "✗ FAIL: example_lesson.json not found at $scenario1_json"
        scenario_results+=("F-10_Maths:FAIL_SOURCE_MISSING")
        overall_success=false
    fi

    # Scenario 2: QCAA Business (build minimal source JSON from curriculum metadata)
    scenario2_outdir="$test_outdir/scenario2_business"
    scenario2_json="$test_outdir/scenario2_business_minimal.json"
    business_curriculum="$DATA_DIR/curriculum/qcaa/economics.json"

    if [ ! -f "$business_curriculum" ]; then
        echo "✗ FAIL: Business curriculum not found at $business_curriculum"
        scenario_results+=("QCAA_Business:FAIL_CURRICULUM_MISSING")
        overall_success=false
    else
        echo ""
        echo "=== Scenario: QCAA Business ==="
        echo "Building minimal lesson.json from $business_curriculum"
        if build_minimal_lesson_json "$business_curriculum" "Business" "$scenario2_json"; then
            run_scenario "QCAA Business" "$scenario2_json" "$scenario2_outdir" false
        else
            echo "✗ FAIL: Could not build minimal source JSON for QCAA Business"
            scenario_results+=("QCAA_Business:FAIL_BUILD_ERROR")
            overall_success=false
        fi
    fi

    # Scenario 3: QCAA Food & Nutrition (build minimal source JSON from curriculum metadata)
    scenario3_outdir="$test_outdir/scenario3_food_nutrition"
    scenario3_json="$test_outdir/scenario3_food_nutrition_minimal.json"
    food_nutrition_curriculum="$DATA_DIR/curriculum/qcaa/food-nutrition.json"

    if [ ! -f "$food_nutrition_curriculum" ]; then
        echo "✗ FAIL: Food & Nutrition curriculum not found at $food_nutrition_curriculum"
        scenario_results+=("QCAA_Food_Nutrition:FAIL_CURRICULUM_MISSING")
        overall_success=false
    else
        echo ""
        echo "=== Scenario: QCAA Food & Nutrition ==="
        echo "Building minimal lesson.json from $food_nutrition_curriculum"
        if build_minimal_lesson_json "$food_nutrition_curriculum" "Food & Nutrition" "$scenario3_json"; then
            run_scenario "QCAA Food & Nutrition" "$scenario3_json" "$scenario3_outdir" false
        else
            echo "✗ FAIL: Could not build minimal source JSON for QCAA Food & Nutrition"
            scenario_results+=("QCAA_Food_Nutrition:FAIL_BUILD_ERROR")
            overall_success=false
        fi
    fi

    # Summary
    echo ""
    echo "============================================================"
    echo " RENDER SMOKE TEST SUMMARY"
    echo "============================================================"
    if [ "$overall_success" = true ]; then
        echo " OVERALL STATUS: PASS"
    else
        echo " OVERALL STATUS: FAIL"
    fi
    echo ""
    echo "Per-scenario results:"
    for result in "${scenario_results[@]}"; do
        echo "  $result"
    done
    echo ""
    echo "Temporary files cleaned up: $test_outdir"
    rm -rf "$test_outdir"

    if [ "$overall_success" = true ]; then
        exit 0
    else
        exit 1
    fi
}

main "$@"
