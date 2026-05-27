import requests
try:
    print(" DELETE POST \n")
    post_id = int(input("Enter Post ID to delete: "))
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.delete(
        url,
        headers=headers
    )
    print("\nStatus Code:", response.status_code)
    response.raise_for_status()
    print(f"""
Deleted Post ID : {post_id}
Status Code     : {response.status_code}
""")
except requests.exceptions.RequestException as error:
    print("API Error:", error)
except ValueError:
    print("Please enter valid numeric ID")