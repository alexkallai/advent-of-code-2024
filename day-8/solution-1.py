from pathlib import Path
import os
from copy import deepcopy
import itertools

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    lines = [list(line.strip()) for line in f.readlines()]

work_list = deepcopy(lines)
width = len(lines[0])
height= len(lines)

def is_coord_valid(coord):
    if 0 <= coord[0] < width and 0 <= coord[1] < height:
        return True
    return False

char_locations = {}
for ir, line in enumerate(lines):
    for il, char in enumerate(line):
        if char != ".":
            if char in char_locations.keys():
                char_locations[char].append((ir, il))
            else:
                char_locations.update({char: [(ir, il)]})

all_valid_locations = []
for char in char_locations.keys():
    coords = char_locations[char]
    if len(coords) < 2:
        continue
    # get all pairs
    possible_combinations = list(itertools.product(coords, repeat=2))
    for pair in possible_combinations:
        elem1 = pair[0]
        elem2 = pair[1]
        diff = (elem1[0] - elem2[0], elem1[1] - elem2[1])
        if diff[0] == 0 and diff[1] == 0:
            continue
        loc_1 = (elem1[0] + diff[0], elem1[1] + diff[1])
        loc_2 = (elem2[0] - diff[0], elem2[1] - diff[1])
        if is_coord_valid(loc_1):
            all_valid_locations.append(loc_1)
        if is_coord_valid(loc_2):
            all_valid_locations.append(loc_2)

for loc in all_valid_locations:
    work_list[loc[0]][loc[1]] = "#"
locations_merged = set(all_valid_locations)
print(len(locations_merged))