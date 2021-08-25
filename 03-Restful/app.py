# 패키지 참조
import os
import sys
from flask import Flask
from flask_restful import Resource, Api

# 다른 폴더안의 파일들까지 import할 수 있도록 path 등록
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# controller 클래스 참조
from controllers.Department import Department as DepartmentController
from controllers.Professor import Professor as ProfessorController

# Flask 메인 객체 생성
app = Flask(__name__)
api = Api(app)

# Class를 /my_restful 이라는 URL로 등록
# 기본적으로 get, post, put, delete라는 메서드는 자동으로 각 접속 방식에 맞게 적용됨
api.add_resource(DepartmentController, '/department')

# 접속방식에 따라 URL 다르게 설정하기
# -> endpoint는 url의 마지막 경로명
api.add_resource(ProfessorController, '/professor/hello', endpoint='hello', methods=['GET'])
api.add_resource(ProfessorController, '/professor/world', endpoint='world', methods=['POST'])
api.add_resource(ProfessorController, '/professor/foo', endpoint='foo', methods=['PUT'])
api.add_resource(ProfessorController, '/professor/bar', endpoint='bar', methods=['DELETE'])

# 프로그램 가동
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9901, debug=True)