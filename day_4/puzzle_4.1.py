puzzle_input = open('/Users/jebbelaar/projects/python/adventofcode/day_4/puzzle_input.txt', 'r')
lines = puzzle_input.readlines()
import json
from re import search
passports = list()

passport = ""
index = 0
print(len(lines))

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
            print("not valid")
            return False
    return True

valid = 0
invalid = 0
for passport in passports:
    if validatePassport(passport, req_fields):
         valid += 1
         continue
    invalid += 1

print("valid: " + str(valid))
print("invalid: " + str(invalid))
    
