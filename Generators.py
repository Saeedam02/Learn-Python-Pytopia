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