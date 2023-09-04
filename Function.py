d_1 = {
    'Ali' : 30,
    'Hmid' : 25,
    'Saeed' : 25,
}

d_2 = {
    'Mohammad' : 26,
    'Ahmad' : 30,
}

d = { **d_1 , **d_2 }
#print(d)

def print_age(**kwargs):
    for name, age in kwargs.items() :
        print(f'{name:10} is {age:3} years old')

print_age(**d)
