# single inheritance

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


# Multi level inheritance

class Cube(Square):
    # the init function is same as square so it isn't necessary to over write it.

    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    
    def volume(self):
        face_area = super().area()
        return face_area * self.length
    



    

