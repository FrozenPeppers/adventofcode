import math

puzzle_input = open('/Users/jebbelaar/projects/python/adventofcode/day_3/puzzle_input.txt', 'r')
lines = puzzle_input.readlines()

def calculateMapDimensions():
    length = len(lines)
    width = len(lines[0])
    needed_width = length * 4
    duplicate_line = needed_width / width

    return math.ceil(duplicate_line)

def createMap():
    new_map = list()
    for line in lines:
        new_line, line, = "", line[:31]
        for i in range(calculateMapDimensions()):
            new_line += line
        new_map.append(new_line)
    return new_map


def slope(map):
    index = 0
    trees = 0
    squares = 0
    skip = True
    for line in map:
        if skip == True:
            skip = False
            continue
        index += 3
        if line[index] == '#':
            trees += 1
        else:
            squares += 1
        continue
    print('trees: ' + str(trees))
    print('squares: ' + str(squares))

slope(createMap())
