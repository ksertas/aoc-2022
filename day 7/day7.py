import os
import sys
from collections import defaultdict

with open (os.path.join(sys.path[0], "directories.txt"), "r") as f:
    lines = f.read().splitlines()
    current_dir = []
    dir_and_size = defaultdict(int) # paths won't have initial values, so default will be int() to prevent KeyError
    for line in lines:
        words = line.split()
        if words[1] ==  "cd":
            if words[2] == "..":
                current_dir.pop()
            else:
                current_dir.append(words[2])
        if words[0][0].isdigit():
            size = int(words[0])
            for i in range(1, len(current_dir)+1): # i=1 because i in [:i] is exclusive
                dir_and_size['/'.join(current_dir[:i])] += size # put size next to current path
    
    total_space_device = 70000000
    space_required_for_update = 30000000
    space_used = dir_and_size['/']
    available_size = total_space_device - space_used
    space_to_free = space_required_for_update - available_size

    sum_total_sizes_directories = 0
    min_sized_dir = 9999999
    for path, value in dir_and_size.items():
        if value <= 100000:
            sum_total_sizes_directories += value
        if value >= space_to_free:
            min_sized_dir = min(value, min_sized_dir) 
        
    print('part one: ', sum_total_sizes_directories)
    print('part two: ', min_sized_dir)
