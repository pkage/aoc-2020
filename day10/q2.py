#! /usr/bin/env python3

import sys
from copy import deepcopy

adapters_original = open('input.txt', 'r').readlines()

# all adapters are unique
adapters_original = set(map(lambda x: int(x), adapters_original))

# find max jolts (largest adapter + 3)
MAX_DEVICE_JOLTS = max(adapters_original) + 3
print('maximum joltage: {}'.format(MAX_DEVICE_JOLTS))

# find what 
def find_compatible(adapters, rating):
    out = set()
    if (rating + 1) in adapters:
        out.add(rating + 1)
    if (rating + 2) in adapters:
        out.add(rating + 2)
    if (rating + 3) in adapters:
        out.add(rating + 3)

    if len(out) == 0:
        return None
    return out

def find_path(adapters, path=[0]):
    # get the last adapter
    head = path[-1]

    if len(path) == len(adapters_original) + 1:
        if (head) <= MAX_DEVICE_JOLTS:
            path.append(MAX_DEVICE_JOLTS)
            return path
        return None


    compatibles = find_compatible(adapters, head)
    if compatibles is None:
        return None
    
    for compat in compatibles:
        inp_path = deepcopy(path)
        inp_path.append(compat)
        potential_path = find_path(adapters.difference(set([compat])), inp_path)

        if potential_path is not None:
            return potential_path

    return None


def get_profile_q1(path):
    jump_1 = 0
    jump_3 = 0
    next_v = 0
    for i, step in enumerate(path):
        if (i + 1) == len(path):
            next_v = MAX_DEVICE_JOLTS
            break
        else:
            next_v = path[i+1]

        if next_v - step == 1:
            jump_1 += 1
        else:
            jump_3 += 1

    print('q1 answer: {}'.format(jump_1 * jump_3))
    print('\t({} 1 jumps, {} 3 jumps)'.format(jump_1, jump_3))

def find_all_permutations(path):
    # find all runs of droppable adapters
    droppables = [0] * len(path)
    for i, step in enumerate(path):
        if i == 0 or i + 1 == len(path):
            continue

        if path[i+1] - path[i-1] <= 3:
            droppables[i] = path[i+1] - path[i-1]
    

    # hackish group by 
    droppables = ''.join(map(lambda x: str(x), droppables))
    droppables = droppables.split('0')
    droppables = list(filter(lambda x: x != '', droppables))

    print(droppables)
    total = 1

    for group in droppables:
        if len(group) == 1:
            total *= 2
        elif len(group) == 2:
            total *= 4
        elif len(group) == 3:
            total *= 7

    print('q2 total: {}'.format(total))


print('pathfinding...')
path = find_path(adapters_original, [0])
#path = [0, 1, 2, 3, 4, 7, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 24, 27, 28, 29, 30, 31, 34, 37, 38, 39, 42, 43, 44, 45, 48, 51, 52, 53, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 70, 73, 74, 75, 78, 79, 80, 81, 82, 85, 86, 87, 88, 91, 94, 95, 98, 99, 100, 103, 104, 105, 106, 109, 112, 113, 114, 115, 116, 119, 122, 123, 124, 125, 126, 129, 130, 131, 132, 133, 136, 139, 140, 141, 142, 143, 146, 147, 150, 151, 152, 153, 156]
#path = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
#path = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52]
print(path)
get_profile_q1(path)
find_all_permutations(path)

