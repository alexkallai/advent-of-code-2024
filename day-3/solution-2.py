from pathlib import Path
import os
from itertools import pairwise
import re

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_string = f.read()

sum = 0
mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
patterns = [mul_pattern, r"don't\(\)", r"do\(\)"]

combined_pattern = '|'.join(patterns)
matches = re.finditer(combined_pattern, file_string)

sum = 0
enabled: bool = True
for find in matches:
    string_find = find.group()
    print(string_find)
    if "don" in string_find:
        enabled = False
    elif "do()" in string_find:
        enabled = True
    elif enabled:
        stripped = string_find.strip()[4:-1]
        first, second = [int(i) for i in stripped.split(",")]
        print(first, " - ", second)
        sum += first * second

print("Solution:", sum)
