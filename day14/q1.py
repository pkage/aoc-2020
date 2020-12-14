#! /usr/bin/env python3

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

    def read(self, line):
        op, arg = line.strip().split(' = ')
        if op[:3] == 'mem':
            tfrm = self.__apply_mask(arg)
            addr = int(op[4:-1])
            print('mem[{}] = {} (from {})'.format(addr, tfrm, arg))
            self.mem[addr] = tfrm
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

