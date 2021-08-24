# 패키지 참조
from flask import Flask, request, render_template
from pandas import read_excel
from pandas import DataFrame
from pandas import merge
from statsmodels.formula.api import logit
import numpy as np

# Flask 메인 객체 생성
# -> __name__ 은 이 소스파일의 이름
app = Flask(__name__)

# get 파라미터 수신 하기 -> methods를 지정하지 않으면 기본값은 GET
@app.route("/gradeuate", methods=['GET'])
def get():
    df = read_excel('http://itpaper.co.kr/data/gradeuate.xlsx', engine='openpyxl')
    model = logit('합격여부 ~ 필기점수+학부성적+병원경력', data=df)
    fit = model.fit()
    pred2 = fit.predict(df)
    pdf = DataFrame(pred2, columns=['추정치'])
    pdf['합격확률(%)'] = round(pdf['추정치']*100, 1)
    pdf['예상결과'] = np.where(pdf['추정치'] > 0.5, "합격", "불합격")
    result_df = merge(df, pdf, left_index=True, right_index=True)
    return result_df.to_json(orient='records')

@app.route('/page', methods=['GET'])
def page():
    return render_template('page.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9901, debug=True)