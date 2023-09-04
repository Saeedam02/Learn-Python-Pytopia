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


######################### difference between * and *ignore 

## with *ignore
def operator(x, y, *ignore, op='+'):
    if op == '+' :
        return x + y
    elif op == '-':
        return x - y
    elif op == '/':
        return x / y 
    
operator(3, 6, 5, 7, op='-')  # by using *ignore we can give positional argments more than defined ones and python put them in ignore

## with *
def operator(x, y, *, op='+'):
    if op == '+' :
        return x + y
    elif op == '-':
        return x - y
    elif op == '/':
        return x / y 
    
operator(3, 6, 5, 7, op='-') # by using * we can't give positional argments more than defined ones