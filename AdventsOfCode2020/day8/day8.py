'''
Created on 8 Dec 2020

@author: richaa
'''
import re

def parseInput(instruct):
    pattern = r'(?P<ints>.{3})\s(?P<add>.)(?P<value>\d+)'
    x = re.search(pattern, instruct)
    what_to_do = x.group('ints')
    add_or_remove = x.group('add')
    value = int(x.group('value'))
    return what_to_do, add_or_remove, value

accumulator = 0

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

crnt_index = 0

instructions = {}

for line in lines:
    instructions[crnt_index] = [line, 0]
    crnt_index += 1
    
crnt_index = 0

while True:
    prev_index = crnt_index
    crnt_instruct = instructions[crnt_index]
    instruct = crnt_instruct[0]
    times_run = crnt_instruct[1]
    if times_run > 0:
        break
    else:
        what_to_do, add_or_remove, value = parseInput(instruct)
        if what_to_do == 'acc':
            if add_or_remove == '+':
                accumulator += value
            else:
                accumulator -= value
            crnt_index += 1
        elif what_to_do == 'nop':
            crnt_index += 1
        elif what_to_do == 'jmp':
            if add_or_remove == '+':
                crnt_index += value
            else:
                crnt_index -= value
        else:
            print(f'Unable to parse {what_to_do}')
        instructions[prev_index][1] += 1
        
    
print(f'Challenge 1: {accumulator}')

all_nop_and_jmp = []

instructions = {}

crnt_index = 0

count = 0

for line in lines:
    instructions[crnt_index] = [line, 0]
    what_to_do, add_or_remove, value  = parseInput(line)
    if what_to_do == 'jmp' or what_to_do == 'nop':
        #print(all_nop_and_jmp)
        all_nop_and_jmp.append(crnt_index)
        count += 1
        
    crnt_index += 1
    
is_complete = False

no_of_lines = len(lines)

for i in all_nop_and_jmp:
    accumulator = 0
    crnt_index = 0
    # reset intstructions
    tmp_index = 0
    for line in lines:
        instructions[tmp_index] = [line, 0]
        tmp_index += 1
    
    while True:
        #print(f'acc: {accumulator}')
        prev_index = crnt_index
        crnt_instruct = instructions[crnt_index]
        instruct = crnt_instruct[0]
        times_run = crnt_instruct[1]
        if times_run > 0:
            #print('Endless loop')
            break
        else:
            what_to_do, add_or_remove, value = parseInput(instruct)
            #print(f'{crnt_index} is current')
            if crnt_index == i:
                if what_to_do == 'nop':
                    what_to_do = 'jmp'
                else:
                    what_to_do = 'nop'
                
            if what_to_do == 'acc':
                if add_or_remove == '+':
                    accumulator += value
                else:
                    accumulator -= value
                crnt_index += 1
            elif what_to_do == 'nop':
                crnt_index += 1
            elif what_to_do == 'jmp':
                if add_or_remove == '+':
                    crnt_index += value
                else:
                    crnt_index -= value
            else:
                print(f'Unable to parse {what_to_do}')
                
            if prev_index == (no_of_lines - 1):
                print(f'Challenge 2: {accumulator}')
                break
            instructions[prev_index][1] += 1
            