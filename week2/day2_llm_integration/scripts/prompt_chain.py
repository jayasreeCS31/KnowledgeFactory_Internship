from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAI(
api_key=os.getenv("OPENAI_API_KEY")
)

step1=client.chat.completions.create(

model="gpt-4.1-mini",

messages=[
{
"role":"user",
"content":"Explain AI"
}
]
)

summary=step1.choices[0].message.content

step2=client.chat.completions.create(

model="gpt-4.1-mini",

messages=[
{
"role":"user",

"content":
f"Convert {summary} into bullet points"
}
]
)

print(step2.choices[0].message.content)