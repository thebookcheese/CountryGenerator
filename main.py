import stats
import random
import conditions

country = stats.CountryStats()
print(country)
print(country.Ideology)
Religion = ['Islam', 'Catholism','Protestantism']
country.Religion = random.choice(Religion)

Countries = []
CountryLeaders = {}
Continents = []
for i in range(3):
    Add = stats.CountryStats() # generates a new country
    Continent = stats.CountryNameGen() # generates the name of a continent
    Countries.append(Add)
    Continents.append(Continent)
    #Adds the countries and continents to their respective lists


#Creates lists for titles, ideologies (and their denonyms), and names of rebellions
CountryTitles = ['Duchy', 'Principality', 'Kingdom']
ideologies = {
    'Democracy': ['Liberal Democracy', 'Social Democracy', 'Constitutional Monarchy', 'Parliamentary Democracy'],
    'Communism': ['Marxism','Leninism','Marxist-Leninism','Stalinist'],
    'Monarchy' : ['Absolute Monarchy', 'Constitutional Monarchy']
}
denonym_ideologies = {
    'Democracy' : 'Democratic',
    'Communism' : 'Communist',
    'Monarchy' : 'Monarchist'
} 
OtherNationRebellionNames = {
    'Democratic' : ['Free state of {NewNation}', 'New republic of {NewNation}'],
    'Communist': ['Liberation Army Of {NewNation}', "People's state of {NewNation}", "Democratic People's republic of {NewNation}"],
    'Nationalist' : ['New Empire of {NewNation}'],
    'Monarchist' : ['Kingdom of {NewNation}', 'Absolute Monarchy of {NewNation}']
,}


def VariableAdder(Line, opposingCountry): # Function to add variables to the string
    MentionedCountry = None # for checking if there is a previously mentioned country
    MentionedLeader = None # for checking if there is a previously mentioned leader :0
    count = 0
    RebellionCountry = random.choice(Countries) # picks a random country
    CurrentIdeology = None # what ideology is it
    splitLine = Line.split() # splits the line into words
    for i in splitLine: # iterates over the split line
        if i == '{OwnCountry}' or i == '{OwnNation}':
            splitLine[count] = country.Name # adds the name of the country to the line
        if i == '{NewNation}':
            if opposingCountry != None: # checks if there  is an opposing leader
                if MentionedLeader == None: # checks if there is a previously mentioned leader
                    a = random.choice(Countries) # picks a random country
                    splitLine[count] = a.Name # replaces the placeholder with the name of the leader
                    RebellionCountry = a #sets the picked countey to the rebillion country
                    MentionedCountry = a # sets the picked country to the mentioned country
                else:
                    keys = [key for key, val in CountryLeaders.items() if val == MentionedLeader] # checks for the country leader in the countryleader dictionary
                    splitLine[count] = keys[0] # replaces the place holder with the mentioned leader

        if i == '{OwnLeader}': 
            splitLine[count] = country.LeaderName # replaces it with the leader name
        if i == '{NewLeader}':
            if MentionedCountry != None: # checks if there is a previously mentioned country
                splitLine[count] = CountryLeaders[MentionedCountry.Name] # if there is set it to that country's leader
            else: # if not
                a = random.choice(list(CountryLeaders.items())) # picks a random leader
                splitLine[count] = a
                MentionedLeader = a # sets the mentioned as the random leader
        if i == '{CountryTitle}':
            splitLine[count] = random.choice(CountryTitles) # picks a country title
        if i == '{OwnIdeology}':
            a = country.BasicIdeologyDenonym # get the ideology of the country
            splitLine[count] = a
            CurrentIdeology = a
        if i == '{Ideology}':
            a = denonym_ideologies[random.choice(list(ideologies.keys()))] # picks a random ideology
            while CurrentIdeology == a:
                a = denonym_ideologies[random.choice(list(ideologies.keys()))] # picks a random ideology until it isn't the country's ideology
            splitLine[count] = a
            CurrentIdeology = a
            
        if i == '{OtherNationRebellionName}':
            a = CurrentIdeology
            line = random.choice(OtherNationRebellionNames[a]) #picks a rebbelion name with the current ideology
            line = line.split()
            count2 = 0
            for i in line:
                if i == '{NewNation}':
                    line[count2] = RebellionCountry.Name
                count2 = count2 + 1
            CorrectedLine = " ".join(str(element) for element in line)
            splitLine[count]  = CorrectedLine #
        if i == '{RebellionNation}':
            splitLine[count] = RebellionCountry.Name
        if i == '{Continent}':
            splitLine[count] = random.choice(Continents) # picks a random continent
        if i == '{OwnReligion}':
            splitLine[count] = country.Religion
        if i == '{OwnRegion}':
            splitLine[count] = random.choice(country.CountryRegions) # picks a random region
        count = count + 1
        
    Line = " ".join(str(element) for element in splitLine) # combines the line back together
    return Line # returns it

Text = ''

'''
for i in range(5):
    PickedLine = conditions.Conditions(country)
    SplitLine = RandomLine.split()
    Line = VariableAdder(SplitLine)
    CorrectedText = " ".join(str(element) for element in Line)
    Text = Text + "\n" + CorrectedText
'''

f = open('history.txt','w')
for i in range(2):
    OpposingCountry = random.choice(Countries) # picks a random opposing country
    PickedLine, InvolvesOtherNation = conditions.Conditions(country, OpposingCountry)

    print(PickedLine)
    if InvolvesOtherNation == True:
        a = VariableAdder(PickedLine, OpposingCountry) # runs variable adder
        f.write(a + '\n')
    else:
        a = VariableAdder(PickedLine, None)
        f.write(a + '\n')
    f.write(str(country.Conditionals['Tension']) + '\n')

