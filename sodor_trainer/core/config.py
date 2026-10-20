from dataclasses import dataclass, field
from pathlib import Path
import tomllib


@dataclass
class TrainerConfig:
    target_process: str = "WondersOfSodor.exe"
    require_admin: bool = True
    esp_enabled: bool = True
    esp_max_distance: float = 450.0
    teleport_hotkey: str = "F7"
    godmode_hotkey: str = "F8"
    overlay_fps: int = 144
    feature_flags: dict = field(default_factory=dict)


def load_config(path: Path) -> TrainerConfig:
    if not path.exists():
        return TrainerConfig()
    raw = tomllib.loads(path.read_text(encoding="utf-8"))
    section = raw.get("trainer", {})
    return TrainerConfig(**{k: v for k, v in section.items() if hasattr(TrainerConfig, k)})