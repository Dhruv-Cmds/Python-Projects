# AUTHOR
# Dhruv

# SECURE ACCOUNT

class accountsecure:
    
    def __init__(self , acc_no , pin , balance):
        
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance
    
    def deposit (self):

        try:
            amount = int(input("Enter an amount for deposit :"))
             
        except ValueError:
                print("Invalid Amount!")
                return
        
        if amount <= 0:
            return("Amount must be greater than zero!")
        
        self.balance += amount

        print("Amount deposited successfully in your account.")
    
    def withdraw (self):

        userpin = input("Enter your pin :").strip()

        if userpin != self.pin :
            return "Invalid pin!"
        
        try:
            amount = int(input("Enter an amount for withdrawn :"))

        except ValueError:
            print("Amount must be greater than zero!")
            return
        
        if amount <= 0:
            print("Amount must be greater than zero!")
            return
        
        if amount > self.balance:
            return "Ininsufficient balance!"
        
        self.balance = self.balance - amount

        print ("Amount wihtdrawn successfully form your account.")
    
    def get_balance (self):

        userpin = input("Enter your pin :").strip()

        if userpin != self.pin :
            return "Invalid pin!"
        
        print(f"You have total {self.balance} amount in your account.")
    
    def show_account_info(self):
        print("Account No:", self.acc_no)

a = accountsecure (1234 , "0000" , 15000)

a.show_account_info()
a.deposit()
a.withdraw()
a.get_balance() 