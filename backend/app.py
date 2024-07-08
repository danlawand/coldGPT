from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
from process_text import initialize_processed_text, ProcessedText
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
# processed_text = initialize_processed_text("https://hotmart.com/pt-br/blog/como-funciona-hotmart")
processed_text = initialize_processed_text("")

@app.route('/genai', methods=['POST'])
def generate_answer():
    # data = request.json
    # answer = data['text']
    answer = processed_text.query_answer("green")
    return jsonify({'answer': f'{answer}'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
