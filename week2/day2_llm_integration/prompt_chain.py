from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(

    api_key=os.getenv("GROQ_API_KEY"),

    base_url="https://api.groq.com/openai/v1"
)

# Step 1
response1 = client.chat.completions.create(

    model="llama-3.1-8b-instant",

    messages=[
        {
            "role":"user",
            "content":"Explain Machine Learning"
        }
    ]
)

summary = response1.choices[0].message.content

print("\nSUMMARY:\n")
print(summary)

# Step 2
response2 = client.chat.completions.create(

    model="llama-3.1-8b-instant",

    messages=[
        {
            "role":"user",

            "content":
            f"Convert this into bullet points:\n{summary}"
        }
    ]
)

print("\nBULLET POINTS:\n")

print(response2.choices[0].message.content)