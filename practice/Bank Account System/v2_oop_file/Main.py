# import json

from db import get_connection

class Bankaccount:

    # def __init__(self , name , acc_no , balance ,  filepath = "practice/Bank Account System/v2_oop_file/bank.json" ): # filepath = "bank.txt"):
    #     self.name = name
    #     self.acc_no = acc_no
    #     self.balance = balance
    #     self.filepath = filepath
    #     self.load()

    # .txt use
    # def save (self):
    #     with open (self.filepath , "w") as f:
    #             f.write(f"{self.name} {self.acc_no} {self.balance}\n")

    # def load(self):

    #     try:
    #         with open(self.filepath, "r") as f:
    #             data = f.read().strip()
    #             if data:
    #                 name, acc_no, balance = data.split()
    #                 self.name = name
    #                 self.acc_no = int(acc_no)
    #                 self.balance = int(balance)

    #     except FileNotFoundError:
    #         self.save()
    
    #  .json use
    # def save(self):
    #     with open (self.filepath , "w") as f:
    #         json.dump({"name": self.name, "acc_no": self.acc_no, "balance": self.balance }, f , indent=4)
    
    # def load (self):
        
    #     try:
    #         with open (self.filepath , "r") as f:
    #             data = json.load(f)

    #             if data: 
    #                 self.name = data.get("name" , self.name)
    #                 self.acc_no = data.get("acc_no" , self.acc_no)
    #                 self.balance = data.get("balance" , self.balance)
                
    #             else:
    #                 self.save()
        
    #     except FileNotFoundError:
    #         self.save()

    def __init__(self):
        
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def add_user(self):

        sql = "INSERT INTO accounts (name, acc_no, balance) VALUES (%s, %s, %s)"
        values = ("Alice", 101, 10000)

        self.cursor.execute(sql, values)
        self.conn.commit()

    def deposit(self):

        while True:

            name = input("Enter your name: ").strip().capitalize()

            try:
                amount = int(input("Enter amount for deposit: "))

            except ValueError:
                print("Invalid amount type.")

                continue

            sql = "SELECT balance FROM accounts WHERE name = %s"
            values = (name,)
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()

            if not result:
                print("Invalid account name.")
                return

            sql = "UPDATE accounts SET balance = balance + %s WHERE name = %s"
            values = (amount, name)
            self.cursor.execute(sql, values)
            self.conn.commit()

            # to get updated balance

            sql = "SELECT balance FROM accounts WHERE name = %s"
            values = (name,)
            self.cursor.execute(sql, values)
            data = self.cursor.fetchone()

            if data:
                updated_balance = data[0]

                print("Amount added successful.")
                print(f"Current Balance: {updated_balance}")

            else:
                print("No data found.")      
                
            break 

    def withdraw (self):

        while True:

            name = input("Enter your name: ").strip().capitalize()

            try:
                amount = int(input("Enter amount for withdrawn: "))

            except ValueError:
                print("Invalid amount type.")

                continue

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            sql = "SELECT balance FROM accounts WHERE name = %s"
            values = (name,)
            self.cursor.execute(sql , values)
            result = self.cursor.fetchone()
            
            if not result:
                print("Invalid account name.")
                return

            current_balance = result[0]

            if amount > current_balance:
                print("Insufficient funds.")
                return
            
            sql = "UPDATE accounts SET balance = balance - %s WHERE name = %s"
            values = (amount, name)
            self.cursor.execute(sql, values)
            self.conn.commit()


            # to get updated balance

            sql = "SELECT balance FROM accounts WHERE name = %s"
            values = (name,)
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()

            if result:
                updated_balance = result[0]

                print("Your money withdrawn successfully from your account")

                print(f"Current Balance: {updated_balance}")
            
            else:
                print("No data found.")

            break

    def show_balance(self):

        while True:

            try:
                acc_no = int(input("Enter your account number: "))

            except ValueError:
                print("Invalid Account number.")

            sql = "SELECT balance FROM accounts WHERE acc_no = %s"
            values = (acc_no,)
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()

            if not result:
                print("No Account found.")
                return
            
            balance = result[0]

            print(f"Available Balance: {balance}")

            break

    # def deposit(self):

    #     name = input("Enter your name: ").capitalize().strip()

    #     if name.isalpha() and name == self.name:

    #         while True:

    #             try:
    #                 amount = int(input("Enter amount for deposit: "))

    #                 if amount <= 0:
    #                     print("Amount must be greater than 0.")
    #                     continue

    #                 self.balance += amount

    #                 self.save()

    #                 print("Amount added successful.")

    #                 print(f"Current Balance: {self.balance}")

    #                 break

    #             except ValueError:
    #                 print("Invalid amount type.")
    #     else:
    #         print("Invalid name.")

    # def withdraw (self):

    #     name = input("Enter your name: ").capitalize().strip()

    #     if name.isalpha() and name == self.name:

    #         while True:

    #             try:
    #                 amount = int(input("Enter withdraw amount: "))

    #                 if amount <= 0:
    #                     print("Amount must be greater than 0.")
    #                     continue

    #                 if amount > self.balance:
    #                     print("Insufficient funds.")
    #                     continue

    #                 self.balance -= amount

    #                 self.save()

    #                 print("Your money withdrawn successfully from your account")

    #                 print(f"Current Balance: {self.balance}")

    #                 break

    #             except ValueError:
    #                 print ("Invalid amount type.")
    #                 continue
    #     else:
    #         print("Invalid name")
           
    # def show_balance(self):
            
    #         try:
    #             acc_no = int(input("Enter your account number: "))

    #             if acc_no == self.acc_no:

    #                 print("-------ACCOUNT DETAILS-------")
    #                 print(f"Name: {self.name}")
    #                 print(f"Balance: {self.balance}") 

    #             else:
    #                 print("Enter correct account number.")

    #         except:
    #             print("Invalid account number type.")
        
    def session_menu (self):

        while True:

            print("\n-------SESSION MENU-------")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Balance")
            print("4. Logout")
        
            try:
                choice = int(input("Chose any one option (1-4): "))

            except ValueError:
                print("Invalid type.")

                continue

            if choice == 1:
                self.deposit()

            elif choice == 2:
                self.withdraw()

            elif choice == 3:
                self.show_balance()

            elif choice == 4:
                print("Thank you for using us! Have a nice day.")
                break
            
            else:
                print("Invalid choice")
            
#  use when you work with .json or .txt
# b = Bankaccount("Alice", 101, 1000)
# b.session_menu() 

# use when you work with DATABASE
b = Bankaccount()
# b.add_user()
b.session_menu() 