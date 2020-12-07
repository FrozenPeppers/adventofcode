puzzle_input = open('/Users/jebbelaar/projects/python/adventofcode/day_6/puzzle_input.txt', 'r')
lines = puzzle_input.readlines()


def getAnswers(answers):
    groups = list()
    group = list()
    for answer in answers:
        if answer == '\n':
            groups.append(group)
            group = list()
        answer = answer.rstrip()
        if answer != "":
            group.append(answer)
        
    return groups

def countAllYes(groups):
    total = 0
    for group in groups:
        persons = len(group)
        result = list()
        result_dict = dict()
        for person in group:
            for answer in person:
                result.append(answer)
        for item in result:
            occurances = result.count(item)
            if occurances == persons:
                result_dict[item] = occurances
        total += len(result_dict)

    return total
    
    
groups = getAnswers(lines)
countAllYes(groups)