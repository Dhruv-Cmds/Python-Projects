# # Word Censorship System
# # Given:
# # story.txt
# # bannedwords list = ["bad", "ugly", "donkey"]
# # Your program should:
# Replace banned words with * (same length)
# Save result into clean_story.txt
# Original file must remain unchanged
# Example:
# donkey → ******

def words ():

    bannedwords = ["bad", "ugly", "donkey"]

    with open("s_tory.txt" , "r") as f:
        content = f.read()

    for i in bannedwords:
        content = content.replace( i , "*" * len(i))

    with open ("s_clean_story.txt" , "w") as f:
        f.write(content)
words ()