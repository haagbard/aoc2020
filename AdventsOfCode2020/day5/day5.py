'''
Created on 5 Dec 2020

@author: richaa
'''

def convertToBinary(data):
    row = data[0:7]
    row = row.replace('F','0')
    row = row.replace('B','1')
    #print(row)
    column = data[7:]
    column = column.replace('L','0')
    column = column.replace('R','1')
    #print(column)
    return row, column

def calcutateChair(row, column):
    row_int = int(row, 2)
    col_int = int(column, 2)
    ret_value = row_int * 8 + col_int
    return ret_value

def initSeatPlacement():
    data = {}
    for i in range(1024): # Maximum no of seats
        #print(i)
        data[i] = 0
    return data

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    
highest_chair = 0
seats_taken = initSeatPlacement()

for line in lines:
    row, column = convertToBinary(line)
    chair = calcutateChair(row, column)
    seats_taken[chair] = 1
    if chair > highest_chair:
        highest_chair = chair
        
print(f'Highest chair no: {highest_chair}')

# clear unused seats (lower)
for seat in seats_taken:
    if seats_taken[seat] == 1:
        break
    seats_taken[seat] = 1

# clear unused seats (higher)
for seat in sorted(seats_taken.keys(), reverse=True):
    if seats_taken[seat] == 1:
        break
    seats_taken[seat] = 1


for seat in seats_taken:
    if seats_taken[seat] == 0:
        print(f'This seat is not taken: {seat}')
