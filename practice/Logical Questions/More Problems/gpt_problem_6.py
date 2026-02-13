# Takes a number n from the user.
# Prints all even and odd numbers from 0 to n.
# Counts how many even numbers and how many odd numbers appear in that range.
# Displays the total count of even and odd numbers at the end.

n = int(input("Enter a number :"))

even_count = 0
odd_count = 0

for i in range (0 , n + 1):
   if(i%2 == 0):
      print("even" , i)
      even_count += 1

   else:
      print("odd" , i)
      odd_count += 1

print("TOTAL COUNT OF EVEN NUMBERS ARE :" , even_count)
print("TOTAL COUNT OF ODD NUMBERS ARE :" , odd_count)

                                             #  secound method

def even_odd (n):
    even_numbers = 0
    odd_numbers = 0
    for i in range (0 , n + 1):
        if (i % 2 == 0):
            even_numbers += 1
            print(i , "Even")

        else:
            odd_numbers += 1
            print(i , "odd")

    print("Total even numbers :" , even_numbers)
    print("Total odd numers :" , odd_numbers)

n = int(input("Enter a number"))
even_odd(n)