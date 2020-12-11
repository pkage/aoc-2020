#! /usr/bin/env python3

from copy import deepcopy
import sys

board_orig = open('input.txt', 'r').readlines()
board_orig = list(map(lambda x: list(x.strip()), board_orig))

BOARD_ROWS = len(board_orig)
BOARD_COLS = len(board_orig[0])

print('board of size: {} x {}'.format(BOARD_ROWS, BOARD_COLS))

def print_board(board):
    for row in board:
        print(''.join(row))
    print('')

def raytrace(board, row, col, r, c):
    while True:
        row += r
        col += c
        if row < 0 or row >= BOARD_ROWS:
            return False
        if col < 0 or col >= BOARD_COLS:
            return False

        if board[row][col] == 'L':
            return False
        if board[row][col] == '#':
            return True

def neighbor_count(board, row, col, fuck=False):
    count = 0
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if fuck:
                print(r,c)
            # don't count self
            if r == 0 and c == 0:
                if fuck:
                    board[row + r][col + c] = 'K'
                continue

            # don't count off the edge
            if (row + r) < 0 or (row + r) >= BOARD_ROWS:
                if fuck:
                    print('skip r')
                continue
            if (col + c) < 0 or (col + c) >= BOARD_COLS:
                if fuck:
                    print('skip c')
                continue

            if raytrace(board, row, col, r, c):
                count += 1

    if fuck:
        print_board(board)
    return count

def apply_rules(board):
    output = deepcopy(board)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            # skip not seats
            ch = board[row][col]
            if ch != 'L' and ch != '#':
                continue

            nc = neighbor_count(board, row, col)
            
            if ch == 'L' and nc == 0:
                output[row][col] = '#'
            
            if ch == '#' and nc >= 5:
                output[row][col] = 'L'

    return output

def compare_boards(b1,b2):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if b1[row][col] != b2[row][col]:
                return False
    return True

def count_occupied(board):
    count = 0
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == '#':
                count += 1
    return count


def converge(board):
    print_board(board)

    count = 0
    while True:
        count += 1
        nextb = apply_rules(board)
        print_board(nextb)
        print('step {}, occupied {}'.format(count, count_occupied(nextb)))
        
        if compare_boards(board, nextb):
            return (count, nextb)
        board = nextb
    

# 
#print(neighbor_count(board_orig, 0, 0, fuck=False))
#sys.exit(0)
#b2 = apply_rules(board_orig)
#print_board(b2)
# full b2
#print(neighbor_count(b2, 0, 2, fuck=False))

#b3 = apply_rules(b2)
#print_board(b3)



#b4 = apply_rules(b3)
#print_board(b4)
#print(compare_boards(b5,b6))
count, board = converge(board_orig)

print('Converged after {} steps, occupied {}'.format(count, count_occupied(board)))

