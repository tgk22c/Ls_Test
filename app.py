from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()  # JSON 형태의 데이터를 받아옵니다.
    text = data.get('text')  # 'text' 키에 해당하는 값을 가져옵니다.
    processed_text = text.upper()  # 문자열 가공 예시 (대문자로 변환)
    return jsonify({'processed_text': processed_text})  # JSON 형태로 결과 반환

if __name__ == '__main__':
    app.run(debug=True)
