import os
import sys
from enum import Enum
os.system('cls' if os.name == 'nt' else 'clear')


outcome_dict = {
    'rock': {
        'rock': 'draw',
        "paper": 'won',
        'scissors': 'lost'
    },
    'paper': {
        'rock': 'lost',
        "paper": 'draw',
        'scissors': 'won'
    },
    'scissors': {
        'rock': 'won',
        "paper": 'lost',
        'scissors': 'draw'
    }
}

convert_moves = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}
convert_results = {
    'X': 'lost',
    'Y': 'draw',
    'Z': 'won',
}


with open(os.path.join(sys.path[0], "strategy.txt"), "r") as f:
    file_content = f.readlines()
    stripped = []
    for pair in file_content:
        stripped.append(pair.replace(" ", "").rstrip())

    total_score_pt_one = 0
    total_score_pt_two = 0

    for pair in stripped:
        opponent_letter = pair[0]
        opponent_move = convert_moves[opponent_letter]
        your_letter = pair[1]
        your_move = convert_moves[your_letter]
        result = outcome_dict[opponent_move][your_move]

        if your_letter == 'X':
            total_score_pt_one += 1
        if your_letter == 'Y':
            total_score_pt_one += 2
        if your_letter == 'Z':
            total_score_pt_one += 3
        if result == 'won':
            total_score_pt_one += 6
        if result == 'draw':
            total_score_pt_one += 3
        if result == 'lost':
            total_score_pt_one += 0

    print(f"Total score part 1:", total_score_pt_one)

    # part 2
    # based on opponent move, I need to choose a move that will result in desired outcome (2nd letter)
    # for that move, count the points up for total, repeat until end of list

    for pair in stripped:
        opponent_letter = pair[0]
        opponent_move = convert_moves[opponent_letter]
        result_letter = pair[1]
        result_word = convert_results[result_letter]

        # look for what move I should play based on opponent move
        dict_section = outcome_dict[opponent_move]
        your_new_move = list(dict_section.keys())[
            list(dict_section.values()).index(result_word)]

        if your_new_move == 'rock':
            total_score_pt_two += 1
        if your_new_move == 'paper':
            total_score_pt_two += 2
        if your_new_move == 'scissors':
            total_score_pt_two += 3
        if result_word == 'lost':
            total_score_pt_two += 0
        if result_word == 'draw':
            total_score_pt_two += 3
        if result_word == 'won':
            total_score_pt_two += 6

    print(f"Total score part 2:", total_score_pt_two)
