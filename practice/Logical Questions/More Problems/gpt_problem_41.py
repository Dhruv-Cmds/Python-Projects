# Create class Calculator:
# Constructor takes number
# Methods:
# square()
# cube()
# square_root()
# Rules:
# If number < 0 → print "Square root not possible"
# Static method:
# def greet():
#     print("Welcome to Calculator")
# Call static method using class.
    

class calculator:
    def __init__(self , n):
        self.n = n

    def square (self):
        print (f"the square is :{self.n * self.n}")

    def cube (self):
        print (f"the cube is :{self.n * self.n * self.n}")

    def squareroot (self):
        if (self.n >= 0):
            print (f"the squareroot is :{self.n ** 0.5}")
        else:
            print("Square root not possible")

    @staticmethod

    def greet():
        print("Welcome to Calculator")

a = calculator(-5)
a.greet()
a.square()
a.cube()
a.squareroot()