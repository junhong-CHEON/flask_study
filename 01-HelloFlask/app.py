"""
HelloFlask.py

첫 번째 Flask 웹 서버
"""

# 패키지 참조
from flask import Flask

# Flask 메인 객체 생성
# -> __name__ 은 이 소스파일의 이름
app = Flask(__name__)

# 특정 함수를 웹 상에 URL로 노출
# -> http://localhost:포트번호/hello_flask
@app.route("/hello_flask")
def hello_flask():
    return "<h1>Hello Flask~!!!</h1>"

if __name__ == "__main__":
    # 기본 옵션 이외의 사용자 지정 옵션을 사용해서 웹 서버 가동하기
    # 기본 옵션대로 가동
    # app.run()
    
    # 가동할 주소와 포트번호 지정 및 디버그 모드 활성화
    # 디버깅이란 에러를 추적하는 행위.
    # 디버그 모드란 프로그램의 실행 과정을 개발자가 파악할 수 있도록 상세하게 출력해 주는 것
    app.run(host='127.0.0.1', port=9901, debug=True)