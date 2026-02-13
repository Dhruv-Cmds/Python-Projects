# Takes a number n from the user.
# Iterates from 1 to n.
# Prints the numbers that are divisible by 3 or 5.
# Displays which number is divisible by 3 or by 5.

n = int(input("Enter a number :"))

for i in range (1 , n + 1):

    if (i % 3 == 0 and  i % 5 == 0):
        print("Numbers that devided by 3 and 5 are :" , i)
        
    elif (i%3 == 0):
        print("number is divided ny 3 :" , i)

    elif (i%5 == 0):
        print("number is divided ny 5 :" , i)
    
                                                     # secound method

def numbers(n):

    divisiable_by_three = []
    divisiable_by_five = []
    divisiable_by_three_and_five = [] 

    for i in range (1 , n + 1):

        if (i % 3 == 0 and  i % 5 == 0):
            print("Numbers that devided by  5 are :" , i)
            divisiable_by_three_and_five.append(i)

        elif (i % 3 == 0):
            print("Numbers that devided by  3 are :" , i)
            divisiable_by_three.append(i)

        elif (i % 5 == 0):
            print("Numbers that devided by 3 and 5 are :" , i)
            divisiable_by_five.append(i)

    print("\nSummary :")
    print("Devisiable by both :" , divisiable_by_five)
    print("Devisiable by 3 :" , divisiable_by_three)
    print("Devisiable by 5 :" , divisiable_by_three_and_five)

n = int(input("Enter a number :"))
numbers(n)