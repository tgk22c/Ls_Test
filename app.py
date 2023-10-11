from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse_case', methods=['POST'])
def reverse_case():
    data = request.get_json()  # JSON 형태의 데이터를 받아옵니다.
    text = data.get('text')  # 'text' 키로 데이터에서 문자열을 추출합니다.

    if text:
        reversed_text = text.swapcase()  # 대소문자를 바꿉니다.
        return jsonify({'reversed_text': reversed_text})  # 결과값을 JSON 형태로 반환합니다.
    
    else:
        return jsonify({'error': 'No text provided.'}), 400
