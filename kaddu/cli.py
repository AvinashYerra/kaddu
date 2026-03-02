import argparse
import sys
from pathlib import Path
from .parser import parse_structure
from .builder import build_tree


def main():
    parser = argparse.ArgumentParser(
        description="Generate project structure from LLM folder structure output"
    )

    parser.add_argument("file", help="Path to structure markdown file")

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without creating files",
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files and directories",
    )

    args = parser.parse_args()

    structure_path = Path(args.file)

    if not structure_path.exists():
        print("Error: Structure file not found.")
        sys.exit(1)

    try:
        content = structure_path.read_text(encoding="utf-8")

        root = parse_structure(content)

        build_tree(
            root,
            base_path=Path.cwd(),
            dry_run=args.dry_run,
            force=args.force,
        )

        if not args.dry_run:
            print("\nProject structure created successfully.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)