# setting attribute for a object of a class
class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")

counter = Counter()
counter() # This pbject is callable because we set a attribute for it. it's equal with counter.__call__()

# class as a decorator:
import functools


class CountCalls:
    def __init__(self, func, *, num_times=2):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_whee():
    print("Whee!")

say_whee()