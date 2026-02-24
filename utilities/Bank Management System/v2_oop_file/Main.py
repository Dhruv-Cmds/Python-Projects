class Bank:

    def __init__(self , filepath = "bank.txt"):
        self.accounts = []
        self.filepath = filepath
        self.load()
    
    def menu(self):

        while True:

            print("--------------------")
            print("1. Create account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check balance")
            print("5. Exit")
            print("--------------------")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice type.")
                continue

            if choice == 1:
                self.create_account()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                self.check_balance()
            elif choice == 5:
                print("Thank you for using us! Have a nice day.")
                break
            else:
                print("Invalid choice.")

    def save(self):
        with open (self.filepath , "w") as f:
            for name , balance in self.accounts:
                f.write(f"{name} , {balance}\n")
    
    def load(self):
        self.accounts = []
        try:
            with open(self.filepath, "r") as f:
                for line in f:
                    name, balance = line.split(",")
                    name = name.strip().lower()
                    balance = int(balance.strip())
                    self.accounts.append([name, balance])
        except FileNotFoundError:
            pass
    def create_account(self):
        while True:
            try:
                acc_name = input("Enter your name: ").strip().lower()
                st_balance = int(input("Enter starting amount: "))
            except ValueError:
                print("Invalid input.")
                continue
            if(st_balance <= 0):
                print("Amount must be grater than 0.")
            break

        new_acc = [acc_name, st_balance]
        self.accounts.append(new_acc)

        print(f"Your account created successfully. Your name is: {acc_name}")

        self.save()
    
    def deposit(self):

        if not self.accounts:
            print("No Account Created.")
            return

        while True:
            try:
                name = input("Enter your name: ").strip().lower()
                amount = int(input("Enter deposit amount: "))
            except ValueError:
                print("Invalid amount type.")
                continue
            break

        found = False

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        for account in self.accounts:
            if account[0] == name:
                account[1] += amount
                print(f"Your amount '{amount}' deposited successfully.")
                print(f"New balance: {account[1]}")
                found = True
                self.save()
                break

        if not found:
            print("Account not found.")

            
    def withdraw(self):

        if not self.accounts:
            print("No Account Created.")
            return

        while True:
            try:
                name = input("Enter your name: ").strip().lower()
                amount = int(input("Enter withdrawn amount: "))
            except ValueError:
                print("Invalid amount type.")
                continue
            break

        found = False 
                    
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        for account in self.accounts:
            if account[0] == name:
                if amount > account[1]:
                    print("Insufficient funds.")
                    return

                account[1] -= amount
                print(f"{amount} withdrawn successfully.")
                print(f"Remaining balance is {account[1]}")
                found = True
                self.save()
                break

        if not found:
            print("Account not found.")

        
    def check_balance(self):
         
        if not self.accounts:
            print("No Account Created.")
            return

        name = input("Enter your name: ").strip().lower()
        found = False

        for account in self.accounts:
            if account[0] == name:
                print(f"Current balance: {account[1]}")
                found = True
                break  

        if not found:
            print("Account not found.")


b = Bank()
b.menu()