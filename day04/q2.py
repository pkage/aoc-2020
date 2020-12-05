#! /usr/bin/env python3
from copy import deepcopy
import re

passports = ''.join(open('input.txt', 'r').readlines()).split('\n\n')

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

def fieldcheck(joined):
    left, right = joined.split(':')
    if left == 'byr':
        if len(right) != 4:
            return False
        if int(right) < 1920 or int(right) > 2002:
            return False
        return True
    elif left == 'iyr':
        if len(right) != 4:
            return False
        if int(right) < 2010 or int(right) > 2020:
            return False
        return True
    elif left == 'eyr':
        if len(right) != 4:
            return False
        if int(right) < 2020 or int(right) > 2030:
            return False
        return True
    elif left == 'hgt':
        if len(right) < 4:
            return False
        unit = right[-2:]
        num = int(right[:-2])
        if unit == 'in':
            if num < 59 or num > 76:
                return False
            return True
        elif unit == 'cm':
            if num < 150 or num > 193:
                return False
            return True
        else:
            return False
    elif left == 'hcl':
        if right[0] != '#':
            return False
        if len(right) != 7:
            return False
        right = right[1:]
        allowed = 'abcdef0987654321'
        for ch in list(right):
            if not (ch in allowed):
                return False
        return True
    elif left == 'ecl':
        allowed = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if right in allowed:
            return True
        return False
    elif left == 'pid':
        if len(right) != 9:
            return False
        allowed = '0987654321'
        for ch in list(right):
            if not (ch in allowed):
                return False
        return True
    elif left == 'cid':
        return True


def check(passport):
    pf = set(deepcopy(fields))
    splitter = re.compile('\W')
    passport = passport.split()
    print(passport)

    for f in passport:
        if f[:3] in pf:
            if not fieldcheck(f):
                return False
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
        
        
