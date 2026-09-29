#!/usr/bin/env python3
"""
List every double-brace placeholder token left in the kit, including the ones inside the
Word (.docx) and Excel (.xlsx) templates that a plain-text search cannot see.

Run from the kit root (the folder containing skills/ and templates/):

    python3 skills/msp-setup/scripts/find_tokens.py

Exit code 0 means no tokens remain; 1 means at least one does (each is listed with its file).
msp-setup/SKILL.md and this script are skipped on purpose: they name the tokens as instructions.
"""

import re
import sys
import zipfile
from pathlib import Path

TOKEN = re.compile(r"\{\{[A-Z_]+\}\}")
TEXT_SUFFIXES = {".md", ".py", ".json", ".txt"}
# Where the visible text lives inside each Office format.
OFFICE_PARTS = {".docx": ("word/",), ".xlsx": ("xl/sharedStrings.xml", "xl/worksheets/")}
SKIP = {Path("skills/msp-setup/SKILL.md"), Path("skills/msp-setup/scripts/find_tokens.py")}


def office_text(path):
    prefixes = OFFICE_PARTS[path.suffix]
    with zipfile.ZipFile(path) as z:
        parts = [n for n in z.namelist() if n.endswith(".xml") and n.startswith(prefixes)]
        return "".join(z.read(n).decode("utf-8", "replace") for n in parts)


def main():
    root = Path.cwd()
    if not (root / "skills").is_dir():
        sys.exit("Run this from the kit root (the folder containing skills/ and templates/).")
    found = {}
    for folder in ("skills", "templates"):
        for path in sorted((root / folder).rglob("*")):
            rel = path.relative_to(root)
            if not path.is_file() or rel in SKIP:
                continue
            if path.suffix in TEXT_SUFFIXES:
                text = path.read_text(encoding="utf-8", errors="replace")
            elif path.suffix in OFFICE_PARTS:
                text = office_text(path)
            else:
                continue
            tokens = sorted(set(TOKEN.findall(text)))
            if tokens:
                found[rel] = tokens
    for rel, tokens in found.items():
        print(f"{rel}: {', '.join(tokens)}")
    print(f"\n{len(found)} file(s) still carry placeholder tokens." if found
          else "No placeholder tokens remain.")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
