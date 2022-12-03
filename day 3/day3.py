import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')


def find_common_letter(data) -> str:
    # for each group, find the letter that is common among all three sacks in that group
    if isinstance(data, list):
        group = data
        first_sack = group[0]
        second_sack = group[1]
        third_sack = group[2]
        common_letter = ''
        for i in first_sack:
            for j in second_sack:
                if (i == j and i in third_sack):
                    common_letter = i
        return common_letter

    # split each rucksack in two, find letter that is in both split parts:
    #   i at 0, j at 0, if i==j return i, else i++. End of line -> j++, repeat
    if isinstance(data, str):
        string = data
        first_half, second_half = string[:len(
            string)//2], string[len(string)//2:]
        for i in first_half:
            for j in second_half:
                if i == j:
                    return i


def convert_letter_to_priority(ch: str) -> int:
    # minuses to account for ASCII positions
    if ch.isupper():
        number = ord(ch) - 38
    else:
        number = ord(ch) - 96
    return number


def get_sum_of_letters(letters: list) -> int:
    sum = 0
    for letter in letters:
        sum += convert_letter_to_priority(letter)
    return sum


with open(os.path.join(sys.path[0], "rucksacks.txt"), "r") as f:
    rucksacks = f.read().splitlines()
    common_letters = []
    for sack in rucksacks:
        common_letters.append(find_common_letter(sack))

    sum_pt_one = get_sum_of_letters(common_letters)

    print(f"Sum of priorities of all item types: {sum_pt_one}")

    # part 2
    # divide rucksacks in groups of 3.
    groups = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]

    common_letter_per_group = []
    for group in groups:
        common_letter_per_group.append(find_common_letter(group))

    sum_pt_two = get_sum_of_letters(common_letter_per_group)

    print(f"Sum of priorities of all item types: {sum_pt_two}")
