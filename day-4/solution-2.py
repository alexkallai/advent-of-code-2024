from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = [list(line.strip()) for line in f.readlines()]

height = len(file_lines_list)
width = len(file_lines_list[0])

number_of_x_mas = 0
for x in list(range(width))[1:-1]:
    for y in list(range(height))[1:-1]:
        if file_lines_list[x][y] == "A":
            chars = "MS"
            left_up = file_lines_list[x-1][y-1]
            right_down = file_lines_list[x+1][y+1]
            left_down = file_lines_list[x-1][y+1]
            right_up = file_lines_list[x+1][y-1]

            if ((left_up != right_down) and 
                (left_down != right_up) and 
                (left_up in chars) and 
                (right_down in chars) and 
                (left_down in chars) and 
                (right_up in chars)):

                number_of_x_mas += 1

print(number_of_x_mas)