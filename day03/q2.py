#! /usr/bin/env python3

tmap = open('input.txt', 'r').readlines()

def slope(hslope, vslope=1):
    tcount = 0
    for i, line in enumerate(tmap[::vslope]):
        target = ((i) * hslope) % len(line.strip())
        if line[target] == '#':
            tcount += 1

        l2 = list(line.strip())
        l2[target] = 'O'
        print(''.join(l2))

    return tcount

print(slope(1,1) * slope(3,1) * slope(5,1) * slope(7,1) * slope(1,2))
