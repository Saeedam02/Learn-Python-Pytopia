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
