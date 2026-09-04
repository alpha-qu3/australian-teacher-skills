"""Test that no unapproved US-specific terms remain in user-facing skill text."""
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SKILL_DIR = REPO_ROOT / "plugin" / "skills"
ALLOWLIST_PATH = REPO_ROOT / "tests" / "localisation" / "allowlist.yml"

# US-specific terms that must NOT appear in user-facing skill text (SKILL.md files)
# unless explicitly allowed in allowlist.yml
US_TERMS = [
    r"\bK-12\b",
    r"\bCCSS\b",
    r"\bNGSS\b",
    r"\bWIDA\b",
    r"\bIEP\b",
    r"\b504\b",
    r"\bcommon core\b",
    r"\bELA\b",
    r"\bsocial studies\b",
    r"\bCommon Core\b",
    r"\bNGSS Performance Expectations\b",
    r"\bWIDA-banded\b",
    r"\bWIDA levels\b",
    r"\bIEP goals\b",
    r"\b504 plans\b",
    r"\b504 accommodations\b",
    r"\bELL levels\b",
    r"\bELL\b",
    r"\bESL\b",
    r"\bstate-prefixed codes\b",
    r"\bstate social-studies standards\b",
    r"\bstate standards\b",
    r"\bTexas\b",
    r"\bVirginia\b",
    r"\bCA/CCSS\b",
    r"\bOpenSciEd\b",
    r"\bIllustrative Mathematics\b",
    r"\bC3 inquiry arc\b",
    r"\bLearning Commons\b",
    r"\bLearning Commons Knowledge Graph\b",
]


def load_allowlist():
    """Load allowed US terms from allowlist.yml."""
    if not ALLOWLIST_PATH.exists():
        return set()
    terms = set()
    with open(ALLOWLIST_PATH) as f:
        content = f.read()
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("- ") or line.startswith("*"):
            term = line[2:].strip().strip("'\"")
            if term:
                terms.add(term.lower())
    return terms


def find_skill_files():
    """Find all SKILL.md files under plugin/skills/."""
    return list(SKILL_DIR.rglob("SKILL.md"))


class TestUSTerminologyInSkills:
    """Ensure no unapproved US-specific terms remain in user-facing skill text."""

    def test_no_unapproved_us_terms_in_skill_md(self):
        """SKILL.md files must not contain unapproved US-specific terms."""
        allowlist = load_allowlist()
        skill_files = find_skill_files()
        failures = []
        for skill_md in skill_files:
            text = skill_md.read_text(errors="replace")
            for pattern in US_TERMS:
                matches = re.findall(pattern, text, re.IGNORECASE)
                for m in matches:
                    if m.lower() not in allowlist:
                        failures.append(
                            f"{skill_md}: US term '{m}' found (pattern: {pattern})"
                        )
        assert not failures, (
            "Unapproved US-specific terms found in user-facing skill text:\n"
            + "\n".join(failures)
        )

    def test_no_k12_skill_directories(self):
        """Skill directories must not be named with US K-12 terminology."""
        skill_dirs = [d for d in SKILL_DIR.iterdir() if d.is_dir()]
        failures = []
        for d in skill_dirs:
            if "k12" in d.name.lower():
                failures.append(f"{d}: directory name contains 'k12' (US grade-band label)")
        assert not failures, (
            "US K-12 skill directories still exist:\n" + "\n".join(failures)
        )

    def test_no_us_frameworks_in_skill_descriptions(self):
        """Plugin metadata descriptions must not contain US frameworks (CCSS, NGSS, WIDA, IEP, 504)."""
        plugin_json = REPO_ROOT / "plugin" / ".claude-plugin" / "plugin.json"
        if not plugin_json.exists():
            pytest.skip("plugin.json not found")
        import json
        with open(plugin_json) as f:
            data = json.load(f)
        desc = data.get("description", "")
        failures = []
        for pattern in US_TERMS:
            matches = re.findall(pattern, desc, re.IGNORECASE)
            for m in matches:
                if m.lower() not in load_allowlist():
                    failures.append(
                        f"{plugin_json}: US term '{m}' found in description"
                    )
        assert not failures, (
            "US-specific terms in plugin.json description:\n" + "\n".join(failures)
        )