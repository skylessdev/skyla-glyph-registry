"""
Generator script to build zine issues from registry.json.
Run this manually or as a GitHub Action.
"""

import json
from datetime import date

with open("registry.json", "r") as f:
    registry = json.load(f)

issue_lines = ["# 🧬 Auto-Generated Zine Entry\n", f"Date: {date.today()}\n"]

for glyph in registry:
    line = f"- {glyph['glyph']} \"{glyph['phrase']}\" → `{glyph['trigger']}`"
    issue_lines.append(line)

with open("zine/issues/auto-generated.md", "w") as out:
    out.write("\n".join(issue_lines))
