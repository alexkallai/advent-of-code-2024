from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = file_lines_list[index].strip().replace("   ", " ")
# FILE READ IN

left_list = []
right_list = []

for index, line in enumerate(file_lines_list):
    left_number, right_number = [int(a) for a in line.split(" ")]
    left_list.append(left_number)
    right_list.append(right_number)

similarity_score = 0
for number in left_list:
    similarity_score += number * right_list.count(number)

print(similarity_score)