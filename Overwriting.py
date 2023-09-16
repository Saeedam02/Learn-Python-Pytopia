# By using Zip function, it gaves us elementwise of two by two of two tuple or list.Point
t1 = (1, 2, 3)
t2 = (3, 2, 8)
list(zip(t1, t2)) #-> [(1,3),(2,2),(3,8)]

# for writing the __add__ function for our calss, we can use the following approach:
list(map(lambda item: item[0] + item[1], zip(t1, t2)))
# second approach
list(map(sum, zip(t1, t2)))

class Point:
    def __init__(self, *args):
        self.vector = args

    def __repr__(self) :
        return f'{self.__class__.__name__} {self.vector}'
    
    def __abs__(self):
        sum_value = sum([e ** 2 for e in self.vector])
        return sum_value ** 0.5 
    
    # The less than function has an input and a object
    def __lt__(self, obj):
        return abs(self) < abs(obj)
    
    def __add__(self, other):
            args = map(sum, zip(self.vector, other.vector))
            return Point(*args)

       
# my_points = [Point(2, 4, 3), Point(5, 9, 8), Point(3, 7, -1), Point(8, 6, 8), Point(6, 6, 11), Point(1, 1, -6) ]
# p = Point(7, 24)
# print(abs(p))
# print(sorted(my_points))
p1 = Point(1, 2, 4)
p2 = Point(3, 2, 8)
print(Point(3, 2, 8)+Point(1, 2, 4))

# Extra information

# Zip  function gives us a list of elementwise of two tuple or list untill shoetest one come over
list(zip([1,2], [2,3,4,5])) #-> [(1,2), (2,3)]

# if we want to go to end of the longest one, we need to use the following approach:
from itertools import zip_longest
list(zip_longest([1,2], [2,3,4,5])) #-> [(1,2), (2,3),(None,4), (None,5)]

# it has a by default value with is None. we can change it:
list(zip_longest([1,2], [2,3,4,5], fillvalue=0)) #-> [(1,2), (2,3),(0,4), (0,5)]
