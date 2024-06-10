import faiss
import numpy as np

d = 64  # dimension of the vectors
nb = 10000  # number of database vectors
nq = 100  # number of query vectors

# Generate random vectors
np.random.seed(1234)
xb = np.random.random((nb, d)).astype('float32') 
xb[:, 0] += np.arange(nb) / 1000.0 
xq = np.random.random((nq, d)).astype('float32')
xq[:, 0] += np.arange(nq) / 1000.0

# Build index
index = faiss.IndexFlatL2(d)  # Using L2 (Euclidean) distance
print(index.is_trained)
index.add(xb)  # Add the database vectors to the index
print(index.ntotal)

# Search
k = 5  # number of nearest neighbors to search
D, I = index.search(xq, k)  # D is the distances, I is the indices of the nearest neighbors
print(I[:5])  # print the indices of the nearest neighbors for the first 5 query vectors
print(D[:5])  # print the distances of the nearest neighbors for the first 5 query vectors

