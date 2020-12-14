#! /usr/bin/env python3

from copy import deepcopy

prog = open('input.txt', 'r').readlines()

class InitializationProg:
    mem = {}
    mask = None
    
    def __init__(self):
        self.mem = {}

    def __apply_mask(self, orig):
        # convert to binary string
        value = list('{0:036b}'.format(int(orig)))
        #print(''.join(value), orig)

        # hoo boy
        outval = [(value[i] if self.mask[i] == 'X' else self.mask[i]) for i in range(len(value))]
        
        outval = ''.join(outval)

        #print(outval, int(outval,2))
        return int(outval,2)

    def __get_all_addr_permutations(self, addr):
        # convert to binary string
        value = list('{0:036b}'.format(int(addr)))

        def ch_replace(addr, mask, i):
            if mask[i] == '0':
                return addr[i]
            elif mask[i] == '1':
                return '1'
            else:
                return 'X'

        value = [ch_replace(value, self.mask, i) for i in range(len(value))]

        number_of_floaters = len(list(filter(lambda x: x=='X', value)))

        potential_addrs = []
        for i in range(2 ** number_of_floaters):
            potential_addrs.append((
                ('{0:0' + str(number_of_floaters) +'b}').format(i),
                deepcopy(value)
            ))

        def join_pair(pair):

            floaters, value = pair
            floaters = list(floaters)

            fcount = 0
            for i in range(len(value)):
                if value[i] == 'X':
                    value[i] = floaters[fcount]
                    fcount += 1

            return int(''.join(value),2)

        potential_addrs = list(map(join_pair, potential_addrs))

        #print(potential_addrs)

        return potential_addrs



    def read(self, line):
        op, arg = line.strip().split(' = ')
        if op[:3] == 'mem':
            addrs = self.__get_all_addr_permutations(op[4:-1])

            #print('mem[{}] = {} (from {})'.format(addr, tfrm, arg))
            print('mem{} = {}'.format(addrs, arg))
            for addr in addrs:
                self.mem[addr] = int(arg)
        elif op[:4] == 'mask':
            print('applying mask ', arg)
            self.mask = list(arg)

    def memsum(self):
        print('\nmem summary: ')
        total = 0
        for key in self.mem:
            print('\tmem[{}] = {}'.format(key, self.mem[key]))
            total += self.mem[key]

        print('total: {}'.format(total))
        return total


init = InitializationProg()
for line in prog:
    init.read(line)

init.memsum()

