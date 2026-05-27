from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb


reader=PdfReader("sample.pdf")

text=""

for page in reader.pages:

    text += page.extract_text()


chunk_size=100

chunks=[]

for i in range(0,len(text),chunk_size):

    chunks.append(
        text[i:i+chunk_size]
    )


model=SentenceTransformer(
'all-MiniLM-L6-v2'
)

embeddings=model.encode(chunks)


client=chromadb.Client()

collection=client.create_collection(
name="pdf_rag"
)


for i,chunk in enumerate(chunks):

    collection.add(
        embeddings=[embeddings[i].tolist()],
        documents=[chunk],
        ids=[str(i)]
    )


while True:

    query=input("\nAsk: ")

    query_embedding=model.encode(query)

    results=collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=2
    )

    retrieved_text=" ".join(
        results["documents"][0]
    )

    print("\nContext Retrieved:\n")

    print(retrieved_text)

    print("\nGenerated Answer:\n")

    print(
        f"Based on the document: {retrieved_text}"
    )