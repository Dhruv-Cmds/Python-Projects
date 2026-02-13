# Property
# Create class Rectangle:
# private variables: __length, __breadth
# property area that returns area
# No setter required
# Use object and print area like:
# print(r.area)

class Rectangle:
    def __init__(self , length , breadth):

        self.length = length
        self.breadth = breadth
    
    @property
    def area (self):
        return self.length * self.breadth
    
    def __str__(self):
        return f"Rectangle(length={self.length}, breadth={self.breadth})"
        

r = Rectangle (10 , 5) 
print(r.area)