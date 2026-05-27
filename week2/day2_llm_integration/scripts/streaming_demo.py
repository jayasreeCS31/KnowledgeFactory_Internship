from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAI(
api_key=os.getenv("OPENAI_API_KEY")
)

stream=client.chat.completions.create(

model="gpt-4.1-mini",

messages=[
{
"role":"user",
"content":"Tell a short story"
}
],

stream=True
)

for chunk in stream:

    if chunk.choices[0].delta.content:

        print(
        chunk.choices[0].delta.content,
        end=""
        )