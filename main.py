#!/usr/bin/env python3
"""Remove active SVG content and unsafe references from local SVG files."""
from __future__ import annotations
import argparse, re, sys, xml.etree.ElementTree as ET
from pathlib import Path

DANGEROUS_TAGS = {"script", "foreignobject", "iframe", "object", "embed"}
UNSAFE_CSS = re.compile(r"""@import|expression\s*\(|url\s*\(\s*['"]?(?!#)""", re.IGNORECASE)

def local_name(name: str) -> str:
    return name.rsplit("}", 1)[-1].lower()

def clean_attributes(element: ET.Element, stats: dict[str, int]) -> None:
    for key, value in list(element.attrib.items()):
        name = local_name(key)
        if name.startswith("on"):
            del element.attrib[key]; stats["event_attributes"] += 1
        elif name in {"href", "src"} and value.strip() and not value.strip().startswith("#"):
            del element.attrib[key]; stats["external_references"] += 1
        elif name == "style" and UNSAFE_CSS.search(value):
            del element.attrib[key]; stats["unsafe_styles"] += 1

def clean_children(parent: ET.Element, stats: dict[str, int]) -> None:
    for child in list(parent):
        name = local_name(child.tag)
        if name in DANGEROUS_TAGS or (name == "style" and UNSAFE_CSS.search(child.text or "")):
            parent.remove(child); stats["removed_elements"] += 1; continue
        clean_attributes(child, stats); clean_children(child, stats)

def sanitize(source: Path):
    stats = {"removed_elements": 0, "event_attributes": 0, "external_references": 0, "unsafe_styles": 0}
    root = ET.parse(source).getroot()
    clean_attributes(root, stats); clean_children(root, stats)
    return root, stats

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path); parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("--check", action="store_true", help="report unsafe content without writing")
    args = parser.parse_args()
    if not args.input.is_file(): parser.error(f"input file does not exist: {args.input}")
    try: root, stats = sanitize(args.input)
    except (ET.ParseError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr); return 2
    total = sum(stats.values()); print(f"Findings removed: {total}")
    for key, value in stats.items(): print(f"  {key.replace('_', ' ')}: {value}")
    if args.check: return 1 if total else 0
    output = args.output or args.input.with_name(args.input.stem + ".clean.svg")
    try:
        ET.indent(root, space="  ")
        ET.ElementTree(root).write(output, encoding="utf-8", xml_declaration=True)
    except OSError as exc:
        print(f"error writing {output}: {exc}", file=sys.stderr); return 2
    print(f"Cleaned SVG written to {output}"); return 0

if __name__ == "__main__":
    raise SystemExit(main())
