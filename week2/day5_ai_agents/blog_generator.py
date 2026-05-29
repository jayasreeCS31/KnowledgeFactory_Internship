from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)
topic = input("Enter Blog Topic: ")
prompt = f"""
Write a professional blog about {topic}.
Include:
1. Introduction
2. Benefits
3. Challenges
4. Future Scope
5. Conclusion
"""
response = llm.invoke(prompt)
print("\n")
print(response.content)