# Takes two numbers from the user and compares them:
# Prints "Same Numbers" if both are equal.
# Prints which number is bigger if they are different.
# Takes a string from the user.
# Checks whether the string exists in a predefined list of names.
# Displays whether the string is found in the list or not.

user1 = int(input("Enter the value : "))
user2 = int(input("Enter the value : "))
user3 = input("Enter the str :")

if (user1 == user2):
    print("Same Numbers")

elif (user1 > user2):
    print ("user1 is bigger than user2 :")

else :
    print("user2 is bigger than user1")

l = ["Dhruv" , "Ayushi"]

if (user3.capitalize() in l):
    print ("string inside the lsit")

# if (user3.lower() in l):
#     print ("string inside the lsit")

else:
    print("stringe not inside the list")

                                                # secound method


def compare ():

    if (num1 == num2):
        print("Both are Same Numbers. ")

    elif (num1 > num2):
        print("Bigger number is num 1 :")

    else:
        print("Bigger number is num 2 :")

    if name.capitalize() in l:
        print("Entered name in list :")

    else:
        print("Entered name is not in lsit. ")

num1 = int(input("Enter an number 1 :"))
num2 = int(input("Enter an number 2 :"))
name = input("Enter a name as string :")

l = ["Dhruv" , "Ayushi"]

compare ()