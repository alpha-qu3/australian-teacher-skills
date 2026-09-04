"""Render smoke test — validates HTML output generation for Task 12 scenarios.

This test harness runs the render_smoke.sh script as a subprocess and
asserts per-scenario HTML output requirements are met.

Scenarios tested:
  1. F-10 Australian Mathematics (uses example_lesson.json)
  2. QCAA Business (minimal source JSON built from curriculum metadata)
  3. QCAA Food & Nutrition (minimal source JSON built from curriculum metadata)

NOTE: This is deterministic plumbing — not a curriculum-alignment model evaluation.
"""

import os
import subprocess
import re
import pytest


RENDER_SMOKE_SH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "scripts", "render_smoke.sh"
)


def run_render_smoke_harness():
    """Run the render smoke harness and capture its output and exit code."""
    result = subprocess.run(
        ["bash", RENDER_SMOKE_SH],
        capture_output=True,
        text=True,
        timeout=120,
    )
    return result


@pytest.fixture(scope="session")
def harness_output():
    """Run the render smoke harness and return output + exit code."""
    result = run_render_smoke_harness()
    return result.stdout + result.stderr, result.returncode


class TestRenderSmoke:
    """Render smoke test suite for Task 12 curriculum scenarios."""

    def test_harness_runs_cleanly(self, harness_output):
        """The harness should complete without crashing and produce output."""
        output, exit_code = harness_output
        assert exit_code in (0, 1), (
            f"Harness exited with unexpected code {exit_code}. "
            f"Output was:\n{output}"
        )

    def test_f10_maths_produces_html(self, harness_output):
        """F-10 Maths must produce at least one .html output."""
        output, _ = harness_output
        match = re.search(r'F-10 Australian Mathematics produced (\d+)', output)
        assert match is not None, (
            "Could not find 'F-10 Australian Mathematics produced N' in harness output"
        )
        html_count = int(match.group(1))
        assert html_count > 0, (
            "F-10 Australian Mathematics must produce at least one .html output"
        )

    def test_business_produces_html(self, harness_output):
        """QCAA Business must produce at least one .html output."""
        output, _ = harness_output
        match = re.search(r'QCAA Business produced (\d+)', output)
        assert match is not None, (
            "Could not find 'QCAA Business produced N' in harness output"
        )
        html_count = int(match.group(1))
        assert html_count > 0, (
            "QCAA Business must produce at least one .html output"
        )

    def test_food_nutrition_produces_html(self, harness_output):
        """QCAA Food & Nutrition must produce at least one .html output."""
        output, _ = harness_output
        match = re.search(r'QCAA Food & Nutrition produced (\d+)', output)
        assert match is not None, (
            "Could not find 'QCAA Food & Nutrition produced N' in harness output"
        )
        html_count = int(match.group(1))
        assert html_count > 0, (
            "QCAA Food & Nutrition must produce at least one .html output"
        )

    def test_docx_skip_recorded_not_hard_failure(self, harness_output):
        """Any docx skip should be recorded as documented SKIP, not a hard failure."""
        output, _ = harness_output
        hard_failures = re.findall(r':FAIL_(NO_HTML|RENDER_ERROR)', output)
        assert len(hard_failures) == 0, (
            f"Hard failures detected: {hard_failures}\nOutput: {output}"
        )

    def test_harness_exit_code_is_clean(self, harness_output):
        """The harness should exit 0 (all pass) or 1 (some fail), never 2 or other."""
        _, exit_code = harness_output
        assert exit_code in (0, 1), (
            f"Harness should exit 0 (all pass) or 1 (some fail), got {exit_code}"
        )