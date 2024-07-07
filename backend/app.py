from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

# @app.route('/genai', methods=['POST'])
# def generate_answer():
#     data = request.json
#     answer = data['text']
#     return jsonify({'response': f'{answer}'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
