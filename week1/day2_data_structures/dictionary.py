student = {
    "name": "Jayasree",
    "age": 21,
    "course": "CSE"
}
print(student)
print("\nName:", student["name"])
student["age"] = 22            #change
print("\nAfter Changing Age:")
print(student)
student["college"] = "ABC College"  #adding
print("\nAfter Adding College:")
print(student)
student.pop("course")       #remove
print("\nAfter Removing Course:")
print(student)
print("\nLooping Dictionary:")   #loop
for key, value in student.items():
    print(key, ":", value)
print("\nLength of Dictionary:")   #length
print(len(student))
new_student = student.copy()   #copy
print("\nCopied Dictionary:")
print(new_student)
#nsted
students = {                    
    "s1": {
        "name": "Jayasree",
        "age": 21
    },
    "s2": {
        "name": "Ravi",
        "age": 22
    }
}
print("\nNested Dictionary:")
print(students["s1"]["name"])
student.clear()           #clear
print("\nAfter Clear:")
print(student)