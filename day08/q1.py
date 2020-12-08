#! /usr/bin/env python3

from copy import deepcopy

inputs = open('input.txt', 'r').readlines()

class Instr:
    itype = None
    value = None
    lineno = None
    
    def __init__(self, line, lineno):
        self.lineno = lineno

        self.itype, self.value = line.strip().split()
        self.value = int(self.value)

    def __repr__(self):
        return '[{}][{}] # {}'.format(self.itype, self.value, self.lineno)

# parse
prog = {}
for i, line in enumerate(inputs):
    prog[i] = Instr(line, i)

print(prog)

def execute(prog):
    # exec
    acc = 0
    seen = set()
    ptr = 0

    while True:
        if ptr in seen:
            print('LOOP! acc {}'.format(acc))
            return None
        if ptr >= len(prog):
            return acc
        seen.add(ptr)

        inst = prog[ptr]

        if inst.itype == 'acc':
            acc += inst.value
            ptr += 1
        elif inst.itype == 'jmp':
            ptr += inst.value
        elif inst.itype == 'nop':
            ptr += 1

execute(prog) 
