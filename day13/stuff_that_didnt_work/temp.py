#! /usr/bin/env python3


from sympy.solvers.diophantine import diophantine
from sympy import symbols, solve
import sys

class DiophantineSync:
    offset = 0
    period = 0

    def __init__(self, start):
        self.offset = 0
        self.period = start

    def __find_smallest_offset(self, num, num_offset):
        add = (self.offset + num_offset) % num
        sub = (self.offset - num_offset) % num
        if add < sub:
            return add
        return -1 * sub

    def sync(self, num, num_offset):
        #virtual_offset = #self.__find_smallest_offset(num,num_offset)
        virtual_offset = num_offset - self.offset
        print('virtual offset', virtual_offset)

        a, b = symbols('a b')

        eq = (self.period * a) - (num * b) - virtual_offset
        soln = diophantine(eq)

        print(soln)
        fst, _ = list(soln)[0]
        subs = {}
        subs[list(fst.free_symbols)[0]] = 1
        new_offset = fst.evalf(subs=subs) * self.period
        print(new_offset)

        self.offset = int(new_offset) - num_offset
        self.period *= int(num)


    def __repr__(self):
        return '<dsync with offset {}, period {}>'.format(self.offset, self.period)


a, b = symbols('a b')

buses = [17,3,13,5]

dsync = DiophantineSync(17)
print(dsync)
dsync.sync(13,2)
print(dsync)
#sys.exit(0)
dsync.sync(19,3)
print(dsync)




sys.exit(0)

eq = (17 * a) - (13 * b) - 2
soln = diophantine(eq)

def get_offset(soln):
    fst,snd = list(soln)[0]
    print(fst,snd)
    

#sys.exit(0)

fst,snd = list(soln)[0]
print(soln)

eq2 = (221*a) - (19 * b) +2
soln2 = diophantine(eq2)
print(soln2)

