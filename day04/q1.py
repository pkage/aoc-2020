#! /usr/bin/env python3
from copy import deepcopy
import re

passports = ''.join(open('input.txt', 'r').readlines()).split('\n\n')

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


def check(passport):
    pf = set(deepcopy(fields))
    splitter = re.compile('\W')
    passport = passport.split()
    print(passport)

    for f in passport:
        if f[:3] in pf:
            pf.remove(f[:3])

    print(pf)
    if len(pf) == 0:
        return True

    if len(pf) == 1 and 'cid' in pf:
        return True

    return False

count = 0
for p in passports:
    print(p.strip())
    if check(p):
        count += 1

print(count)
        
        
