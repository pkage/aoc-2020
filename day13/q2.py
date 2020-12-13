#! /usr/bin/env python3

from sympy.ntheory.modular import crt

_, buses = open('input.txt','r').readlines()
buses = buses.strip().split(',')
buses = [(i, int(bus)) for i, bus in enumerate(buses) if bus != 'x'] 


residuals = [i   for i, bus in buses]
moduli    = [bus for i, bus in buses]

rem, lcm = crt(moduli, residuals)

print('answer: ', lcm - rem)

