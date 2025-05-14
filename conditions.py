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
                    if owncountry == True: # if owncountry = true then
                        if type(data[key]) == str: # checks if the type of the new data is a string
                            splitresult = data[key].split() #and splits it if it is
                        else:
                            splitresult = '' # if it isn't, then it splits the result to an empty string
                        if type(data[key]) == bool: # checks if the type of the new data is a boolean
                            country.Conditionals[key] = data[key] # sets the condional key to the new data
                        elif type(data[key]) == str and len(splitresult) == 3: # if the new data is a string and it has 3 words then
                            splitresult = data[key].split() # split it by spaces
                            if splitresult[0] == 'randint': # if its first word is randint
                                country.Conditionals[key] = random.randint(int(splitresult[1]), int(splitresult[2])) # then it generates a random number
                        elif 'var' in splitresult: # checks if there is a variable in split result
                            times_var = 0
                            index = 0
                            for i in range(len(splitresult)): # iterates over the length of split result
                                if i == 'var': # checks if i is equal to 'var'
                                    times_var += 1 # increases times_var by one if it is
                            if times_var == 1: # checks if times_var is equal to one
                                for i in range(len(splitresult)-1): # iterates over the length of split result - 1
                                    if i == 'var': # checks if i is equal to 'var'
                                        break
                                    else: 
                                        index += 1 # increases index by 1
                                variable = splitresult[index+1] # sets variable to index
                                if splitresult[0] == 'randint': # if the first element in split result is 'randint' then
                                    if index == 2: # check if index is equal to 2
                                        country.Conditionals[key] = random.randint(country.Conditionals[variable], splitresult[4]) # random number generating - sets a variable to it
                                    elif index == 3:
                                        country.Conditionals[key] = random.randint(splitresult[1], country.Conditionals[variable]) # same as above but reversed
                        elif type(data[key]) == int:
                            country.Conditionals[key] = data[key]  # changes the conditions to the results
            OtherNation = ['{NewNation}', '{NewLeader}']
            splitline = line.split()
            OtherNationIncluded = False
            for i in splitline:
                if i in OtherNation:
                    OtherNationIncluded = True # checks if other nations are mentioned
            f.close()
            return line, OtherNationIncluded