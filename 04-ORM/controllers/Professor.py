from flask import request
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from models.Professor import Professor as professorModel
import json
from utils.Util import replace_quotes
from utils.Util import get_now_string

db = SQLAlchemy()

# JSON 페이지를 담당하는 클래스
class Professor(Resource):
    def get(self):
        # 조회 결과를 저장할 빈 변수
        rs = None
        
        try:
            # 전체 데이터 조회
            rs = professorModel.query.all()
        except Exception as e:
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        # 전체 조회 결과가 리스트이고, 리스트의 각 원소가 departmentModel의 객체 타입이므로
        # JSON 출력을 위해 각 원소를 dict로 변환
        for i,v in enumerate(rs):
            rs[i] = v.to_dict()
        
        return {'rt': 'OK', 'item': rs, 'pubDate': get_now_string()}
    
    def post(self):
        # 저장할 값을 post 파라미터로 수신
        name = request.form.get('name')
        userid = request.form.get('userid')
        position = request.form.get('position')
        sal = request.form.get('sal')
        hiredate = request.form.get('hiredate')
        comm = request.form.get('comm')
        deptno = request.form.get('deptno')
        
        # 수신된 값을 model 객체로 묶는다.
        item = professorModel(name=name, userid=userid, position=position, sal=sal, hiredate=hiredate, comm=comm, deptno=deptno)
        
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
        profno = request.form.get('profno')
        name = request.form.get('name')
        userid = request.form.get('userid')
        position = request.form.get('position')
        sal = request.form.get('sal')
        hiredate = request.form.get('hiredate')
        comm = request.form.get('comm')
        deptno = request.form.get('deptno')
        
        try:
            # query(테이블을 의미하는 모델)
            # filter(WHERE절 조건)
            # update({컬럼: 값...})
            db.session.query(professorModel).filter(professorModel.profno==profno).update({'name': name, 'userid': userid, 'position': position,
            'sal': sal, 'hiredate': hiredate, 'comm': comm,'deptno':deptno})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        return {'rt': 'OK', 'pubDate': get_now_string()}, 200
    
    def delete(self):
        profno = request.form.get('profno')
        
        try:
            db.session.query(professorModel).filter(professorModel.profno==profno).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        return {'rt': 'OK', 'pubDate': get_now_string()}, 200