from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
db = SQLAlchemy()

# 클래스 선언시 괄호 안에 들어 가는 내용은 해당 기능을 그대로 상속 받겠다는 의미
class Members(db.Model, SerializerMixin):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String, nullable=False)
    user_pw = db.Column(db.String, nullable=False)
    user_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    gender = db.Column(db.Enum('M','F'), nullable=False)
    postcode = db.Column(db.String, nullable=False)
    addr1 = db.Column(db.String, nullable=False)
    addr2 = db.Column(db.String, nullable=False)
    photo = db.Column(db.LargeBinary, nullable=True)
    is_out = db.Column(db.Enum('Y','N'), nullable=False)
    is_admin = db.Column(db.Enum('Y','N'), nullable=False)
    login_date = db.Column(db.DateTime, nullable=True)
    reg_date = db.Column(db.DateTime, nullable=False)
    edit_date = db.Column(db.DateTime, nullable=False)

    
    # 자동증가를 제외한 항목들을 파라미터로 받아서 멤버변수에 맵핑

    def __init__(self, id, user_id, user_pw, user_name, email, phone, birthday, gender, postcode, addr1, addr2,
                photo, is_out, is_admin, login_date, reg_date, edit_date):
        self.id = id
        self.user_id = user_id
        self.user_pw = user_pw
        self.user_name = user_name
        self.email = email
        self.phone = phone
        self.birthday = birthday
        self.gender = gender
        self.postcode = postcode
        self.addr1 = addr1
        self.addr2 = addr2
        self.photo = photo
        self.is_out = is_out
        self.is_admin = is_admin
        self.login_date = login_date
        self.reg_date = reg_date
        self.edit_date = edit_date