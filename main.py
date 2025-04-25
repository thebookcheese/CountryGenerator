import stats
import json
import random

country = stats.CountryStats()
print(country)
print(country.Ideology)

# Open and read the JSON file
with open('history.json', 'r') as file:
    data = json.load(file)


CountryTitles = ['Duchy', 'Principality', 'Kingdom']
# Addings Variables to the randomly selected line
ideologies = {
    'Democracy': ['Liberal Democracy', 'Social Democracy', 'Constitutional Monarchy', 'Parliamentary Democracy',''],
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
    Continents = []
    for i in range(5):
        Add = stats.CountryNameGen()
        Continent = stats.CountryNameGen()
        Countries.append(Add)
        Continents.append(Continent)
    count = 0
    RebellionCountry = random.choice(Countries)
    CurrentIdeology = None
    for i in Line:
        if i == '{OwnCountry}':
            Line[count] = country.Name
        if i == '{NewNation}':
            a = random.choice(Countries)
            Line[count] = a
            RebellionCountry = a

        if i == '{OwnLeader}':
            Line[count] = country.LeaderName
        if i == '{NewLeader}':
            FirstName = stats.CountryNameGen()
            LastName = stats.CountryNameGen()
            Line[count] = FirstName + ' ' + LastName
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
            Line[count] = random.choice(Cont)
        count = count + 1
        
    return Line

Text = ''
for i in range(5):
    Section = random.choice(list(data[0]))
    Era = random.choice(list(data[0][Section]))
    RandomDataFromSection = random.choice(list(data[0][Section][Era]))
    RandomLine = random.choice(list(data[0][Section][Era][RandomDataFromSection]))
    SplitLine = RandomLine.split()
    Line = VariableAdder(SplitLine)
    CorrectedText = " ".join(str(element) for element in Line)
    Text = Text + "\n" + CorrectedText
print(Text)
