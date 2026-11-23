"""Print the one-line roast for the make.fun bounty.

Reads the roast from entry.txt next to this file and prints it.
If the file is missing or empty, a fallback roast is printed instead.
"""

from pathlib import Path


FALLBACK = (
    "My phone dies at 4pm every day, yet somehow still has enough "
    "battery left to ask me to rate the app that drained it."
)


def load_roast() -> str:
    """Return the roast line from entry.txt, or the fallback.

    The entry file holds exactly one line. Anything blank or unreadable
    falls back to the built-in roast so the script always prints a line.
    """
    entry_path = Path(__file__).with_name("entry.txt")
    try:
        text = entry_path.read_text(encoding="utf-8").strip()
    except (FileNotFoundError, OSError):
        return FALLBACK
    return text if text else FALLBACK


if __name__ == "__main__":
    print(load_roast())
