

from flask import Flask, render_template, make_response, send_file

import numpy as np 

from io import BytesIO, StringIO
# 아래 부분을 세팅해줘야 맥
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 


app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/user')
def user():
  return render_template('user.html')
"""
- img 연결하기
- 단 캐쉬를 어떻게 없애야 하는지는 추가 보완이 필요함
- 지금은 동일한 url인 경우 지난번에 떴던 그림이 그대로 뜸
"""
@app.route('/images/<img1>')
def images(img1):
  return render_template("images.html", title=img1)

@app.route('/fig/<img1>')
def fig(img1):
  plt.figure()
  xs = np.random.normal(0, 1, 100)
  ys = np.random.normal(0, 1, 100)
  plt.scatter(xs, ys)
  
  img = BytesIO()
  plt.savefig(img)
  img.seek(0)
  
  return send_file(img, mimetype='image/png')

if __name__ == '__main__':
  app.run(debug=True)