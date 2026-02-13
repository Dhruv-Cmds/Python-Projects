# Takes a number n from the user
# Creates a list of numbers from 1 to n using a loop
# From that list:
# create another list of even numbers
# create another list of odd numbers
# Print:
# All numbers: [...]
# Even numbers: [...]
# Odd numbers: [...]

n = int(input("Enter a number :"))

l_for_a_to_n_numbers = []
l_for_even_numbers = []
l_for_odd_numbers = []

all_numers = 0
even_numbers = 0
odd_numbers = 0

for i in range (1 , n + 1):
    l_for_a_to_n_numbers.append(i)
    all_numers += 1

for i in l_for_a_to_n_numbers :
    if (i % 2 == 0):
        even_numbers += 1

        l_for_even_numbers.append(i)
        
    else :
        odd_numbers += 1
        l_for_odd_numbers.append(i)
        
print("a to n numbers :" , l_for_a_to_n_numbers)
print("Even numbers :" , l_for_even_numbers)
print("odd numbers :" , l_for_odd_numbers)

print("all numbers :" , all_numers)
print("even numbers :" , even_numbers)
print("odd numbers :" , odd_numbers)

                                              # SECOUND METHOD

def odd_even (n):

    all_number = []

    for i in range (1 , n + 1):
        all_number.append(i)

    even_numbers = []
    odd_numbers = []

    for i in all_number:

        if (i  % 2 == 0):
            even_numbers.append(i)
        
        elif (i % 2 != 0):
            odd_numbers.append(i)

    print("\nALL NUMBERS LIST :")
    print(f"EVEN NUMBERS : {even_numbers}")
    print(f"ODD NUMBERS : {odd_numbers}")
    print(f"ALL NUMBERS : {all_number}") 

                    #  no counter asked so no added it
n = int(input("Enter numbrs as much as you want :"))
odd_even(n)