# Takes a list and a value as input.
# Removes all occurrences of the given value from the list.
# Returns a new list without that value.
# Prints the updated list.
# 
def clean_list(lst , value):
    new_list = []

    for i in lst:
        if i != value :
            new_list.append(i)
    return new_list

lst = [1 , 2 , 3 , 4 , 2]
value = int(input("Enter a value form removal :"))

print(clean_list(lst , value))