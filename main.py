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
    Add = stats.CountryStats()
    Continent = stats.CountryNameGen()
    Countries.append(Add)
    Continents.append(Continent)

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
def VariableAdder(Line, opposingCountry):
    MentionedCountry = None
    MentionedLeader = None
    count = 0
    RebellionCountry = random.choice(Countries)
    CurrentIdeology = None
    splitLine = Line.split()
    for i in splitLine:
        if i == '{OwnCountry}' or i == '{OwnNation}':
            splitLine[count] = country.Name
        if i == '{NewNation}':
            if opposingCountry != None:
                if MentionedLeader == None:
                    a = random.choice(Countries)
                    splitLine[count] = a.Name
                    RebellionCountry = a
                    MentionedCountry = a
                else:
                    keys = [key for key, val in CountryLeaders.items() if val == MentionedLeader]
                    splitLine[count] = keys[0]

        if i == '{OwnLeader}':
            splitLine[count] = country.LeaderName
        if i == '{NewLeader}':
            if MentionedCountry != None:
                splitLine[count] = CountryLeaders[MentionedCountry.Name]
            else:
                a = random.choice(list(CountryLeaders.items()))
                splitLine[count] = a
                MentionedLeader = a
        if i == '{CountryTitle}':
            splitLine[count] = random.choice(CountryTitles)
        if i == '{OwnIdeology}':
            a = country.BasicIdeologyDenonym
            splitLine[count] = a
            CurrentIdeology = a
        if i == '{Ideology}':
            a = denonym_ideologies[random.choice(list(ideologies.keys()))]
            while CurrentIdeology == a:
                a = denonym_ideologies[random.choice(list(ideologies.keys()))]
            splitLine[count] = a
            CurrentIdeology = a
            
        if i == '{OtherNationRebellionName}':
            a = CurrentIdeology
            line = random.choice(OtherNationRebellionNames[a])
            line = line.split()
            count2 = 0
            for i in line:
                if i == '{NewNation}':
                    line[count2] = RebellionCountry.Name
                count2 = count2 + 1
            CorrectedLine = " ".join(str(element) for element in line)
            splitLine[count]  = CorrectedLine
        if i == '{RebellionNation}':
            splitLine[count] = RebellionCountry.Name
        if i == '{Continent}':
            splitLine[count] = random.choice(Continents)
        if i == '{OwnReligion}':
            splitLine[count] = country.Religion
        if i == '{OwnRegion}':
            splitLine[count] = random.choice(country.CountryRegions)
        count = count + 1
        
    Line = " ".join(str(element) for element in splitLine)
    return Line

Text = ''
'''
for i in range(5):
    PickedLine = conditions.Conditions(country)
    SplitLine = RandomLine.split()
    Line = VariableAdder(SplitLine)
    CorrectedText = " ".join(str(element) for element in Line)
    Text = Text + "\n" + CorrectedText
'''
OpposingCountry = random.choice(Countries)
PickedLine, InvolvesOtherNation = conditions.Conditions(country, OpposingCountry)
print(PickedLine)
if InvolvesOtherNation == True:
    print(VariableAdder(PickedLine, OpposingCountry))
else:
    print(VariableAdder(PickedLine, None))