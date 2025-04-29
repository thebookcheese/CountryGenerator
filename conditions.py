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

def Conditions(country, opposingCountry):
    count = 0
    countcount = 0
    with open('history.json', 'r') as file:
        data = json.load(file)
    a = False
    Line = ''
    jsonSectionsDict = {

    }
    dict = None
    while a == False:
        dict = data[0]
        for i in jsonSectionsDict:
            dict = dict[i]
        prevdict = dict
        Condition = random.choice(list(dict.keys()))
        prev = Condition
        print(Condition)
        print(list(prevdict.keys()))
        splitCondition = Condition.split()
        print(splitCondition)
        if count_dict(dict) == 2:
            for key in dict['Result']:
                if key == 'OwnNation':
                    if dict['Result'][key] == 'false':
                        if dict['Result'][key] == 'false' or dict['Result'][key] == 'true':
                            if dict['Result'][key] == 'false':
                                opposingCountry.Conditionals[key] = False
                            else:
                                opposingCountry.Conditionals[key] = True
                        else:
                            opposingCountry.Conditionals[key] = dict['Result'][key]

                else:
                    if dict['Result'][key] == 'false' or dict['Result'][key] == 'true':
                        if dict['Result'][key] == 'false':
                            country.Conditionals[key] = False
                        else:
                            country.Conditionals[key] = True
                    else:
                        country.Conditionals[key] = dict['Result'][key]
            Line = random.choice(dict['TextOptions'])
            splitLine = Line.split()
            if '{NewNation}' in splitLine:
                return Line, True
            else:
                return Line, False
        else:
            if len(splitCondition) == 2:
                if splitCondition[0].lower() == 'not':
                    if country.Conditionals[splitCondition[1]] == True:
                        Condition = random.choice(list(prevdict.keys()))
                        splitCondition = Condition.split()
                        count = count + 1
                    else:
                        jsonSectionsDict[Condition] = None
                        count = 0
                        countcount = countcount + 1

            if len(splitCondition) == 1:
                if country.Conditionals[splitCondition[0]] != True:
                    print(list(prevdict.keys()))
                    print(count)
                    if count > len(list(prevdict.keys()))-1:
                        if len(list(prevdict.keys()))-count > len(list(prevdict.keys())) or len(list(prevdict.keys()))-count < 0:
                            Condition = list(prevdict.keys())[random.randint(1, len(list(prevdict.keys())))-1]
                        else:
                            Condition = list(prevdict.keys())[len(list(prevdict.keys()))-count]
                        splitCondition = Condition.split()
                        count = count + 1
                    else:
                        Condition = list(prevdict.keys())[count]
                        splitCondition = Condition.split()
                        count = count + 1
                else:
                    jsonSectionsDict[splitCondition[0]] = None
                    count = 0
                    countcount = countcount + 1
            if len(splitCondition) == 3:
                print(country.Conditionals[splitCondition[0]])
                if splitCondition[1] == '>':
                    if int(country.Conditionals[splitCondition[0]]) < int(splitCondition[2]):
                        Condition = random.choice(list(prevdict.keys()))
                        splitCondition = Condition.split()
                        count = count + 1
                    else:
                        b = " "
                        splitCondition = b.join(splitCondition)
                        jsonSectionsDict[splitCondition] = None
                        count = 0
                        countcount = countcount + 1
                if splitCondition[1] == '<':
                    if int(country.Conditionals[splitCondition[0]]) > int(splitCondition[2]):
                        Condition = random.choice(list(prevdict.keys()))
                        splitCondition = Condition.split()
                        count = count + 1    
                    else:
                        b = " "
                        splitCondition = b.join(splitCondition)
                        jsonSectionsDict[splitCondition] = None
                        count = 0
                        countcount = countcount + 1

