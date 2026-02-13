# Property Decorator
# Create class Temperature:
# private variable __celsius
# property fahrenheit to get temperature in Fahrenheit
# setter to update Celsius when Fahrenheit is changed

class Temerature:

    def __init__(self , celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    @fahrenheit.setter

    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

t = Temerature(0)
print(t.fahrenheit)  
t.fahrenheit = 212    
print(t.fahrenheit)  


