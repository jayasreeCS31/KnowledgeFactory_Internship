class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)
# Creating Objects
s1 = Student("Jayasree", 21, "CSE")
s2 = Student("Ravi", 22, "ECE")
s1.display()
print()
s2.display()