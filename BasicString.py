Iran = ['Mahsa', 'Nika', 'Hadis']
print(*Iran, sep = '-~-')

# Note that we can unpack a list by using " * " before the list's name.

List=['Ali', 19, 'Tehran']
for i in List:
    print(i, end = '\n---\n')


####################### Format string usimg name indexing 

print("The area of the circle with radius {r} is equal to {area}".format( r = (r:=5), area = 3.14 * (r ** 2)))

## the Walrus operator " := " , it is used to define a variable and also assign a value for it

a=3265489752
print(f'{a:,}')

N=[5421241,83992949,331002651]
for n in N:
    print(f'{ n:,}'.zfill(11)) # we can use zfill for pad specific number length 

# second way :
for n in N:
    print(f'{n:011,}')