# package import
import os
import sys
from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# registration modul path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# controller class import
from controllers.Department import Department as DepartmentController

# Flask object create
app = Flask(__name__)

# database object create
# "mysql+pymysql://아이디:비밀번호@주소:포트번호/DB이름"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost:3306/myschool"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# restful object create
api = Api(app)

# controller url mapping
api.add_resource(DepartmentController, '/department')

# application activate
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9901, debug=True)