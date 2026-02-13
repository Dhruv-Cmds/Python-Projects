# Stores a fixed password.
# Gives the user 3 attempts to enter the correct password.
# If the password is correct:
# Return or display "Welcome" and stop.
# If the password is wrong:
# Print "wrong password" and continue.
# If all 3 attempts fail, the program ends.

def login_system():
    password = "python123"

    for i in range(3):
        user = input("Enter password :")

        if (user == password):
            return "Welcome"
        
        else:
            print("wrong password")
            
login_system()

                        #  SECOUND METHOD

def password ():
    password = "admin123"
    total_attemps = 3

    for i in range (3):

        user_password = input("Enter a password :")

        if (password == user_password):
            return "WELCOME"
        
        elif (password != user_password):
            total_attemps -= 1
            print(f"TOTAL remaing ATTEMPS : {total_attemps}")
        
        if (password != user_password and total_attemps == 0):
            print("WRONG PASSWORD")

password()