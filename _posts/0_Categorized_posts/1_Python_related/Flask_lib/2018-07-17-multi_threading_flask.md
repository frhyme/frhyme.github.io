---
title: flask에서 multi-threading 세팅하기 
category: python-lib
tags: python python-lib matplotlib flask multi-threading 
---

## flask 서버에 multi-threading 세팅하기 

- flask를 서버로 사용하면서, html 페이지에 여러 개의 matplotlib의 figure를 embed하고 싶었습니다. 
- 다음과 같은 html template가 있을 경우 mean, var를 다르게 한 다양한 그림을 한 웹페이지 안에 보여주게 하고 싶은 것이죠. 

```html
{% raw %}
<html>
  <head>
    <title>random normal - {{mean}}, {{var}} </title>
  </head>
  <body>
    <h2>This is random normal image</h2>
    <h3>this is h3 </h3>
    <p>this is the paragraph</p>
      <img src="{{ url_for('fig', mean=5, var=3) }}" alt="Image Placeholder" 
      width={{width}}, height={{height}}>
    <p>this is the paragraph</p>
      <img src="{{ url_for('fig', mean=100, var=5) }}" alt="Image Placeholder" 
      width={{width}}, height={{height}}>
  </body>
</html>
{% endraw %}
```

## 그러나.

- 이상하게 저게 잘 안됩니다. 그림이 여러 개 있다면 단지 하나만 출력되고 나머지 하나는 출력되지 않아요. 
- 서로 다른 img 태그 내에서 콜하는 컴포넌트 코드는 대략 다음과 같습니다. 이 코드 상의 문제는 없을 것 같고요. 
- 안되는 이유는 해당 component에서 multiple-threading이 지원되지 않기 때문인 것이 아닐까? 싶었습니다. 

```python
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
```

## 그래서 

- 단순하게 맨 밑에 아래 코드를 넣어주니까 분명해졌습니다. 
- 단, 아직 이유는 모르겠지만 '새로고침'으로는 여전히 특정 이미지 파일에서 잘 읽히지 않네요. 

```python
if __name__ == '__main__':
    ## threaded=True 로 넘기면 multiple plot이 가능해짐
    ## host='0.0.0.0', port=5000 을 함께 넘기면 서버 내부의 0.0.0.0의 주소에 5000포트에서 프로그램이 실행됨
  app.run(debug=True, threaded=True)
```


## reference 

- https://medium.com/@dkhd/handling-multiple-requests-on-flask-60208eacc154
- https://stackoverflow.com/questions/14672753/handling-multiple-requests-in-flask

## raw code

### hello3.py

```python
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
```

### random_gen.html 

```html
{% raw %}
<html>
  <head>
    <title>random normal - {{mean}}, {{var}} </title>
  </head>
  <body>
    <h2>This is random normal image</h2>
    <h3>this is h3 </h3>
    <p>this is the paragraph</p>
      <img src="{{ url_for('fig', mean=5, var=3) }}" alt="Image Placeholder" 
      width={{width}}, height={{height}}>
    <p>this is the paragraph</p>
      <img src="{{ url_for('fig', mean=100, var=5) }}" alt="Image Placeholder" 
      width={{width}}, height={{height}}>
    <p>this is the paragraph</p>
      <img src="{{ url_for('fig', mean=100, var=5) }}" alt="Image Placeholder" 
      width={{width}}, height={{height}}>
  </body>
</html>
{% endraw %}
```