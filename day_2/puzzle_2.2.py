puzzle_input = open('/Users/jebbelaar/projects/python/adventofcode/day2/puzzle_input.txt', 'r')
lines = puzzle_input.readlines()

valid_counter = 0

def isPasswordValid(low, high, letter, password):
    counter_low, counter_high = 0, 0
    result = False

    if password[int(low)-1] == letter:
        counter_low += 1
    if password[int(high)-1] == letter:
        counter_high += 1

    if counter_low > counter_high or counter_low < counter_high:
        return True
    return False

for line in lines:
    low, high, letter, pwd = "", "", "", ""
    state_low = True
    state_high = False
    state_letter = True
    state_pwd = False
    for char in line:
        if char.isdigit() and state_low == True:
            low += char
        if char.isdigit() and state_high == True:
            high += char
        if char == "-":
            state_low = False
            state_high = True
        if char.isalpha() and state_letter == True:
            letter = char
            state_letter = False
        if char == ":":
            state_pwd = True
        if char.isalpha() and state_pwd == True:
            pwd += char
    if isPasswordValid(low, high, letter, pwd):
        valid_counter += 1

print(valid_counter)