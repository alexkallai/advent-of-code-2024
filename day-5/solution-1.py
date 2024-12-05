from pathlib import Path
import os
from itertools import pairwise
import re

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = [line.strip() for line in f.readlines()]

sum = 0

page_ordering = []
page_ordering_dict = {}
pages_to_produce = [] # in each update
for line in file_lines_list:
    if "|" in line:
        first, second = [int(no) for no in line.strip().split("|")]
        page_ordering.append([first, second])
        if first in page_ordering_dict.keys():
            page_ordering_dict[first].append(second)
        if not first in page_ordering_dict.keys():
            page_ordering_dict.update({first: [second]})
    if "," in line:
        pages_to_produce.append([int(no) for no in line.strip().split(",")])

def line_correct(line: list[int]) -> bool:
    checks = []
    for ordering in page_ordering:
        if ordering[0] in line and ordering[1] in line:
            if line.index(ordering[0]) < line.index(ordering[1]):
                checks.append(True)
            else:
                checks.append(False)
    return all(checks)

def get_middle(no_list):
    length = len(no_list)
    mid_idx = int(length / 2)
    return no_list[mid_idx]

for line in pages_to_produce:
    mid_no = get_middle(line)
    if line_correct(line):
        sum += mid_no

print(sum)