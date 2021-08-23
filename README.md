# flask_study
---

Flask 학습 자료

## #01. Flask 개발 준비

### 프로그램 설치

1. Python
2. VSCode
3. 지금까지 진행된 모든 파이썬 패키지들.
4. Flask (파이썬 패키지)

#### Flask 설치
```shell
pip install --upgrade flask
```

## #02. Flask 웹 서버 작성하기

### 1) 기본 소스코드 작성

#### 01-HelloFlask/app.py
```python
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
```

### 2) 작성된 프로그램 가동하기

`flask run` 이라는 명령으로 가동하지만 특별한 옵션 이 없을 경우 
명령어가 실행되는 디렉토리의 `app.py`라는 파일을 찾아서 실행시키는 것이 기본값.

#### 방법1) - 수업에서 채택한 방법

예제마다 폴더를 생성하고 그 안에서 flask 프로그램의 소스코드 이름을 app.py로 지정

#### 방법2) - 소스파일 이름이 app.py가 아닌 경우

예제마다 파일이름을 다르게 지정하고 명령어 실행시

##### windows
```shell
set FLASK_APP=소스파일이름
flask run
```

##### mac, linux
```shell
export $env FLASK_APP=소스파일이름
flask run
```

### 3) 가동중인 웹 서버의 주소 확인하기

명령프롬프트(터미널)에 출력되는 내용을 확인

```shell
❯ flask run
 * Serving Flask app 'HelloFlask.py' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

위의 내용에 따라 첫 번째 Flask 페이지의 주소는 아래와 같다.

> http://127.0.0.1:5000/hello_flask

혹은

> http://localhost:5000/hello_flask

혹은

> http://자신의_실제_IP주소:5000/hello_flask

`127.0.0.1`과 `localhost`는 모든 컴퓨터가 자기 자신을 의미하는 값이다.