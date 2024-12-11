from pathlib import Path
import os
from copy import deepcopy

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    lines = [(line.strip()) for line in f.readlines()]

for index, line in enumerate(lines):
    lines[index] = [int(a) if a.isalnum() else ' ' for a in list(lines[index].strip())]

width = len(lines[0])
height = len(lines)
dirs = [(-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)]

def debug_print(current_list):
    work_copy = deepcopy(lines)
    for coord in current_list:
        work_copy[coord[0]][coord[1]] = "X"
    for line in work_copy:
        print([str(i) for i in line])
    print("\n")

available_heads = {}
def search_next_recur(current_list: list):
    global lines
    global dirs

    curr_value = lines[current_list[-1][0]][current_list[-1][1]]

    start_coord = current_list[0]
    #debug_print(current_list)
    for dir in dirs:
        nc = (current_list[-1][0] + dir[0], current_list[-1][1] + dir[1]) 
        if 0 <= nc[0] < height and 0 <= nc[1] < width:
            if (nc[0], nc[1]) not in current_list:
                # if next coord is current + 1
                next_value = lines[nc[0]][nc[1]]
                if next_value == curr_value + 1:
                    if next_value == 9:
                        if start_coord in available_heads:
                            available_heads[start_coord].append(nc)
                        else:
                            available_heads.update({start_coord: [nc]})
                        
                        continue
                    search_next_recur(current_list + [(nc[0], nc[1])])


for i, line in enumerate(lines):
    for j, no in enumerate(line):
        if lines[i][j] == 0:
            coord = (i, j)
            search_next_recur([(i, j)])


# 640 too high
sum = 0
for key in available_heads.keys():
    sum += len(set(available_heads[key]))
print(sum)
pass