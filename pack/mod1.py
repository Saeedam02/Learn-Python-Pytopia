# Private variables.
_x = 'xx' # this variable doesn't appear when we import mod1.py, for importing these kind of variables, we need to import them by their name.

def foo():
    print('[mod1] foo()')

class Foo:
    pass
# we can use relative import( just we can use this way for current directory . and one ego directory ..)
from .mod2 import bar # from current working directory imort bar from mod2.py