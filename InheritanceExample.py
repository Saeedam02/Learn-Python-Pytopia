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
print(isins)