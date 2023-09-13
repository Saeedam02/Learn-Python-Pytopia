########################
## single inheritance ##
########################

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
        
    def area(self):
        return self.length + (2 * self.width)
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width

r = Rectangle(3, 4)
print(r.area())

# for defining square class : approach 1

class Square:
    def __init__(self, length) -> None:
        self.length = length

    def area(self):
        return self.length * self.length
    
    def perimeter(self):
        return self.length * 4

# approach 2 : with inheritance

# class Square(Rectangle):
#     pass -> in this situation Square is the same as Retangle

class Square(Rectangle):
    def __init__(self, length) -> None:
        #the following way become hard when our init function was complex
        # self.length = length
        # self.width = length
        
        # the following way still is complex 
        #Rectangle.__init__(self, length, length)

        # Python has a built in function named super() we can use it in his situation
        super(Square, self).__init__(length, length) 
        # with super, we don't need to use self in init function. becouse super sends object to function automatically

############################
## Multi level inheritance##
############################

class Cube(Square):
    # the init function is same as square so it isn't necessary to over write it.

    # cube has no attribute named area and perimeter so we need to raise error when someone call them

    def area(self):
        raise AttributeError('Cube has no attribute named area')
    
    def perimeter(self):
        raise AttributeError('Cube has no attribute named perimeter')
    
    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    
    def volume(self):
        face_area = super().area()
        return face_area * self.length
    

#############################
## Hierarchical Inheritance##
#############################


#           shape
#         /      \
#     Retangle    circle
#       /
#    Square
#     /
#   Cube

class Shape:
    def __init__(self, color=None):
        self.color = color
class Circle(Shape):
    def __init__(self, radius, color=None) :
        super().__init__(color)
        self.radius = radius

    def perimeter(self):
        return self.radius * 2 * 3.14
    
    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(3, "Red")
print(c.area())

class Rectangle(Shape):
    def __init__(self, length, width, color=None):
        super().__init__(color)
        self.length = length
        self.width = width
        
    def area(self):
        return self.length + (2 * self.width)
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width
    

class Square(Rectangle):
    def __init__(self, length, color=None):
        super(Square, self).__init__(length, length, color) 
class Cube(Square):

    def area(self):
        raise AttributeError('Cube has no attribute named area')
    
    def perimeter(self):
        raise AttributeError('Cube has no attribute named perimeter')
    
    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    
    def volume(self):
        face_area = super().area()
        return face_area * self.length
###############################
## isinstance and issubclass ##
###############################

c = Cube(3)
# isinstance
print(isinstance(c, Square))
print(isinstance(c, Rectangle))
print(isinstance(c, Circle))

#issubclass
print(issubclass(Cube, Square))
print(issubclass(Rectangle, Shape))

# Note that all class are a subclass of Object class
print(issubclass(Cube, object))

# Extra information
print(issubclass(type, object))
print(isinstance(object, type))

#########################
## Multiple Inheritance##
#########################
# this kind of inheritance is very complex and we need to try avoid using this as much as possible
 
# superclass 1       superclass 2
#    \                   /
#     \                 /
#      \               /
#          subclass

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
    
    def perimeter(self):
        return self.length * 4
    
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class RightPyramid(Square, Triangle):
    def __init__(self,base, slant_height):
        self.base = base
        self.slant_height = slant_height
        # if we don't set the length for the square area, we will face with error, so:
        super().__init__(base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        tri_area = perimeter * self.slant_height * 0.5
        return tri_area + base_area
    
pyramid = RightPyramid(2, 4) # This code will face with an error caused by method resolution order
print(pyramid.area())

# Overriding
# we can rewrite built in functions in the way that we want.
class Cart:
    def __init__ (self, *args):
        self.items = list(args) # we change the args from tuple to list till we can set items.

    def __len__(self):
        return len(self.items)
    
    def __bool__(self):
        return bool(self.items)
    

    def __add__(self, other):
        new_item = self.items + other.items
        return Cart(*new_item)
    
    def __getitem__(self, key):
        return self.items[key]
    
    def __Setitem__(self, key, value):
        self.items[key] = value

c1 = Cart('apple')
c2 = Cart('banana','pear')
c3 = Cart('mango')
# c1 + c2 -> c1.__add__(c2)
 