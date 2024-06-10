from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from response import get_response
from sqlite_actions import insert_whatsapp_history_and_update_profile, store_session_message_and_response
from utils.sqlite_db import show_table, show_tables
import sqlite3

app = Flask(__name__, static_folder='static')

# Configure CORS
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]}})


# Endpoint for uploading chat history from WhatsApp to the database and updating the user profile
@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    whatsapp_name = data.get('whatsapp_name')
    whatsapp_history = data.get('whatsapp_history')
    user_slang_dictionary = data.get('user_slang_dictionary')

    # Validate if required data is present
    if not whatsapp_name or not whatsapp_history:
        return jsonify({'error': 'Missing whatsapp_name or whatsapp_history'}), 400

    emoji_examples_limit = 60
    topn_words_limit = 150

    # Save the chat history to the database and update profile 
    insert_whatsapp_history_and_update_profile(whatsapp_name, whatsapp_history, emoji_examples_limit, topn_words_limit, user_slang_dictionary)

    # Return a success message
    return jsonify({'message': 'Chat history and profile updated successfully'}), 200

# Endpoint for getting LLM response / chatting and updating the sessions_history
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    session_id = data.get('session_id')
    user_message = data.get('message')
    whatsapp_name = data.get('whatsapp_name')

    # Validate if required data is present
    if not session_id or not user_message:
        return jsonify({'error': 'Missing session_id or message'}), 400

    history_obj = [{}]

    message_obj = {
        "role": "user",
        "content": user_message,
    }   

    response = get_response(history_obj, message_obj, whatsapp_name)

    # Save the user message to the session_database
    store_session_message_and_response(whatsapp_name, session_id, user_message, response)

    return jsonify({'message': response})

# Endpoint for returning all the session history in JSON format that can be used for the prompt 
@app.route('/session', methods=['GET'])
def get_sessions():
    conn = sqlite3.connect('/Users/matthewtaruno/Library/Mobile Documents/com~apple~CloudDocs/Dev/type-like-you/data/db/chat.db')
    cursor = conn.cursor()
    session_history = cursor.execute('SELECT session_id, name, message FROM session_history')
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