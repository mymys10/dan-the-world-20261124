"""Entry program for the news-image-20261124 bounty.

The repository holds the finished one-page image, entry.png,
next to this file. All this program does is place a copy of
that image where the grader looks for it: the directory named
by the MAKEFUN_OUTPUT_DIR environment variable, falling back
to /output when the variable is not set.

It uses only the standard library, touches no network, and
writes the same bytes on every run, because it copies one
fixed file. The output name stays entry.png, as the brief
requires.
"""

import os
import shutil
from pathlib import Path


def output_folder():
    """Where the finished image has to land."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not wanted:
        wanted = "/output"
    return Path(wanted)


def source_image():
    """The image shipped in this repository, beside this file."""
    return Path(__file__).resolve().parent / "entry.png"


def main():
    destination = output_folder()
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source_image(), destination / "entry.png")


if __name__ == "__main__":
    main()
