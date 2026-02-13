# name
# roll_no
# Create 2 objects and print their details.

class details:
    def __init__(self , name , rollNo):
        self.name = name
        self.rollNo = rollNo
    
d = details("Dhruv" , 21)
print(f"Name is {d.name} and Rollno is {d.rollNo}")
d = details("Ayushi" , 11)
print(f"Name is {d.name} and Rollno is {d.rollNo}")