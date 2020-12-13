#! /usr/bin/env python3

import sys
from copy import deepcopy
import math

begin, buses = open('input.txt', 'r').readlines()


buses = buses.strip().split(',')
#buses = list(map(lambda x: int(x), buses))

print(buses)

timestamp_reqs = [i + 1 for i in range(len(buses))]
print(timestamp_reqs)


def tolerant_map(buses,reqs,t):
    return [int(buses[i]) - (t % int(buses[i])) if buses[i] != 'x' else reqs[i] for i in range(len(buses))]

def arreq(l1, l2):
    if len(l1) != len(l2):
        print('length mismatch')
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

print(tolerant_map(buses, timestamp_reqs, 939))

#min_bus = min(map(lambda x: int(x)), filter(lambda y: mint
min_bus = int(buses[0])
print('min_bus: ', min_bus)
t = math.prod([int(x) for x in buses if x != 'x'])
min_bus = min([int(x) for x in buses if x != 'x'])
#t = 1201900000

def largest_step(buses):
    largest = 0
    largest_i = 0
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        if int(bus) > largest:
            largest_i = i
            largest = int(bus)

    return largest_i, largest

step, offset = largest_step(buses)
print(step,offset)

t = offset + (t - (t % step))  - 1
#sys.exit(0)
#t=0 + offset - 1

def check(t, buses):
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        c = (((t + i) % int(bus)))
        #print('bus {}, c {}, i {}'.format(bus, c, i))
        if c != 0:
            return False
    
    return True


#print(check(1068781, buses))
#sys.exit(0)


while True:
    if check(t, buses):
        break

    if 0 == t % 100000:
        print(t, 1202161486)
    t -= step

print('first stamp: ' + str(t))

