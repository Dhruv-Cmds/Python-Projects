# count_even_odd(numbers_list)
# It should return two values:
# total even numbers
# total odd numbers
# Then print them outside the function.




def count_even_odd(numbers_list):
    even_numbers = 0
    odd_numbers = 0

    for i in number_list:
        if (i%2 == 0):
            even_numbers += 1      
        elif (i%2 != 0):
            odd_numbers += 1

    return even_numbers , odd_numbers

number_list = [1 , 2 , 3 , 4 , 5]
even, odd = count_even_odd(number_list)

count_even_odd(number_list)

print("Even numbers:", even)
print("Odd numbers:", odd)