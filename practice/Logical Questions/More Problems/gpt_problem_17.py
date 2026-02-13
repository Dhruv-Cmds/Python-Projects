# Takes the number of students as input.
# For each student:
# Takes the student’s name.
# Takes the student’s marks.
# Determines whether the student has passed or failed:
# Pass if marks are 40 or above.
# Fail otherwise.
# Stores the names of passed students in one list and failed students in another list.
# Counts the total number of passed and failed students.
# Prints:
# The list of passed students.
# The list of failed students.
# The total count of passed students.


# For how many student you want to check their marks

n = int(input("How many students :"))

# List where students name will stored

passed_student = []
failed_student = []

# Count total passed or falied students

passed_students = 0
failed_students = 0

# Loop starts here

for i in range (n):

    # student_name that use to take student name from the user

    student_name = input("Enter a student name :")

    #  student_marks that use to take student marks from the user

    studen_marks = int(input("Enter students marks :"))

    '''f and elis condtions that use to check eather student 
    failed or passed according to given conditions'''

    if (studen_marks >= 40):
        print ("You passed the exams")

        # This condition store passed_student name in passed_student list

        passed_student.append(student_name)

        # passed_students that is a counter to count total passed students

        passed_students += 1

    else:
        print ("You failed the exams")

        # This condition store failed_student name in failed_student list

        failed_student.append(student_name)

        # failed_Stuents that is a counter to count total failed students

        failed_students += 1

     # if , else and loop all ends here  

# This print condtion print passed and failed studens names 

print("Passed studens are :" , passed_student)
print("failed studens are :" , failed_student)

# This print condtion print total passed and failed studens

print("Total passed studens are :" , passed_students)
print("Total failed students are :" , failed_students)

                                                                            #  SECOUND METHOD


def pass_fail (n):

    passed_student = []
    failed_student = []
    total_student = []

    passed_student_count = 0
    failed_student_count = 0
    total_student_count = 0


    for i in range (n):

        student_name = input("Enter a studen name :")
        m = int(input("Enter marks of subject 1 :"))

        total_student.append(student_name.capitalize())

        if (m < 33):

            failed_student.append(student_name.capitalize())

            failed_student_count += 1
            total_student_count += 1

        elif (m >= 40):

            passed_student.append(student_name.capitalize())

            passed_student_count += 1
            total_student_count += 1


    print("\nSTUDENTS :")
    print("Passed studens are :" , passed_student)
    print("failed studens are :" , failed_student)
    print("total studens are :" ,total_student)

    print("\nCOUNTER")
    print("Total passed studens are :" , passed_student_count)
    print("Total failed students are :" , failed_student_count)
    print("Total students are :" , total_student_count)

n = int(input("Enter a number of studens :"))

pass_fail(n)