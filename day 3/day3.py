import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')


def find_common_letter(string: str) -> str:
    first_half, second_half = string[:len(string)//2], string[len(string)//2:]
    for i in first_half:
        for j in second_half:
            if i == j:
                return i
    return 'NONE'


def find_common_letter_group(group: list) -> str:
    first_sack = group[0]
    second_sack = group[1]
    third_sack = group[2]
    common_letter = ''
    for i in first_sack:
        for j in second_sack:
            if (i == j and i in third_sack):
                common_letter = i
    return common_letter


def convert_letter_to_alphabet_pos(ch: str) -> int:
    # minuses to account for ASCII positions
    if ch.isupper():
        number = ord(ch) - 38
    else:
        number = ord(ch) - 96
    return number


# split each rucksack in two, find letter that is in both split parts:
#   i at 0, j at 0, if i==j return i, else i++. end of line -> j++, repeat
# find sum:
#   count number positions ('priorities') of common letters together

with open(os.path.join(sys.path[0], "rucksacks.txt"), "r") as f:
    rucksacks = f.read().splitlines()

    all_common_letters = []
    for sack in rucksacks:
        all_common_letters.append(find_common_letter(sack))

    sum_pt_one = 0
    for letter in all_common_letters:
        sum_pt_one += convert_letter_to_alphabet_pos(letter)

    print(f"Sum of priorities of all item types: {sum_pt_one}")

    # part 2
    # divide rucksacks in groups of 3.
    groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]

    # for each group, find the letter that is common among all three sacks in that group. Store that letter in list
    common_letter_per_group = []
    for group in groups:
        common_letter_per_group.append(find_common_letter_group(group))

    # convert all letters in that list to numbers and sum them up -> answer to part 2.
    sum_pt_two = 0
    for letter in common_letter_per_group:
        sum_pt_two += convert_letter_to_alphabet_pos(letter)

    print(f"Sum of priorities of all item types: {sum_pt_two}")
