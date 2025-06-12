import os
from pathlib import Path

PROJECT_NAME = "mir-model-collection"


def get_cache_dir() -> Path:
    if os.name == "nt":
        p = Path(os.environ["LOCALAPPDATA"]) / PROJECT_NAME
    else:
        p = Path.home() / ".cache" / PROJECT_NAME

    p.mkdir(parents=True, exist_ok=True)

    return p
