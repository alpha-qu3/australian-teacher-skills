"""Test that every file linked from each plugin/skills/**/SKILL.md exists."""
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SKILL_DIR = REPO_ROOT / "plugin" / "skills"


def find_skill_files():
    """Find all SKILL.md files under plugin/skills/."""
    return list(SKILL_DIR.rglob("SKILL.md"))


def find_linked_references(skill_md):
    """Extract file references from backtick-quoted paths in SKILL.md."""
    text = skill_md.read_text(errors="replace")
    # Match backtick-quoted relative paths that look like file references
    refs = re.findall(r"`([a-zA-Z][a-zA-Z0-9_/\.\-]*\.(?:md|json|sh|py|css|yml|yaml))`", text)
    return refs


def find_script_references(skill_md):
    """Find script references in SKILL.md."""
    text = skill_md.read_text(errors="replace")
    # Match bash commands or script references
    scripts = re.findall(r"`(?:bash\s+)?(scripts/[a-zA-Z0-9_/\.\-]+)`", text)
    return scripts


class TestSkillLinks:
    """Ensure every file referenced from SKILL.md files exists."""

    def test_backtick_referenced_files_exist(self):
        """Every file referenced in backticks from SKILL.md must exist."""
        skill_files = find_skill_files()
        failures = []
        for skill_md in skill_files:
            refs = find_linked_references(skill_md)
            for ref in refs:
                ref_path = skill_md.parent / ref
                if not ref_path.exists():
                    failures.append(
                        f"{skill_md}: referenced '{ref}' does not exist (resolved to {ref_path})"
                    )
        assert not failures, (
            "Missing referenced files:\n" + "\n".join(failures)
        )

    def test_script_references_exist(self):
        """Every script referenced in SKILL.md must exist."""
        skill_files = find_skill_files()
        failures = []
        for skill_md in skill_files:
            scripts = find_script_references(skill_md)
            for ref in scripts:
                ref_path = REPO_ROOT / ref
                if not ref_path.exists():
                    failures.append(
                        f"{skill_md}: script '{ref}' does not exist"
                    )
        assert not failures, (
            "Missing script references:\n" + "\n".join(failures)
        )

    def test_all_skill_directories_have_skill_md(self):
        """Every skill directory must have a SKILL.md file."""
        skill_dirs = [d for d in SKILL_DIR.iterdir() if d.is_dir()]
        failures = []
        for d in skill_dirs:
            if not (d / "SKILL.md").exists():
                failures.append(f"{d}: missing SKILL.md")
        assert not failures, (
            "Skill directories missing SKILL.md:\n" + "\n".join(failures)
        )

    def test_skill_md_has_frontmatter(self):
        """Every SKILL.md must have YAML frontmatter with name and description."""
        skill_files = find_skill_files()
        failures = []
        for skill_md in skill_files:
            text = skill_md.read_text(errors="replace")
            if not text.startswith("---"):
                failures.append(f"{skill_md}: missing YAML frontmatter")
            else:
                if "name:" not in text[:text.find("---", 3)]:
                    failures.append(f"{skill_md}: missing 'name:' in frontmatter")
                if "description:" not in text[:text.find("---", 3)]:
                    failures.append(f"{skill_md}: missing 'description:' in frontmatter")
        assert not failures, (
            "SKILL.md files missing frontmatter fields:\n" + "\n".join(failures)
        )