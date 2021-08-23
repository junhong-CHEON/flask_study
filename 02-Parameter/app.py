"""
02-Parameter

클라이언트로부터 데이터 수신하기
"""

# 패키지 참조
from flask import Flask, request

# Flask 메인 객체 생성
# -> __name__ 은 이 소스파일의 이름
app = Flask(__name__)

# get 파라미터 수신 하기
@app.route("/parameter/get", methods=['GET'])
def get():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    sum1 = num1 + num2
    sum2 = int(num1) + int(num2)
    
    output = "<h1>sum1=%s</h1><h1>sum2=%d</h1>" % (sum1, sum2)
    return output

@app.route("/parameter/post", methods=['POST'])
def post():
    name = request.form('name')
    email = request.form('email')
    
    output = "<h1>%s님의 이메일은 %s 입니다.</h1>" % (name, email)
    return output

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9901, debug=True)