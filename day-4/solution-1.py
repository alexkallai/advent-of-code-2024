from pathlib import Path
import os
from itertools import pairwise
import re

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = [list(line.strip()) for line in f.readlines()]

search_strings = ["XMAS", "SAMX"]

def rotate_45_matrix(n, m, li):
    generated = []
    ctr = 0
    while(ctr < 2 * n-1):
        print(" "*abs(n-ctr-1), end ="")
        lst = []
        for i in range(m):
            for j in range(n):
                if i + j == ctr:
                    lst.append(li[i][j])
        lst.reverse()
        ctr += 1
        generated.append(lst)
    return generated

def rot_90_matrix(matrix):
    generated = list(list(x) for x in zip(*matrix))[::-1]
    return generated
 
def print_array(array):
    for line in array:
        print(line) 

height = len(file_lines_list)
width = len(file_lines_list[0])

rot_45 = rotate_45_matrix(height, width, file_lines_list)
rot_90 = rot_90_matrix(file_lines_list)
rot_135 = rotate_45_matrix(height, width, rot_90)

found_instances = 0
for matrix in [file_lines_list, rot_45, rot_90, rot_135]:
    for line in matrix:
        string_line = "".join(line)
        for search_string in search_strings:
            found_instances += len(re.findall('(?={0})'.format(re.escape(search_string)), string_line))

print(found_instances)