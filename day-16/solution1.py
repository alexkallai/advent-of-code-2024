from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    lines = [list(line.strip()) for line in f.readlines()]

def get_point(character: str):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if lines[i][j] == character:
                return (i, j)

start_coord = get_point("S")
end_coord = get_point("E")

dirs = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]

moves = 0
rotations = 0

curr_dir = dirs[1]
curr_char = lines[start_coord[0]][start_coord[1]]
while curr_char != "E":
    for dir in dirs
pass