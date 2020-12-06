'''
Created on 3 Dec 2020

@author: richaa
'''


with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

data = []

magic_sum = 2020

# Strips the newline character 
for line in lines: 
    data.append(int(line))
    
for crnt in data:
    for crnt_sec in data:
        #print(f'{crnt} + {crnt_sec}')
        crnt_sum = crnt + crnt_sec
        #print(f'{crnt_sum}')
        if crnt_sum == magic_sum:
            total_prod = crnt * crnt_sec
            print(f'1: {crnt} * {crnt_sec} = {total_prod}')
            
for crnt in data:
    for crnt_sec in data:
        for crnt_thrd in data:
            #print(f'{crnt} + {crnt_sec}')
            crnt_sum = crnt + crnt_sec + crnt_thrd
            #print(f'{crnt_sum}')
            if crnt_sum == magic_sum:
                total_prod = crnt * crnt_sec * crnt_thrd
                ##print(f'{crnt} + {crnt_sec} + {crnt_thrd} = {crnt_sum}')
                print(f'2: {crnt} * {crnt_sec} * {crnt_thrd} = {total_prod}')