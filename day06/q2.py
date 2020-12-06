#! /usr/bin/env python3

from copy import deepcopy
groups = open('input.txt', 'r').read().split('\n\n')

def get_group(grp):
    print(grp)
    grp = grp.split('\n')

    qs = None

    #allqs = 'abcdefghijklmnopqrstuvwxyz'

    for person in grp:
        pqs = set(list(person.strip()))
        if len(pqs) == 0:
            continue
        print('pqs\t{}'.format(pqs))
        if qs is None:
            qs = deepcopy(pqs)
        else:
            qs = deepcopy(pqs.intersection(qs))
            print('qs:\t{}'.format(qs))


    print('fqs:\t{} {}'.format(qs, len(qs)))
    
    return len(qs)

count = 0
for grp in groups:
    count += get_group(grp)

print(count)
