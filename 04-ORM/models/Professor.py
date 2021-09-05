from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from models.Department import Department

db = SQLAlchemy()

# 클래스 선언시 괄호 안에 들어 가는 내용은 해당 기능을 그대로 상속 받겠다는 의미
class Professor(db.Model, SerializerMixin):
    __tablename__ = 'professor'
    profno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    userid = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    sal = db.Column(db.Integer, nullable=False)
    hiredate = db.Column(db.DateTime, nullable=False)
    comm = db.Column(db.Integer, nullable=True)
    deptno = db.Column(db.Integer, nullable=False)

    
    # 자동증가를 제외한 항목들을 파라미터로 받아서 멤버변수에 맵핑
    def __init__(self, name, userid, position, sal, hiredate, comm, deptno):
        self.name = name
        self.userid = userid
        self.position = position
        self.sal = sal
        self.hiredate = hiredate
        self.comm = comm
        self.deptno = deptno