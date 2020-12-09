'''
Created on 9 Dec 2020

@author: richaa
'''

preamp = 25
# For test
#preamp = 5

magic_sum = 0

def new_list_from_intervals(original_list, intervals):
    b = []
    start_value = intervals[0]
    end_value = intervals[1]
    
    for i in range(start_value, end_value):
        b.append(i)
        
    new_list = [original_list[x] for x in b]
    
    return new_list

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    
data = []

for line in lines:
    data.append(int(line))
    
next_index = preamp

while next_index != len(data):

    crnt_list_check = new_list_from_intervals(data, (next_index - preamp, next_index))
    
    value_to_check = data[next_index]
    
    found = False
    
    for i in range(0, preamp):
        for j in range(0, preamp):
            if i != j: 
                sum_tmp = crnt_list_check[i] + crnt_list_check[j]
                if sum_tmp == value_to_check:
                    found = True
    if found == False:
        magic_sum = value_to_check
        break
    
    next_index = next_index + 1
    

print(f'{magic_sum} is the number where are looking for.')

iterations = 0

min_i = 0
max_i = len(data)

while min_i != max_i -1:
    for i in range(min_i, max_i):
        iterations += 1
        #print(f'{min_i},{i}')
        new_list = new_list_from_intervals(data, (min_i, i))
        if len(new_list) > 1:
            count = 0
            for item in new_list:
                count += item
            if count == magic_sum:
                smallest = min(new_list)
                biggest = max(new_list)
                final_sum = smallest + biggest
                print(f'After {iterations} iterations, {smallest} + {biggest} = {final_sum}')
                print(new_list)
    min_i += 1
