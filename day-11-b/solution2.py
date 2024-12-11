from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    lines = [[int(i) for i in (line.strip().split())] for line in f.readlines()]

array = lines[0]

def get_numbers_based_on_rules(number):
    if number == 0:
        return [1]
    elif len(str(number)) % 2 == 0:
        char_length = len(str(number))
        str_number = str(number)
        half_length = int(char_length / 2)
        number_first = int(str_number[0:half_length])
        number_second = int(str_number[half_length:])
        return [number_first, number_second]
    else:
        return [number * 2024]

new_array = []
blinks = 75
iteration = 0

numbers = {}
for no in array:
    numbers.update({no: 1})
new_numbers = {}

def get_sum():
    sum = 0
    for i in numbers.keys():
        sum += numbers[i]
    return sum

for c in range(blinks):
    print("Cycle:", c)
    iteration += 1
    for no in list(numbers.keys()):
        received = get_numbers_based_on_rules(no)
        number_to_add = numbers[no]
        for res in received:
            if res in new_numbers.keys():
                new_numbers[res] += number_to_add
            else:
                new_numbers.update({res:number_to_add})

    numbers = new_numbers
    new_numbers = {}

print("Solution:", get_sum())