"""Real-Life Patch Notes: The Comedy Changelog — make.fun entry.

Writes one patch-note line (max 160 characters) for a bug in real life:
the mouth auto-replying "you too" when the waiter says "enjoy your meal".
Standard library only; no network; no input beyond this constant.
"""

import os

LINE = "v3.1.4: fixed a bug where the mouth auto-replied 'you too' when the waiter said 'enjoy your meal'."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if not 1 <= len(text) <= 160:
        raise SystemExit("entry must be 1 to 160 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("read-back verification failed")


if __name__ == "__main__":
    main()
