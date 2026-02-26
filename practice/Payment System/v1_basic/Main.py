# AUTHOR
# Dhruv

# Parent class
class Payment:
    def pay (self , amount):
        pass

# Children class
class Cash(Payment):
    def pay (self , amount):
        print(f"₹{amount} paid using cash")
    
# Children class
class Card(Payment):
    def pay (self , amount):
        print(f"₹{amount} paid using card, processing bank transaction")
        
# Children class
class UPI(Payment):
    def pay (self , amount):
        print(f"₹{amount} paid using UPI, verifying PIN")


# Polymorphism demonstration
payments = [Cash(), Card(), UPI()]  
for p in payments:
    p.pay(500)


# Polymorphism MEANS Same method name, different behavior