'''
Created on 3 Dec 2020

@author: richaa
'''

def skislope(slope, x_inc, y_inc):
    max_value = len(slope)
    x = x_inc
    y = y_inc
    trees = 0
    while y < max_value:
        crnt_row = slope[y]
        crnt_len = len(crnt_row)
        if x >= crnt_len:
            x = x - crnt_len
        crnt_char = crnt_row[x]
        if crnt_char == '#':
            trees += 1
        x += x_inc
        y += y_inc
    
    return trees
    

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

tree = skislope(lines, 3, 1)
print(f'challenge 1: {tree}')

day2 = []
day2.append(skislope(lines, 1, 1))
day2.append(skislope(lines, 3, 1))
day2.append(skislope(lines, 5, 1))
day2.append(skislope(lines, 7, 1))
day2.append(skislope(lines, 1, 2))

total = 1
for tmp in day2:
    total = total * tmp
    
print(f'challenge 2: {total}')