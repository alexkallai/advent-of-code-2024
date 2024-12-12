from pathlib import Path
import os
from collections import deque

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    lines = [list(line.strip()) for line in f.readlines()]

width = len(lines[0])
height = len(lines)
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
processed_coords = set() 
list_of_gardens = []


def collect_plots_iterative(start_coord):
    queue = deque([start_coord])  
    curr_value = lines[start_coord[0]][start_coord[1]]
    garden = []

    while queue:
        coord = queue.popleft()
        if coord in processed_coords:
            continue

        processed_coords.add(coord) 
        garden.append(coord)

        for dir in dirs:
            nc = (coord[0] + dir[0], coord[1] + dir[1])
            if (
                0 <= nc[0] < height
                and 0 <= nc[1] < width
                and nc not in processed_coords
                and lines[nc[0]][nc[1]] == curr_value
            ):
                queue.append(nc)
    return garden


for i, line in enumerate(lines):
    for j, char in enumerate(line):
        coord = (i, j)
        if coord not in processed_coords:
            garden_elems = collect_plots_iterative(coord)
            list_of_gardens.append(garden_elems)

def get_number_of_neighbours(garden, coord):
    sum = 0
    for dir in dirs:
        if (coord[0]+dir[0], coord[1]+dir[1]) in garden:
            sum += 1
    return sum

neighbour_fence_len_map = {
    0: 4,
    1: 3,
    2: 2,
    3: 1,
    4: 0
}

total_fencing = 0
for garden in list_of_gardens:
    current_char = lines[garden[0][0]][garden[0][1]]
    cur_area = len(garden)
    sum_of_garden = 0
    fence_len = 0
    for coord in garden:
        fence_len += neighbour_fence_len_map[get_number_of_neighbours(garden, coord)]
    
    sum_of_garden = fence_len * cur_area
    total_fencing += sum_of_garden
    print(current_char, sum_of_garden)

print(total_fencing)
pass