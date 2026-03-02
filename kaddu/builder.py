import os
from pathlib import Path
from .models import Node


def build_tree(
    node: Node,
    base_path: Path,
    dry_run: bool = False,
    force: bool = False,
) -> None:
    path = base_path / node.name

    if node.is_file:
        if path.exists() and not force:
            raise FileExistsError(f"File exists: {path}")

        if dry_run:
            print(f"[DRY RUN] Create file: {path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch(exist_ok=force)
            print(f"Created file: {path}")

    else:
        if path.exists() and not force:
            raise FileExistsError(f"Directory exists: {path}")

        if dry_run:
            print(f"[DRY RUN] Create directory: {path}")
        else:
            path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {path}")

        for child in node.children:
            build_tree(child, path, dry_run=dry_run, force=force)