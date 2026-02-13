# Takes a number n from the user
# Using a loop from 1 to n, do the following:
# For each number:
# # If number is divisible by 2 and 3 both → store in a list called special_numbers
# If number is divisible by only 2 → store in even_only
# If number is divisible by only 3 → store in three_only
# Else → store in others
# At the end print:
# Special numbers: [...]
# Even only numbers: [...]
# Three only numbers: [...]
# Other numbers: [...]
# Count Even and Three and Others Numbers 

# Name of the list 

even_only = []
three_only = []
special_numbers = []
store_in_others = []

# Counter starts at 0

even_only_count = 0
three_only_count = 0
special_numbers_count = 0
store_in_others_count = 0

# Counter Taking ends here

#  Input that taken from user

n = int(input("Enter a number :"))

# Input taking ends here

# Loop starts from here :

for i in range (1 , n + 1):
 
#  IF elif and else conditions :

 if (i % 2 == 0 and i % 3 == 0):
  special_numbers.append(i)
  special_numbers_count += 1

 elif (i % 2 == 0):
  even_only.append(i)
  even_only_count += 1

 elif (i % 3 == 0):
  three_only.append(i)
  three_only_count += 1

 else:
  store_in_others.append(i)
  store_in_others_count += 1
#   if else and loop both are ends here

# Total number are stored in list 

print("Special numbers ",special_numbers)
print("Even only numbers ", even_only)
print("Three only numbers ", three_only)
print("store in others ", store_in_others)

# Store in list ends here

# Total Number count

print("Special numbers ",special_numbers_count)
print("Even only numbers ", even_only_count)
print("Three only numbers ", three_only_count)
print("store in others ", store_in_others_count)

# Total Number count ends here


                                #  SECOUND METHOD

def divisible (n):

    special_numbers = []
    even_only = []
    three_only = []
    store_in_others = []

    even_only_count = 0
    three_only_count = 0
    special_numbers_count = 0
    store_in_others_count = 0

    for i in range (1 , n + 1):
        if (i % 2 == 0 and i % 3 == 0):
            special_numbers.append(i)

            special_numbers_count += 1

        elif (i % 2 == 0):
            even_only.append(i)

            even_only_count += 1

        elif (i % 3 == 0):
            three_only.append(i)

            three_only_count += 1

        else:

            store_in_others.append(i)

            store_in_others_count += 1

    print("\nLISTS :")
    print("Special numbers ",special_numbers)
    print("Even only numbers ", even_only)
    print("Three only numbers ", three_only)
    print("store in others ", store_in_others)

    print("\nCOUNTERS :")
    print("Special numbers ",special_numbers_count)
    print("Even only numbers ", even_only_count)
    print("Three only numbers ", three_only_count)
    print("store in others ", store_in_others_count)


n = int(input("Enter a number :"))

divisible(n)