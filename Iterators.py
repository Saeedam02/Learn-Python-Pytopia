my_list = [4, 7, 0, 3] # it's an iterable

myiter = iter(my_list) # it's an iterator
# iterate through it using next()
next(myiter)

# next(obj) is same as obj.__next__()
myiter.__next__()