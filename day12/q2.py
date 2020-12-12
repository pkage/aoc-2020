#! /usr/bin/env python3

import sys

instructions = open('input.txt', 'r').readlines()

# EAST  = 0
# NORTH = 90
# WEST  = 180
# SOUTH = 270

class Ferry:
    wx = 10
    wy = 1
    x = 0
    y = 0
    heading = 0

    def go(self, instr):
        cmd = instr[0]
        amt = int(instr[1:])

        if cmd == 'N':
            self.wy += amt
        elif cmd == 'E':
            self.wx += amt
        elif cmd == 'S':
            self.wy -= amt
        elif cmd == 'W':
            self.wx -= amt
        elif cmd == 'L':
            if amt == 90:
                tmp = self.wy
                self.wy = self.wx
                self.wx = -1 * tmp
            elif amt == 180:
                self.wx *= -1
                self.wy *= -1
            elif amt == 270:
                tmp = self.wy
                self.wy = -1 * self.wx
                self.wx = tmp
        elif cmd == 'R':
            if amt == 90:
                tmp = self.wy
                self.wy = -1 * self.wx
                self.wx = tmp
            elif amt == 180:
                self.wx *= -1
                self.wy *= -1
            elif amt == 270:
                tmp = self.wy
                self.wy = self.wx
                self.wx = -1 * tmp
        elif cmd == 'F':
            for i in range(amt):
                self.x += self.wx
                self.y += self.wy

    def report(self):
        return abs(self.x) + abs(self.y)

ferry = Ferry()
for instr in instructions:
    ferry.go(instr)

print(ferry.report())
