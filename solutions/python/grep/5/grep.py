"""
Grep Utility
"""
import re
from re import Match

OPTION_FLAGS: list[str] = ["n", "l", "i", "v", "x"]

def grep(pattern: str, flags: str, files: list[str]) -> str:
    """
    Grep Utility method that supports these options:

    - `-n` Prepend the line number and a colon (':') to each line in the output, placing the number after the filename (if present).
    - `-l` Output only the names of the files that contain at least one matching line.
    - `-i` Match using a case-insensitive comparison.
    - `-v` Collect all lines that fail to match.
    - `-x` Search only for lines where the search string matches the entire line.

    :param pattern: Pattern to search for
    :param flags: Flag of options
    :param files:
    :return:
    """
    options: list[str] = list(flags.replace("-", "").replace(" ", ""))
    if any(option not in OPTION_FLAGS for option in options):
        raise ValueError("Invalid option, must be -n, -l, -i, -v, or -x")

    pattern = re.escape(pattern.rstrip())
    if "x" in options:
        pattern = r"^" + pattern + r"$"

    result: list[str] = []
    try:
        for filename in files:
            filename_set: bool = False
            with open(filename, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file):
                    search: Match[str] | None = re.search(pattern, line, re.I) if "i" in options else re.search(pattern, line)
                    if (search and "v" not in options) or (not search and "v" in options):
                        if "l" not in options and len(files) > 1:
                            result.append(f"{filename}:")
                        if "l" in options:
                            if not filename_set:
                                result.append(f"{filename}\n")
                                filename_set = True
                        elif "n" in options:
                            result.append(f"{line_number + 1}:" + line)
                        else:
                            result.append(line)
    except FileNotFoundError as e:
        raise ValueError("File not found") from e
    return "".join(result)