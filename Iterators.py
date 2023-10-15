my_list = [4, 7, 0, 3] # it's an iterable

myiter = iter(my_list) # it's an iterator
# iterate through it using next()
next(myiter)

# next(obj) is same as obj.__next__()
myiter.__next__()

# Working of for loop for Iterators
# create an iterator object from that iterable
iter_obj = iter(my_list)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
# Note that when you run this while or a for loop on an iterator, after that if you want to go through that,
# you need to initialize it again.beacuse after loop, the next of the iterator is none and it's false.