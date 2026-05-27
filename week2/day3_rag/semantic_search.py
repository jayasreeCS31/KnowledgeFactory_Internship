from sentence_transformers import SentenceTransformer
import chromadb

chunks=[

"Artificial Intelligence",

"Machine learning",

"Deep learning uses neural networks"

]

model=SentenceTransformer(
'all-MiniLM-L6-v2'
)

embeddings=model.encode(chunks)

client=chromadb.Client()

collection=client.create_collection(
name="rag_collection"
)

for i,chunk in enumerate(chunks):

    collection.add(
        embeddings=[embeddings[i].tolist()],
        documents=[chunk],
        ids=[str(i)]
    )

query="neural network"

query_embedding=model.encode(query)

results=collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=2
)

print("\nRelevant Chunks:\n")

for doc in results["documents"][0]:

    print(doc)