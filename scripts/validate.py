#!/usr/bin/env python3
"""Validate the repository's agent skills without third-party dependencies."""

from __future__ import annotations

import json
import py_compile
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RESOURCE_RE = re.compile(r"`((?:references|scripts)/[^`]+)`")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_skill(skill_dir: Path) -> str:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        fail(f"missing {skill_file.relative_to(ROOT)}")

    text = skill_file.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not frontmatter:
        fail(f"invalid frontmatter in {skill_file.relative_to(ROOT)}")

    header = frontmatter.group(1)
    name_match = re.search(r"^name:\s*([^\n]+)$", header, re.MULTILINE)
    if not name_match:
        fail(f"missing name in {skill_file.relative_to(ROOT)}")

    name = name_match.group(1).strip().strip('"\'')
    if not NAME_RE.fullmatch(name):
        fail(f"invalid skill name: {name}")
    if name != skill_dir.name:
        fail(f"skill name {name} does not match folder {skill_dir.name}")
    if not re.search(r"^description:\s*(?:>|\S)", header, re.MULTILINE):
        fail(f"missing description in {skill_file.relative_to(ROOT)}")

    metadata = skill_dir / "agents" / "openai.yaml"
    if not metadata.is_file():
        fail(f"missing {metadata.relative_to(ROOT)}")
    metadata_text = metadata.read_text(encoding="utf-8")
    for key in ("display_name:", "short_description:", "default_prompt:"):
        if key not in metadata_text:
            fail(f"missing {key} in {metadata.relative_to(ROOT)}")
    if f"${name}" not in metadata_text:
        fail(f"default prompt does not invoke ${name}")

    if (skill_dir / "README.md").exists():
        fail(f"README.md must stay at repository level, not inside {name}")

    for relative_path in RESOURCE_RE.findall(text):
        if not (skill_dir / relative_path).is_file():
            fail(f"broken resource reference in {name}: {relative_path}")

    for python_file in skill_dir.rglob("*.py"):
        py_compile.compile(str(python_file), doraise=True)

    print(f"OK: {name}")
    return name


def main() -> None:
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    catalog_names = {entry["name"] for entry in catalog["skills"]}
    skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    validated_names = {validate_skill(path) for path in skill_dirs}

    if catalog_names != validated_names:
        fail(f"catalog mismatch: catalog={sorted(catalog_names)}, folders={sorted(validated_names)}")

    subprocess.run(["bash", "-n", str(ROOT / "scripts" / "install.sh")], check=True)
    print(f"Validated {len(validated_names)} skills.")


if __name__ == "__main__":
    main()
