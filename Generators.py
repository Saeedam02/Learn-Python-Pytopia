# Note that functions like map or filter or zip have output in form of generator.
l = [1, 2, 3]
map(lambda i : i*2 ,l)
filter(lambda i: i!= 1, l)
zip(l, l)

# we can write a zip generator by ourself:
def zip_gen(l1, l2):
    for i in range(len(l1)):
        item1 = l1[i]
        item2 = l2[i]
        yield (item1, item2)

g = zip_gen([1,2,3],[4,5,6])
next(g)


def my_gen(mylist): # input must be an iterable.
    for item in mylist:
        yield item**2

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gen = my_gen(x)
next(gen)

##infinite_sequence generator
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
next(gen)

## multi_yield
def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str

multi_obj = multi_yield()
next(multi_obj)


####################################################
## Building Generators With Generator Expressions###
####################################################
nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (num**2 for num in range(5))

# Both nums_squared_lc and nums_squared_gc look basically the same, but there’s one key difference. Can you spot it? Take a look at what happens when you inspect each of these objects:
# nums_squared_lc ->[0, 1, 4, 9, 16]
# nums_squared_gc -> <generator object <genexpr> at 0x7f9143561f50>

###################################
##Profiling Generator Performance##
###################################

import sys

nums_squared_lc = [i * 2 for i in range(10000)]
sys.getsizeof(nums_squared_lc) #87632

nums_squared_gc = (i ** 2 for i in range(10000))
sys.getsizeof(nums_squared_gc) #128

# So generators are very space efficent than other ones.
# But in the sense of time complexity: 