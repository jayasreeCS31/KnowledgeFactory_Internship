import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)

users = response.json()

for user in users:
    print(user["name"])
    print(user["email"])
    print(user["address"]["city"]) 
    print(user["website"])

print(len(users))