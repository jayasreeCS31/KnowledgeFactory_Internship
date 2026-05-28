import chromadb
# create client
client = chromadb.Client()
# create collection
collection = client.create_collection(
    name="student_notes"
)
# add documents
collection.add(
    documents=[
        "Python programming basics",
        "Machine learning introduction",
        "Cooking recipes for beginners",
        "Artificial Intelligence concepts"
    ],
    ids=["1", "2", "3", "4"]
)
# query
results = collection.query(
    query_texts=["AI and deep learning"],
    n_results=2
)
print(results)