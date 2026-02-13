# Stores a fixed password/string ("hello world").
# Repeatedly asks the user to enter a string.
# Compares the input with the stored string (case-insensitive).
# If it matches:
# Print "matched" and stop the program.
# If it does not match:
# Print "Try again" and continue asking.

a = "hello world"

for i in range (10000000000):
    n = input("Enter a name :")

    if (n.lower() == a):
        print("matched " , n)


        break
    else:
        print("Try again")

                        #  SECOUND METHOD

def password (user):
    # password = "hello world"

    for i in range (10000000000000):

        user = input("Enter STRING as a password :")

        if user.lower() == "hello world":
            print("matched")

            return
        
        else:
           print( "Try again")
           
password("hello world")