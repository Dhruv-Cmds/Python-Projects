# import json
from db import get_connection
class Student:

    # def __init__(self, name, rollno, filepath="practice/Student Management System/v2_oop_file/student.json"): # filepath="student.txt"
    #     self.name = name
    #     self.rollno = rollno
    #     self.filepath = filepath
    #     self.marks = []
    #     self.load()


    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    
    def add_data(self):
        sql = "INSERT INTO students (name, roll_no, marks) VALUES (%s, %s, %s)"
        values = ('Dhruv', 1, '80,70,90')
        self.cursor.execute(sql,values)
        self.conn.commit()
    
    # .txt
    # def save(self):

    #     with open(self.filepath, "w") as f:
    #         marks_str = ",".join(map(str, self.marks))
    #         f.write(f"{self.name} {self.rollno} {marks_str}\n")

    # def load(self):

    #     try:
    #         with open(self.filepath, "r") as f:
    #             data = f.read().split()
    #             if len(data) >= 3:
    #                 self.name = data[0]
    #                 self.rollno = int(data[1])
    #                 self.marks = list(map(int, data[2].split(",")))

    #     except FileNotFoundError:
    #         self.save()


    # .json
    # def save (self):

    #     with open (self.filepath , "w") as f:
    #         json.dump ({"name" : self.name, "roll_no" : self.rollno, "marks" : self.marks}, f, indent=4)

    # def load (self):

    #     try:
             
    #         with open (self.filepath , "r") as f:

    #             data = json.load(f)

    #             if data: 
    #                 self.name = data.get("name" , self.name)
    #                 self.rollno = data.get("roll_no" , self.rollno)
    #                 self.marks = data.get("marks" , self.marks)
                
    #             else:
    #                 self.save()
        
    #     except FileNotFoundError:
    #         self.save()

    # def add_marks(self, mark):

    #     self.marks.append(mark)
    #     self.save()

    def calculate_average(self):

        # if not self.marks:
        #     return 0
        # return sum(self.marks) / len(self.marks)

        studnet_roll_no = int(input("Enter your roll_no: "))
        
        sql = "SELECT marks FROM students WHERE roll_no = %s"
        values = (studnet_roll_no,)
        self.cursor.execute(sql, values)
        data = self.cursor.fetchone()

        if not data:
            print("No student found.")
            return 0
        
        marks_str = data[0]
        marks_list = list(map(int, marks_str.split(",")))

        avg = sum(marks_list) / len(marks_list)
        return avg

    def pass_fail(self):

        return "You passed the exam." if self.calculate_average() >= 40 else "You failed the exam."

    def info(self):

        # print(f"Name: {self.name}")
        # print(f"RollNo: {self.rollno}")
        # print(f"Marks: {self.marks}")
        # print(f"Average: {self.calculate_average()}")
        # print(f"Result: {self.pass_fail()}")

        student_roll_no = int(input("Enter your roll_no: "))

        sql = "SELECT name, roll_no, marks FROM students WHERE roll_no = %s"
        values = (student_roll_no,)

        self.cursor.execute(sql, values)
        data = self.cursor.fetchone()

        if not data:
            print("No student found.")
            return

        name, roll_no, marks_str = data

        marks_list = list(map(int, marks_str.split(",")))

        avg = sum(marks_list) / len(marks_list)
        result = "You passed the exam." if avg >= 40 else "You failed the exam."

        print(f"Name: {name}")
        print(f"RollNo: {roll_no}")
        print(f"Marks: {marks_list}")
        print(f"Average: {avg}")
        print(f"Result: {result}")

# s = Student("Dhruv", 1)
# s.add_marks(80)
# s.add_marks(70)
# s.add_marks(90)

s = Student()

s.add_data()

s.info()