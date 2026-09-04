#!/usr/bin/env python3
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

pages = list(ROOT.rglob("*.md"))
names = {}
for p in pages:
    rel = p.relative_to(ROOT).with_suffix("")
    names[str(rel).replace("\\", "/")] = p
    names[p.stem] = p

link_re = re.compile(r"\[\[([^\]|#]+)")
for p in pages:
    text = p.read_text(encoding="utf-8")
    for target in link_re.findall(text):
        target = target.strip()
        if target not in names and target.replace(".md","") not in names:
            warnings.append(f"Possible broken wiki link: {p.relative_to(ROOT)} -> {target}")
    if "CERTIFIED_CREDIT" in text and p.name not in {"AGENTS.md", "credit-status.md", "calculation-run.md"}:
        warnings.append(f"Review CERTIFIED_CREDIT usage: {p.relative_to(ROOT)}")

profile = ROOT / "data/project-profile.yaml"
if not profile.exists():
    errors.append("Missing data/project-profile.yaml")

print(f"Markdown pages: {len(pages)}")
print(f"Warnings: {len(warnings)}")
for w in warnings:
    print("WARN:", w)
print(f"Errors: {len(errors)}")
for e in errors:
    print("ERROR:", e)

sys.exit(1 if errors else 0)
