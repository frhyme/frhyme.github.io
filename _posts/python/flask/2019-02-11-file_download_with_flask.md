---
title: flask에서 파일 다운받는 버튼 만들기
category: python-libs
tags: flask file-download python python-libs 
---

## csv download

- 요즘 웹페이지를 만드는 프로젝트를 하고 있습니다. 
- 간단하게 분석을 수행하고, 분석 결과를 보여주는 부분을 진행하고 있는데, 이 과정에서 분석 결과를 csv의 형식으로 다운받도록 처리하고 싶다는 생각을 했습니다. 
- 왜, 보통 csv파일을 다운받도록 해주는 버튼 많잖아요. 아무튼 그걸 해주려고 합니다. 
- 방식은 크게 두 가지로 나뉩니다. 
    - file을 stream으로 만들어서 그 stream을 바로 다운받는 방식(서버에 파일이 저장되지 않습니다)
    - file을 static file로 만들어서 그 파일을 다운받도록 하는 방식. 
- 둘-다 설명하겠습니다. 

### code with html  

- 원래대로라면, html 파일을 따로 만들어야 하지만 귀찮기 때문에...그냥 flask에서 적당한 html코드를 리턴하기로 합니다 하하핫. 
- 아래처럼, 그냥 hyperlink를 가지고 다운받을 수 있도록 할 수도 있고, button의 형식으로 다운받을 수 있도록 할 수도 있습니다.
- `href`, `action`에 들어가는 내용은 아래에서 정의한 URL이 되죠.

```python
@app.route("/file_download")
def hello():
    return '''
    <a href="/csv_file_download_with_file">Click me.</a>
    
    <form method="get" action="csv_file_download_with_file">
        <button type="submit">Download!</button>
    </form>
    '''
```

### download static file 

- 여기서는 정적으로 만들어진 파일을 직접 다운받을 수 있도록 처리합니다. 

```python
from flask import send_file

@app.route('/csv_file_download_with_file')
def csv_file_download_with_file():
    file_name = f"static/results/file_path.csv"
    return send_file(file_name,
                     mimetype='text/csv',
                     attachment_filename='downloaded_file_name.csv',# 다운받아지는 파일 이름. 
                     as_attachment=True)
```


### send file stream

- 여기서는 파일을 생성하지 않고, `pd.DataFrame`을 직접 stream으로 변환하고, 바로 다운받을 수 있도록 처리해줍니다. 
    - [이 블로그의 내용을](https://beomi.github.io/2017/11/28/Flask-CSV-Response/) 참고했습니다. 

```python
from io import StringIO
from flask import Response

@app.route('/csv_file_download_with_stream')
def csv_file_download_with_stream():
    output_stream = StringIO()## dataframe을 저장할 IO stream 
    temp_df = pd.DataFrame({'col1':[1,2,3], 'col2':[4,5,6]})## dataframe을 아무거나 만들어주고, 
    temp_df.to_csv(output_stream)## 그 결과를 앞서 만든 IO stream에 저장해줍니다. 
    response = Response(
        output_stream.getvalue(), 
        mimetype='text/csv', 
        content_type='application/octet-stream',
    )
    response.headers["Content-Disposition"] = "attachment; filename=post_export.csv"
    return response 
```


## wrap-up

- 변하지 않는 파일이라면,`send_file`이 좋고, 임시로 만들어지는 파일이라면, `Response`가 좋겠네요. 