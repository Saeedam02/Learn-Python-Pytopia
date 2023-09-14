class Parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

        self.kids = []

    def speak(self, text):
        return f'{self.fname} says: {text}'
    
    def have_child(self, child_name):
        child = Child(self, child_name)
        self.kids.append(child)
        return child
        
meysam = Parent('Meysam', 'Pirfalak')
meysam.speak('Hi')

class  Child(Parent):
    def __init__(self, parent, fname):
        self.parent = parent
        self.fname = fname
        self.lname= parent.lname

k = meysam.have_child('Kian')

print(type(meysam))