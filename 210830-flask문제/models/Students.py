"""
@filename    : Student.py
@description : Student 테이블 Model 클래스 구현
@author      : 천준홍 (cj562270@gmail.com)
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

# 클래스 선언시 괄호 안에 들어 가는 내용은 해당 기능을 그대로 상속 받겠다는 의미
class Student(db.Model, SerializerMixin):
    __tablename__ = 'student'
    studno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    userid = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    idnum = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)
    tel = db.Column(db.String, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    deptno = db.Column(db.Integer, nullable=False)
    profno = db.Column(db.Integer, nullable=True)
    
    # 자동증가를 제외한 항목들을 파라미터로 받아서 멤버변수에 맵핑
    def __init__(self, name, userid, grade, idnum, birthdate, tel, height, weight, deptno, profno):
        self.name = name
        self.userid = userid
        self.grade = grade
        self.idnum = idnum
        self.birthdate = birthdate
        self.tel = tel
        self.height = height
        self.weight = weight
        self.deptno = deptno
        self.profno = profno