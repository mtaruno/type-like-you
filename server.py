from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from response import get_response, get_history
import sqlite3

app = Flask(__name__, static_folder='static')

# Configure CORS
CORS(app, resources={r"/chat": {"origins": "http://localhost:3000"}})

# Database query function
def query_db(query, args=(), one=False):
    conn = sqlite3.connect('chat_history.db')
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# Chat endpoint
@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        return response
    
    data = request.get_json()
    user_message = data.get('message')
    start = data.get('start')
    ai_response = get_response(user_message, start)
    start = False
    return jsonify({'reply': ai_response})

# Serve index.html
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# Retrieve endpoint
@app.route('/retrieve', methods=['POST'])
def retrieve():
    data = request.json
    user_message = data['message']
    user_embedding = get_embedding(user_message)
    return jsonify(vector_db[closest_date])

if __name__ == '__main__':
    app.run(port=5000, debug=True)