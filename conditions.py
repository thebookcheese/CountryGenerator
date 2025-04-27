import json
import random

def count_dict(d):
    if isinstance(d, dict):
        # count 1 if it is a dict
        count = 1
        # iterate values for dict
        iterable = d.values()
    else:
        count = 0
        iterable = d

    for v in iterable:
        if isinstance(v, dict):
            # count recursively
            count += count_dict(v)
    return count

def Conditions(country):
    neededResult = True
    with open('history.json', 'r') as file:
        data = json.load(file)
    a = False
    Line = ''
    jsonSectionsDict = {

    }
    while a == False:
        Condition = random.choice(data)
        print(jsonSectionsDict)
        for i in jsonSectionsDict:
            Condition = Condition[i]
        prev = Condition
        splitCondition = next(iter(Condition)).split()
        if count_dict(Condition) == 2:
            Line = random.choice(Condition['TextOptions'])
            return Line
        else:
            if len(splitCondition) == 2:
                if splitCondition[0].lower() == 'not':
                    while country.Conditionals[splitCondition[1]] != False:
                        Condition = random.choice(list(prev.keys()))
                    jsonSectionsDict[Condition] = None
            elif len(splitCondition) == 1:
                while country.Conditionals[splitCondition[0]] != True:
                    Condition = random.choice(list(prev.keys()))
                jsonSectionsDict[splitCondition[0]] = None
            elif len(splitCondition) == 3:
                if splitCondition[1] == '>':
                    while country.Conditionals[splitCondition[0]] < int(splitCondition[2]):
                        Condition = random.choice(list(prev.keys()))
                    b = " "
                    splitCondition = b.join(splitCondition)
                    jsonSectionsDict[splitCondition] = None
