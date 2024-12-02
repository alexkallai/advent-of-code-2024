from pathlib import Path
import os
from itertools import pairwise

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = [int(a) for a in file_lines_list[index].strip().split(" ")]
# FILE READ IN

is_decreasing = True
is_increasing = True

sum = 0
for line in file_lines_list:
    decr_list = [(i[0] > i[1] and abs(i[0]-i[1]) <= 3) for i in pairwise(line)]
    decr_any = all(decr_list)
    incr_list = [(i[0] < i[1] and abs(i[0]-i[1]) <= 3) for i in pairwise(line)]
    incr_any = all(incr_list)
    if decr_any or incr_any:
        print("Safe")
        sum += 1
    else:
        print("Unsafe")
print(sum)