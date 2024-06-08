import faiss
import numpy as np
from utils.parse import get_conversation
from sentence_transformers import SentenceTransformer
import json

# Store 


# Build index
def build_l2_index(d):
    index = faiss.IndexFlatL2(d)  # Using L2 (Euclidean) distance
    print("Is trained?:")
    print(index.is_trained)
    index.add(xb)  # Add the database vectors to the index
    print("Total N:")
    print(index.ntotal)
    return index

def search():
    k = 5  # number of nearest neighbors to search
    D, I = index.search(xq, k)  # D is the distances, I is the indices of the nearest neighbors
    print(I[:5])  # print the indices of the nearest neighbors for the first 5 query vectors
    print(D[:5])  # print the distances of the nearest neighbors for the first 5 query vectors


if __name__ == "__main__":
    conversations = get_conversation(50, "/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/bryan.txt", True)
    # Initialize the Sentence Transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Convert conversations to embeddings
    texts = [conv["text"] for conv in conversations]
    embeddings = model.encode(texts)
    embeddings = np.array(embeddings)


    # config
    d = 64  # dimension of the vectors
    nb = 10000  # number of database vectors
    nq = 100  # number of query vectors

    # Generate random vectors
    np.random.seed(1234)
    xb = np.random.random((nb, d)).astype('float32') 
    xb[:, 0] += np.arange(nb) / 1000.0 
    xq = np.random.random((nq, d)).astype('float32')
    xq[:, 0] += np.arange(nq) / 1000.0

    index = build_l2_index(d)
    search()