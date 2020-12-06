'''
Created on 6 Dec 2020

@author: richaa
'''

def getUnique(input_value):
    unique = ''.join(set(input_value)) # Sort unique chars
    unique = unique.replace(' ', '') # Replace all white spaces
    unique = unique.strip() # Trim it
    return unique

data = []

# Read input
with open('input.txt', 'r') as file:
    lines = file.read().split('\n\n')

# Replace line break with space
for line in lines:
    data.append(line.replace('\n', ' '))
    

final_sum = 0

# part 1
for crntrow in data:
    unique = getUnique(crntrow)
    final_sum += len(unique)
    
print(f'Final sum: {final_sum}')

final_sum = 0

# part 2
for crntrow in data:
    
    persons = crntrow.split() # Split string with white space to get each person in group
    
    first_person = getUnique(persons[0]) # Get the first person in group with unique chars
    
    for crnt_char in first_person: # Loop through each character in that string
        count_it = True # This will be False if a character is not found in a other person
        
        for person in persons:
            if crnt_char not in person: # If crnt_char is not found in person, we will not count it
                count_it = False
        if count_it is True: # This means that the crnt_char is found in all persons
            final_sum += 1
        
        
print(f'Final sum (part 2): {final_sum}')