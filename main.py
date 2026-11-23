#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

The joke: a corporate "per my last email" standoff where the
escalation is that the fire in the server room is literal.
Standard library only, deterministic, no network.
"""

JOKE = (
    'Per my last email, the server room is still on fire \u2014 and per '
    'this email, I\u2019ve stopped clarifying that "fire" is literal.'
)


def main() -> None:
    import os

    # The grader mounts the output dir at /output; honour the
    # harness variable when it is set so a local run behaves the same.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Self-check against the gate: 1-199 chars, not only whitespace.
    written = open(path, encoding="utf-8").read()
    if not 1 <= len(written) <= 199 or not written.strip():
        raise SystemExit("gate check failed: entry.txt is %d chars" % len(written))


if __name__ == "__main__":
    main()
