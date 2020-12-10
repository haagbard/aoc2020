'''
Created on 10 Dec 2020

@author: richaa
'''

import collections

no_of_one = 0
no_of_three = 0

final_list = []
    
data = []

def brute_force_pt2(crnt_list):
    last_value = crnt_list[len(crnt_list) - 1]
    if last_value == highest_jolts:
        final_list.append(crnt_list)
    else:
        if (last_value + 1) in data:
            new_list = crnt_list
            new_list.append(last_value + 1)
            brute_force_pt2(new_list)
        if (last_value + 2) in data:
            new_list = crnt_list
            new_list.append(last_value + 2)
            brute_force_pt2(new_list)
        if (last_value + 3) in data:
            new_list = crnt_list
            new_list.append(last_value + 3)
            brute_force_pt2(new_list)
            
def find_max():
    # From https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
    # Usually, a Python dictionary throws a KeyError if you try to get an item with 
    # a key that is not currently in the dictionary. The defaultdict in contrast will 
    # simply create any items that you try to access (provided of course they do not exist yet). 
    tmp_data = collections.defaultdict(int)
    tmp_data[0] = 1

    for crnt_index in data:
        sum_final = 0
        for i in range(1,4):
            sum_final += tmp_data[crnt_index - i]
        tmp_data[crnt_index] = sum_final
    
    res = tmp_data[max(data)]
    
    return res
    
highest_jolts = 0

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
for line in lines:
    crnt_jolts = int(line)
    data.append(crnt_jolts)
    if crnt_jolts > highest_jolts:
        highest_jolts = crnt_jolts

data.sort()
    
start_jolts = 0    

for crnt_jolt in data:
    if crnt_jolt == (start_jolts + 1):
        no_of_one += 1
        start_jolts = crnt_jolt
    elif crnt_jolt == (start_jolts + 2):
        start_jolts = crnt_jolt
    elif crnt_jolt == (start_jolts + 3):
        no_of_three += 1
        start_jolts = crnt_jolt
        
final_res = no_of_one * (no_of_three + 1)
print(f'Final results: {final_res}')

tmp_list = [0]

# Well, yeah. Bruteforce was not the way to go on this.
#bruteforce = brute_force_pt2(tmp_list)
part2 = find_max()

#print(f'Total possibilities (bruteforce): {len(final_list)}')
print(f'Total possibilities: {part2}')