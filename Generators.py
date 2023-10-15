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