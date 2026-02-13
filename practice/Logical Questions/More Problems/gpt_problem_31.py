# You have two files:
# s_file1.txt
# s_file2.txt
# Write a program to:
# Find lines that are different
# Print line numbers where they differ
# Also write those lines into difference.txt

def files (s_file1 , s_file2):

    with open("s_file1.txt" , "r") as f1 , open("s_file2.txt" , "r") as f2:

        line1 = f1.readlines()
        
        line2 = f2.readlines()

        difference = []

    min_len =  min(len(line1) , (len(line2)))

    for i in range (min_len):
        
        if (line1[i] != line2[i]):

            lineno = i + 1

            print(f"Difference at line no {lineno}")

            print("s_file1 :" , line1[i].strip())

            print("s_file :" , line2[i].strip())

            difference.append(f"line , {lineno} \n")

            difference.append(f"s_file1 , {line1[i]}")

            difference.append(f"s_file2 , {line2[i]} \n")

    with open("difference.txt" , "w") as f:

        f.writelines(difference)
        
files("s_file.txt" , "file2.txt")