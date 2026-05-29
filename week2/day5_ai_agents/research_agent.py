from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
load_dotenv()
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)
search = DuckDuckGoSearchRun()
query = input("Ask a research question: ")
print("\nSearching...\n")
search_results = search.run(query)
prompt = f"""
You are a research assistant.
Question:
{query}
Search Results:
{search_results}
Provide:
1. Summary
2. Key Points
3. Conclusion
"""
response = llm.invoke(prompt)
print("\n========== FINAL ANSWER ==========\n")
print(response.content)