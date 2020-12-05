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

max_sid = 0
for bp in passes:
    pos = parserow(bp)
    sid = (pos[0] * 8) + pos[1]
    if sid > max_sid:
        max_sid = sid
    

#print(parserow('FBFBBFFRLR'))
print(max_sid)
