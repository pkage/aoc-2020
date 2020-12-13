#! /usr/bin/env python3

import sys
from copy import deepcopy

begin, buses = open('input.txt', 'r').readlines()


buses = filter(lambda x: x != 'x', buses.strip().split(','))
buses = list(map(lambda x: int(x), buses))

print(begin, buses)

times = deepcopy(buses)

times = list(map(lambda x: x - (int(begin) % x), times))

print(times)
