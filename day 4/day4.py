import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')

# for each line, split the assignments in two, with ',' as delimiter:
#   for each assignment, create list with that assignment range (e.g. 2-4 becomes [2, 3, 4])
#   check if list A contains list B, if not, check if list B contains list A
#   if contains -> add 1 to sum of containing pairs

with open(os.path.join(sys.path[0], "assignments.txt"), "r") as f:
    pairs = f.read().splitlines()
    sum_of_containing_pairs = 0
    sum_of_overlapping_pairs = 0
    for pair in pairs:
        first_pair, second_pair = pair.split(",")
        list_a = [i for i in range(
            int(first_pair.split("-")[0]), int(first_pair.split("-")[1])+1)]
        list_b = [i for i in range(int(second_pair.split("-")[0]), int(second_pair.split("-")[1])+1)]

        if all(num in list_a for num in list_b) or all(num in list_b for num in list_a):
            sum_of_containing_pairs += 1
        
        # part 2
        if any(num in list_a for num in list_b) or any(num in list_b for num in list_a):
            sum_of_overlapping_pairs += 1
        
    print(f"sum of containing pairs: {sum_of_containing_pairs}")
    print(f"sum of overlapping pars: {sum_of_overlapping_pairs}")
