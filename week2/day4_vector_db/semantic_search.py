import chromadb
# initialize database
client = chromadb.Client()
# create collection
collection = client.create_collection(
    name="knowledge_base"
)
# documents
documents = [
    "Python is used for web development",
    "Machine learning uses algorithms",
    "Artificial Intelligence simulates human thinking",
    "Cloud computing provides scalable resources",
    "RAG combines retrieval and generation"
]
ids = ["1", "2", "3", "4", "5"]
# add documents
collection.add(
    documents=documents,
    ids=ids
)
print("\nSemantic Search System")
print("----------------------")
while True:
    query = input("\nSearch: ")
    if query.lower() == "exit":
        break
    results = collection.query(
        query_texts=[query],
        n_results=2
    )
    print("\nRelevant Results:\n")
    for doc in results["documents"][0]:
        print("-", doc)