# Takes details of 5 students:
# Name
# Marks in 3 subjects
# Calculates each student’s average percentage
# Determines whether the student has passed or failed based on:
# Fails if any subject mark is below 33, or
# Passes if the average percentage is 40 or more.
# Stores the names of passed students in one list and failed students in another list.
# Prints both lists at the end.


passed_student_in_exam = []
failed_student_in_exam = []

for i in range (5):
    user_name = input("Enter a name of the student :")
    marks1 = int(input("Enter the marks of subjet :"))
    marks2 = int(input("Enter the marks of subjet :"))
    marks3 = int(input("Enter the marks of subjet :"))
    total_percentage = (marks1 + marks2 + marks3)/3

    if (marks1 < 33 or marks2 < 33 or marks3 < 33 ):
        failed_student_in_exam.append(user_name)
    
    elif(total_percentage >= 40):
        passed_student_in_exam.append(user_name)
    
    else:
        failed_student_in_exam.append(user_name)


print("Passed students:", passed_student_in_exam)
print("Failed students:", failed_student_in_exam)

                                #  sescound method

def student(n):

    passed_students = []
    failed_students = []

    for i in range (n):
        student_name = input("Enter a student name :")  
        marks1 =int(input("Enter marks of subject 1 :"))
        marks2 =int(input("Enter marks of subject 2 :"))
        marks3 =int(input("Enter marks of subject 3 :"))

        # AVERAGE PERCENTAGE OF STUDENTS :

        average_percentage = (marks1 + marks2 + marks3)/3

        # if elif else [condtions] to find wheter a student fails or passed the exam

        if (marks1 < 33 or marks2 < 33 or marks3 < 33):

            print("\nRESULT :")
            print("YOU FAILED THE EXAM. ")

            failed_students.append(student_name.capitalize())

        elif (average_percentage > 40):

            print("\nRESULT :")
            print("YOU PASSED THE EXAM. ")

            passed_students.append(student_name.capitalize())

    print("\nLIST OF THE PASSED AND FAILD STUDENT IN EXAMS :")
    print("PASSED STUDENTS NAME IN EXAMS ARE :" , passed_students)
    print("FAILED STUDENTS NAME IN EXAMS ARE :" , failed_students)

n = int(input("Enter a number of students :"))

student(n)