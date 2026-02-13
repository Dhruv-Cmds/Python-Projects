# Takes a student's name and marks for 3 subjects.
# Checks if the student’s name exists in a given list.
# Calculates the student’s percentage.
# Determines whether the student has passed or failed:
# Fail if any subject is below 33.
# Pass if percentage is above 40 and all subjects are 33 or more.
# Displays the result.

student_name = input("Enter the name of the student :")

marks_of_subjects1 = int(input("Enter the marks of subject 1 :"))
marks_of_subjects2 = int(input("Enter the marks of subject 2 :"))
marks_of_subjects3 = int(input("Enter the marks of subject 3 :"))

l = ["Dhruv" , "Aryan" , "Meet" , "Om"]

if (student_name.capitalize() in l):
    print("The name of the student in list is :" , student_name)

else:
    print("student not found in the list")

# total_percentage = (marks_of_subjects1 + marks_of_subjects2 + marks_of_subjects3)/3
total_percetage = ((100)*(marks_of_subjects1 + marks_of_subjects2 + marks_of_subjects3))/300

if (marks_of_subjects1 < 33 or marks_of_subjects2 < 33 or marks_of_subjects3 < 33):
    print ("You failed the exam :")

elif (total_percetage > 40): 
    print ("You passed the exam :")

else:
    print("You failed the exam :")


print(type(l))

                                                        #  secound way

def pass_fail ():
        
        if name.capitalize() not in l:
            print("Entered name is not available in list :")
            return
        
        else:
            print("Your name is in  list :")

            marks1 = int(input("Enter marks"))
            marks2 = int(input("Enter marks"))
            marks3 = int(input("Enter marks"))

            total_percentage = (marks1 + marks2 + marks3)/3

        if (total_percentage > 40):
             print("You passed the exam :")
        
        elif (marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
                print("You failed the exam :") 
 
          
name = input("Enter student name :")
l = ["Dhruv" , "Aryan" , "Meet" , "Om"]
pass_fail()

                                                    # third way

def pass_fail ():

        found = False

        for n in l:
             if n.capitalize() == name.capitalize():
              found = True
              break
        
        if not found:
              print("Entered name is not available in list :")
              return
        
        else:
            print("Your name is in  list :")

            marks1 = int(input("Enter marks"))
            marks2 = int(input("Enter marks"))
            marks3 = int(input("Enter marks"))

            total_percentage = (marks1 + marks2 + marks3)/3

        if (total_percentage > 40):
             print("You passed the exam :")
        
        elif (marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
                print("You failed the exam :") 
 
          
name = input("Enter student name :")
l = ["Dhruv" , "Aryan" , "Meet" , "Om"]
pass_fail()