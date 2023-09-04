# Python Function Annotations
# As of version 3.0, Python provides an additional feature for documenting a function called:
# a function annotation. Annotations provide a way to attach metadata to a function’s parameters and return value.

def f(a: float, b: float = 8) -> int:
    """Add two number.

    :param a: First input
    :param b: Second input
    :return: Sum of two numbers.
    """
    
    return a + b

# for more details, take a look at :
# https://github.com/pytopia/Python/blob/main/Python/01.%20Basics/19%20Defining%20Your%20Own%20Python%20Function%20(Part%202).ipynb


# there is a lbrary in python named typing that help us to define more specific about arguments type:

from typing import List , Dict

def f(a: List[int], b: dict ) -> set :
    """Add two number.

    :param a: First input
    :param b: Second input
    :return: Sum of two numbers.
    """
    
    return a + b
