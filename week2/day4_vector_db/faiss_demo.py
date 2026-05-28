import faiss
import numpy as np
# vectors
vectors = np.array([
    [1.0, 2.0],
    [2.0, 3.0],
    [3.0, 4.0],
    [10.0, 10.0]
]).astype("float32")
# dimension
dimension = 2
# create index
index = faiss.IndexFlatL2(dimension)
# add vectors
index.add(vectors)
print("Total vectors:", index.ntotal)
# query vector
query = np.array([
    [2.5, 3.5]
]).astype("float32")
# search nearest 2 vectors
distances, indices = index.search(query, 2)
print("Nearest indices:")
print(indices)
print("Distances:")
print(distances)