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

sum = 0

def is_safe(line):
    decr_list = [(i[0] > i[1] and abs(i[0]-i[1]) <= 3) for i in pairwise(line)]
    decr_all = all(decr_list)
    incr_list = [(i[0] < i[1] and abs(i[0]-i[1]) <= 3) for i in pairwise(line)]
    incr_all = all(incr_list)
    return decr_all or incr_all

for line in file_lines_list:
    line_length = len(line)
    can_be_dampened_array = []
    for number_idx in range(line_length):
        working_copy: list = list(line)
        working_copy.pop(number_idx)
        if is_safe(working_copy):
            can_be_dampened_array.append(True)
    if any(can_be_dampened_array):
        print("Can be dampened")
        sum += 1
        continue
    if is_safe(line):
        print("Safe")
        sum += 1
    else:
        print("Unsafe")
print(sum)