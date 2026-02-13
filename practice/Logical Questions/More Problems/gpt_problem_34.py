# Student Result Analyzer
# You have a file students.txt:
# Rahul 78
# Aman 34
# Neha 90
# Priya 29
# Write a program to:
# Separate passed students (>=40) into passed.txt
# Failed students into failed.txt
# Print:
# total students
# passed count
# failed count
# topper name + marks

def student ():
    Total_students = 0
    passed_count = 0
    failed_count = 0

    topper_name = ""
    topper_marks = -1

    passed_student = []
    failed_student = []

    with open ("s_students.txt" , "r") as f:
        for j in f:
            Total_students += 1

            name , i = j.split()

            i = int(i)
            if (i >= 40):
                passed_student.append(j)
                passed_count += 1

            else:
                failed_student.append(j)
                failed_count += 1
            
            if i > topper_marks:
                topper_marks = i
                topper_name = name

        with open("s_passed.txt" , "w") as f:
            f.writelines(passed_student)

        with open("s_failed.txt" , "w") as f:
            f.writelines(failed_student)

    print("Passed students :" , passed_count)            
    print("faield students :" , failed_count)            
    print("Total students :" , Total_students)   
    print("Topper :" , topper_name , "/" , topper_marks)         
student ()