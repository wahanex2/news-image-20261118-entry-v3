#!/usr/bin/env python3
"""Publish the bundled news-image entry.

The entry image lives next to this script as ``entry.png``.  Running this
program drops an exact copy of it at ``$MAKEFUN_OUTPUT_DIR/entry.png``
(``/output/entry.png`` when the variable is unset) and then proves the
copy is intact by comparing SHA-256 digests.  Nothing here touches the
network, a model, or the clock, so the result is identical every run.
"""

import hashlib
import os
import sys
from pathlib import Path

MAX_ENTRY_BYTES = 1_048_576
ENTRY_FILENAME = "entry.png"


def die(message):
    """Print an error and stop with a non-zero status."""
    print(f"main.py: {message}", file=sys.stderr)
    sys.exit(1)


def digest(path):
    """Return the hex SHA-256 of the file at *path*."""
    hasher = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main():
    script_dir = Path(__file__).resolve().parent
    source = script_dir / ENTRY_FILENAME

    if not source.is_file():
        die(f"missing entry image: {source}")

    payload = source.read_bytes()
    if len(payload) > MAX_ENTRY_BYTES:
        die(
            f"entry image is {len(payload)} bytes, over the "
            f"{MAX_ENTRY_BYTES}-byte limit"
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    destination = Path(out_dir) / ENTRY_FILENAME
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)
    except OSError as exc:
        die(f"could not write {destination}: {exc}")

    if digest(destination) != hashlib.sha256(payload).hexdigest():
        die("written copy failed its SHA-256 check")

    print(f"wrote {destination} ({len(payload)} bytes, sha256 OK)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
