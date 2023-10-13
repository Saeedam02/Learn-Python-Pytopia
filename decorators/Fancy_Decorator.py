# Decorators With Arguments

import functools

def repeat(num_times):
    def decorator_repeat(func):

        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

print(greet('Saeed'))

#Decorators that Can Optionally Take Arguments

def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

# _func=None
@repeat(num_times=4)
def say_hi(name):
    print(f"Hello {name}")

# _func=say_hi
@repeat
def say_hi(name):
    print(f"Hello {name}")


#Stateful Decorators

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)

    # set attribute before return
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


@count_calls
def say_whee():
    print("Whee!")

#cache decorator: if we call a function with an argument, at another call, if the argument was the before one, it doesn't calculate again and uses a memory.
def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args in wrapper.memory: #check if its in our memory
            print('reading from cache...')
            return wrapper.memory[args] #if yes then just return in right away!
        print('computing....')
        output = func(*args, **kwargs)
        wrapper.memory[args] = output #its not in our memory so lets compute and save it!
        return output
    wrapper.memory = {} #making an attribute for wrapper by monkey patching!
    return wrapper

@cache
def factorial(n):
    print(f'factorial {n}')
    return n * factorial(n-1) if n else 1