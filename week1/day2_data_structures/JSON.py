import json
student = {
    "name": "Jayasree",
    "age": 21,
    "course": "CSE",
    "marks": {
        "python": 95,
        "java": 90
    }
}
# Dictionary to JSON
json_data = json.dumps(student, indent=4)
print("JSON Data:")
print(json_data)
# JSON to Python Dictionary
python_data = json.loads(json_data)
print("\nConverted Back to Python Dictionary:")
print(python_data)
# Access Data
print("\nStudent Name:")
print(python_data["name"])
# Writing JSON to File
file = open("student.json", "w")
json.dump(student, file, indent=4)
file.close()
print("\nJSON written to file successfully")
# Reading JSON from File
file = open("student.json", "r")
data = json.load(file)
print("\nData Read From File:")
print(data)
file.close()