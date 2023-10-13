import functools

def do_twice(func):
    @functools.wraps(func) #It'll put the fun's dir into wrapper function like: doc,__name__, __annotations__ and ...
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_whee():
    """
    This function says whee!
    """
    print("Whee!")