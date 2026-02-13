# Takes 5 numbers from the user (using a loop) and stores them in a list.
# Using another loop:
# find the largest number
# find the smallest numbe
# Print:
# Largest number = X
# Smallest number = Y

l = []
for i in range (5):
    user_number = (int(input("Enter a number:" )))
    l.append(user_number)
        
largest_number = l [0]
smallest_number = l [0]

for i in l:
    if (i > largest_number):
        largest_number = i

    elif(i > largest_number):
        smallest_number = i

print("largest numbers is :" , largest_number)
print("smallest numbers is :" , smallest_number)

#  YOU CAN COMPARE ANYTHING DIRECT NEED TO CONVER IT LIKE FOR LIST NEED TO CONER NUMBER INTO LIST


                                            # SECOUND METHOD

def store (n):

        # THIS LOOP THAT USED TO ADD N NUMBER IN LIST WHICH GIVEN BY USER

    Total_numers = []

    for i in range (n):
        user_number = int(input("Enter a number for list :"))
        Total_numers.append(user_number)

    print("\nTotal Numbers in 'List' are :")
    print(Total_numers)

        # THIS LOOP TO FID THE ONLY ONE LARGEST AND SMALLEST NUMBER FROM ENTERED BY USER

    # Total_numers [5 , 6 , 7 , 8 , 9] FOR UNDERSTANDING TOTAL[O] HAI MEAND VO INDEX O PE NUMBER H USSE ST KAREGA
    largest_number = Total_numers [0]
    smallest_number = Total_numers [0]

    for i in Total_numers:

        if (i > largest_number):
            largest_number = i

        if (i < smallest_number):
            smallest_number = i

        #  PRINT THAT HELPS TO PRINT WHOLE PROGRAM
            
    print("\n'LARGEST' and 'SMALLEST' numbers :")
    print("LARGEST NUMBER IS :" , largest_number)
    print("SMALLEST NUMBER IS :" , smallest_number)

n = int(input("Enter a number :"))
store(n)