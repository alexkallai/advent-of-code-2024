from pathlib import Path
import os
from itertools import pairwise
import re

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

sum = 0
pattern = r"mul\(\d{1,3},\d{1,3}\)"
for test in file_lines_list:
    match = re.findall(pattern, test)
    for find in match:
        print(find)
        stripped = find.strip()[4:-1]
        first, second = [int(i) for i in stripped.split(",")]
        print(first, " - ", second)
        sum += first * second
print("Solution", sum)
