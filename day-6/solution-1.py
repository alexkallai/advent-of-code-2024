from pathlib import Path
import os
from copy import deepcopy

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = [list(line.strip()) for line in f.readlines()]

work_list = deepcopy(file_lines_list)
width = len(file_lines_list[0])
height= len(file_lines_list)

def get_init_pos():
    for y_idx, line in enumerate(file_lines_list):
        for x_idx, line2 in enumerate(line):
            if "^" in line2:
                return y_idx, x_idx

def get_dir():
    return dirs[dir_changes % 4]

init_y, init_x = get_init_pos()
print(init_y, init_x)
runner_y, runner_x = init_y, init_x

dirs = [(-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)]

dir_changes = 0
direction = get_dir()
while runner_x < width - 1 and runner_y < height - 1:
    work_list[runner_y][runner_x] = "X"
    next_y = runner_y + direction[0]
    next_x = runner_x + direction[1]
    if file_lines_list[next_y][next_x] == "#":
        # Turn right
        dir_changes += 1
        direction = get_dir()
        continue
    else:
        runner_y = next_y
        runner_x = next_x
distinct_locations = 1
for line in work_list:
    print(line)
    for char in line:
        if char == 'X':
            distinct_locations += 1
print(distinct_locations)



    #UP = (-1, 0)
    #RIGHT = (0, 1)
    #DOWN = (1, 0)
    #LEFT = (0, -1)