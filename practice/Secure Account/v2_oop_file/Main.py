# import json

from db import get_connection

class accountsecure:

    # def __init__(self , acc_no , pin , balance , filepath = "practice/Secure Account/v2_oop_file/account.json"): #filepath = "account.txt"
    #     self.acc_no = acc_no
    #     self.pin = pin
    #     self.balance = balance
    #     self.filepath = filepath
    #     self.load()

    #  .txt formate
    # def load(self):
    #     try:
    #         with open(self.filepath, "r") as f:
    #             data = f.read().strip()
    #             if data:
    #                 acc_no, pin, balance = data.split()
    #                 self.acc_no = int(acc_no)
    #                 self.pin = str(pin)
    #                 self.balance = int(balance)

    #     except FileNotFoundError:
    #         self.save()

    # def save(self):
    #     with open (self.filepath , "w") as f:
    #         f.write(f"{self.acc_no} {self.pin} {self.balance}\n")

    # .json
    # def load (self):
        
    #     try:
    #         with open (self.filepath , "r") as f:
    #             data = json.load(f)

    #             if data: 
    #                 self.name = data.get("acc_no" , self.acc_no)
    #                 self.acc_no = data.get("pin" , self.pin)
    #                 self.balance = data.get("balance" , self.balance)
                
    #             else:
    #                 self.save()
        
    #     except FileNotFoundError:
    #         self.save()

    # def save (self):
    #     with open (self.filepath , "w") as f:
    #         json.dump({"acc_no": self.acc_no ,"pin": self.pin  , "balance" : self.balance}, f , indent=4)

    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
    
    def add_user(self):
        sql = "INSERT INTO accounts (acc_no, pin, balance) VALUES (%s, %s, %s)"
        values = (1234, '0000', 15000)
        # values = (4321, '0000', 153000)
        self.cursor.execute(sql, values)
        self.conn.commit()

    def deposit(self):

        while True:
            try:
                amount = int(input("Enter an amount for deposit :"))
                acc_no = int(input("Enter acc_no: "))
                
            except ValueError:
                    print("Invalid Amount!")
                    continue
            
            if amount <= 0:
                print ("Amount must be greater than zero!")
                return
            
            # self.balance += amount
            # self.save()

            sql = "UPDATE accounts SET balance = balance + %s WHERE acc_no = %s "
            values = (amount, acc_no)
            self.cursor.execute(sql, values)
            self.conn.commit()

            break

        print("Amount deposited successfully in your account.")
    
    def withdraw(self):

        while True:

            try:
                acc_no = int(input("Enter account number: "))

            except ValueError:
                print("Invalid Account number.")

                continue

            userpin = input("Enter your pin: ").strip()


            # if userpin != self.pin:
            #     print("Invalid pin.")
            #     continue

            sql = "SELECT pin, balance FROM accounts WHERE acc_no= %s"
            values = (acc_no,)

            self.cursor.execute(sql, values)

            result = self.cursor.fetchone()

            if not result:

                print("Account not found.")
                break

            pin , balance = result

            if userpin != pin:
                print("Invalid PIN.")
                continue

            try:
                amount = int(input("Enter an amount for withdrawn :"))

            except ValueError:
                print("Invalid Amount type")

                continue
            
            if amount <= 0:
                print("Amount must be greater than zero!")
                continue

            # if amount > self.balance:
            #     print ("Ininsufficient balance!")
            #     continue
            
            # self.balance = self.balance - amount
            # self.save()

            if balance < amount:
                print("Insufficient fund.")
                break
            
            else:
                
                sql = "UPDATE accounts SET balance = balance - %s WHERE acc_no = %s"
                values = (amount, acc_no)

                self.cursor.execute(sql , values)
                self.conn.commit()

                print ("Amount wihtdrawn successfully.")

            break

        # print ("Amount wihtdrawn successfully form your account.")

    def get_balance (self):

        while True:

            try:
                acc_no = int(input("Enter account number: "))

            except ValueError:
                print("Invalid Account number.")

                continue

            userpin = input("Enter your pin :").strip()

            # if userpin != self.pin :
            #     print("Invalid pin!")
            #     continue

            sql = "SELECT pin, balance FROM accounts WHERE acc_no = %s"
            values = (acc_no,)
            
            self.cursor.execute(sql, values)
            data = self.cursor.fetchone()

            if data:
                pin , balance = data

                if userpin == pin:
                    print(f"Available Balance: {balance}")
                    break

                else:
                    print("Invalid PIN!")
                    continue

            else:
                print("Account not found.")

                break 
            
        # print(f"You have total {self.balance} amount in your account.")
    
    def show_account_info(self):

        # print("Account No:", self.acc_no)

        sql = "SELECT acc_no FROM accounts"
        self.cursor.execute(sql)

        results = self.cursor.fetchall()

        if results:
             for i, row in enumerate (results , 1):     
                print(f"{i}. Account No:", row[0])
        
        else:
            print("Account not found")
    
    def menu(self):

        while True:
            print("---------------")
            print("1. Show Account info")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            print("---------------")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice type.")
                continue

            if choice == 1:
                self.show_account_info()
            
            elif choice == 2:
                self.deposit()
            
            elif choice ==3:
                self.withdraw()

            elif choice == 4:
                self.get_balance()
            
            elif choice == 5:
                print("Thank you for using us! Have a nice day.")
                break
            else:
                print("Choice outof range.")

# a = accountsecure (1234 , "0000" , 15000)
# a.menu()

a = accountsecure()

# no copy user can go in database uncomment when you need to add new users
# a.add_user()
a.menu()