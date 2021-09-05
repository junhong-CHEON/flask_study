from sys import getwindowsversion
from flask import request
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from models.Members import Members as membersModel
import json
from utils.Util import replace_quotes
from utils.Util import get_now_string
from utils.Regex import Regex
from sqlalchemy import and_
from pandas import DataFrame
from werkzeug.security import check_password_hash,generate_password_hash
from numpyencoder import NumpyEncoder


db = SQLAlchemy()
regex = Regex()

# JSON 페이지를 담당하는 클래스
class Members(Resource):
    def get(self):
        # 조회 결과를 저장할 빈 변수
        rs = None
        user_id = request.args.get('user_id')
        user_pw = request.args.get('user_pw')       
        login_date = get_now_string()

        # 쿼리를 통해 아이디 조회
        try:
            rs = membersModel.query.filter(membersModel.user_id == user_id).all()
        except Exception as e:
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        

        # 아이디 리스트를 데이터 프레임으로 만들기 위해 dict로 변환 후 DataFrame으로 변환
        for i,v in enumerate(rs):
            rs[i] = v.to_dict()
        df = DataFrame(rs)

        # 데이터 프레임의 user_pw 컬럼과 쿼리의 user_pw를 check_password_hash함수를 이용해 암호화된 비밀번호와 맞는지 확인
        # Series객체를 dict로 변환했을때 int64 자료형을 json은 인식하지 못하기 때문에 dict로 변환 후 json으로 변환(NumpyEncoder 함수를 통해 강제 형변환)
        # 여기서 변환된 json을 출력하면 출력이 깔끔하지 않게나옴
        for i,v in enumerate(df['user_pw']):
            if(check_password_hash(v, user_pw)):
                result = json.dumps(df.loc[i].to_dict(),cls= NumpyEncoder)
                break
        
        # 깔끔한 출력을 위해 json -> dict로 재변환(이때 dict의 자료형은 json으로 변환 가능한 자료형으로 바뀜)
        result = json.loads(result)

        # is_out == 'Y' 라면, 탈퇴한 회원
        if (result['is_out'] == 'Y'):
            result = None
        # 로그인 날짜를 변경
        try:
            db.session.query(membersModel).filter(membersModel.user_id==user_id).update({'login_date':login_date})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500

        return {'rt': 'OK', 'item': result, 'pubDate': get_now_string()}
    
    def post(self):
        # 저장할 값을 post 파라미터로 수신
        id = request.form.get('id')
        user_id = request.form.get('user_id')
        user_pw = generate_password_hash(request.form.get('user_pw'))
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        birthday = request.form.get('birthday')
        gender = request.form.get('gender')
        postcode = request.form.get('postcode')
        addr1 = request.form.get('addr1')
        addr2 = request.form.get('addr2')
        photo = request.form.get('photo')
        is_out = 'N'
        is_admin = 'N'
        login_date = request.form.get('login_date')
        reg_date = get_now_string()
        edit_date = get_now_string()
        
        # 수신된 값을 model 객체로 묶는다.
        item = membersModel(id = id,user_id = user_id, user_pw = user_pw, user_name = user_name, email = email, phone = phone, birthday = birthday, gender = gender, postcode = postcode, addr1 = addr1, addr2 = addr2, photo = photo, is_out = is_out, is_admin = is_admin, login_date = login_date, reg_date = reg_date, edit_date = edit_date)
        
        try:
            # 저장 (insert)
            db.session.add(item)
            # 변경사항 반영
            db.session.commit()
        except Exception as e:
            # 에러가 났다면 변경사항 되돌리기
            db.session.rollback()
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        print(item.to_dict())
        return {'rt': 'OK','new_user':item.to_dict(), 'pubDate': get_now_string()}, 200
    
    def put(self):
        id = request.form.get('id')
        user_id = request.form.get('user_id')
        user_pw = generate_password_hash(request.form.get('user_pw'))
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        birthday = request.form.get('birthday')
        gender = request.form.get('gender')
        postcode = request.form.get('postcode')
        addr1 = request.form.get('addr1')
        addr2 = request.form.get('addr2')
        photo = request.form.get('photo')
        edit_date = get_now_string()
        
    
        try:
            # query(테이블을 의미하는 모델)
            # filter(WHERE절 조건)
            # update({컬럼: 값...})
            db.session.query(membersModel).filter(membersModel.id==id).update({'user_id': user_id, 'user_pw': user_pw, 'user_name': user_name,
            'email': email, 'phone': phone, 'birthday': birthday,'gender':gender,'postcode':postcode,'addr1':addr1,'addr2':addr2,'photo':photo,'edit_date':edit_date})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        # 바뀐 정보
        try:
            item = membersModel.query.filter(membersModel.id == id).all()
        except Exception as e:
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500

        result = json.dumps(item[0].to_dict(),cls= NumpyEncoder)
        result = json.loads(result)
        return {'rt': 'OK', 'edit_user': result,'pubDate': get_now_string()}, 200
        
    def delete(self):
        id = request.form.get('id')
        is_out = 'Y'
        edit_date = get_now_string()

        try:
            db.session.query(membersModel).filter(membersModel.id == id).update({'is_out': is_out, 'edit_date': edit_date})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        # 바뀐 정보
        try:
            item = membersModel.query.filter(membersModel.id == id).all()
        except Exception as e:
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500

        result = json.dumps(item[0].to_dict(),cls= NumpyEncoder)
        result = json.loads(result)

        return {'rt': 'OK', 'out_user': result,'pubDate': get_now_string()}, 200