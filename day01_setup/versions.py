"""Day 1: confirm the environment works."""
import platform
import sys

import matplotlib
import numpy
import pandas

print(f"Python     {sys.version.split()[0]} on {platform.system()}")
for mod in (numpy, pandas, matplotlib):
    print(f"{mod.__name__:<10} {mod.__version__}")
