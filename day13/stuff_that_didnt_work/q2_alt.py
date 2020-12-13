#! /usr/bin/env python3

begin, buses = open('input.txt', 'r').readlines()
buses = buses.strip().split(',')

from sympy import cos, pi, symbols, Symbol
from sympy.solvers.solveset import nonlinsolve
from sympy.sets.sets import Interval

def create_correctbutshitty_eqs(buses):
    eqs = 0
    offset = 0
    t = Symbol('t', integer=True)
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        print('cos( (2 * pi * (t + {})) / {}) - 1'.format(i, int(bus)))
        eqs += cos( (2 * pi * (t + i)) / int(bus))
        offset += 1
    return t, eqs - offset, offset

t, eqs, offset = create_correctbutshitty_eqs(buses)
print(eqs)

def eulers_eqs(buses):
    eqs = []
    offset = 0

    for i, bus in enumerate(buses):
        if bus == 'x':
            continue

        eqs.append(  )

print('... solving ...')
soln_set = nonlinsolve([eqs], [t])
soln = list(soln_set)[0][0]
print(soln)
print('evaling over set')

dom = Interval(0, 1000000000000000)
print(soln.intersect(dom))


