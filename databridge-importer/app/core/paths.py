from pathlib import Path


def ensure_project_directories() -> None:
    for path in ["data", "data/imports", "data/exports"]:
        Path(path).mkdir(parents=True, exist_ok=True)
