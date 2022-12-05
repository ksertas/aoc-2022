import os
import sys
import re
from pprint import pprint

# remove text per command so only the numbers are left over
def extract_arguments_from_command(command: str) -> tuple:
    target_containers, source, destination = re.findall(r'\b\d+\b', command)
    return int(target_containers), int(source), int(destination)

with open(os.path.join(sys.path[0], "crates.txt"), "r") as f:
    commands = f.read().splitlines()[10:]
    stacks = {
        1: 'TRGWQMFP',
        2: 'RFH',
        3: 'DSHGVRZP',
        4: 'GWFBPHQ',
        5: 'HJMSP',
        6: 'LPRSHTZM',
        7: 'LMNHTP',
        8: 'RQDF',
        9: 'HPLNCSD'
    } 

    # convert each value per key to list of str characters
    for key in stacks:
        stacks[key] = list(stacks[key])

    arguments_per_command = [extract_arguments_from_command(command) for command in commands]
    
    for command in arguments_per_command:
        target_containers: int = command[0] # move this many containers
        source: int = command[1] # from this list
        destination: int = command[2] # to this list
        taken_containers = stacks[source][:target_containers] # grab the target containers
        stacks[destination][0:0] = reversed(stacks[source][:target_containers]) # insert taken containers on top of destination stack
        del stacks[source][:target_containers] # remove the taken containers from the source 
    
    crates_on_top_each_stack = [stacks[i][0] for i in stacks] # select only the top crate of each stack
    print(f"Crates on top of each stack are: {crates_on_top_each_stack}")
