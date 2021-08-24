# 03-Restful

---

## 파이썬에서 웹에 반응하는 기능을 구현하는 방법

### 1) URL과 함수를 맵핑

앞 단원의 예제 형식

URL과 함수 이름은 아무런 연관이 없으며 함수 이름은 개발자가 임의로 정할 수 있다.

URL과 methods의 조합은 다른 함수에 적용된 내용과 중복되면 안된다.

```python
@app.route('URL', methods=['GET|POST|PUT|DELETE'])
def 함수이름():
    ...
```

### 1) 클래스를 사용하는 방식

#### 패키지 설치
```shell
pip install --upgrade flask_restful
```

### 기본 코드 구조

클래스에 URL을 맵핑하고 get, post, put, delete 등의 메서드를 구현하여 하나의 주소에 접속하는 방법을 다양하게 구성

```python
# 패키지 참조
from flask import Flask
from flask_restful import Resource, Api

# Flask 메인 객체 생성
app = Flask(__name__)
api = Api(app)

# JSON 페이지를 담당하는 클래스
class MyRestful1(Resource):
    def get(self):
        # 출력 결과는 json 형식으로 구성되어야 함
        return {'msg': "MyRestful1::get 방식으로 접속함"}
    
    def post(self):
        return {'msg': "MyRestful1::post 방식으로 접속함"}
    
    def put(self):
        return {'msg': "MyRestful1::put 방식으로 접속함"}
    
    def delete(self):
        return {'msg': "MyRestful1::delete 방식으로 접속함"}

# Class를 /my_restful 이라는 URL로 등록
# 기본적으로 get, post, put, delete라는 메서드는 자동으로 각 접속 방식에 맞게 적용됨
api.add_resource(MyRestful1, '/my_restful')
```