import faiss
import numpy as np
from utils.parse import get_messages, get_all_message_objects
from sentence_transformers import SentenceTransformer




# def search():
    # k = 5  # number of nearest neighbors to search
    # D, I = index.search(xq, k)  # D is the distances, I is the indices of the nearest neighbors
    # print(I[:5])  # print the indices of the nearest neighbors for the first 5 query vectors
    # print(D[:5])  # print the distances of the nearest neighbors for the first 5 query vectors

def get_nearest_chunks():
    pass 


if __name__ == "__main__":
    conversations = get_all_message_objects("/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/bryan.txt")
    
    # Initialize the Sentence Transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Convert conversations to embeddings
    texts = [conv["message"] for conv in conversations]
    print("Head of texts:")
    print(texts[:5])
    embeddings = model.encode(texts)
    embeddings = np.array(embeddings)

    print("Shape of embeddings:", embeddings.shape)
    print("Head of embeddings:")
    print(embeddings[:5])


    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # start with this example
    user_message = "Hi there, could you teach me about airplanes bro"
    message_embedding = model.encode([user_message])
    
