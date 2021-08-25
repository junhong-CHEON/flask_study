"""
02-Parameter

클라이언트로부터 데이터 수신하기
"""

# 패키지 참조
import os
import sys

# 다른 폴더안의 파일들까지 import할 수 있도록 path 등록
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, render_template
from utils.Regex import Regex

# Flask 메인 객체 생성
# -> __name__ 은 이 소스파일의 이름
app = Flask(__name__)

regex = Regex()

# get 파라미터 수신 하기 -> methods를 지정하지 않으면 기본값은 GET
@app.route("/parameter/get", methods=['GET'])
def get():
    # URL에 포함된 변수 추출
    # ?num1=OOOO&num2=OOOOO
    my_num1 = request.args.get('num1')
    my_num2 = request.args.get('num2')
    
    # 정확한 구현을 위해서는 이 위치에서 파라미터가 존재하는지 여부와 숫자 형식이 맞는지 검증이 필요함.
    # -> 유효성 검사
    try:
        regex.num(my_num1, 'num1값이 숫자 형식이 아닙니다.')
        regex.num(my_num2, 'num2값이 숫자 형식이 아닙니다.')
    except Exception as e:
        return str(e)
    
    # parameter로 전송받은 모든 변수는 무조건 문자열.
    sum1 = my_num1 + my_num2
    
    # 연산이 필요하다면 형변환이 필수.
    sum2 = int(my_num1) + int(my_num2)
    
    output = "<h1>sum1=%s</h1><h1>sum2=%d</h1>" % (sum1, sum2)
    return output

# post 파라미터 수신 하기
# methods에 `POST`라고 지정하였으므로 post 전송방식이 아니면 접근 불가.
# 브라우저에 주소 직접 입력은 GET방식 전송에 해당하므로 브라우저로는 이 페이지 접근 불가.
@app.route("/parameter/post", methods=['POST'])
def post():
    # POST방식으로 전송된 변수 추출하기
    # <input type="???" name="name">
    # <input type="???" name="email">
    my_name = request.form.get('name')
    my_email = request.form.get('email')
    
    try:
        regex.kor(my_name, '이름은 한글만 입력 가능합니다.')
        regex.min_length(my_name, 2, '이름은 2~5글자까지만 입력 가능합니다.')
        regex.max_length(my_name, 5, '이름은 2~5글자까지만 입력 가능합니다.')
        regex.email(my_email, '이메일 형식이 잘못되었습니다.')
    except Exception as e:
        return str(e)
    
    output = "<h1>(Post) %s님의 이메일은 %s 입니다.</h1>" % (my_name, my_email)
    return output

# put 파라미터 수신 하기
@app.route("/parameter/put", methods=['PUT'])
def put():
    # POST방식으로 전송된 변수 추출하기
    # <input type="???" name="name">
    # <input type="???" name="email">
    my_name = request.form.get('name')
    my_email = request.form.get('email')
    
    try:
        regex.kor(my_name, '이름은 한글만 입력 가능합니다.')
        regex.min_length(my_name, 2, '이름은 2~5글자까지만 입력 가능합니다.')
        regex.max_length(my_name, 5, '이름은 2~5글자까지만 입력 가능합니다.')
        regex.email(my_email, '이메일 형식이 잘못되었습니다.')
    except Exception as e:
        return str(e)
    
    output = "<h1>(Put) %s님의 이메일은 %s 입니다.</h1>" % (my_name, my_email)
    return output

# put 파라미터 수신 하기
@app.route("/parameter/delete", methods=['DELETE'])
def delete():
    # POST방식으로 전송된 변수 추출하기
    # <input type="???" name="name">
    # <input type="???" name="email">
    my_name = request.form.get('name')
    my_email = request.form.get('email')
    
    try:
        regex.kor(my_name, '이름은 한글만 입력 가능합니다.')
        regex.min_length(my_name, 2, '이름은 2~5글자까지만 입력 가능합니다.')
        regex.max_length(my_name, 5, '이름은 2~5글자까지만 입력 가능합니다.')
        regex.email(my_email, '이메일 형식이 잘못되었습니다.')
    except Exception as e:
        return str(e)
    
    output = "<h1>(Delete) %s님의 이메일은 %s 입니다.</h1>" % (my_name, my_email)
    return output

@app.route('/parameter/my_webpage_test', methods=['GET'])
def page():
    return render_template('page.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9901, debug=True)