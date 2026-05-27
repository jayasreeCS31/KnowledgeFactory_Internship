import ollama

response=ollama.chat(
model="llama3",

messages=[
{
'role':'user',
'content':'Explain AI'
}
]
)

print(response['message']['content'])