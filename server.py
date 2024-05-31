from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from response import get_response, get_history
import sqlite3
import faiss
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch


# Load model and tokenizer for embeddings
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

def get_embedding(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1)
    return embeddings.numpy()

def query_db(query, args=(), one=False):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# Initialize FAISS index
index = faiss.IndexFlatL2(384)  # Assuming embedding size is 384
vector_db = {}


app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')
    start = data.get('start')
    ai_response = get_response(user_message, start)
    return jsonify({'reply': ai_response})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)


@app.route('/retrieve', methods=['POST'])
def retrieve():
    data = request.json
    user_message = data['message']
    user_embedding = get_embedding(user_message)
    
    D, I = index.search(user_embedding, 1)
    closest_date = list(vector_db.keys())[I[0][0]]
    
    return jsonify(vector_db[closest_date])

if __name__ == '__main__':
    app.run(debug=True)
