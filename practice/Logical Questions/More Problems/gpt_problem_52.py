# Simple Inheritance
# Create two classes:
# Person → attribute: name
# Student (inherits Person) → attribute: roll_no
# Create object of Student and print both values.

class Person:
    def __init__(self , name):
        self.name = name 

class Student (Person):
    def __init__ (self , name, rollno):
        super().__init__(name)
        self.rollno = rollno

    def __str__(self):
        return f"{self.name} and {self.rollno}"
    
s = Student("Dhruv" , 25)

print(s)