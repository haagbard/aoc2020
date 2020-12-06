'''
Created on 3 Dec 2020

@author: richaa
'''
import re
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

pattern = r"(?P<pos1>\d+)-(?P<pos2>\d+)\s(?P<char>.):\s(?P<pwd>.*)"

passwords = {}
 
count = 0

for line in lines:
    x = re.search(pattern, line)
    pos1 = int(x.group('pos1'))
    pos2 = int(x.group('pos2'))
    crnt_char = x.group('char')
    passwd = x.group('pwd')
    cout_chars = 0
    for tmp in passwd:
        if tmp == crnt_char:
            cout_chars += 1
    #print(f'{pos1}:{pos2} = {cout_chars}')
    if cout_chars >= pos1 and cout_chars <= pos2:
        count += 1
        
print(f'1: Total: {count}')

count = 0

for line in lines:
    x = re.search(pattern, line)
    pos1 = int(x.group('pos1'))
    pos2 = int(x.group('pos2'))
    crnt_char = x.group('char')
    passwd = x.group('pwd')
    
    firstfound = False
    valid = False
    
    if passwd[pos1-1] == crnt_char:
        firstfound = True
        valid = True
    if passwd[pos2-1] == crnt_char:
        if firstfound is False:
            valid = True
        else:
            valid = False
        
    if valid is True:
        #print(line)
        count += 1
        
print(f'2: Total: {count}')