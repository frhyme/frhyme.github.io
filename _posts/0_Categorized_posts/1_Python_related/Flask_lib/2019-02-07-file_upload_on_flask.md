---
title: flask에서 html페이지로부터 파일 업로드하기 
category: python-libs
tags: python flask python-libs file
---

## file submit via webpage 

- 요즘 저는 간단한 analytics tool을 만들고 있습니다. 특정한 분석을 수행하기 위해서 필요한 데이터를 정의하고, 그 데이터를 사용자가 입력했을 때 데이터를 분석해서 결과를 뿌려주는 형식의 간단한 분석도구죠. 
- 아무튼 그 과정에서, 사용자의 파일을 입력받는 것이 필요합니다. 
    - 만약, 입력받는 파일이 동적으로 변하지 않고, static하게 있다고 하면, 그냥 static_file_url을 지정해서 가져오면 되는 것이기는 합니다
- 아무튼, 웹페이지에서 사용자의 컴퓨터에 있는 파일을 경로를 통해 자동으로 입력받고, 그 자료를 읽어서 웹페이지 상에서 보여주는, 비교적 간단한 형태의 자료를 만들어보려고 합니다. 

## 뭘 할 것인가. 

- 다음을 처리할 수 있는 비교적 간단한 웹페이지를 만들어보려고 합니다. 
    - 특정한 파일을 웹페이지로부터 넘겨 받고(일단은 편의상 해당 파일을 csv로 합니다)
    - 해당 csv를 읽어서, 그 결과를 대략 보여주는 형식 
- 의 간단한 것을 처리합니다. 즉 다음의 두가지 페이지 혹은 펑션을 만들어주면 되겠죠. 
    - 파일 입력받는 페이지
    - 입력된 파일을 보여주는 페이지 


## do it 

- python 코드는 다음과 같습니다. 실행할 때는 그냥 `python hello.py`로 실행하면 됩니다.

```python
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import pandas as pd 

# file을 submit하는 페이지 
# /upload 의 페이지로 들어와서, upload.html의 파일을 렌더링하여 보여줌 
# 여기서, upload.html은 프로젝트 폴더 내의 templates 폴더에 존재해야 함(default)
@app.route('/upload')
def render_file():
    return render_template('upload.html')

# file이 submit되면 전달되는 페이지
# upload.html에서 form이 제출되면 /file_uploaded로 옮겨지게 되어 있음.
@app.route('/file_uploaded', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST': # POST 방식으로 전달된 경우
        f = request.files['file1']
        # 파일 객체 혹은 파일 스트림을 가져오고, html 파일에서 넘겨지는 값의 이름을 file1으로 했기 때문에 file1임. 
        f.save(f'uploads/{secure_filename(f.filename)}') # 업로드된 파일을 특정 폴더에저장하고, 
        df_to_html = pd.read_csv(f'uploads/{secure_filename(f.filename)}').to_html() # html로 변환하여 보여줌
        return df_to_html

if __name__ == '__main__':
    # debug를 True로 세팅하면, 해당 서버 세팅 후에 코드가 바뀌어도 문제없이 실행됨. 
    app.run(host='127.0.0.1', port=8000, debug = True)
```

- `upload.html`의 파일은 다음과 같습니다. 

```html 
<html>
    <body>
        <h1>file을 업로드하는 페이지입니다.</h1>
        <p> POST 방식으로 업로드하며, enctype은 post방식으로 전달되는 객체가 어떤 형태로 encoding되어야 하는지를 의미합니다. </p>
        <p> 또한 input에 type을 file이라고만 정의하면 알아서 잘 됩니다 하하핫.</p>
        <p> 또한 file이 업로드되어, submit 버튼을 누르면, action 부분에 작성된 url로 넘어가게 됩니다. </p>
        <form action="http://localhost:8000/file_uploaded" 
        method="POST" enctype="multipart/form-data">
            <input type="file" name="file1" />
            <input type="submit" />
        </form>
    </body>
</html>
```

## other things 

- 앞에서는 대충 한 것인데, 몇가지만 정리해봅니다. 

### what is secure_filename

- 넘겨 받은 파일명과 저장하는 파일명이 다릅니다. SQL injection처럼 사용자로부터 값을 입력받는 부분에 SQL 구문을 넣거나 하여 서버로부터 데이터를 가져오거나 망가뜨리는 경우들이 있죠. 
- 이런 것을 막기 위해서 `secure_filename`을 활용해서 파일 명을 변경해서 저장해줍니다. 
- 그래서, `secure_filename`을 통해서 변경된 파일이름을 활용해서 파일을 읽어야 합니다. 

```python
f = request.files['file1']
# 파일 객체 혹은 파일 스트림을 가져오고, html 파일에서 넘겨지는 값의 이름을 file1으로 했기 때문에 file1임. 
f.save(f'uploads/{secure_filename(f.filename)}') # 업로드된 파일을 특정 폴더에저장하고, 
```

### what is "multipart/form-data"

- 자세한 내용은 [여기에서 파악할 수 있습니다](https://www.w3schools.com/tags/att_form_enctype.asp). 
- POST방식으로 데이터를 전달할 때, 해당 데이터를 어떻게 인코딩하여 전처리할지를 선택해줘야 합니다. 다음과 같은 총 세 가지 방식이 있는데. 
    - application/x-www-form-urlencoded: Default값이고, space는 +로 변환되고 특수 문자들은 ASCII HEX 값으로 변환
    - multipart/form-data: 어떤 문자도 인코딩되지 않고, 파일을 업로드할 때 사용뙤는 형식이다. 
    - text/plain
- 그냥 파일을 업로드할 때는 "multipart/form-data"을 쓴다 라고 외우면 될것 같습니다 하하하핫

## wrap-up

- 비교적 간단하게, 파일을 읽어서 읽은 것을 보여주는 것을 쉽게 만들었다. 좀 더 웹페이지를 예쁘게 만들어주는 것이 필요할 것 같기는 하다. 
- 이제 bootstrap과 flask를 연결하는 방법이 있는지를 좀 찾아봐야겠다.



## reference 

- <https://hashcode.co.kr/questions/6789/%ED%8C%8C%EC%9D%B4%EC%8D%AC-flask%EB%A1%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%97%85%EB%A1%9C%EB%93%9C-%ED%95%A0%EB%95%8C>
- <https://flask-docs-kr.readthedocs.io/ko/latest/patterns/fileuploads.html>