# import json
import mysql.connector

class Management:  

     #  use this when you use .json or .txt
    # def __init__(self , filepath = "utilities/Management System/v2_oop_file/task.json"): #"task.txt"

    #     self.tasks = []
    #     self.filepath = filepath
    #     self.load()

    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "YOUR_PASSWORD_HERE",
            database = "managementsystem"
        )

        self.cursor = self.conn.cursor()

    '''Data save in .txt file'''
    # def save(self):
    #     with open (self.filepath , "w") as f:
    #         for task in self.tasks:
    #             f.write(task + "\n")
                
    # def load(self):
    #     try:
    #         with open(self.filepath , "r") as f:
    #             self.tasks = [line.strip() for line in f if line.strip()]
    #     except FileNotFoundError:
    #             self.tasks = []

    '''Data save in .json file'''
    # def save(self):
        
    #     with open (self.filepath , "w") as f:
    #         json.dump(self.tasks , f , indent=4)

    # def load(self):

    #     try:
    #         with open(self.filepath , "r") as f:
    #             self.tasks = json.load(f)

    #     except FileNotFoundError:
    #         self.tasks = []
            
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
                task = input(("Enter your task: ")).strip()

                if not task:
                    print("Task cannot be empty.")
                    return

                # self.tasks.append({"task" : task})
                # self.save()

                sql = "INSERT INTO tasks (task) VALUES (%s)"
                values = (task,)

                self.cursor.execute(sql , values)
                self.conn.commit()

                print("Task added")

            elif (choice == 2):
                # if (not self.tasks):
                #     print("No Task yet added.")

                # else:
                #     print("----Your tasks:----")
                #     for i , task in enumerate(self.tasks , 1):
                #         print(f"{i}. {task}")


                sql = "SELECT task from tasks"

                self.cursor.execute(sql)
                result = self.cursor.fetchone()

                if result:
                    print ("--- Your Tasks ---")
                    for i , task in enumerate (result , 1):
                        print(f"{i}: {task[0]}")

                else:
                    print("No TASKS found.")

            elif (choice == 3):
                # if (not self.tasks):
                #     print("No Task yet added.")     

                # else:
                #     print("----Tasks list:----")
                #     for i , task in enumerate(self.tasks , 1):
                #         print(f"{i}. {task['task']}")

                #     try:
                #         numOfTask = int(input("Enter task number to delete: "))
                #     except ValueError:
                #         print("Invalid choice.")
                #         continue
                    
                #     if (numOfTask >= 1 and numOfTask <= len(self.tasks)):
                #         remove = self.tasks.pop(numOfTask - 1)
                #         print(f"Task has been removed {remove}")

                #         self.save()
                    
                    # else:
                    #     print("Invalid Task number.")

                sql = "DELETE FROM tasks"
                self.cursor.execute(sql)
                self.conn.commit()

                if self.cursor.rowcount > 0:
                    print(f"TASK: {self.cursor.rowcount} Deleted.")
                else:
                    print("Task not found")
                
            elif (choice == 4):
                    # self.save()
                    print("Thank you for using us! Have a nice day.")
                    break
            
            else:
                print("Invalid choice")

                        
          
m = Management()
m.run()