import ollama
response = ollama.chat(
    model='llama3',
    messages=[
        {
            'role': 'user',
            'content': 'Explain REST APIs simply'
        }
    ]
)
print(response['message']['content'])