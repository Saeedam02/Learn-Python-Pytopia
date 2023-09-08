class PeopleOfIran:
    #class attributes
    nationality = 'Iran'
    official_language = 'Farsi'

    # dunder method
    def __init__(self, fname, lname, age, location):
        #instance attributes
        self.fn = fname
        self.ln = lname
        self.age = age
        self.loc = location

    # this dunder method is used to print what it returns when we create an object from class and we just print its name
    def __str__(self):
        return 'Hi Dear'
    
    # instance method
    def speak(self):
        print(f'#MahsaAmini')

    def description(self):
        print(f' Hi, I am {self.fn} {self.ln} from {self.loc}')

Nika = PeopleOfIran('Nika', 'Shakarami', 16, 'Tehran')

