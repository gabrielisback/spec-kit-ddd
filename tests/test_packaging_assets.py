"""Regression tests for wheel packaging of bundled assets."""

from __future__ import annotations

import json
import tomllib
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _load_force_include() -> dict[str, str]:
    pyproject = PROJECT_ROOT / "pyproject.toml"
    with pyproject.open("rb") as f:
        data = tomllib.load(f)
    return data["tool"]["hatch"]["build"]["targets"]["wheel"]["force-include"]


def _load_bundled_ids(catalog_path: Path, key: str) -> set[str]:
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    return {
        item_id
        for item_id, item in catalog[key].items()
        if item.get("bundled") is True
    }


class TestBundledAssetsIncludedInWheel:
    """All bundled assets in catalogs must be shipped in the wheel."""

    def test_bundled_extensions_are_force_included(self):
        force_include = _load_force_include()
        bundled_extensions = _load_bundled_ids(
            PROJECT_ROOT / "extensions" / "catalog.json",
            "extensions",
        )

        missing = sorted(
            ext_id for ext_id in bundled_extensions
            if f"extensions/{ext_id}" not in force_include
        )

        assert missing == [], (
            "Bundled extensions missing from wheel force-include: "
            + ", ".join(missing)
        )

    def test_bundled_presets_are_force_included(self):
        force_include = _load_force_include()
        bundled_presets = _load_bundled_ids(
            PROJECT_ROOT / "presets" / "catalog.json",
            "presets",
        )

        missing = sorted(
            preset_id for preset_id in bundled_presets
            if f"presets/{preset_id}" not in force_include
        )

        assert missing == [], (
            "Bundled presets missing from wheel force-include: "
            + ", ".join(missing)
        )
