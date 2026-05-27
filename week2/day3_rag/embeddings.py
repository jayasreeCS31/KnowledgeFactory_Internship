from sentence_transformers import SentenceTransformer

chunks=[

"Artificial Intelligence",

"Machine learning",

"Deep learning"

]

model=SentenceTransformer(
'all-MiniLM-L6-v2'
)

embeddings=model.encode(
chunks
)

print(embeddings.shape)