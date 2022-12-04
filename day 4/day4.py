import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')

with open(os.path.join(sys.path[0], "assignments.txt"), "r") as f:
    assignments = f.read().splitlines()
    sum_of_containing_assignments = 0
    sum_of_overlapping_assignments = 0

    for pairs in assignments:
        # for each line, split the assignments in two, with ',' as delimiter
        first_pair, second_pair = pairs.split(",")

        # for each assignment, create list with that assignment range (e.g. 2-4 becomes [2, 3, 4])
        list_a = [i for i in range(int(first_pair.split("-")[0]), int(first_pair.split("-")[1])+1)]
        list_b = [i for i in range(int(second_pair.split("-")[0]), int(second_pair.split("-")[1])+1)]

        # check if list A contains list B or if list B contains list A
        if all(num in list_a for num in list_b) or all(num in list_b for num in list_a):
            sum_of_containing_assignments += 1
        
        # part 2
        # check if any number in list A overlaps with a number in list B or vice versa
        if any(num in list_a for num in list_b) or any(num in list_b for num in list_a):
            sum_of_overlapping_assignments += 1
        
    print(f"sum of containing pairs: {sum_of_containing_assignments}")
    print(f"sum of overlapping pairs: {sum_of_overlapping_assignments}")
