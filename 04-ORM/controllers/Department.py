from flask import request
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from models.Department import Department as departmentModel
import json
from utils.Util import replace_quotes
from utils.Util import get_now_string

db = SQLAlchemy()

# JSON 페이지를 담당하는 클래스
class Department(Resource):
    def get(self):
        # 조회 결과를 저장할 빈 변수
        rs = None
        
        try:
            # 전체 데이터 조회
            rs = departmentModel.query.all()
        except Exception as e:
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        # 전체 조회 결과가 리스트이고, 리스트의 각 원소가 departmentModel의 객체 타입이므로
        # JSON 출력을 위해 각 원소를 dict로 변환
        for i,v in enumerate(rs):
            rs[i] = v.to_dict()
        
        return {'rt': 'OK', 'item': rs, 'pubDate': get_now_string()}
    
    def post(self):
        # 저장할 값을 post 파라미터로 수신
        dname = request.form.get('dname')
        loc = request.form.get('loc')
        
        # 수신된 값을 model 객체로 묶는다.
        item = departmentModel(dname=dname, loc=loc)
        
        try:
            # 저장 (insert)
            db.session.add(item)
            # 변경사항 반영
            db.session.commit()
        except Exception as e:
            # 에러가 났다면 변경사항 되돌리기
            db.session.rollback()
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        return {'rt': 'OK', 'pubDate': get_now_string()}, 200
    
    def put(self):
        deptno = request.form.get('deptno')
        dname = request.form.get('dname')
        loc = request.form.get('loc')
        
        try:
            # query(테이블을 의미하는 모델)
            # filter(WHERE절 조건)
            # update({컬럼: 값...})
            db.session.query(departmentModel).filter(departmentModel.deptno==deptno).update({'dname': dname, 'loc': loc})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        return {'rt': 'OK', 'pubDate': get_now_string()}, 200
    
    def delete(self):
        deptno = request.form.get('deptno')
        
        try:
            db.session.query(departmentModel).filter(departmentModel.deptno==deptno).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        return {'rt': 'OK', 'pubDate': get_now_string()}, 200