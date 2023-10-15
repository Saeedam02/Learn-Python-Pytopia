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

#####################################
##### Building Custom Iterators #####
#####################################
class Counter:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, min=0, max=0):
        self.max = max

    def __iter__(self):
        self.n = self.min
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# create an object
numbers = Counter(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
next(i)

#################################
### Python Infinite Iterators ###
#################################
inf = iter(int, 1)
next(inf)