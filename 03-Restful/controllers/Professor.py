from flask_restful import Resource

class Professor(Resource):
    def get(self):
        # 출력 결과는 json 형식으로 구성되어야 함
        return {'msg': "Professor::get 방식으로 접속함"}
    
    def post(self):
        return {'msg': "Professor::post 방식으로 접속함"}
    
    def put(self):
        return {'msg': "Professor::put 방식으로 접속함"}
    
    def delete(self):
        return {'msg': "Professor::delete 방식으로 접속함"}