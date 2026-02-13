# AUTHOR 
# DHRUV

# Bank Account System

class BankAccount:

    def __init__(self ,acc_no , name , balance):

        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        

    def deposit (self):
        
        amount = input("Enter amount to deposit: ").strip()

        if not amount.isdigit():
            print("Invalid amount type")
            return
        
        amount = int(amount)

        if amount <= 0:
            return "Invalid amount"

        self.balance += amount

        print ("Your money deposited successfully into your account.")
        return amount

    def withdraw (self):

        amount = input("Enter amount to withdraw: ").strip()

        if not amount.isdigit():
            print("Invalid amount type")
            return

        amount = int(amount)

        if amount <= 0:
            print("Invalid amount")
            return

        if amount > self.balance:
            print("Insufficient balance")
            return

        self.balance -= amount

        print ("Your money withdrawn successfully from your account.")
        return amount
    
    def show_balance(self):
     
        print("Account No:", self.acc_no) 
        print("Name:", self.name) 
        print("Balance:", self.balance)
    
    def Season_menu (self):

        while True:

            print("\n---SESSION MENU ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Balance")
            print("4. Logout")

            userchoice = input("Choce any one option.")

            if userchoice == "1":
                self.deposit()

            elif userchoice == "2":
                self.withdraw()

            elif userchoice == "3":
                self.show_balance()

            elif userchoice == "4":
                print("Log out")
                break
            else:
                print("Invalid option.")

acc1 = BankAccount(101, "Alice", 1000)
acc2 = BankAccount(102, "Bob", 500)
acc3 = BankAccount(103, "Charlie", 2000)

accounts = [acc1, acc2, acc3]

for acc in accounts:
    print("----- New Account Session -----")
    acc.Season_menu()