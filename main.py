"""Print the autocorrect-fail entry line (stdlib only).

The entry lives in entry.txt next to this file, so it prints correctly
from any working directory, even on a read-only filesystem.
"""
from pathlib import Path

import sys


def main() -> int:
    entry = Path(__file__).with_name("entry.txt")
    sys.stdout.write(entry.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
