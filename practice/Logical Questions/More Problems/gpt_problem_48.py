# Operator Overloading
# Create a class Money with attribute amount.
# Overload the + operator to add two Money objects.

class Money:

    def __init__(self , money):
        self.money = money

    def __add__(self, other):
       return Money(self.money + other.money)
    
    def __str__(self):
        return f"{self.money}"

m = Money(500)
n = Money(300)
print(m + n)