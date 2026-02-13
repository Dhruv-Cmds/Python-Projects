# AUTHOR
# Dhruv

# Bank Management System
accounts = []

while True:

    print("\n---CHOSE ANY ONE OPTION---")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Exit")

    userchoice = input("Plese select your option to proced :")

    if userchoice == "1":
        name = input("Enter your name :")
        balance = int(input("Enter starting balance: "))

        print(f"You sucsuccessfully created account. Your account name is {name}")

        new_account = [name , balance]
        accounts.append(new_account)
    
    elif userchoice == "2":

        if not accounts:
            print("Account not found")

        else:
            name = input("Enter your name :")
            # da = deposit amount
            da = int(input("Enter an amount to Deposit :"))

            found = False

            for account in accounts:
                
                if account[0] == name:
                    account[1] = account[1] + da
                    print(f"Your amount '{da}' deposit sucsuccessfully..")
                    print(f"New balance is {account[1]}")
                    found = True
                    break

            if not found:
                print("Account not found.")

    elif userchoice == "3":

        if not accounts:
            print("Account not found")

        else:
            name = input("Enter your name :")
            # wa = wihtdraw amount
            wa = int(input("Enter withdraw amount :"))

            found = False
            
            for account in accounts:

                if account[0] == name :

                    if account[1] >= wa:
                        account[1] = account[1] - wa 
                        print (f"{wa} withdraw sucsuccessfully..")
                        print (f"Remaining Balance is {account[1]}")

                    else:
                        print ("Not enough Balance in your accoun.")
                    found = True
                    break

            if not found:
                print("Account not found.")

    elif userchoice == "4":

        if not accounts:
            print("No account found.")

        else:
            name = input("Enter account name: ")

            found = False

            for account in accounts:

                if account[0] == name:
                    print(f"Current balance: {account[1]}")
                    found = True
                    break  

                if not found:
                    print("Account not found.")

    elif userchoice == "5":
        print("Thank you for using our bank system 😊")
        print("Good bye...")
        break

    else:
        print("Invalid choice")
           