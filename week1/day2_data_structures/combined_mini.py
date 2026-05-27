import json
# List
numbers = [1, 2, 3, 4, 5]
# List comprehension
squares = [x*x for x in numbers]
# Tuple
data = ("Python", "JSON")
# Set
unique = {1, 2, 2, 3}
# Dictionary
student = {
    "name": "Jayasree",
    "age": 21
}
# JSON
json_data = json.dumps(student, indent=4)
print("Numbers:", numbers)
print("Squares:", squares)
print("Tuple:", data)
print("Set:", unique)
print("Dictionary:", student)
print("\nJSON Data:")
print(json_data)