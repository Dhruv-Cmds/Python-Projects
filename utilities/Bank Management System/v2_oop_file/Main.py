# import json
import mysql.connector 

class Bank:

    #  use this when you use .json or .txt

    # def __init__(self , filepath = "utilities/Bank Management System/v2_oop_file/bank.json"): #"bank.txt"
    #     self.accounts = []
    #     self.filepath = filepath
    #     self.load()


    # DATA store in MySql databasae
    def __init__(self):

        # create connection
        self.conn = mysql.connector.connect (
            host = "localhost",
            user = "root",
            password = "YOUR_PASSWORD_HERE",
            database = "BankManagementSystem"
        )
        
        self.cursor = self.conn.cursor()
    
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

# --------------------------------------------------------------------------------------------------------------------

    '''Data save in .txt file'''
    # def save(self):
    #     with open (self.filepath , "w") as f:
    #         for name , balance in self.accounts:
    #             f.write(f"{name} , {balance}\n")
    
    # def load(self):
    #     self.accounts = []
    #     try:
    #         with open(self.filepath, "r") as f:
    #             for line in f:
    #                 name, balance = line.split(",")
    #                 name = name.strip().lower()
    #                 balance = int(balance.strip())
    #                 self.accounts.append([name, balance])
    #     except FileNotFoundError:
    #         pass

# --------------------------------------------------------------------------------------------------------------------

    # '''Data save in .json file'''

    # def save(self):
        
    #     with open (self.filepath , "w") as f:
    #         json.dump(self.accounts , f , indent=4)

    # def load(self):

    #     try:
    #         with open (self.filepath , "r") as f:
    #             self.accounts = json.load(f)

    #     except FileNotFoundError:
    #         self.accounts = []

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
                continue
            
            break

        # new_acc = {"name" : acc_name, "balance" : st_balance}
        # self.accounts.append(new_acc)

        # FOR MySql data base
        sql = "INSERT INTO accounts (name, balance) VALUES (%s, %s)"
        values = (acc_name , st_balance)

        self.cursor.execute(sql, values)
        self.conn.commit()

        print(f"Your account created successfully. Your name is: {acc_name}")

        # self.save()
    
    def deposit(self):

        # if not self.accounts:
        #     print("No Account Created.")
        #     return

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

        # for account in self.accounts:
        #     if account["name"] == name:
        #         account["balance"] += amount

        #         print(f"Your amount '{amount}' deposited successfully.")
        #         print(f"New balance: {account["balance"]}")

        #         found = True
        #         self.save()
        #         break

        # if not found:
        #     print("Account not found.")

        sql = "UPDATE accounts SET balance = balance + %s WHERE name = %s"
        values = (amount, name)

        self.cursor.execute(sql, values)
        self.conn.commit()


        if self.cursor.rowcount == 0:
            print("Account not found.")
        else:
            print("Deposit successful.")


            
    def withdraw(self):

        # if not self.accounts:
        #     print("No Account Created.")
        #     return

        while True:

            try:
                name = input("Enter your name: ").strip().lower()
                amount = int(input("Enter withdrawn amount: "))

            except ValueError:
                print("Invalid amount type.")
                continue

            break

        # found = False 
                    
        # if amount <= 0:
        #     print("Amount must be greater than 0.")
        #     return

        # for account in self.accounts:
            
        #     if account["name"] == name:

        #         if amount > account["balance"]:
        #             print("Insufficient funds.")
        #             return

        #         account["balance"] -= amount

        #         print(f"{amount} withdrawn successfully.")
        #         print(f"Remaining balance is {account["balance"]}")

        #         found = True

        #         self.save()

        #         break

        # if not found:
        #     print("Account not found.")


        # check balance first
        sql = "SELECT balance FROM accounts WHERE name = %s"
        self.cursor.execute(sql, (name,))
        result = self.cursor.fetchone()

        if not result:
            print("Account not found.")
            return

        balance = result[0]

        if amount > balance:
            print("Insufficient funds.")
            return

        # update
        sql = "UPDATE accounts SET balance = balance - %s WHERE name = %s"
        self.cursor.execute(sql, (amount, name))
        self.conn.commit()

        print("Withdrawal successful.")

        
    def check_balance(self):
         
        # if not self.accounts:
        #     print("No Account Created.")
        #     return

        name = input("Enter your name: ").strip().lower()
        found = False

        # for account in self.accounts:
        #     if account["name"] == name:
        #         print(f"Current balance: {account["balance"]}")
        #         found = True
        #         break  

        # if not found:
        #     print("Account not found.")

        sql = "SELECT balance FROM accounts WHERE name = %s"
        self.cursor.execute(sql, (name,))
        result = self.cursor.fetchone()

        if result:
            print(f"Current balance: {result[0]}")

        else:
            print("Account not found.")


b = Bank()
b.menu()