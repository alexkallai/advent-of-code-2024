from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    lines = [list(line.strip()) for line in f.readlines()]

input = lines[0]

print(input)

class CustomString(str):
    def __new__(cls, value, index):
        # Create the string instance using the parent class's __new__
        instance = super().__new__(cls, value)
        # Store additional information
        instance.index = index
        return instance

    def __repr__(self):
        return f"CustomString('{self}', additional_info={self.index})"

max_file_index = 0
def decompress(input: list):
    global max_file_index
    new_list = []
    is_file = True
    file_index = 0
    for index, char in enumerate(input):
        char_no = int(char)
        if is_file:
            is_file = False
            new_list.extend([CustomString(3, index=file_index) for i in range(char_no)])
            max_file_index = file_index
            file_index += 1
            continue

        if not is_file:
            is_file = True
            new_list.extend(["." for i in range(char_no)])
            continue
    return new_list

decomp_list = decompress(input)
print("".join(decomp_list))
work_list = decomp_list

def organized(work_list):
    numbers_ended = False
    for char in work_list:
        if not char.isalnum():
            numbers_ended = True
        if numbers_ended:
            if char != ".":
                return False
    return True

def get_last_non_alphanumeric_index(s):
    for i in range(len(s) - 1, -1, -1):
        if not s[i].isalnum():
            return i
    return -1

def get_last_alphanumeric_index(s):
    for i in range(len(s) - 1, -1, -1):
        if s[i].isalnum():
            return i
    return -1

length = len(work_list)
for i in range(len(s) - 1, -1, -1):
#while not organized(work_list):
    #text = "".join(work_list)
    #first_dot_location = text.index(".")
    #last_alpha = get_last_alphanumeric_index(text)

    #if first_dot_location < last_alpha:
        #work_list[first_dot_location] = work_list[last_alpha]
        #work_list[last_alpha] = "."


checksum = 0
for i, char in enumerate(work_list):
    if char.isalnum():
        no = int(char.index)
        checksum += i * no
    pass
pass
print(checksum)
