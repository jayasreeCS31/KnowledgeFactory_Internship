from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(

    api_key=os.getenv("GROQ_API_KEY"),

    base_url="https://api.groq.com/openai/v1"
)

stream = client.chat.completions.create(

    model="llama-3.1-8b-instant",

    messages=[
        {
            "role":"user",
            "content":"Tell a short motivational story"
        }
    ],

    stream=True
)

print("\nAI Response:\n")

for chunk in stream:

    if chunk.choices[0].delta.content:

        print(
            chunk.choices[0].delta.content,
            end=""
        )