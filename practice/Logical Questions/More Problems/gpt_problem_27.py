# Takes a list of numbers as input.
# Separates the numbers into two lists:
# Numbers greater than or equal to 50
# Numbers less than 50
# Returns both lists.
# Prints the two lists.

def  split_numbers(lst):
    bigger_than_50 = []
    small_than_50 = []

    for i in lst:
        if (i >= 50):
         bigger_than_50.append(i)
        
        else:
           small_than_50.append(i)
    return bigger_than_50 , small_than_50   

lst = [50 , 696 , 46 , 67 , 12 , 45]
big , small = split_numbers(lst)

print("BIGGER" , big)
print("SMALLER" , small)