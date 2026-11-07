"""
Python Basics — practice code
=============================

This topic is split into several small files so each one stays focused.
See the files inside the `01_basics/` folder:

  01_basics/01_literals.py     — int, float, string, bool, None, list/tuple/set/dict, ...
  01_basics/02_variables.py    — naming, dynamic typing, scope, unpacking, copy trap
  01_basics/03_keywords.py     — list all 35 Python keywords

Run one of them directly:
  python 01_basics/01_literals.py
  python 01_basics/02_variables.py
  python 01_basics/03_keywords.py

Or run all of them in order:
  python 01_basics.py
"""

import runpy
from pathlib import Path

FOLDER = Path(__file__).parent / "01_basics"


def main():
    for script in sorted(FOLDER.glob("*.py")):
        print(f"\n########## {script.name} ##########\n")
        runpy.run_path(str(script), run_name="__main__")


if __name__ == "__main__":
    main()
