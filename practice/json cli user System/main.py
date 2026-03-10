import json

try:
    with open ("t.json" , "r") as f:
        data = json.load(f)

except:
    data = {
        "users" : [],
    }

while True:

    print("1. Register")
    print("2. Login")
    print("3. Show users")
    print("4. Change password/username")
    print("5. Delete user")
    print("6. Exit")

    while True:
        try:
            choice = int(input("Choose option: "))
            
        except ValueError:
            print("Invalid choice.")

            continue

        break

    if choice == 1:

        while True:
            name  = input("Enter username: ").strip()
            password = input("Enter password: ").strip()

            if password.isdigit() and len(password) != 4:

                print("Invalid password")

                continue

            break

        user = {
            "username" : name,
            "password" : password
        }

        exist = False

        for u in data["users"]: 

            if u["username"] == name:
                exist = True
                break
        
        if exist:
            print("User already exists.")
        
        else:

            data["users"].append(user)

            with open ("t.json" , "w") as f: 
                json.dump(data , f, indent=4)

            print("User registred.")
    
    elif choice == 2:

        while True:
            name  = input("Enter username: ").strip()
            password = input("Enter password: ").strip()

            if password.isdigit() and len(password) != 4:
                print("Invalid password")
                continue

            break

        found = False

        for i in data["users"]:

            if i['username'] == name and i['password'] == password:

                found = True

                print("welcome")

                break
        
        if not found:
            print("Invalid login")
            
    elif choice == 3:

        for u in data["users"]:
            print(f"username: {u['username']} | password: {'*' * len(u['password'])}")
    
    elif choice == 4:

        name = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        found = False

        for u in data["users"]:

            if u["username"] == name and u["password"] == password:

                found = True

                print("1. Change username")
                print("2. Change password")
                print("3. Back")

                ch = int(input("Choose option: "))

                if ch == 1:

                    new_name = input("Enter new username: ").strip()

                    if any(x["username"] == new_name for x in data["users"]):
                        print("Username already exists")

                    else:
                        u["username"] = new_name

                    print("Username updated")

                elif ch == 2:

                    new_password = input("Enter new password: ").strip()

                    if new_password.isdigit() and len(new_password) != 4:
                        print("Invalid password")
                        break

                    u["password"] = new_password

                    print("Password updated")

                break

        if found:

            with open("t.json", "w") as f:
                json.dump(data, f, indent=4)

        else:
            print("User not found")

    elif choice == 5:

        while True:

            name = input("Enter name to remove").strip()

            password = input("Enter password: " ).strip()

            if password.isdigit() and len(password) != 4:

                print("Invalid password")

                continue

            break

        found = False
        for up in data["users"]:

            if up["username"] == name and up["password"] == password:

                data["users"].remove(up)

                found = True

                break
        
        if found:

            with open("t.json", "w") as f:

                json.dump(data, f, indent=4)

            print("User deleted")

        else:
            print("User not found")

    elif choice == 6:
        print("exit...")
        break

    else:
        print("Invalid choice")