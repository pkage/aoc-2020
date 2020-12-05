#! /usr/bin/env python3

passwords = open('passwords.txt', 'r').readlines()

def parse_line(line):
    # cursed
    rule, password = line.strip().split(': ')
    rule_left, rule_char = rule.split(' ')
    pos_l, pos_r = rule_left.split('-')

    pos_l = int(pos_l)
    pos_r = int(pos_r)

    print('pw: [{}] needs ch {} or {} to be \'{}\''.format(password, pos_l, pos_r, rule_char), end='')

    pos_l -= 1
    pos_r -= 1

    # != is an xor
    if (password[pos_l] == rule_char) != (password[pos_r] == rule_char):
        print(' ... valid!')
        return True
    print(' ... INVALID!')
    return False


count = 0
for line in passwords:
    if parse_line(line):
        count += 1

print('valid: {}'.format(count))
