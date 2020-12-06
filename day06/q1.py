#! /usr/bin/env python3

groups = open('input.txt', 'r').read().split('\n\n')

def get_group(grp):
    qs = set()

    allqs = 'abcdefghijklmnopqrstuvwxyz'

    for ch in list(grp):
        if ch in allqs:
            qs.add(ch)

    return len(qs)

count = 0
for grp in groups:
    count += get_group(grp)

print(count)
