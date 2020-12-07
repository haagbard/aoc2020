'''
Created on 7 Dec 2020

@author: richaa
'''
import re

shiny_gold = 'shiny gold'

valid_bags = [shiny_gold]
stored_bags = {}
bags = {}

def parseBag(x):
    bag = x.group('bag')
    bag = bag.replace('bags','').replace('bag','').strip()
    return bag

def getBags(crnt_line):
    pattern = r'(?P<bag>.*)\scontain\s(?P<contain>.*)'
    x = re.search(pattern, crnt_line)
    bag = parseBag(x)
    contains = x.group('contain')
    content = getContent(bag, contains)
    return bag, content

def getContent(bag, contents):
    inner_bags = []
    
    if contents == 'no other bags.':
        return inner_bags
    
    pattern = r'(?P<total>\d+)\s(?P<bag>.*)'
    splitted = contents.split(', ')
    
    for split_str in splitted:
        split_str = split_str.replace('.','')
        x = re.search(pattern, split_str)
        bag = parseBag(x)
        x = re.search(pattern, split_str)
        total = int(x.group('total'))
        inner_bags.append((bag, total))
        
    return inner_bags

def checkForBags():
    toRun = True
    while toRun:
        toRun = False
        for bag in bags:
            for inner_bag in bags[bag]:
                if inner_bag[0] in valid_bags:
                    if bag not in valid_bags: # Or endless loop
                        valid_bags.append(bag)
                        toRun = True
                        break

def countTotal(bag):
    if bag in stored_bags:
        return stored_bags[bag]
    
    bags_in_total = 0
    
    for inner_bag in bags[bag]:
        bags_in_total += inner_bag[1] + inner_bag[1] * countTotal(inner_bag[0])
    
    stored_bags[bag] = bags_in_total
    
    return bags_in_total

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    for line in lines:
        bag, contains = getBags(line)
        bags[bag] = contains

print(f'Bags: {bags}')

checkForBags() # part 1
count_total = countTotal(shiny_gold)

print(f'Total bags (part1): {len(valid_bags)-1}') # Minus 1 since we start with shiny_gold
print(f'Total bags (part2): {count_total}')