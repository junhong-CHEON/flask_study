from flask import request
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from models.Department import Department as departmentModel
import json
from utils.Util import replace_quotes
from utils.Util import get_now_string
from utils.Regex import Regex

db = SQLAlchemy()
regex = Regex()

# JSON 페이지를 담당하는 클래스
class Department(Resource):
    def get(self):
        q = request.args.get('q')
        page = request.args.get('page')
        size = request.args.get('size')
        
        try:
            regex.value(page)
        except Exception as e:
            page = 1
        
        try:
            regex.value(size)
        except Exception as e:
            size = 20
            
        try:
            regex.num(page, '페이지 번호는 숫자만 가능합니다.')
            regex.num(size, '한 페이지당 검색수는 숫자만 가능합니다.')
            regex.between(size, 1, 30, '검색수는 1~30사이만 설정 가능합니다.')
        except Exception as e:
            return {'rt': str(e), 'pubDate': get_now_string()}, 400
        
        page = int(page)
        size = int(size)
        
        # 전체 게시물 수
        total_count = 0
        
        try:
            # 전체 데이터 조회
            step1 = db.session.query(departmentModel)
            
            if q:
                search = "%{query}%".format(query=q)
                step1 = step1.filter(departmentModel.dname.like(search))
            
            total_count = step1.count()
        except Exception as e:
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        
        # 전체 페이지 수
        total_page = ((total_count-1) // size) + 1
        
        # 파라미터로 전달된 page 번호를 보정
        if page > total_page:
            page = total_page
        
        # SQL의 limit절에서 사용할 시작위치값
        offset = (page - 1) * size
        
        # 조회 결과를 저장할 빈 변수
        rs = None
        
        try:
            # 전체 데이터 조회
            step1 = db.session.query(departmentModel)
            
            if q:
                search = "%{query}%".format(query=q)
                step1 = step1.filter(departmentModel.dname.like(search))
            
            # 페이지 구현 적용
            step2 = step1.offset(offset).limit(size)
            rs = step2.all()
        except Exception as e:
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        # 전체 조회 결과가 리스트이고, 리스트의 각 원소가 departmentModel의 객체 타입이므로
        # JSON 출력을 위해 각 원소를 dict로 변환
        for i,v in enumerate(rs):
            rs[i] = v.to_dict()
        
        return {'rt': 'OK', 'total_count': total_count, 'total_page': total_page, 'item': rs, 'pubDate': get_now_string()}
    
    def post(self):
        # 저장할 값을 post 파라미터로 수신
        dname = request.form.get('dname')
        loc = request.form.get('loc')
        
        # 입력값에 대한 유효성 검사
        try:
            regex.value(dname, "학과이름이 없습니다.")
            regex.kor(dname, "학과이름은 한글만 입력 가능합니다.")
            regex.min_length(dname, 4, "학과이름은 4~15자 까지만 입력 가능합니다.")
            regex.max_length(dname, 15, "학과이름은 4~15자 까지만 입력 가능합니다.")
        except Exception as e:
            return {'rt': str(e), 'pubDate': get_now_string()}, 400
        
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
        
        # 입력값에 대한 유효성 검사
        try:
            regex.value(deptno, "학과번호가 없습니다.")
            regex.num(deptno, "학과번호는 숫자만 입력 가능합니다.")
            
            regex.value(dname, "학과이름이 없습니다.")
            regex.kor(dname, "학과이름은 한글만 입력 가능합니다.")
            regex.min_length(dname, 4, "학과이름은 4~15자 까지만 입력 가능합니다.")
            regex.max_length(dname, 15, "학과이름은 4~15자 까지만 입력 가능합니다.")
        except Exception as e:
            return {'rt': str(e), 'pubDate': get_now_string()}, 400
        
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
        
        # 입력값에 대한 유효성 검사
        try:
            regex.value(deptno, "학과번호가 없습니다.")
            regex.num(deptno, "학과번호는 숫자만 입력 가능합니다.")
        except Exception as e:
            return {'rt': str(e), 'pubDate': get_now_string()}, 400
        
        try:
            db.session.query(departmentModel).filter(departmentModel.deptno==deptno).delete()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        return {'rt': 'OK', 'pubDate': get_now_string()}, 200