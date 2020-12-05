#! /usr/bin/env python3

tmap = open('input.txt', 'r').readlines()

hslope = 3
tcount = 0
for i, line in enumerate(tmap):
    target = ((i) * hslope) % len(line.strip())
    if line[target] == '#':
        tcount += 1

    l2 = list(line.strip())
    l2[target] = 'O'
    print(''.join(l2))

print(tcount)
