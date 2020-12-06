'''
Created on 4 Dec 2020

@author: richaa
'''
import re

def contains_all_fields(passport, fields):
    for field in fields:
        if field not in passport:
            return None
    
    return passport

def validate_fields(passport, fields):
    for field in fields:
        if field == 'byr':
            pattern = r'byr:(?P<pos>\d+)'
            x = re.search(pattern, passport)
            ret_value = int(x.group('pos'))
            if ret_value < 1920 or ret_value > 2002:
                #print(passport)
                return None
        if field == 'iyr':
            pattern = r'iyr:(?P<pos>\d+)'
            x = re.search(pattern, passport)
            ret_value = int(x.group('pos'))
            if ret_value < 2010 or ret_value > 2020:
                #print(passport)
                return None
        if field == 'eyr':
            pattern = r'eyr:(?P<pos>\d+)'
            x = re.search(pattern, passport)
            ret_value = int(x.group('pos'))
            if ret_value < 2020 or ret_value > 2030:
                #print(passport)
                return None
        if field == 'hgt':
            pattern_cm = r'hgt:(?P<pos>\d+)cm'
            pattern_in = r'hgt:(?P<pos>\d+)in'
            x_cm = re.search(pattern_cm, passport)
            x_in = re.search(pattern_in, passport)
            if x_cm is not None:
                ret_value = int(x_cm.group('pos'))
                if ret_value < 150 or ret_value > 193:
                    #print(passport)
                    return None
            elif x_in is not None:
                ret_value = int(x_in.group('pos'))
                if ret_value < 59 or ret_value > 76:
                    #print(passport)
                    return None
            else:
                #print(passport)
                return None
        if field == 'hcl':
            pattern = r'hcl:#([0-9A-Fa-f]{6})'
            x = re.search(pattern, passport)
            if x is None:
                #print(passport)
                return None
        if field == 'ecl':
            pattern = r'ecl:(amb|blu|brn|gry|grn|hzl|oth)'
            x = re.search(pattern, passport)
            if x is None:
                #print(passport)
                return None
        if field == 'pid':
            pattern = r'(pid:\d{9}\s)|(pid:\d{9}$)'
            x = re.search(pattern, passport)
            if x is None:
                #print(passport)
                return None
    
    return passport

with open('input.txt', 'r') as file:
    lines = file.read().split('\n\n')

required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
optional_fields = ['cid']

data = []

for line in lines:
    data.append(line.replace('\n', ' '))
    
valid_passports = []
    
for passport in data:
    passport_ret = contains_all_fields(passport, required_fields)
    if passport_ret is not None:
        valid_passports.append(passport_ret)
        
print(f'Challenge 1: {len(valid_passports)} passports')

valid_passports_2 = []

for passport in valid_passports:
    passport_ret = validate_fields(passport, required_fields)
    if passport_ret is not None:
        valid_passports_2.append(passport_ret)
        
print(f'Challenge 2: {len(valid_passports_2)} passports')