# Stores a fixed password.
# Allows the user 3 attempts to enter the correct password.
# If the user enters the correct password:
# Print "login" and stop the program.
# the user fails all 3 attempts:
# Print "account blocked".

password = "Ayushi"

for i in range(3):
    user = input("enter password :")
    # if (user == password.lower()):
    if (user == password.capitalize()):   
        print("login")
        break

else:
        print("account blocked :")

                                        #  secound method

def password (n):
    password = "Ayushi"
    for i in range (n):
        n = input("Enter a password :")
        if (n.capitalize() == password):
            print("Login")
            break
        else:
            print("Try Again... :")

    print("Account Blocked")
password(3)