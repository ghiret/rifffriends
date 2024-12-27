from django.apps import AppConfig
from django.conf import settings
from pathlib import Path
import toml


class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"

    def ready(self):
        try:
            pyproject_path = Path(settings.BASE_DIR) / "pyproject.toml"
            pyproject_data = toml.load(pyproject_path.open())
            settings.APP_VERSION = pyproject_data.get("project", {}).get(
                "version", "unknown"
            )
        except (FileNotFoundError, toml.TomlDecodeError):
            settings.APP_VERSION = "unknown"
