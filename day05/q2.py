#! /usr/bin/env python3

passes = open('input.txt', 'r').readlines()

def parserow(bpass):
    bpass = bpass.strip()
    print('bpass: ', bpass)
    row = bpass[:7]
    col = bpass[7:]

    print('row ' + row + ', col ' + col)

    row_min = 0
    row_max = 128

    col_min = 0
    col_max = 8


    for ch in list(row):
        if ch == 'F':
            row_max = (row_min + row_max) / 2
        else:
            row_min = (row_min + row_max) / 2

    for ch in list(col):
        if ch == 'L':
            col_max = (col_min + col_max) / 2
        else:
            col_min = (col_min + col_max) / 2

    return (row_min, col_min)

sids = []
for bp in passes:
    pos = parserow(bp)
    sid = (pos[0] * 8) + pos[1]
    sids.append(sid)

before = False
for i in range(len(sids)):
    if i in sids and not before:
        before = True
        continue

    if before:
        if (i+1) not in sids:
            print('missing seat at ' + str(i + 1))

#print(parserow('FBFBBFFRLR'))
