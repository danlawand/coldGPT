import os
from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
from process_text import initialize_processed_text, ProcessedText
from api_llm import llm_query


app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

url_hotmart = os.getenv('URL_HOTMART')
processed_text = initialize_processed_text(url_hotmart)

@app.route('/genai', methods=['POST'])
def generate_answer():
    data = request.json
    question =  data['text']
    context = processed_text.query_answer(question)
    llm_result = llm_query(question, context)
    return  f'{llm_result}'

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
