# File Statistics Generator (Boss Level)
# For a file book.txt, calculate:
# Total characters
# Total words
# Total lines
# Longest line length
# How many times word "python" appears (case-insensitive)
# Print everything clearly.

with  open("s_book.txt" , "r") as f:
    Longest_line_length = 0
    Total_words = 0
    Total_characters = 0
    Total_lines = 0
    count_python = 0


    for i in f:
        Total_lines += 1
        Total_characters += len(i)
        Total_words += len(i.split())

        if "python" in i.lower():
            count_python += 1

        if len(i) > Longest_line_length :
            Longest_line_length = len(i)

        
        
print("Total lines are :" , Total_lines)
print("Total python are :" , count_python)
print("Total characters are :" , Total_characters)
print("Total words are :" , Total_words)
print("Total longest line length is :" , Longest_line_length)
