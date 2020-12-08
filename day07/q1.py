#! /usr/bin/env python3
import sys

rules = open('input.txt', 'r').readlines()

# bright olive bags contain 5 dotted white bags, 2 wavy lavender bags.

class BagRule:
    # this rule's color
    color = None

    # tuple of quantity, color
    contents = []

    def __init__(self, rule):
        self.color, childs = rule.strip()[:-1].split(' bags contain ')
        #print('parsed: ' + self.color + ' w/ [' + childs + ']')
        self.contents = []
        
        if childs != 'no other bags':
            childs = childs.split(', ')
            print('\tchilds: {}'.format(childs))
            print('\tcontents: {}'.format(self.contents))
            for child in childs:
                child = child.split(' ')[:-1]
                self.contents.append((int(child[0]), ' '.join(child[1:])))

    def __repr__(self):
        return 'bagrule for {}: {}'.format(self.color, ', '.join(map(lambda x: str(x[0]) + ' ' + x[1], self.contents)))

print(BagRule('dim maroon bags contain 1 dotted beige bag, 2 drab black bags, 5 posh tomato bags, 3 striped lavender bags.').contents)

def get_rules_map(rules):
    rulesmap = {}
    for rule in rules:
        br = BagRule(rule)
        print(str(br) + '\n')
        rulesmap[br.color] = br

    return rulesmap

rulesmap = get_rules_map(rules)
print('{} rules processed.'.format(len(rulesmap)))

def find_all_direct(rulesmap, target_color):
    parents = set()
    for color in rulesmap:
        rule = rulesmap[color]
        for count, child_color in rule.contents:
            if child_color == target_color:
                print('color {} contains {} directly'.format(color, target_color))
                parents.add(color)

    return parents

def get_containing_uniques(rulesmap, target_colors):
    parents = set(target_colors)
    for color in target_colors:
        parents = parents.union(find_all_direct(rulesmap, color))

    if len(parents) != len(target_colors):
        return get_containing_uniques(rulesmap, parents)

    return parents


can_have_gold = get_containing_uniques(rulesmap, ['shiny gold'])
can_have_gold.remove('shiny gold')

print(can_have_gold)
print(len(can_have_gold))
