from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# 클래스 선언시 괄호 안에 들어 가는 내용은 해당 기능을 그대로 상속 받겠다는 의미
class Department(db.Model, SerializerMixin):
    __tablename__ = 'department'
    deptno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dname = db.Column(db.String, nullable=False)
    loc = db.Column(db.String, nullable=True)
    
    # 자동증가를 제외한 항목들을 파라미터로 받아서 멤버변수에 맵핑
    def __init__(self, dname, loc):
        self.dname = dname
        self.loc = loc