class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("Person Name:", self.name)
class Student(Person):
    def __init__(self, name, branch, year):
        super().__init__(name)
        self.branch = branch
        self.year = year
    def display(self):
        print(" Student Details ")
        print("Name   :", self.name)
        print("Branch :", self.branch)
        print("Year   :", self.year)
s1 = Student("Jayasree", "CSE", 4)
s1.show()
print()
s1.display()