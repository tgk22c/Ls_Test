from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse_case', methods=['POST'])
def reverse_case():
    data = request.get_json()
    original_text = data['text']
    reversed_text = original_text.swapcase()
    return jsonify({'reversed_text': reversed_text})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
