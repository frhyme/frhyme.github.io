from flask import Flask, send_file, render_template, make_response

from io import BytesIO
import numpy as np 

## macOS의 경우 아래 순서에 따라서 library를 import해줘야 에러없이 잘 됩니다. 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#################

## remove cache 
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
###############

app = Flask(__name__, static_url_path='/static', )

@app.route('/normal/<m_v>')
@nocache
def normal(m_v):
  m, v = m_v.split("_")
  m, v = int(m), int(v)
  return render_template("random_gen.html", mean=m, var=v, width=400, height=300)


@app.route('/fig/<int:mean>_<int:var>')
@nocache
def fig(mean, var):
  plt.figure(figsize=(4, 3))
  xs = np.random.normal(mean, var, 100)
  ys = np.random.normal(mean, var, 100)
  plt.scatter(xs, ys, s=100, marker='h', color='red', alpha=0.3)
  """
  file로 저장하는 것이 아니라 binary object에 저장해서 그대로 file을 넘겨준다고 생각하면 됨
  """
  img = BytesIO()
  plt.savefig(img, format='png', dpi=300)
  img.seek(0)## object를 읽었기 때문에 처음으로 돌아가줌
  return send_file(img, mimetype='image/png')
  # plt.savefig(img, format='svg')
  # return send_file(img, mimetype='image/svg')

#################
if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(debug=True, threaded=True)