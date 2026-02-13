# Takes a comment from the user.
# Checks if the comment contains any banned phrases:
# "no fight"
# "no abuse"
# "no sexual talk"
# If any of these phrases are found (case-insensitive), display "Spam comment detected".
# Otherwise, display "Spam comment not detected".


comment = input("Write a comment you ")

l = ["No fight" , "No abuse" , "No sexual talk"]

if ("no fight" in comment.lower() or
    "no abuse" in comment.lower() or
    "no sexual talk" in comment.lower()):
    print ("Spam comment detected :")

else:
    print ("Spam comment not detected :")
                                        # secound way

def comment ():
    for user_comment in l :
        if (user_comment.capitalize() in l):
            print("spam comment detected.")
            return

        else:
            print("spam comment not detected.")
user_comment = input("Enter a comment :")
l = ["No fight" , "No abuse" , "No sexual talk"]
comment()
