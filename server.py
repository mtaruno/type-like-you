from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from response import get_response, get_regular_response
from sqlite_actions import insert_whatsapp_history_and_update_profile, store_session_message_and_response, get_history_obj, get_history_for_endpoint
from utils.sqlite_db import show_table, show_tables, delete_user_history

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
    user_message = data.get('message')
    whatsapp_name = data.get('whatsapp_name')

    # Validate if required data is present
    if not whatsapp_name or not user_message:
        return jsonify({'error': 'Missing whatsapp_name or message'}), 400

    history_objs = get_history_obj(whatsapp_name)

    message_obj = {
        "role": "user",
        "content": user_message,
    }   

    response = get_response(history_objs, message_obj, whatsapp_name)
    regular_response = get_regular_response(history_objs, message_obj, whatsapp_name)

    # Save the user message to the session_database
    store_session_message_and_response(whatsapp_name, user_message, response)

    return jsonify({'ditto_message': response, 'gpt4_message': regular_response})

# Endpoint for returning all the session history in JSON format that can be used for the prompt
@app.route('/history', methods=['GET'])
def get_history():
    history = get_history_for_endpoint()

    return jsonify(history)

@app.route('/delete', methods=['DELETE'])
def delete_history():
    data = request.get_json()
    whatsapp_name = data.get('whatsapp_name')

    # Validate if required data is present
    if not whatsapp_name:
        return jsonify({'error': 'Missing whatsapp_name'}), 400
    
    # Delete the user history from the database
    delete_user_history(whatsapp_name)

    return jsonify({'message': 'History deleted successfully'}), 200



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