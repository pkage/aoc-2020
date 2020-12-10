#! /usr/bin/env python3

import sys

nums = list(map(lambda x: int(x), open('input.txt', 'r').readlines()))

def verify(lst, i):
    assert i > 24
    
    preamble = lst[i - 25:i]
    candidate = lst[i]

    print(preamble, len(preamble), candidate)

    for num in lst:
        for num2 in lst:
            if num + num2 == candidate:
                return True

    return False

print(nums[:26])
print(verify(nums, 25))

for i in range(25, len(nums)):
    if not verify(nums, i):
        print('index {}, {}'.format(i, nums[i]))
        sys.exit(0)
