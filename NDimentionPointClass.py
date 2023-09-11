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
       
my_points = [Point(2, 4, 3), Point(5, 9, 8), Point(3, 7, -1), Point(8, 6, 8), Point(6, 6, 11), Point(1, 1, -6) ]
p = Point(7, 24)
print(abs(p))
print(sorted(my_points))