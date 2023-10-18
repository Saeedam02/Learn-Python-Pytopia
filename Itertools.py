import itertools as it
def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
naive_grouper(nums, 2)

# by using of itertools
def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)

def better_grouper_two(inputs, n):
    iters = [iter(inputs)] * n
    return it.zip_longesst(*iters)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(better_grouper(nums, 4))

list(better_grouper_two(nums, 4))

############# Combination with itertools
bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
set(it.combinations(bills, 5)) # 5 is length of combinations

list(it.combinations_with_replacement([1, 2], 2))

############# Permutations with itertools
list(it.permutations(['a', 'b', 'c'])) #جایگشت های ممکن

def evens():
    """Generate even integers, starting with 0."""
    n = 0
    while True:
        yield n
        n += 2

def odds():
    """Generate odd integers, starting with 1."""
    n = 1
    while True:
        yield n
        n += 2

# Evens with itertools
evens = it.count(step=2)
list(next(evens) for _ in range(5))

# Odds with itertools
odds = it.count(start=1, step=2)
list(next(odds) for _ in range(5))

# Indexing member of a list using itertools
list(zip(it.count(), ['a', 'b', 'c'])) # ->[(0, 'a'), (1, 'b'), (2, 'c')]

# Repeating using by itertools
all_ones = it.repeat(1)  # 1, 1, 1, 1, ...
five_ones = it.repeat(1, 5)  # 1, 1, 1, 1, 1

# Cycle
alternating_ones = it.cycle([1, -1])  # 1, -1, 1, -1, 1, -1, ...

#accumulate
def accumulate(inputs, func):
    itr = iter(inputs)
    prev = next(itr)
    for cur in itr:
        yield prev
        prev = func(prev, cur)

import operator
list(it.accumulate([1, 2, 3, 4, 5], operator.add)) #->[1, 3, 6, 10, 15]

# first_order
def first_order(p, q, initial_val):
    """Return sequence defined by s(n) = p * s(n-1) + q."""
    return it.accumulate(it.repeat(initial_val), lambda s, _: p*s + q)

evens = first_order(p=1, q=2, initial_val=0)
list(next(evens) for _ in range(5)) #-> [0, 2, 4, 6, 8]

# Recurrence Relations
def fibs():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# for more details about itertools:
# https://docs.python.org/3/library/itertools.html