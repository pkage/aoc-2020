#! /usr/bin/env python3

numbers = list(map(lambda n: int(n), open('numbers.txt','r').readlines()))

for i in numbers:
    for j in numbers:
        if (i + j) == 2020:
            print(i * j)

