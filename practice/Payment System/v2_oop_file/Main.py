class Payment:

    filepath = "pay.txt"
    def __init__(self , amount):
        self.amount = amount
        self.load()

    def pay(self):
        pass

    def load(self):
        try:
            with open(self.filepath, "r") as f:
                f.read()
        except FileNotFoundError:
            open(self.filepath , "w").close()

    def save(self):
        with open (self.filepath , "a") as f:
            f.write(f"{self.amount}\n") 

class Cash(Payment):
    def pay(self):
        print (f"{self.amount}, Amount paid using cash.")
        self.save()

class Card(Payment):
    def pay(self):
        print(f"{self.amount}, Amount paid using card.")
        self.save()

class Upi(Payment):
    def pay(self):
        print(f"{self.amount}, Amount paid using upi.")
        self.save()

Payments = [Cash(500), Card(600), Upi(700)] 

for p in Payments:
    p.pay()