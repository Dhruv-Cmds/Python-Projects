# Create class Employee:
# Class attribute:
# company = "Microsoft"
# Instance attributes:
# name
# salary
# Tasks:
# Create 2 objects
# Change company using one object
# Print company from:
# both objects
# class
# Observe result.

class Employee:
    company = "Microsoft"

    def __init__(self , name , salary):
        self.name = name 
        self.salary = salary

e1 = Employee("Dhruv" , 120000)
print(f"Name of the employee is : {e1.name} and salary is {e1.salary} work at {e1.company}")
e2 = Employee("Ayushi" , 120000)
print(f"Name of the employee is : {e2.name} and salary is {e2.salary} work at {e2.company}")


print("Before changing company:")
print("e1 company:", e1.company)
print("e2 company:", e2.company)
print("Class company:", Employee.company)

print("\nChanging company using e1...\n")

# changing using one object
e1.company = "Google"

print("After changing company:")
print("e1 company:", e1.company)
print("e2 company:", e2.company)
print("Class company:", Employee.company)