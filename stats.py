import random
consonents = ['b','c','d','f','g','h','j','k','m','n','l','p','q','r','s','t','v','w','y','z']
vowels = ['a','e','i','o','u']
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
PopulationsChances = {
    "300000": 0,
    "500000": 15,
    "1000000": 6,
    "5000000": 7,
    "10000000": 17,
    "15000000": 9,
    "20000000": 5,
    "25000000": 3,
    "30000000": 4,
    "35000000": 2,
    "40000000": 4,
    "45000000": 2,
    "50000000": 2,
    "55000000": 3,
    "60000000": 1,
    "65000000": 1,
    "70000000": 1,
    "75000000": 1,
    "80000000": 0,
    "85000000": 1,
}
class CountryStats:
    def __init__(self):
        self.LeaderFirstName = CountryNameGen()
        self.LeaderLastName = CountryNameGen()
        self.LeaderName = self.LeaderFirstName + ' ' + self.LeaderLastName
        self.Name = ''
        for i in range(5):
            if i == 0 or i == 2 or i == 4:
                a = random.choice(consonents)
                if i == 0:
                    a = a.upper()
                self.Name = self.Name + a
            else:
                a = random.choice(vowels)
                self.Name = self.Name + a
        Prev = 0
        self.PopulationUnformatted = 0
        for key in PopulationsChances:
            if random.randint(1,100) > PopulationsChances[key]:
                Prev = int(key)
            else:
                self.PopulationUnformatted = random.randint(Prev, int(key))
        self.PopulationUnformatted = self.PopulationUnformatted+1
        self.Population = "{:,}".format(self.PopulationUnformatted)
        self.GDPunformatted = random.randint(3, 2500)*1000000000
        self.GDP = "{:,}".format(self.GDPunformatted)
        self.GDP_per_capita_Unformatted = str(self.GDPunformatted/self.PopulationUnformatted)
        self.GDP_per_capita = ''
        DecimalPoint = False
        count = 0
        DecimalPointLocation = 0
        for i in self.GDP_per_capita_Unformatted:
            if i == '.':
                DecimalPoint = True
                break
            count = count+1
        if DecimalPoint == True:
            self.GDP_per_capita = self.GDP_per_capita_Unformatted[:count+3]
        else:
            self.GDP_per_capita = self.GDP_per_capita_Unformatted

        self.Religion = None
        self.BasicIdeology = random.choice(list(ideologies.keys()))
        self.BasicIdeologyDenonym = denonym_ideologies[self.BasicIdeology]
        self.Ideology = random.choice(ideologies[self.BasicIdeology])
        if self.GDPunformatted <= 10000000000:
            self.Catagory = 'Very Poor'
        elif self.GDPunformatted <= 100000000000 and self.GDPunformatted >= 10000000000:
            self.Catagory = 'Poor'
        elif self.GDPunformatted <= 100000000000 and self.GDPunformatted >= 1000000000000:
            self.Catagory = 'Middle'

    def __str__(self):
        return f'{self.Name} has a population of {self.Population} and a GDP of £{self.GDP} with a GDP per capita of £{self.GDP_per_capita}'

def CountryNameGen():
    Name = ''
    for i in range(5):
        if i == 0 or i == 2 or i == 4:
            a = random.choice(consonents)
            if i == 0:
                a = a.upper()
            Name = Name + a
        else:
                a = random.choice(vowels)
                Name = Name + a
    return Name
