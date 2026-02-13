# Stores a list of numbers.
# Iterates through the list.
# Prints numbers that are greater than or equal to 10 and counts them.
# Prints numbers that are less than or equal to 10 and counts them.
# Displays the total count of both categories.

l = [5, 12, 7, 18, 3, 25, 10]
greater = 0
less = 0
for i in l:
    if (i >= 10):
        print("greter numbers is :" , i)
        greater += 1

    elif (i <= 10):
        print("less numers is " , i)
        less  += 1

print (":",greater)
print(":",less)

                                #  secound method

def greater_less (l):

    Greater_numbers_count = 0

    less_numbers_count = 0

    Greater_numbers = []
    
    less_numbers = []

    for i in l:

        if (i > 10):
            
            Greater_numbers.append(i)

            Greater_numbers_count += 1

        elif (i < 10):

            less_numbers.append(i)

            less_numbers_count += 1

        print("Greater numbers then 10 are :" , i )
        print("less numbers then 10 are :" , i)

    print("\nNUMBER THAT LESS OR GREATER THEN 10 :")

    print(f"Greater numbers then 10 are : {i}") 

    print(f"less numbers then 10 are : {i}")

    print("\nCOUNTER :")

    print("Total Greater counter is :" , Greater_numbers_count)

    print("Total less counter is :" , less_numbers_count)

    print("\nGREATER AND LESS NUMBERS LIST :")

    print(f"Greater,{Greater_numbers}")

    print(f"Less,{less_numbers}")

l = [5, 12, 7, 18, 3, 25, 10]

greater_less(l)