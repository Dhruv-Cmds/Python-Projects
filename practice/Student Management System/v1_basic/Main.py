# AUTHOR
# DHRUV

# STUDENT MANAGEMENT SYSTEM

class Student:

    def __init__(self , name , rollno):

        self.name = name
        self.rollno = rollno
        self.marks = []

    def add_marks (self , mark):

        self.mark = mark

        self.marks.append(self.mark)

    def calculate_average (self):

        if len(self.marks) == 0:
            return 0
        
        evaluation = sum(self.marks) / len(self.marks)
        return evaluation
    
    def pass_fail (self):

        if self.calculate_average() >= 40 :
            return "Pass"
        return "Failed"
    
    def info (self):
                
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Marks:", self.marks)
        print("Average:", self.calculate_average())
        print("Result:", self.pass_fail())


s = Student("Dhruv" , 1)
s.add_marks(80)
s.add_marks(70)
s.add_marks(90)

s.calculate_average()
s.info()
s.pass_fail()