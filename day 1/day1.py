import os
import sys
import re
os.system('cls' if os.name == 'nt' else 'clear')

# get file. then, count how many elves:
#   between two elves, there are 2 whitespaces (regex: \s\s),
#   so number of elves: total parts that were spliced -> length of spliced array.
# add up how many calories total each elf has, biggest calorie count is answer


def convert_strings_to_ints(strings: list) -> list:
    return [int(x) for x in strings]


def strip_part_of_whitespace(part: list) -> list:
    return re.split("\s", part)


with open(os.path.join(sys.path[0], "calories.txt"), "r") as f:
    file_content = f.read()
    split_elves = re.split("\s\s", file_content)

    list_of_sums = []

    for i in range(len(split_elves)):

        if (i == len(split_elves)-1):
            stripped_list = strip_part_of_whitespace(
                split_elves[len(split_elves)-1][:-1])  # removing last character of file ("\n") before stripping other whitespace
        else:
            stripped_list = strip_part_of_whitespace(split_elves[i])

        list_of_ints = convert_strings_to_ints(stripped_list)
        list_of_sums.append(sum(list_of_ints))

    print("Largest number of total calories is: ", max(list_of_sums))
