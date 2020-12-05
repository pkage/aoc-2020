#! /usr/bin/env python3

passwords = open('passwords.txt', 'r').readlines()

def parse_line(line):
    # cursed
    rule, password = line.strip().split(': ')
    rule_left, rule_char = rule.split(' ')
    rule_min, rule_max = rule_left.split('-')

    rule_min = int(rule_min)
    rule_max = int(rule_max)

    print('pw: [{}] needs {} to {} of \'{}\''.format(password, rule_min, rule_max, rule_char), end='')

    count = len(password.split(rule_char)) - 1
    
    if count >= rule_min and rule_max >= count:
        print(' ... valid!')
        return True
    print(' ... INVALID!')
    return False


count = 0
for line in passwords:
    if parse_line(line):
        count += 1

print('valid: {}'.format(count))
