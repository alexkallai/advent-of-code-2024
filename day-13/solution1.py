from pathlib import Path
import os
from collections import deque

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    lines = [(line.strip()) for line in f.readlines()]

tokens = {
    "A": 3,
    "B": 1
}


for i, line in enumerate(lines):

pass