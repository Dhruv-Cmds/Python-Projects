# AUTHOR
# Dhruv

# VEHICLE SYSTEM OOP

# Parent class
class Vehicle:
    
    def __init__(self , speed , fuel): 
        self.speed = speed
        self.fuel = fuel

    def show_info (self):
        print("Speed:", self.speed)
        print("Fuel:", self.fuel)

# Children class
class Car(Vehicle):

    def __init__ (self , speed , fuel , brand):
        self.brand = brand

        # From parent class
        super().__init__(speed , fuel)

        # UNIQUE METHOD
    def open_trunk(self):
        print("Car trunk is opened")

# Children class
class Bike(Vehicle):
    
    def __init__ (self , speed , fuel , brand):
        self.brand = brand

        # From parent class
        super().__init__(speed , fuel)

        # UNIQUE METHOD
    def kick_start(self):
        print("Bike started using kick") 


print("---CAR INFO---")
c = Car(120, "Petrol", "Toyota")
c.show_info()
c.open_trunk()
print(f"The brand of the car is {c.brand}")

print("---BIKE INFO---")
b = Bike(80, "Petrol", "Honda")
b.show_info()
b.kick_start()
print(f"The brand of the bike is {b.brand}")