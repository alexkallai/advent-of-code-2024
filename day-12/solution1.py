from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    lines = [list(line.strip()) for line in f.readlines()]

width = len(lines[0])
height = len(lines)
dirs = [(-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)]
processed_coords = []
list_of_gardens = []

def collect_plots_recur(current_list: list):

    curr_value = lines[current_list[-1][0]][current_list[-1][1]]
    processed_coords.append(current_list[-1])

    for dir in dirs:
        nc = (current_list[-1][0] + dir[0], current_list[-1][1] + dir[1]) 
        if 0 <= nc[0] < height and 0 <= nc[1] < width:
            if (nc[0], nc[1]) not in processed_coords:
                # if next coord is current + 1
                next_value = lines[nc[0]][nc[1]]
                if next_value == curr_value:
                    return collect_plots_recur(current_list + [(nc[0], nc[1])])
    return current_list

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        coord = (i, j)
        if coord not in processed_coords:
            garden_elems = collect_plots_recur([coord])
            list_of_gardens.append(garden_elems)
            pass

#for garden in list_of_gardens:
    #for coord in garden:
        #print(lines[coord[0]][coord[1]], end="")
    #print("\n")

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