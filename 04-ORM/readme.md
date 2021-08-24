# 04-ORM

---

기존의 sqlite 라이브러리는 sql문법에 의존해서 파이썬코드로 sql을 동작했었다.

sql 문법을 전부 파이썬 객체로 맵핑하여 파이썬 객체의 메소드를 통해서 구현할 수 있다면 훨씬 더 체계적이고 가독성이 좋을 것이다.

그러한 객체와 SQL 의 MAPPING을 바로 ORM이라고 한다.

## 패키지 설치하기

```
pip install --upgrade pymysql
pip install --upgrade SQLAlchemy
pip install --upgrade sqlalchemy_serializer
pip install --upgrade flask_sqlalchemy
```

## MVC 패턴

웹의 기능을 3부분으로 나누어 구현하는 객체지향 디자인(설계) 패턴

### Model 패키지

데이터(=DB테이블)의 구조를 정의해 놓은 클래스들의 모음

### View 패키지

화면을 구현하는 HTML 파일의 모음 (Restful의 경우 사용안함)

### Controller 패키지

클라이언트의 요청을 처리하고 응답을 전송하는 클래스들의 모음

route에 의해 URL로 노출되는 부분이라고 생각할 수 있다.