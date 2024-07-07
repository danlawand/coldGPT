from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
from web_scrapping import extract_text_from_url

app = Flask(__name__)
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/genai', methods=['POST'])
def generate_answer():
# https://hotmart.com/pt-br/blog/como-funciona-hotmart
    data = request.json
    answer = data['text']
    # answer = extract_text_from_url("https://hotmart.com/pt-br/blog/como-funciona-hotmart")
    return jsonify({'answer': f'{answer}'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
