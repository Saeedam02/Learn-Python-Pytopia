class Vehicle:
    def __init__(self, max_speed, milage, capacity) :
        self.max_speed = max_speed
        self.milage = milage 
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100 # 100 is the fare for each person
    
v = Vehicle(120, 500, 5)
# Copmuter Operitional logic
Vehicle.fare(v)
# Mental mind programmer(syntactic sugar)
v.fare()

class Bus(Vehicle):
    def fare(self):
        #return self.capacity * 100 * 1.1 : in tjis way, is our logic changed, we must rewrite whole logic in both fare functions
        #return Vehicle.fare(self) * 1.1 # 1.1 is the fare for bus instance which is more than others
        # in the above logic, if our bus class inherite from other class, we must change the logic
        #return super(Bus, self).fare() * 1.1 : this suoper function still has a duplicate problem related to Bus name
        return super().fare() * 1.1
    
bus = Bus(100, 120, 60)
print(isinstance(v, Vehicle))


#### Example 2: Train

class Train:
    def __init__(
            self,
            last_visited_city:str,
            weight_capacity:float,
            is_on_trip:bool
    ):
        self.last_visited_city = last_visited_city
        self.weight_capacity = weight_capacity
        self.is_on_trip = is_on_trip

class TripP:
    #class attribute
    all_cities=(
        'Arak', 'Ardabil', 'Miyaneh', 'Tehran', 'Mashhad'
    )
    def __init__(
            self,
            train:Train,
            origin_city:str,
            destination_city:str
            ):
        if not isinstance(train, Train):
            raise Exception(' This input is not a train!')
        self.train = train
        self.origin_city = origin_city
        self.destination_city = destination_city

    def origin_city_validation(self):
        if self.origin_city not in self.all_cities:
            raise Exception('This input is not a verified city!')
        return self.origin_city
    
    # with call method, we can call each attributes
    def __call__(self):
        pass 
        

train = Train('Arak', 6666, is_on_trip=True)

# Example 3: Point table

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # __str__ represents what is readable for human
    # def __str__(self) :
    #     # return f"Point( {self.x}, {self.y})" :this isn't dynamic because of Point
    #     return f'{self.__class__.__name__} ({self.x}, {self.y})'
    
    # __repr__ represents what is readable for computer, the above code is both __str__ and __repr__
    # it is good to define __repr__ when both str and repr are same.
    def __repr__(self) :
        return f'{self.__class__.__name__} ({self.x}, {self.y})'
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    # The less than function has an input and a object
    def __lt__(self, obj):
        return abs(self) < abs(obj)
    
 
my_points = [Point(2, 4), Point(5, 9), Point(3, 7), Point(8, 6), Point(6, 6), Point(1, 1), ]
p = Point(3, 4)
print(abs(p))
print(sorted(my_points))
print(sorted(my_points, key=lambda p:p.y)) # the sorted function sorts our list by given method.

# Extra function for fun: Bubble sorting method
# This sorting method has O(N^2) time complexity 
# This sorting method has O(N) space complexity
# If we delete copy() part and use the origin list we will have O(1) space complexity
def sort_list(l_source): 
    l = l_source.copy()
    for _ in range(len(l)):
        for ind in range(len(l) - 1):
            if l[ind + 1] < l[ind]:
                l[ind] , l[ind + 1] = l[ind + 1], l[ind]

    return l 
print(sort_list([1, 3 ,-5, -2, 7, -6, 2]))

# This function doesn't work for a list of point because for point class we don't have less than or grater than function
# Extra function for fun: Bubble sorting method for list of point
def sort_list(l_source): 
    l = l_source.copy()
    for _ in range(len(l)):
        for ind in range(len(l) - 1):
            if abs(l[ind + 1]) < abs(l[ind]):
                l[ind] , l[ind + 1] = l[ind + 1], l[ind]

    return l 
print(sort_list(my_points))