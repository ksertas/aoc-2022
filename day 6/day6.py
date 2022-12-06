import os
import sys


def is_unique(string: str) -> bool:
    return len(set(string)) == len(string)


with open(os.path.join(sys.path[0], "datastream.txt"), "r") as f:
    ds = f.read()
    
    for i in range(len(ds)):
        packet_length = 14 # '4' for part one of puzzle
        packet = ds[i:i+packet_length]
        marker_index = i+packet_length

        if (is_unique(packet)):
            print(marker_index)
            break
