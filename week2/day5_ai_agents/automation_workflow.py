from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)
topic = input("Enter topic: ")
summary = llm.invoke(
    f"Give a short summary on {topic}"
)
print("\n=== SUMMARY ===\n")
print(summary.content)
points = llm.invoke(
    f"Extract 5 key points from:\n{summary.content}"
)
print("\n=== KEY POINTS ===\n")
print(points.content)
report = llm.invoke(
    f"""
Create a professional report.
Topic: {topic}
Summary:
{summary.content}
Key Points:
{points.content}
"""
)
print("\n=== FINAL REPORT ===\n")
print(report.content)