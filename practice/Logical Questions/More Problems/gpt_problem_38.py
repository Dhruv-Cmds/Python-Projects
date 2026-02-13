# Create a class Calculator:
# Constructor takes a number.
# Methods:
# square()
# cube()
# Call both methods using object.

class Calculator:
    def __init__(self , n):
        self.n = n
    
    def square (self):
        print(f"Square is : {self.n * self.n}")

    def cube (self):
        print(f"Cube is : {self.n * self.n * self.n}")

c = Calculator(4)
c.square()
c.cube()