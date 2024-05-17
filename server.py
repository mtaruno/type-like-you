from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from response import get_response


app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')
    ai_response = get_response(user_message)
    return jsonify({'reply': ai_response})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
