#! /usr/bin/env python3

import sys

nums = list(map(lambda x: int(x), open('input.txt', 'r').readlines()))

def verify(lst, i):
    assert i > 24
    
    preamble = lst[i - 25:i]
    candidate = lst[i]

    #print(preamble, len(preamble), candidate)

    for num in lst:
        for num2 in lst:
            if num + num2 == candidate:
                return True

    return False

def find_invalid(lst):
    print('finding invalid...')
    for i in range(25, len(nums)):
        if not verify(nums, i):
            print('\tindex {}, {}'.format(i, nums[i]))
            return nums[i]

    sys.exit(1)

def find_run(lst, target):
    print('searching for candidate runs...')
    for begin in range(len(lst)):
        for end in range(begin, len(lst)):
            if sum(lst[begin:end]) == target and len(lst[begin:end]) > 1:
                print('found at nums[{}:{}]\n\tsmallest: {}\n\tlargest: {}\n\t\trange: {}\n\t\tsum: {}'.format(
                    begin, end,
                    min(lst[begin:end]),
                    max(lst[begin:end]),
                    lst[begin:end],
                    min(lst[begin:end]) + max(lst[begin:end]),
                ))

find_run(nums, find_invalid(nums))
