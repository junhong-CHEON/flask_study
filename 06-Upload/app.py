# package import
import os
import sys
from flask import Flask, render_template, request, send_from_directory
# pip3 install --upgrade werkzeug
from werkzeug.utils import secure_filename

# registration modul path
root_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_path)

# Flask object create
app = Flask(__name__)

# upload된 파일이 저장될 폴더 위치
app.config['UPLOAD_FOLDER'] = os.path.join(root_path, 'upload')

@app.route('/upload/send', methods=['GET'])
def page():
    return render_template('send.html')

# 업로드 된 파일을 받아서 flask 프로그램 내의 upload 라는 폴더에 저장하는 함수
# upload를 받기 위해서는 GET방식은 사용할 수 없다.
@app.route('/upload/save', methods=['POST'])
def save():
    # 파일 수신 받기
    # -> <input type='file' name='myphoto'> 라는 필드로 파일이 전송되어야 함.
    f = request.files['myphoto']
    # 업로드 된 파일의 이름 받기
    filename = secure_filename(f.filename)
    # 설정된 폴더 안에 업로드 된 파일 저장
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    return filename

# 주소를 라우팅할 때 <이름> 형식의 항목은 그 위치의 단어를 함수에게 파라미터로 전달함.
# 이 때 파라미텅 이름은 괄호안에 명시한 이름이 된다.
@app.route('/upload/<filename>', methods=['GET'])
def file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# application activate
if __name__ == "__main__":
    app.run(host='192.168.0.9', port=9901, debug=True)