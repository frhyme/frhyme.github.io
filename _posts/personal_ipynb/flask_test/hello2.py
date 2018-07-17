from flask import Flask, render_template, make_response, send_file

from functools import wraps, update_wrapper
from datetime import datetime

import numpy as np 

from io import BytesIO, StringIO
# 아래 부분을 세팅해줘야 맥

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, mpld3

app = Flask(__name__, static_url_path='/static')
 
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

from functools import wraps, update_wrapper
from datetime import datetime

def nocache(view):
  @wraps(view)
  def no_cache(*args, **kwargs):
    response = make_response(view(*args, **kwargs))
    response.headers['Last-Modified'] = datetime.now()
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response      
  return update_wrapper(no_cache, view)

@app.route('/images/<img1>')
@nocache
def images(img1):
  return render_template("images.html", title="img_{}".format(img1), 
  width=800, height=200)

## 그림 url 
@app.route('/fig/<img1>')
@nocache
def fig(img1):
  plt.figure(figsize=(8, 2))
  xs = np.random.normal(0, 1, 100)
  ys = np.random.normal(0, 1, 100)
  plt.scatter(xs, ys, s=200, alpha=0.3)
  
  img = BytesIO()
  plt.savefig(img, dpi=200)
  img.seek(0)
  plt.close()
  return send_file(img, mimetype='image/png')

@app.route('/normal/<m_v>')
@nocache
def normal(m_v):
  m, v = m_v.split("_")
  m, v = int(m), int(v)
  return render_template("random_gen.html", mean=m, var=v, width=800, height=600)

@app.route('/random_fig/<m_v>')
@nocache
def random_fig(m_v):
  m, v = m_v.split("_")
  m, v = int(m), int(v)

  plt.figure(figsize=(4, 3))
  xs = np.random.normal(m, v, 100)
  ys = np.random.normal(m, v, 100)
  plt.scatter(xs, ys, s=100, alpha=0.2, marker='h', color='red')
  plt.title('normal dist, m: {}, v: {}'.format(m, v))
  
  img = BytesIO()
  plt.savefig(img, dpi=500)
  plt.close()
  img.seek(0)
  
  return send_file(img, mimetype='image/png')

@app.route('/random_fig1/<m_v>')
@nocache
def random_fig1(m_v):
  m, v = m_v.split("_")
  m, v = int(m), int(v)

  plt.figure(figsize=(8, 6))
  xs = np.random.normal(m, v, 1000)
  ys = np.random.normal(m, v, 1000)
  plt.scatter(xs, ys, s=100, alpha=0.2, marker='h', color='blue')
  plt.title('normal dist, m: {}, v: {}'.format(m, v))
  
  img = BytesIO()
  plt.savefig(img, dpi=200)
  img.seek(0)
  
  return send_file(img, mimetype='image/png')
#######################
if __name__ == '__main__':
  app.run(debug=True)