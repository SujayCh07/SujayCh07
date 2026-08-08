#!/usr/bin/env python3
"""Validate the self-hosted SVG assets used by the profile README."""

from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("hero.svg", "ecosystem.svg", "projects.svg", "telemetry.svg", "route.svg", "stack.svg", "footer.svg")


def main() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for name in REQUIRED:
        path = ROOT / "assets" / name
        if not path.is_file():
            raise SystemExit(f"missing asset: {path}")
        if f"./assets/{name}" not in readme:
            raise SystemExit(f"asset is not referenced by README.md: {name}")
        ElementTree.parse(path)
    print(f"validated {len(REQUIRED)} profile SVG assets")


if __name__ == "__main__":
    main()
