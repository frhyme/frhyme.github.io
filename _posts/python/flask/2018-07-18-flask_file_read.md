---
title: flask에서 파일 읽고 결과 뿌려주기
category: python-lib
tags: python flask python-lib html 
---

## flask가 텍스트 파일을 읽고 웹페이지에 표시하게 해줍시다. 

- 저는 이후에 excel을 읽어서 데이터 처리를 한 다음 웹페이지로 표시해주는 프로그램을 만들어보려고 합니다. 
- 그러려면 아주 간단하게 flask 내부에서 파일을 읽고 보여줄 수 있는지를 확인하는 것이 필요하죠.
- 그래서 아주 간단한 텍스트 파일을 만들고 flask에서 읽은 다음 뿌려주도록 해보았습니다. 

## make txt 

- 아주 간단한 txt 파일을 만들어서 flask app 내부의 `/static/`폴더 내에 만들어두었습니다. 

```text
this is test file.
for checking the file.
this is test file.
for checking the file.
this is test file.
for checking the file.
```

## url mapping 

- 일단 `Flask()`을 세팅할 때 `static_url_path='/static'`을 세팅해줍니다. 
    - 간단히 말하면 static file들은 해당 경로에 있는 파일들은 동적으로 변화하는 것이 아니므로 값 자체를 그대로 보내주어도 된다는 것을 의미합니다. 
    - 해당 경로에는 보통 css, image 들이 포함되는데, 이들은 매번 동적인 페이지를 생성한다기 보다는 이미 만들어진 값들이 그대로 보내지는 형태죠. 
    - 따라서 이러한 부분들은 그냥 static하다고 정의하고 편하게 처리합니다. 

- 아래에서 `localhost:5000/txt`로 접근하면, 파일을 읽어서 그 결과를 문자열로 리턴하는 식으로 처리하였습니다. 
    - `render_template`를 사용하지 않고 문자열 자체를 보내주기 때문에, html 로 표현되도록 해주어야 합니다. 

```python
from flask import Flask
app = Flask(__name__, static_url_path='/static')
 
## localhost:5000/txt 로 접근하면 다음 부분이 수행됨 
@app.route('/txt')
def read_txt():
    f = open('static/test.txt', 'r')
    ## 단 리턴되는 값이 list형태의 타입일 경우 문제가 발생할 수 있음.
    ## 또한 \n이 아니라 </br>으로 처리해야 이해함
    ## 즉 파일을 읽더라도 이 파일을 담을 html template를 만들어두고, render_template 를 사용하는 것이 더 좋음
    return "</br>".join(f.readlines())

if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(debug=True, threaded=True)
```

## wrap-up

- 이후에는 `pandas`를 이용하여 엑셀을 읽고 그 결과를 잘 보여줄 수 있도록 처리할 수도 있을 것 같습니다. 
