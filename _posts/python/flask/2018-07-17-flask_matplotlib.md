---
title: matplotlib와 flask 연결하기 
category: python-lib
tags: python python-lib flask matplotlib image numpy io html decorator
---

## matplotlib와 flask를 연결해보려고 합니다.

- 처음에는 매우 간단하게 다음의 순서로 진행하면 된다고 생각했는데, 잘 안되는 것 같아요. 
    - call url
    - `plt.savefig`를 이용해서 이미지 저장 
    - `render_html`을 사용하여 html 리턴

## send_file 

- 브라우저에서 이미지만 뜨게 하려면 다음의 코드를 만들어서 수행하면 됩니다. 
- `send_file`은 url 요청이 왔을 때 그에 상응하는 파일을 내부에서 생성해서 보내주는 함수입니다. 
    - 즉, 내부에서 `binaryobject`에 파일을 저장하고 그 값을 `send_file`에 넘기면 파일로 만들어서 넘어가게 됩니다. 
- 즉, 모두 똑같이 해줘도 되는데 마지막에 저장할 때만 binary object로 저장하여 넘겨줍니다. 
- 파일의 크기가 커질 경우 어떤 문제가 생기지 않을까 싶은데, 아직까지는 잘 모르겠어요. 

```python
from flask import Flask, send_file

from io import BytesIO, StringIO
import numpy as np 

## macOS의 경우 아래 순서에 따라서 library를 import해줘야 에러없이 잘 됩니다. 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#################

app = Flask(__name__, static_url_path='/static')

## mean, var를 url에서 입력받아서 적합한 그림 파일을 만들어준다. 
## url주소와 함수 이름은 같아야 함
## url의 argument와 함수의 argument는 같아야 함
@app.route('/fig/<int:mean>_<int:var>')
def fig(mean, var):
  plt.figure(figsize=(4, 3))
  ## url에서 입력받은 mean, var를 그대로 사용하여 random sampling
  xs = np.random.normal(mean, var, 100)
  ys = np.random.normal(mean, var, 100)
  plt.scatter(xs, ys, s=100, marker='h', color='red', alpha=0.3)
  ## file로 저장하는 것이 아니라 binary object에 저장해서 그대로 file을 넘겨준다고 생각하면 됨
  ## binary object에 값을 저장한다. 
  ## svg로 저장할 수도 있으나, 이 경우 html에서 다른 방식으로 저장해줘야 하기 때문에 일단은 png로 저장해줌
  img = BytesIO()
  plt.savefig(img, format='png', dpi=200)
  ## object를 읽었기 때문에 처음으로 돌아가줌
  img.seek(0)
  return send_file(img, mimetype='image/png')
  
  # plt.savefig(img, format='svg')
  # return send_file(img, mimetype='image/svg')

if __name__ == '__main__':
  app.run(debug=True)
```

- 위 코드를 저장하고 `python hello3.py`를 실행하시면 잘 실행이 됩니다. 
- 만약 오류가 발생한다면 다음 부분이 제대로 되어 있는지 확인 하면 좋구요. 

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
```

## make html file

- 그냥 png파일만 띄우는 것이 아니라 html 파일로 만들어서 저장을 하고 싶어요. 
- 그렇다면 어떻게 표현되게 할지, html을 대략 만들어줘야 합니다.
    - url을 통해서 `mean`, `var`를 전달 받는데, 그 값을 내부에서 사용할 수 있고요 
    - `url_for`를 사용해서 `src`를 설정해줍니다. 

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
      <img src="{{ url_for('fig', mean=mean, var=var) }}" alt="Image Placeholder" 
      width={{width}}, height={{height}}>
  </body>
</html>
{% endraw %}
```

- 우리는 그림을  `/fig/<int:mean>_<int:var>` 를 통해 그림을 전달받는다. 
- 이 때 아래와 같은 방식으로 img tag에 해당 url을 넣어서 처리해준다. 

```html 
{% raw %}
<img src="{{ url_for('fig', mean=mean, var=var) }}" alt="Image Placeholder" width={{width}}, height={{height}}>
{% endraw %}
```

## render_template 

- 앞서 만든 `html`파일과 `send_html`을 연결해주는 부분을 만들어줍니다. 
- 우리가 직접 접근하는 url은 `/normal/<m_v>` 인데, 여기에 적합하게 코딩을 해주고, 
- `render_template`을 활용해서 우리가 렌더링할 html을 연결해주고 
- html 파일에서 요구하는 변수들을 모두 넘겨줍니다. 

```python
@app.route('/normal/<m_v>')
def normal(m_v):
  m, v = m_v.split("_")
  m, v = int(m), int(v)
  return render_template("random_gen.html", mean=m, var=v, width=800, height=600)
```

- 이제 `python hello3.py`를 실행해주면 지킬이 서버에서 아주 잘 돌아가는 것을 볼 수 있습니다. 

## remove cache

- 가끔 그림이 브라우저 상에서 캐쉬에 저장되어서 그림이 계속 업데이트되지 않을때가 있습니다. 
- 이를 막기 위해서는 캐시를 삭제해줘야 하는데, 이걸 하기 위해서는 캐시를 삭제해주는 decorator를 만들어주는 것이 필요합니다. 

### decorator를 만듭시다 

- 데코레이터는 심플하게 함수를 먹고 함수를 내뱉는 것이라고 생각하면 됩니다. 
- 원래 url을 연결해주기 위해서 붙는, `@app.route('/normal/<m_v>')`도 데코레이터죠. 
- 아무튼, 다음처럼 데코레이터를 만들어주구요. [캐시 없애기](https://arusahni.net/blog/2014/03/flask-nocache.html) 를 참고했습니다. 

```python
from flask import make_response

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
```

### url에 데코레이터를 씌워줍니다. 

- 다음처럼 씌워줍니다. 그러면 새로고침을 할 때마다 그림이 바뀌죠. 

```python
@app.route('/fig/<int:mean>_<int:var>')
@nocache ### 요기가 바뀌었죠
def fig(mean, var):
    ...
```

## macOS의 경우 발생하는 에러 

- 다음과 같은 오류가 발생하곤 합니다. 

```bash
Assertion failed: (NSViewIsCurrentlyBuildingLayerTreeForDisplay() != currentlyBuildingLayerTree), function NSViewSetCurrentlyBuildingLayerTreeForDisplay, file /BuildRoot/Library/Caches/com.apple.xbs/Sources/AppKit/AppKit-1561.40.112/AppKit.subproj/NSView.m, line 14485.
```

- 이유는 잘 모르겠지만, 비교적 간단하게 해결할 수 있습니다. 
- library를 임포트할 때 다음 순서에 맞춰서 해주시면 문제가 일단 해결됩니다. 

```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
```

## reference

- <http://hplgit.github.io/web4sciapps/doc/pub/._web4sa_flask013.html>
- [캐시 없애기](https://arusahni.net/blog/2014/03/flask-nocache.html)


## raw file 

### hello3.py 

```python 
from flask import Flask, send_file, render_template, make_response

from io import BytesIO, StringIO
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

app = Flask(__name__, static_url_path='/static')

@app.route('/normal/<m_v>')
@nocache
def normal(m_v):
  m, v = m_v.split("_")
  m, v = int(m), int(v)
  return render_template("random_gen.html", mean=m, var=v, width=800, height=600)


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

if __name__ == '__main__':
  app.run(debug=True)
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
      <img src="{{ url_for('fig', mean=mean, var=var) }}" alt="Image Placeholder" 
      width={{width}}, height={{height}}>
  </body>
</html>
{% endraw %}
```