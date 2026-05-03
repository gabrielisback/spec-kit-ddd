"""
Tests for the bundled ddd preset (presets/ddd/).
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
PRESET_DIR = PROJECT_ROOT / "presets" / "ddd"


class TestDDDPresetManifest:
    def test_manifest_validates(self):
        """preset.yml passes manifest validation."""
        from specify_cli.presets import PresetManifest

        manifest = PresetManifest(PRESET_DIR / "preset.yml")
        assert manifest.id == "ddd"
        assert manifest.version == "1.1.0"

    def test_manifest_templates(self):
        """Manifest declares DDD template overrides plus architecture template."""
        from specify_cli.presets import PresetManifest

        manifest = PresetManifest(PRESET_DIR / "preset.yml")
        names = [template["name"] for template in manifest.templates]
        assert names == [
            "spec-template",
            "plan-template",
            "tasks-template",
            "architecture-template",
        ]

    def test_manifest_files_exist(self):
        """All template files referenced in the manifest exist."""
        from specify_cli.presets import PresetManifest

        manifest = PresetManifest(PRESET_DIR / "preset.yml")
        for template in manifest.templates:
            template_path = PRESET_DIR / template["file"]
            assert template_path.is_file(), f"Missing template file: {template['file']}"


class TestDDDPresetContent:
    def test_spec_template_is_domain_driven(self):
        """Spec template should include DDD framing sections."""
        content = (PRESET_DIR / "templates" / "spec-template.md").read_text(encoding="utf-8")
        assert "## Domain Goal" in content
        assert "## Domain Context" in content
        assert "Bounded Contexts" in content
        assert "Business Invariants" in content
        assert "specs/architecture.md" in content

    def test_plan_template_is_domain_driven(self):
        """Plan template should include domain realization sections."""
        content = (PRESET_DIR / "templates" / "plan-template.md").read_text(encoding="utf-8")
        assert "## Domain Framing" in content
        assert "## Domain Model Realization" in content
        assert "## Data & Consistency Strategy" in content
        assert "domain-model.md" in content
        assert "specs/architecture.md" in content

    def test_tasks_template_tracks_architecture_constraints(self):
        """Tasks template should mention architecture constraints explicitly."""
        content = (PRESET_DIR / "templates" / "tasks-template.md").read_text(encoding="utf-8")
        assert "specs/architecture.md" in content
        assert "bounded contexts" in content.lower()
        assert "Architecture Dependencies" in content

    def test_architecture_template_focuses_on_bounded_contexts(self):
        """Architecture template should scaffold product architecture decisions."""
        content = (PRESET_DIR / "templates" / "architecture-template.md").read_text(encoding="utf-8")
        assert "## Bounded Contexts" in content
        assert "## Context Map" in content
        assert "## Architecture Constraints for Feature Work" in content


class TestDDDPresetInstall:
    def test_install_from_directory(self, tmp_path: Path):
        """Preset installs via PresetManager.install_from_directory."""
        from specify_cli.presets import PresetManager

        (tmp_path / ".specify").mkdir()
        manager = PresetManager(tmp_path)
        manifest = manager.install_from_directory(PRESET_DIR, "0.6.0")
        assert manifest.id == "ddd"
        assert manager.registry.is_installed("ddd")

    def test_bundled_preset_locator(self):
        """_locate_bundled_preset finds the ddd preset."""
        from specify_cli import _locate_bundled_preset

        path = _locate_bundled_preset("ddd")
        assert path is not None
        assert (path / "preset.yml").is_file()
