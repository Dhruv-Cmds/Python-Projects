# Takes a username as input from the user.
# Checks if the username contains double spaces.
# If yes, display "Invalid username".
# Checks if the username length is less than 10 characters.
# If yes, display "Username valid".
# Otherwise, display a message indicating the space issue is not fixed.

username = input("Enter the username :")

if ("  " in username):
    print ("Invalid username")

elif (len(username) < 10):
    print ("Username valid")

else:
    print("space not fixed")

                                # secound method

def check ():
    if ("  " in user_name):
        print("Username in valid. ")

    else:
        print("username valid.")

user_name = input("Enter an username :")
check ()
    