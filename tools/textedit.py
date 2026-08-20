"""Shared helpers for the copy-editing passes.

Paragraphs are matched on their text with whitespace collapsed, so the source
indentation and line wrapping do not have to be reproduced in the edit tables.
"""

from __future__ import annotations

import re
import textwrap

PARAGRAPH_RE = re.compile(r"([ \t]*)<p>(?!<)(.*?)</p>", re.DOTALL)
WRAP_WIDTH = 110


def apply_paragraphs(text: str, table: dict[str, str]) -> str:
    """Replace whole <p> bodies, re-wrapping to match the surrounding source."""

    def fix(match: re.Match) -> str:
        indent, body = match.group(1), match.group(2)
        replacement = table.get(" ".join(body.split()))
        if replacement is None:
            return match.group(0)
        wrapped = textwrap.fill(
            replacement,
            width=WRAP_WIDTH,
            initial_indent=indent + "    ",
            subsequent_indent=indent + "    ",
        )
        return f"{indent}<p>\n{wrapped}\n{indent}</p>"

    return PARAGRAPH_RE.sub(fix, text)


def apply_snippets(text: str, table: dict[str, str]) -> str:
    """Plain string replacements, for headings, captions and part-sentences."""
    for old, new in table.items():
        text = text.replace(old, new)
    return text
