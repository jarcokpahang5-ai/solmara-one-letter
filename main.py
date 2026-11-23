"""One Letter for Your Day — make.fun entry.

The entry is exactly one character, a letter from A to Z, and nothing
else. The letter is Z: the word behind it is "zero sleep", after a night
of hourly bounty runs. It is validated, printed, and written to
/output/entry.txt with no trailing newline, so the file holds exactly
one character.
Pure Python 3.13 standard library only; deterministic; no network.
"""

import os
import string

LETTER = "Z"  # the word behind it: zero sleep

OUTPUT_PATH = "/output/entry.txt"


def validate_letter(letter: str) -> str:
    """Validate the entry is exactly one letter from A to Z."""
    if not isinstance(letter, str):
        raise ValueError("letter must be a string")
    if len(letter) != 1 or letter not in string.ascii_uppercase:
        raise ValueError("entry must be exactly one letter from A to Z")
    return letter


def main() -> None:
    letter = validate_letter(LETTER)
    print(letter)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(letter)


if __name__ == "__main__":
    main()
