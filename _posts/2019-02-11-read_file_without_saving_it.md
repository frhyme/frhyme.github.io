---
title: flask에서 csv 파일 업로드할때, 파일 생성하지 않고 값만 읽기. 
category: python-libs
tags: python python-libs flask csv file-upload
---

## file을 읽읍시다.

- 이전에는 html 페이지로부터 파일을 전달받은 다음, 파일을 저장하고 읽었습니다. 아래 코드처럼요. 

```python
from flask import request

@app.route('/file_uploaded', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST': # POST 방식으로 전달된 경우
        f = request.files['file1']
        f.save(f'uploads/{secure_filename(f.filename)}') # 업로드된 파일을 특정 폴더에저장하고, 
        df_to_html = pd.read_csv(f'uploads/{secure_filename(f.filename)}').to_html() # html로 변환하여 보여줌
        return df_to_html
```

- 그런데, 생각해보니까 굳이 그렇게 할 필요가 없는 것 같아요. 
- 그냥 그 값을 바로 읽어들이면 되는 것 아닌가? 싶었습니다. 

- 그냥 아래처럼, 해당 접근해서 바로 read를 해버리면 아무 문제가 없습니다. 쉽군요 하하핫

```python
from flask import request

@app.route('/file_uploaded', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST': # POST 방식으로 전달된 경우
        # 파일 객체 혹은 파일 스트림을 가져오고
        f1 = request.files['file1'].read()
        f2 = request.files['file2'].read()
        return f2
```


## wrap-up

- 더 정확하게 해결하기 위해서는 `request`라는 놈의 맥락을 이해할 필요가 있습니다. 그냥 request는 http method에 의해서 전달된 값이라고, 생각하면 될것 같아요. 
- html 문서에서 form을 통해서 전달받았다면, files이 아닌 form에 값이 들어가 있을 것이고, 그렇지 않다면, files에 값이 들어가 있을 것 같습니다. 
- 반대로 제가 다른 누군가에게 데이터를 http method를 따라서 보낸다면, response가 되고, 그걸 만들어서 내부의 값을 조정하면 되겠죠. 