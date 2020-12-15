#! /usr/bin/env python3

# example
#inputs = '0,3,6' # tgt -> 175594
#inputs = '1,3,2'  # tgt -> 2578
# puzzle
inputs = '10,16,6,0,1,17'

target_val = 30_000_000
#target_val = 2020
#target_val = 10

inputs = [int(i) for i in inputs.split(',')]

class MemoryGame:
    lasts  = {}
    step   = 0
    latest = 0
    debug  = False

    def __init__(self, history, debug=False):
        self.history = history
        for i, val in enumerate(history[:-1]):
            self.lasts[val] = i + 1

        self.latest = history[-1]
        self.step = len(history)

        self.debug = debug

    def __iter__(self):
        return self

    def __next__(self):
        if self.latest in self.lasts:
            next_val = self.step - self.lasts[self.latest]
            if self.debug:
                print('[{:4}] {:4}     found before, nv {} = {} - {}'.format(
                    self.step+1,
                    self.latest,
                    next_val,
                    self.step,
                    self.lasts[self.latest]
                ))
        else:
            if self.debug:
                print('[{:4}] {:4} not found before, nv 0'.format(self.step+1, self.latest))
            next_val = 0

        self.step += 1
        self.lasts[self.latest] = self.step - 1
        to_ret = self.latest
        self.latest = next_val
        
        return (self.step, self.latest)
        
mem = MemoryGame(inputs, debug=False)

for i, val in mem:
    if 0 == i % 1000000:
        print('turn {:12}: {:12} ({}%)'.format(i,val, int(100 * (i / target_val))))
    if i == target_val:
        print('\nlast turn {:12}: {:12}'.format(i,val))
        break
