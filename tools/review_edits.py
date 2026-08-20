"""Print every copy edit made by the passes, as before -> after.

The passes applied rules. Rules kill good lines as happily as bad ones, so this
dumps the lot for a human read-through.

    python tools/review_edits.py            # everything
    python tools/review_edits.py cull        # one pass
"""

from __future__ import annotations

import importlib
import sys

PASSES = [
    ("tone", "tone_pass", ["REPLACEMENTS"]),
    ("voice", "voice_pass", ["HEADINGS", "PARAGRAPHS", "CAPTIONS", "SNIPPETS"]),
    ("humility", "humility_pass", ["PARAGRAPHS", "SNIPPETS", "PER_PAGE"]),
    ("sharpen", "sharpen_pass", ["PARAGRAPHS"]),
    ("cull", "cull_pass", ["PARAGRAPHS", "SNIPPETS"]),
    ("stub-copy", "stub_copy", ["COPY"]),
    ("stub-head", "stub_headings", ["HEADINGS"]),
]


def strip_tags(value: str) -> str:
    import re

    return re.sub(r"<[^>]+>", "", value).strip()


def main() -> int:
    only = sys.argv[1] if len(sys.argv) > 1 else None
    total = 0
    for label, module_name, tables in PASSES:
        if only and only not in label:
            continue
        module = importlib.import_module(module_name)
        for table_name in tables:
            table = getattr(module, table_name, None)
            if not isinstance(table, dict):
                continue
            # PER_PAGE is a dict of dicts
            items = []
            for key, value in table.items():
                if isinstance(value, dict):
                    items.extend(value.items())
                elif isinstance(value, tuple):
                    items.append((key, " / ".join(value)))
                else:
                    items.append((key, value))
            for before, after in items:
                before_text, after_text = strip_tags(str(before)), strip_tags(str(after))
                if before_text == after_text:
                    continue
                total += 1
                print(f"--- {label}/{table_name}")
                print(f"  -  {before_text}")
                print(f"  +  {after_text}")
    print(f"\n{total} edits")
    return 0


if __name__ == "__main__":
    sys.exit(main())
