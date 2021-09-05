"""
@filename    : Student.py
@description : Student 테이블 Controller 구현 
@author      : 천준홍 (cj562270@gmail.com)
"""
from flask import request
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from models.Students import Student as studentModel
import json
from utils.Util import replace_quotes
from utils.Util import get_now_string

db = SQLAlchemy()

# JSON 페이지를 담당하는 클래스
class Student(Resource):
    def get(self):
        # 조회 결과를 저장할 빈 변수
        rs = None
        name = request.args.get('name')
        pk = request.args.get('pk')

        # 문제 3번(검색어 목록 조회)
        if(pk == None):
            if(name == None):
                name = ''
            search = "%{}%".format(name)
            try:
                # like를 이용하여 파라미터가 포함된 이름을 찾고 원하는 컬럼만 select
                rs = studentModel.query.filter(studentModel.name.like(search)).with_entities(studentModel.name, studentModel.grade, studentModel.deptno, studentModel.userid).all()
            except Exception as e:
                return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
            
            # select 결과를 json으로 내보내기 위해 dictionary로 변환
            dic = []
            for i,v in enumerate(rs):
                dic.append({'name': v[0] ,'grade' : v[1] ,'deptno': v[2] ,'userid': v[3]})
            
            return {'rt': 'OK', 'item': dic, 'pubDate': get_now_string()}

        # 문제 4번 (pk 파라미터 입력 상세조회)
        else:
            try:
                rs = studentModel.query.filter(studentModel.studno == pk).all()
            # query 오류시 메세지 출력
            except Exception as e:
                return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
            
            # 존재하지 않는 pk값을 입력했을떄 오류메세지 출력
            if (len(rs) == 0):
                return '해당 pk값을 데이터베이스에서 찾을 수 없습니다.'
            dic = rs[0].to_dict()

            return {'rt': 'OK', 'item': dic, 'pubDate': get_now_string()}

    # 문제 5
    def post(self):
        # 저장할 값을 post 파라미터로 수신
        name = request.form.get('name')
        userid = request.form.get('userid')
        grade = request.form.get('grade')
        idnum = request.form.get('idnum')
        birthdate = request.form.get('birthdate')
        tel = request.form.get('tel')
        height = request.form.get('height')
        weight = request.form.get('weight')
        deptno = request.form.get('deptno')
        profno = request.form.get('profno')
        
        # 수신된 값을 model 객체로 묶는다.
        item = studentModel(name=name, userid=userid,grade=grade, idnum=idnum, birthdate=birthdate, tel=tel, height=height, weight=weight, deptno=deptno, profno=profno)
        
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
    
    # 문제 6
    def put(self):
        studno = request.form.get('studno')
        name = request.form.get('name')
        userid = request.form.get('userid')
        grade = request.form.get('grade')
        idnum = request.form.get('idnum')
        birthdate = request.form.get('birthdate')
        tel = request.form.get('tel')
        height = request.form.get('height')
        weight = request.form.get('weight')
        deptno = request.form.get('deptno')
        profno = request.form.get('profno')
        
        # 입력받은 파라미터만 dictionary로 구성(원하는 파라미터만 변경하기 위함)
        param_list = [name, userid, grade, idnum, birthdate, tel, height, weight, deptno, profno]
        param_str = ['name','userid','grade','idnum','birthdate','tel','height','weight','deptno','profno']
        dic = {}
        for i,v in enumerate(param_list):
            if (v == None):
                continue
            dic[param_str[i]] = v

        # 존재하지 않는 studno(pk) 값 입력시 에러메세지 출력
        try:
            rs = studentModel.query.filter(studentModel.studno == studno).all()
        except Exception as e:
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        if (len(rs) == 0):
            return '해당 pk값을 데이터베이스에서 찾을 수 없습니다.'

        # 생성한 dictionary를 이용하여 update수행
        try:
            db.session.query(studentModel).filter(studentModel.studno==studno).update(dic)
            db.session.commit()
        # 에러 처리
        except Exception as e:
            db.session.rollback()
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        return {'rt': 'OK', 'pubDate': get_now_string()}, 200
    
    # 문제 7
    def delete(self):
        studno = request.form.get('studno')
        
        # 존재하지 않는 studno(pk)를 입력시 에러메세지 출력
        try:
            rs = studentModel.query.filter(studentModel.studno == studno).all()
        except Exception as e:
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        if (len(rs) == 0):
            return '해당 pk값을 데이터베이스에서 찾을 수 없습니다.'

        # pk값을 기준으로 delete수행
        try:
            db.session.query(studentModel).filter(studentModel.studno==studno).delete()
            db.session.commit()
        # 에러 처리
        except Exception as e:
            db.session.rollback()
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        return {'rt': 'OK', 'pubDate': get_now_string()}, 200