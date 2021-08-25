# package import
import os
import sys
from flask import Flask, render_template
from flask_restful import Resource, Api

# registration modul path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# controller class import
from controllers.Titanic import Titanic as TitanicController

# Flask object create
app = Flask(__name__)

# restful object create
api = Api(app)

# controller url mapping
api.add_resource(TitanicController, '/titanic')

@app.route('/titanic/my_webpage_test', methods=['GET'])
def page():
    return render_template('page.html')

# application activate
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9901, debug=True)