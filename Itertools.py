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


# for more details about itertools:
# https://docs.python.org/3/library/itertools.html