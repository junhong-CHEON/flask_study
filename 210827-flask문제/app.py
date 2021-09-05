# package import
import os
import sys
from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# registration modul path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# controller class import
from controllers.Members import Members as MembersController

# Flask object create
app = Flask(__name__)

# database object create
# "mysql+pymysql://아이디:비밀번호@주소:포트번호/DB이름"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost:3306/helloshop"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# restful object create
api = Api(app)

@app.route('/', methods=['GET'])
def page():
    return render_template('page.html')
# controller url mapping
api.add_resource(MembersController, '/addMemberinfo', endpoint='addMemberinfo', methods=['POST'])
api.add_resource(MembersController, '/editMemberinfo', endpoint='editMemberinfo', methods=['PUT'])
api.add_resource(MembersController, '/doOut', endpoint='doOut', methods=['DELETE'])
api.add_resource(MembersController, '/doLogin', endpoint='doLogin', methods=['GET'])
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9901, debug=True)