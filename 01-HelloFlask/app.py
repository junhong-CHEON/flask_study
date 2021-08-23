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