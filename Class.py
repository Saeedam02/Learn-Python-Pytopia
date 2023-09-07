class PeopleOfIran:
    #class attributes
    nationality = 'Iran'
    official_language = 'Farsi'
    def __init__(self, fname, lname, age, location):
        #instance attributes
        self.fn = fname
        self.ln = lname
        self.age = age
        self.loc = location

    # instance method
    def speak(self):
        print(f'#MahsaAmini')

    def description(self):
        print(f' Hi, I am {self.fn} {self.ln} from {self.loc}')
         