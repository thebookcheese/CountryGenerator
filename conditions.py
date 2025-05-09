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
    f = open('history.json', 'r') # opens the json file
    data = json.load(f) # loads the json file as a list
    data = data[0] # converts it to a dict (0 index = 1st element)
    LinePicked = False # checks if a line has been picked
    while LinePicked == False: # while it isn't picks
        condition = random.choice(list(data.keys())) # picks a random condition
        if count_dict(data) != 3 and condition != 'TextOptions': # check if the dictionary does not have 3 nested dictionarys inside it or if the condition is text options
            splitcondition = condition.split() # splits the condition into a list (by spaces)
            if len(splitcondition) == 2: # checks if the length of the list is 2
                if splitcondition[0] == 'Not': # and then checks if the first element in the split condition is 'Not'
                    if country.Conditionals[splitcondition[1]] == False: # if the country's condition is False
                        data = data[condition] # move the dictionary further inside that section by 1 layer
            elif len(splitcondition) == 3: # if the length of the list is 3
                comparators = ['>', '<'] # creates the comparators list
                if splitcondition[1] in comparators: # checks if the 2nd element in the split condition is a comparator
                    if splitcondition[1] == comparators[0]:
                        if country.Conditionals[splitcondition[0]] > int(splitcondition[2]): # checks if the 1st element of the split condition is
                            data = data[condition] # moves the dictionary in by one layer
                    elif splitcondition[1] == comparators[1]: # checks if the 2nd element of the split condtion is equal to the 2nd element in comparators
                        if country.Conditionals[splitcondition[0]] < int(splitcondition[2]):
                            data = data[condition] # moves the dictionary in by a layer
            else:
                if country.Conditionals[condition] == True:
                    data = data[condition] # moves the data in by a layer
        else: # if there is 3 nested dictionaries
            data = data['TextOptions'] # move the dictiornary in by a layer
            line = random.choice(list(data.keys())) # picks a line
            data = data[line]
            data = data["Result"] # moves the data in by some more layers
            owncountry = True
            for key in data: # iterates over the keys in the data
                if key == 'owncountry':
                    if data[key] == 'false':
                        owncountry = False
                else:
                    if owncountry == True:
                        if data[key] == 'true':
                            country.Conditionals[key] = True # read below
                        elif data[key] == 'false':
                            country.Conditionals[key] = False # read below
                        elif type(data[key]) == int:
                            country.Conditionals[key] = data[key]  # changes the conditions to the results
            OtherNation = ['{NewNation}', '{NewLeader}']
            splitline = line.split()
            OtherNationIncluded = False
            for i in splitline:
                if i in OtherNation:
                    OtherNationIncluded = True # checks if other nations are mentioned
            return line, OtherNationIncluded