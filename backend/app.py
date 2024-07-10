from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
from process_text import initialize_processed_text, ProcessedText
from llm import  initialize_llm_model

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

processed_text = initialize_processed_text("https://hotmart.com/pt-br/blog/como-funciona-hotmart")
model = initialize_llm_model()

@app.route('/genai', methods=['POST'])
def generate_answer():
    data = request.json
    query_ans = processed_text.query_answer(data['text'])
    answer = model.generate_2nd(query_ans)
    return  f'{answer}'

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
