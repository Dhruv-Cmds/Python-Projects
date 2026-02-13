# Login Validator Function
# Write a function:
# check_login(username, password)
# Rules:
# correct username = "admin"
# correct password = "1234"
# Function should return:
# "Access Granted"
# or "Access Denied"
# Call it from main code and print the result.

# def check_login(username, password):
#     if (username == "admin" and password == 1234):
#      return "Access Granted"

#     else:
#        return "Access Denied"

# username = input("Enter a username :")
# password = int(input("Enter a password :"))
# result = check_login(username , password)
# print(result)

                                        #   secound mehod

def check_login():
    if (username == "admin" and password == 1234):
     return "Access Granted"

    else:
       return "Access Denied"

username = input("Enter a username :")
password = int(input("Enter a password :"))
result = check_login()
print(result)                                       