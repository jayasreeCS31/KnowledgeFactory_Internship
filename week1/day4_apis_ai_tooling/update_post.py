import requests
try:
    print(" UPDATE POST \n")
    post_id = int(input("Enter Post ID: "))
    title = input("Enter New Title: ")
    body = input("Enter New Body: ")
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    payload = {
        "title": title,
        "body": body,
        "userId": 1
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(
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
    print("Please enter valid numeric ID")