import math

puzzle_input = open('/Users/jebbelaar/projects/python/adventofcode/day_3/puzzle_input.txt', 'r')
lines = puzzle_input.readlines()

def calculateMapDimensions():
    length = len(lines)
    width = len(lines[0])
    needed_width = length * 8
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


def slope(map, right, down):
    index = 0
    trees = 0
    squares = 0
    skip = True
    down_cnt = 0
    for line in map:
        if skip == True:
            skip = False
            continue
        if down == 2 and down_cnt < 1:
            down_cnt+=1
            continue
        index += right
        if line[index] == '#':
            trees += 1
        else:
            squares += 1
        down_cnt = 0
        continue
    print('trees: ' + str(trees))
    print('squares: ' + str(squares))
    return trees

map = createMap()
slope1 = slope(map, 1, 1)
slope2 = slope(map, 3, 1)
slope3 = slope(map, 5, 1)
slope4 = slope(map, 7, 1)
slope5 = slope(map, 1, 2)

print(slope1*slope2*slope3*slope4*slope5)
