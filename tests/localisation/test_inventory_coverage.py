"""Test inventory coverage: every US-specific item must have a mapping or explicit rejection."""
import csv
import pytest


def load_inventory():
    path = "docs/localisation/01-us-specific-inventory.csv"
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def load_replacement_matrix():
    path = "docs/localisation/03-replacement-matrix.csv"
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


class TestInventoryCoverage:
    """Validate that every inventory item has a corresponding mapping or rejection."""

    def test_every_inventory_item_has_matrix_row(self):
        """Every US inventory item must have a row in the replacement matrix."""
        inventory = load_inventory()
        matrix = load_replacement_matrix()
        matrix_ids = {row["inventory_id"] for row in matrix}
        missing = []
        for inv in inventory:
            inv_id = inv["inventory_id"]
            if inv_id not in matrix_ids:
                missing.append(inv_id)
        assert not missing, (
            f"Inventory items missing from replacement matrix: {missing}. "
            "Each US-specific item must be mapped or explicitly rejected."
        )

    def test_mapped_rows_have_source_ids(self):
        """Any replacement matrix row with a mapping (not blank/skip) must carry source_ids."""
        matrix = load_replacement_matrix()
        failures = []
        for row in matrix:
            src = row.get("source_ids", "").strip()
            if not src:
                # Check if this is a legitimate skip vs missing
                decision = row.get("reviewer_decision", "").strip().lower()
                action = row.get("proposed_file_action", "").strip().lower()
                if decision not in {"rejected", "pending"} and action not in {"review", "remove"}:
                    failures.append(
                        f"{row['inventory_id']}: has mapping_strength={row.get('mapping_strength')} "
                        f"but empty source_ids (decision={decision}, action={action})"
                    )
        assert not failures, (
            "Mapped rows missing source_ids:\n" + "\n".join(failures)
        )

    def test_matrix_references_valid_source_ids(self):
        """source_ids in replacement matrix must reference existing source-register entries."""
        matrix = load_replacement_matrix()
        with open("docs/localisation/02-source-register.csv", newline="") as f:
            sources = {row["source_id"] for row in csv.DictReader(f)}
        failures = []
        for row in matrix:
            src_field = row.get("source_ids", "").strip()
            if not src_field:
                continue
            for src in src_field.split(","):
                src = src.strip()
                if src and src not in sources:
                    failures.append(
                        f"{row['inventory_id']}: references unknown source_id '{src}'"
                    )
        assert not failures, "Invalid source_ids in replacement matrix:\n" + "\n".join(failures)