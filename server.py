from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS


from response import get_response



import sqlite3














app = Flask(__name__, static_folder='static')

# Configure CORS
CORS(app, resources={r"/chat": {"origins": "http://localhost:3000"}})


# Endpoint for uploading chat history from WhatsApp to the database and updating the user profile
@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    whatsapp_name = data.get('whatsapp_name')
    whatsapp_history = data.get('whatsapp_history')

    # Save the chat history to the database
    con = sqlite3.connect('')




    # Simulated chat history for the example
    chat_history = None
    return jsonify({'data': chat_history.strip()})

# Endpoint for getting LLM response / chatting and updating the sessions_history
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    session_id = data.get('session_id')
    user_message = data.get('message')
    ai_response = get_response(user_message, session_id)
    return jsonify({'message': [ai_response]})

# Endpoint for returning all the session history in JSON format
@app.route('/sessions', methods=['GET'])
def get_sessions():
    sessions = query_db('SELECT session_id, name, message FROM conversations ORDER BY session_id')
    session_dict = {}
    for session in sessions:
        session_id = session[0]
        if session_id not in session_dict:
            session_dict[session_id] = {'session_id': session_id, 'messages': []}
        session_dict[session_id]['messages'].append({'name': session[1], 'message': session[2]})
    return jsonify({'data': list(session_dict.values())})

# Serve index.html
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(port=5000, debug=True)