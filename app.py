# Flask Server Code
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse_case', methods=['POST'])
def reverse_case():
    data = request.get_json()
    if 'text' in data:
        reversed_text = data['text'].swapcase()
        return jsonify({'reversed_text': reversed_text})
    else:
        return jsonify({'error': 'No text field provided.'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
