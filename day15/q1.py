#! /usr/bin/env python3

# example
#inputs = '0,3,6' # 2020 -> 436
inputs = '1,3,2'  # 2020 -> 1
# puzzle
inputs = '10,16,6,0,1,17'

#val = 30_000_000

inputs = [int(i) for i in inputs.split(',')]

class MemoryGame:
    history = []

    def __init__(self, history):
        self.history = history

    def __iter__(self):
        return self

    def __next__(self):
        last = self.history[-1]
        if not last in self.history[:-1]:
            self.history.append(0)
            print('[{:8}] {:8} not found before,\tappending 0'.format(len(self.history), last))
            return (len(self.history), 0)
        else:
            before_idx = len(self.history[:-1]) - (self.history[:-1])[::-1].index(last)
            latest_idx = len(self.history)
            self.history.append(latest_idx - before_idx)
            print('[{:8}] {:8}     found before,\tappending {} = {} - {}'.format(len(self.history), last, latest_idx - before_idx, latest_idx, before_idx))
            return (len(self.history), before_idx)

mem = MemoryGame(inputs)

for i, val in mem:
    #print('turn {}:\t {}'.format(i,val))
    if i == 2020:
        break
