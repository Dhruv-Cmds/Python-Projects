import json

class Bankaccount:

    def __init__(self , name , acc_no , balance ,  filepath = "practice/Bank Account System/v2_oop_file/bank.json" ): # filepath = "bank.txt"):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        self.filepath = filepath
        self.load()

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
    def save(self):
        with open (self.filepath , "w") as f:
            json.dump({"name": self.name, "acc_no": self.acc_no, "balance": self.balance }, f , indent=4)
    
    def load (self):
        
        try:
            with open (self.filepath , "r") as f:
                data = json.load(f)

                if data: 
                    self.name = data.get("name" , self.name)
                    self.acc_no = data.get("acc_no" , self.acc_no)
                    self.balance = data.get("balance" , self.balance)
                
                else:
                    self.save()
        
        except FileNotFoundError:
            self.save()

    def deposit(self):

        name = input("Enter your name: ").capitalize().strip()

        if name.isalpha() and name == self.name:
            while True:
                try:
                    amount = int(input("Enter amount for deposit: "))
                    if amount <= 0:
                        print("Amount must be greater than 0.")
                        continue
                    self.balance += amount
                    self.save()
                    print("Amount added successful.")
                    print(f"Current Balance: {self.balance}")
                    break
                except ValueError:
                    print("Invalid amount type.")
        else:
            print("Invalid name.")

    def withdraw (self):

        name = input("Enter your name: ").capitalize().strip()

        if name.isalpha() and name == self.name:
            while True:
                try:
                    amount = int(input("Enter withdraw amount: "))
                    if amount <= 0:
                        print("Amount must be greater than 0.")
                        continue
                    if amount > self.balance:
                        print("Insufficient funds.")
                        continue
                    self.balance -= amount
                    self.save()
                    print("Your money withdrawn successfully from your account")
                    print(f"Current Balance: {self.balance}")
                    break
                except ValueError:
                    print ("Invalid amount type.")
        else:
            print("Invalid name")
           
    def show_balance(self):
            
            try:
                acc_no = int(input("Enter your account number: "))
                if acc_no == self.acc_no:
                    print("-------ACCOUNT DETAILS-------")
                    print(f"Name: {self.name}")
                    print(f"Balance: {self.balance}")        
                else:
                    print("Enter correct account number.")
            except:
                print("Invalid account number type.")
        
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
            

b = Bankaccount("Alice", 101, 1000)
b.session_menu()        