# Author: Dhruv
tasks = []

while True:

    print("\n----------")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    userChoice = input("Plese select your choice from option (1-4) :")

    if userChoice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")
    
    elif userChoice == "2":

        if not tasks:
            print("\n-----SOMETHING WENT WRONG-----")
            print("No task found")

        else:
            print("\n-----YOUR TASKS ARE-----")
            for i, task in enumerate(tasks, 1):     #enumerate used to check index number and item                                                 
                print(f"{i}. {task}")    #Here we start form 1 that why its shows index 1 insted 0
    
    elif userChoice == "3":
        
        if not tasks:
            print("\n-----SOMETHING WENT WRONG-----")
            print("No task to delete")

        else:
            print("\nSELECT TAST FOR DELETE")
            print(tasks)
            
            num = int(input("Enter task number to delete task :"))

            if 1 <= num <= len(tasks):
                remove = tasks.pop(num - 1)
                print("\n-----THANKYOU-----")
                print(f"Task has been removed {remove}")
            
            else:
                print("\n-----SOMETHING WENT WRONG-----")
                print("Invalid number")
    
    elif userChoice == "4":
        print("Good Bye")
        break

    else:
        print("Invalid choice")