# This file is related to packages in python
# inside of each package it is possible to have other sub packages like : pack.sub_paCK1.MOD3
# inside of a package file we can have a __init__ file which will be run when we run the main file.
# we can use this dunder method to initialize our packages.

import pack # in this way, by default, python doesn't do anything and if we use pack.mod1, we will face with error.
import pack.mod2
# for calling an attribute from this mpdule, we follow like:
pack.mod2.foo()

from pack.mod1 import foo # in this way, we put foo attribute inside of the global namespace.
# for calling an attribute from this mpdule, we follow like:
foo()
print(foo)

from pack.mod1 import foo
from pack.mod2 import foo #@ foo overwrite on the first foo.