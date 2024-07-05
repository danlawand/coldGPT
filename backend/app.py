from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sendText', methods=['POST'])
def process_text():
    data = request.json
    text = data['text']
    return jsonify({'response': f'@{text}'})

if __name__ == '__main__':
    app.run(port=5000)

