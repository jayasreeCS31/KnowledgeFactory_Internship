from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create client
client = OpenAI(

    api_key=os.getenv("GROQ_API_KEY"),

    base_url="https://api.groq.com/openai/v1"
)

# Take user input
user_query = input("Ask AI Anything: ")

# Send request
response = client.chat.completions.create(

    model="llama-3.1-8b-instant",

    messages=[
        {
            "role":"user",
            "content": user_query
        }
    ]
)

# Print AI response
print("\nAI Response:\n")

print(response.choices[0].message.content)