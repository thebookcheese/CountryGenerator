import stats
import random
import conditions

country = stats.CountryStats()
print(country)
print(country.Ideology)
Religion = ['Islam', 'Catholism','Protestantism']
country.Religion = random.choice(Religion)


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
def VariableAdder(Line):
    Countries = []
    CountryLeaders = {}
    Continents = []
    MentionedCountry = None
    MentionedLeader = None
    for i in range(3):
        Add = stats.CountryNameGen()
        Continent = stats.CountryNameGen()
        Countries.append(Add)
        Continents.append(Continent)
        CountryLeaders[Add] = stats.CountryNameGen() + ' ' + stats.CountryNameGen()
    count = 0
    RebellionCountry = random.choice(Countries)
    CurrentIdeology = None
    for i in Line:
        if i == '{OwnCountry}':
            Line[count] = country.Name
        if i == '{NewNation}':
            if MentionedLeader == None:
                a = random.choice(Countries)
                Line[count] = a
                RebellionCountry = a
                MentionedCountry = a
            else:
                keys = [key for key, val in CountryLeaders.items() if val == MentionedLeader]
                Line[count] = keys[0]

        if i == '{OwnLeader}':
            Line[count] = country.LeaderName
        if i == '{NewLeader}':
            if MentionedCountry != None:
                Line[count] = CountryLeaders[MentionedCountry]
            else:
                Line[count] = random.choice(list(CountryLeaders.items()))
        if i == '{CountryTitle}':
            Line[count] = random.choice(CountryTitles)
        if i == '{OwnIdeology}':
            a = country.BasicIdeologyDenonym
            Line[count] = a
            CurrentIdeology = a
        if i == '{Ideology}':
            a = denonym_ideologies[random.choice(list(ideologies.keys()))]
            while CurrentIdeology == a:
                a = denonym_ideologies[random.choice(list(ideologies.keys()))]
            Line[count] = a
            CurrentIdeology = a
            
        if i == '{OtherNationRebellionName}':
            a = CurrentIdeology
            line = random.choice(OtherNationRebellionNames[a])
            line = line.split()
            count2 = 0
            for i in line:
                if i == '{NewNation}':
                    line[count2] = RebellionCountry
                count2 = count2 + 1
            CorrectedLine = " ".join(str(element) for element in line)
            Line[count]  = CorrectedLine
        if i == '{RebellionNation}':
            Line[count] = RebellionCountry
        if i == '{Continent}':
            Line[count] = random.choice(Continents)
        if i == '{OwnReligion}':
            Line[count] = country.Religion
        if i == '{OwnRegion}':
            Line[count] = random.choice(country.CountryRegions)
        count = count + 1
        
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
PickedLine = conditions.Conditions(country)
print(PickedLine)
print(country.Conditionals)