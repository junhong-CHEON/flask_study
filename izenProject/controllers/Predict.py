from flask import Response,request,render_template
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from models.Predict import Predict as predictModel
import json
from utils.Util import replace_quotes
from utils.Util import get_now_string

db = SQLAlchemy()

# JSON 페이지를 담당하는 클래스
class Predict(Resource):
    def get(self):
        # 조회 결과를 저장할 빈 변수
        rs = None
        
        try:
            # 전체 데이터 조회
            rs = predictModel.query.limit(5).all()
        except Exception as e:
            return {'rt': replace_quotes(str(e)), 'pubDate': get_now_string()}, 500
        
        # 전체 조회 결과가 리스트이고, 리스트의 각 원소가 departmentModel의 객체 타입이므로
        # JSON 출력을 위해 각 원소를 dict로 변환
        for i,v in enumerate(rs):
            rs[i] = v.to_dict()
        
        return {'rt': 'OK', 'item': rs, 'pubDate': get_now_string()}

    def post(self):
            value_1 = request.form['gu']
            value_2 = request.form['search']
            value = str(value_1) + ' ' + str(value_2)
            print(value)
            return Response(render_template('index.html', value = value))