class Student:
    def __init__(self, name, rollno, filepath="student.txt"):
        self.name = name
        self.rollno = rollno
        self.filepath = filepath
        self.marks = []
        self.load()

    def save(self):
        with open(self.filepath, "w") as f:
            marks_str = ",".join(map(str, self.marks))
            f.write(f"{self.name} {self.rollno} {marks_str}\n")

    def load(self):
        try:
            with open(self.filepath, "r") as f:
                data = f.read().split()
                if len(data) >= 3:
                    self.name = data[0]
                    self.rollno = int(data[1])
                    self.marks = list(map(int, data[2].split(",")))
        except FileNotFoundError:
            self.save()

    def add_marks(self, mark):
        self.marks.append(mark)
        self.save()

    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def pass_fail(self):
        return "You passed the exam." if self.calculate_average() >= 40 else "You failed the exam."

    def info(self):
        print(f"Name: {self.name}")
        print(f"RollNo: {self.rollno}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average()}")
        print(f"Result: {self.pass_fail()}")

s = Student("Dhruv", 1)
s.add_marks(80)
s.add_marks(70)
s.add_marks(90)

s.info()