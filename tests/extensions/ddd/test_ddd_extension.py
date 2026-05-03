"""
Tests for the bundled ddd extension (extensions/ddd/).
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
EXT_DIR = PROJECT_ROOT / "extensions" / "ddd"


class TestDDDExtensionManifest:
    def test_manifest_validates(self):
        """extension.yml passes manifest validation."""
        from specify_cli.extensions import ExtensionManifest

        manifest = ExtensionManifest(EXT_DIR / "extension.yml")
        assert manifest.id == "ddd"
        assert manifest.version == "1.1.0"

    def test_manifest_commands(self):
        """Manifest declares the architecture and modeling commands."""
        from specify_cli.extensions import ExtensionManifest

        manifest = ExtensionManifest(EXT_DIR / "extension.yml")
        names = [command["name"] for command in manifest.commands]
        assert names == ["speckit.ddd.architecture", "speckit.ddd.modeling"]

    def test_manifest_command_files_exist(self):
        """All command files referenced in the manifest exist."""
        from specify_cli.extensions import ExtensionManifest

        manifest = ExtensionManifest(EXT_DIR / "extension.yml")
        for command in manifest.commands:
            command_path = EXT_DIR / command["file"]
            assert command_path.is_file(), f"Missing command file: {command['file']}"


class TestDDDExtensionContent:
    def test_architecture_command_targets_product_architecture_artifact(self):
        """Command content should direct output to specs/architecture.md."""
        content = (EXT_DIR / "commands" / "speckit.ddd.architecture.md").read_text(encoding="utf-8")
        assert "specs/architecture.md" in content
        assert "bounded contexts" in content.lower()
        assert ".spec/" in content

    def test_modeling_command_targets_domain_model_artifact(self):
        """Command content should direct output to domain-model.md."""
        content = (EXT_DIR / "commands" / "speckit.ddd.modeling.md").read_text(encoding="utf-8")
        assert "domain-model.md" in content
        assert "bounded contexts" in content.lower()
        assert "aggregates" in content.lower()


class TestDDDExtensionInstall:
    def test_install_from_directory(self, tmp_path: Path):
        """Extension installs via ExtensionManager.install_from_directory."""
        from specify_cli.extensions import ExtensionManager

        (tmp_path / ".specify").mkdir()
        manager = ExtensionManager(tmp_path)
        manifest = manager.install_from_directory(EXT_DIR, "0.5.0", register_commands=False)
        assert manifest.id == "ddd"
        assert manager.registry.is_installed("ddd")

    def test_bundled_extension_locator(self):
        """_locate_bundled_extension finds the ddd extension."""
        from specify_cli import _locate_bundled_extension

        path = _locate_bundled_extension("ddd")
        assert path is not None
        assert (path / "extension.yml").is_file()
