from flask import request
from flask_restful import Resource
import json
from pandas import read_excel
from pandas import DataFrame
from utils.Util import get_now_string

# JSON 페이지를 담당하는 클래스
class Titanic(Resource):
    def get(self):
        # 데이터 불러오기
        df = read_excel("http://itpaper.co.kr/data/titanic.xlsx", engine='openpyxl')
        
        # 결측치 삭제
        if 'Cabin' in df.columns:
            df.drop('Cabin', axis=1, inplace=True)
        
        # 탑승지의 경우 결측치를 최빈값으로 대체
        most_frequent = df['Embarked'].mode()
        df['Embarked'].fillna(most_frequent[0], inplace=True)
        
        # 나이의 경우 결측치를 중앙값으로 대체
        df['Age'].fillna(df['Age'].median(), inplace=True)
        
        # 승객 일련번호는 인덱스 설정
        if 'PassengerId' in df.columns:
            df.set_index('PassengerId', inplace=True)
        
        # 선실 등급별 탑승자 수
        pclass_total_df = df.filter(['Pclass', 'Survived']).groupby('Pclass').count()
        
        # 각 선실별 생존자 수
        pclass_surv_df = df.filter(['Pclass', 'Survived']).query('Survived==1').groupby('Pclass').count()
        
        # 각 선실별 생존자 비율
        ratio = DataFrame((pclass_surv_df['Survived'] / pclass_total_df['Survived']) * 100)
        
        output = {
            'rt': 'OK', 
            'item': json.loads(df.to_json(orient='table')), 
            'describe': json.loads(df.describe().to_json(orient='table')),
            'surv_ratio': json.loads(ratio.to_json(orient='table')),
            'pub_date': get_now_string()
        }
        return output