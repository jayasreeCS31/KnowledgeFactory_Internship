import requests
try:
    print(" CREATE NEW POST \n")
    title = input("Enter Title: ")
    body = input("Enter Body: ")
    user_id = int(input("Enter User ID: "))
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url,
        json=payload,
        headers=headers
    )
    print("\nStatus Code:", response.status_code)
    response.raise_for_status()
    result = response.json()
    print(f"""
ID       : {result["id"]}
Title    : {result["title"]}
Body     : {result["body"]}
User ID  : {result["userId"]}
""")
except requests.exceptions.RequestException as error:
    print("API Error:", error)
except ValueError:
    print("Please enter valid number for User ID")