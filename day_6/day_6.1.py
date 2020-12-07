puzzle_input = open('/Users/jebbelaar/projects/python/adventofcode/day_6/puzzle_input.txt', 'r')
lines = puzzle_input.readlines()


def getAnswers(answers):
    groups = list()
    group = ""
    for answer in answers:
        if answer == '\n':
            groups.append(group)
            group = ""
        group += answer.rstrip()
    return groups

def unique(answers):
    total = 0
    for x in answers:
        unique = []
        for char in x:
            if char not in unique:
                unique.append(char)
        total += len(unique)
    print(total)
    
    return total

answers = getAnswers(lines)
unique(answers)