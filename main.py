"""One-Line Office Jokes: a funny office-life line.

Writes one office joke to /output/entry.txt. Stdlib only, no
network, deterministic: the same joke on every run.
"""

import io
import os

JOKE = "My manager scheduled a meeting to discuss why we have too many meetings, then scheduled a follow-up."


def main() -> None:
    output = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output, exist_ok=True)
    target = os.path.join(output, "entry.txt")
    with io.open(target, "w", encoding="utf-8", newline="\n") as out:
        out.write(JOKE + "\n")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
