from pathlib import Path
import os
import itertools

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = [line.strip() for line in f.readlines()]

equations = []
for line in file_lines_list:
    first_number = int(line.split(":")[0].strip())
    numbers = [int(i) for i in line.split(":")[-1].strip().split()]
    equations.append((first_number, numbers))

total_res = 0

def add(a, b):
    return a+b

def mult(a, b):
    return a*b

operations = [add, mult]

for line in equations:
    numbers = line[1]
    length = len(numbers)
    if length < 2:
        continue
    possible_operator_locations = length - 1
    possible_combinations = list(itertools.product(operations, repeat=possible_operator_locations))
    for ops in possible_combinations:
        result = line[1][0]
        for i, number in enumerate(numbers[:-1]):
            result = ops[i](result, numbers[i+1])
        if result == line[0]:
            total_res += line[0]
            #print("Correct:", result)
            break
        else:
            pass
            #print("Incorrect:", result)
print("Total:", total_res)