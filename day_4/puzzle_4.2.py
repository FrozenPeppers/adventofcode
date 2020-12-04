puzzle_input = open('/Users/jebbelaar/projects/python/adventofcode/day_4/puzzle_input.txt', 'r')
lines = puzzle_input.readlines()
import json
from re import search, match
passports = list()

passport = ""
index = 0

for line in lines:
    index += 1
    if line == "\n":
        passport = passport[:-2]
        passports.append(passport)
        passport = ""
        continue
    
    line = line.replace(' ', ', ')
    line = line.replace('\n', ', ')
    
    passport += line
    
    if (index+1) == (len(lines)+1):
        passport = passport[:-2]
        passports.append(passport)
        passport = ""
        continue

req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def validatePassport(passport, req_fields):
    for field in req_fields:
        if search(field, passport):
            continue
        else:
            return False
    return True

valid_passports = list()
valid = 0
invalid = 0
for passport in passports:
    if validatePassport(passport, req_fields):
         valid += 1
         valid_passports.append(passport)
         continue
    invalid += 1

print("valid: " + str(valid))
print("invalid: " + str(invalid))



def setFieldDict(passport):
    passport = passport.replace(' ', '')
    fields = passport.split(',')
    field_dict = dict()
    for field in fields:
        split = field.split(':')
        field_dict[split[0]] = split[1]
    # print(field_dict)
    return field_dict


field_dict = setFieldDict(passports[0])

def validateEcl(ecl):
    valid_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if any(ecl in s for s in valid_list) and ecl != "":
        return True
    return False
        

def validateFields(field_dict):
    print(field_dict)
    byr = field_dict['byr']
    iyr = field_dict['iyr']
    eyr = field_dict['eyr']
    hgt = field_dict['hgt']
    hcl = field_dict['hcl']
    ecl = field_dict['ecl']
    pid = field_dict['pid']
    if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
        print('byr')
        return False
    if len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
        print('iyr')
        return False
    if len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
        print('eyr')
        return False
    if hgt.find('cm') > 0 or hgt.find('in') > 0:
        if hgt.find('cm') > 0:
            height = ""
            for char in hgt:
                if char.isdigit():
                    height += char
            if int(height) < 150 or int(height) > 193:
                print('height')
                return False
        if hgt.find('in') > 0:
            height = ""
            for char in hgt:
                if char.isdigit():
                    height += char
            if int(height) < 59 or int(height) > 76:
                print('height')
                return False
    else:
        print('height')
        return False
    if len(hcl) != 7 or not match("#[a-f0-9]{6}", hcl):
        print('hcl')
        return False
    if not validateEcl(ecl):
        print('ecl')
        return False
    if not match("^[0-9]{9}$", pid):
        print('pid')
        return False
    return True

passport_field_dicts = list()
for passport in valid_passports:
    passport_field_dicts.append(setFieldDict(passport))

valid_fields = 0
invalid_fields = 0
for passport in passport_field_dicts:
    if validateFields(passport):
        valid_fields += 1
    else:
        invalid_fields += 1

print("valid fields: ", valid_fields)
print("invalid fiedls: ", invalid_fields)