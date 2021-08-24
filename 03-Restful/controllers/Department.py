from flask_restful import Resource

# JSON 페이지를 담당하는 클래스
class Department(Resource):
    def get(self):
        # 출력 결과는 json 형식으로 구성되어야 함
        return {'msg': "Department::get 방식으로 접속함"}
    
    def post(self):
        return {'msg': "Department::post 방식으로 접속함"}
    
    def put(self):
        return {'msg': "Department::put 방식으로 접속함"}
    
    def delete(self):
        return {'msg': "Department::delete 방식으로 접속함"}