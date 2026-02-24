class Management:  
    def __init__(self , filepath = "task.txt"):

        self.tasks = []
        self.filepath = filepath
        self.load()

    def save(self):
        with open (self.filepath , "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
                
    def load(self):
        try:
            with open(self.filepath , "r") as f:
                self.tasks = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
                self.tasks = []

    def run(self):

        while True:

            print ("--------------------")
            print("1. Add Task")
            print("2. View Task")
            print("3. Delete Task")
            print("4. Exit")
            print ("--------------------")

            try:
                choice = int(input("Enter your choice: "))

            except ValueError:
                print("Invalid choice type.")
                continue
            
            if (choice == 1):
                task = input(("Enter your task: "))
                self.tasks.append(task)
                print("Task added")

            elif (choice == 2):
                if (not self.tasks):
                    print("No Task yet added.")

                else:
                    print("----Your tasks:----")
                    for i , task in enumerate(self.tasks , 1):
                        print(f"{i}. {task}")

            elif (choice == 3):
                if (not self.tasks):
                    print("No Task yet added.")     

                else:
                    print("----Tasks list:----")
                    for i , task in enumerate(self.tasks , 1):
                        print(f"{i}. {task}")

                    try:
                        numOfTask = int(input("Enter task number to delete: "))
                    except ValueError:
                        print("Invalid choice.")
                        continue
                    
                    if (numOfTask >= 1 and numOfTask <= len(self.tasks)):
                        remove = self.tasks.pop(numOfTask - 1)
                        print(f"Task has been removed {remove}")
                    
                    else:
                        print("Invalid Task number.")
                
            elif (choice == 4):
                    self.save()
                    print("Thank you for using us! Have a nice day.")
                    break
            
            else:
                print("Invalid choice")

                        
          
m = Management()
m.run()