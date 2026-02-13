# Takes a username as input.
# Checks if the length of the username is greater than 5 characters.
# Returns "valid" if it is, otherwise returns "Invalid".
# Prints the result.

def validate_username(name):
    if (len(name) > 5):
        return "valid"
    
    else :
        return "Invalid"
    
name = input("Enter name :")
print(validate_username(name))

                            #  SAME BUT WITH LIST

def check_username ():

    for i in l:
        if (5 < len(l)):
            return "Valid"
        
        else:
            return "Invalid"

l = ["Dhruv" , "Ayushi" , "Meet" , "Kashyap" , "Dhruvam" , "Jaypdip"]
# username = input("Enter a username :")
print(check_username())