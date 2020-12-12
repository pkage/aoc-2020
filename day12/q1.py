#! /usr/bin/env python3

import sys

instructions = open('input.txt', 'r').readlines()

# EAST  = 0
# NORTH = 90
# WEST  = 180
# SOUTH = 270

class Ferry:
    x = 0
    y = 0
    heading = 0

    def go(self, instr):
        cmd = instr[0]
        amt = int(instr[1:])

        if cmd == 'N':
            self.y += amt
        elif cmd == 'E':
            self.x += amt
        elif cmd == 'S':
            self.y -= amt
        elif cmd == 'W':
            self.x -= amt
        elif cmd == 'L':
            self.heading = (self.heading + amt) % 360
        elif cmd == 'R':
            self.heading = (self.heading - amt) % 360
        elif cmd == 'F':
            if self.heading == 0:
                self.x += amt
            elif self.heading == 90:
                self.y += amt
            elif self.heading == 180:
                self.x -= amt
            elif self.heading == 270:
                self.y -= amt

    def report(self):
        return abs(self.x) + abs(self.y)

ferry = Ferry()
for instr in instructions:
    ferry.go(instr)

print(ferry.report())
