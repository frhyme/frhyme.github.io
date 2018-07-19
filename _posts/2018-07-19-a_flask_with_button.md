---
title: flask) form 형식을 통해 값을 입력받고 뭔가 출력하기 
category: python-lib 
tags: python python-lib flask html http form
---

## intro

- `url/<id>`와 같은 방식으로 url에 값을 넘겨서 그 값에 따라서 동적인 페이지를 만들어서 진행할 수도 있지만, 웹페이지 에서 직접 값을 입력받는 형태로 만들어보고 싶었습니다. 
- 예를 들면 다음과 같은 방식으로 처리하고 싶은 것이죠. 

![submit_form_ex](http://javascript-coder.com/wp-content/uploads/2010/07/html-form-sample1-300x200.png)

- 우선 GET와 POST의 차이를 정리해봅시다. 

## http method: GET, POST

- `http://url/aa.html?id=5` 와 같이 url에 parameter를 함께 넘기는 방식이 GET이고 
- 전송되는 http 내부에 데이터를 추가하여 보내는 방식이 POST입니다. 
- 따라서 GET의 경우는 url에 붙어서 보내져야 해서 데이터에 제한이 있는 반면, POST는 상대적으로 큰 길이의 데이터에 적합하다고 합니다(물론 이 경우에도 용량 제한은 있다고 합니다만)

- GET의 경우는 url을 통해서 값이 넘어가기 때문에 특정한 리소스를 검색하는 경우(SQL에서 select처럼)에 많이 사용되는 반면
- POST의 경우는 form을 통해 서버로 넘겨진 데이터를 데이터베이스 등에 저장하기 위해서 많이 사용합니다. 

- 다시 이를 예를 들어 설명하자면
    - 게시판에 있는 글을 검색하여 그 결과를 보여줘야 하는 경우 ==> GET을 통해 검색하고 그 결과를 리턴하는 방식
    - 게시판에 새로운 글을 쓰는 경우 ==> POST를 통해 그 값을 데이터베이스에 작성 
- 이라고 사용된다고 생각하는 것이 좋습니다. 

- 사실 form을 사용해서 값을 넘길 때 GET, POST 중 어느 것을 쓰든 상관은 없습니다만, 가능하면 다음의 기준으로 구분하여 사용하는 것이 좋습니다. 

> 넘겨받는 argument를 url에 넣어서 제공하는 것이 필요한가? 

- 예를 들어 봅시다. 
- 네이버의 검색결과를 다른 사람에게 보여주는 경우: 
    - 네이버에서 무엇인가를 검색하면 그 결과가 `https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=frhyme`에 표시됩니다. url을 통해서 값이 넘어왔으므로 GET 방식을 이용하고 있다고 할 수 있겠죠. 
    - 그런데, 만약 이 경우 GET이 아니라 POST라면 url 상에서 값이 숨겨져서 보여지게 됩니다. 다른 사람에게 해당 url을 보내도 그 사람은 저와 같은 화면을 볼 수가 없겠죠. 
- 개인정보나 긴 글을 작성한 경우 
    - 만약 이 방식을 GET을 사용해서 보낼 경우에는 url 자체가 너무 길어질 수도 있고, 개인정보에 대한 문제도 있을 수 있습니다. 이 경우에는 해당 페이지를 의미하는 명확한 url이 필요하지 않으므로 POST 방식으로 데이터를 보내는 것이 좋겠죠. 

- 이런 식으로 GET/POST 를 구분하여 사용하는 것이 필요합니다. 


## submit.html 을 작성합니다. 

- 이제 flask 에서 GET method를 사용해보려고 합니다. 
- 우선 사용한 html 문서를 만들어 봅시다. 

- 중간에 있는 `<div>`태그는 무시하셔도 되고요. 중간에 `<form>`태그가 있습니다. 
    - `<input>`: html에서 서버로 전달되는 값들, type, name을 함께 넘김. 여기서 name이 서버에서 인식하는 변수명 
    - `<button>`: button의 경우는 form 태그 내에 있는 모든 값을 한번에 넘겨줍니다. 즉 form 태그 내에 몇 개의 `<input>` 태그들이 있다고 해도, `name`에서 충돌이 발생하지만 않는다면 다 넘어가서 서버에서 처리할 수 있다는 말입니다. 

```html 
{% raw %}
<!DOCTYPE html>
<html>
<head>
    <title>
        draw star by number
    </title>
    <style>
    </style>
</head>
<body>
    <h1> 어떤 문자를 표시하실건가요</h1><br>
    <form method="GET" action="/calculate">
        <div>
            <label for="char1"> 표시할 문자 </label>
            <input type="text" name="char1">
        </div>
        <div>
            <label for="num"> 몇 번 </label>
            <input type="text" name="num">
        </div>
        <div class='button'>
            <button type="submit">숫자만큼 별 표시하기</button>
        </div>
    </form>
    <div>
        <p>
            {% if num == None %}
                <h5> 아직 아무 값도 입력이 안되었습니다. </h5>
            {% else %}
                <h5> {{num}} 를 입력받았습니다. </h5>
                {% for i in range(1, num+1) %}
                <p>
                    {% for j in range(0, i) %}
                        {{char1}}
                    {% endfor %}
                </p>
                {% endfor %}
            {% endif %}
        </p>
    </div>
</body>
</html>
{% endraw %}
```

## submit_test.py 작성하기 

- 일단 모두 GET의 방식으로 전달받았습니다. 
    - 앞서 말한 바와 같이 POST와 GET의 경우는 전달받은 값을 읽는 방식이 다릅니다. 
    - POST: `temp = request.form['num']`
    - GET: `temp = request.args.get('num')`

- 넘겨받은 값을 읽고, 간단히 처리하여 `render_template`에 넘겨줍니다. 
    - 값을 하나씩 넘기지 않고, 묶어서 하나의 딕셔너리로 넘길 수 있지 않을까? 싶기는 한데 이건 나중에 알아볼게요

```python
from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='/static')

## GET 방식으로 값을 전달받음. 
## num이라는 이름을 가진 integer variable를 넘겨받는다고 생각하면 됨. 
## 아무 값도 넘겨받지 않는 경우도 있으므로 비어 있는 url도 함께 mapping해주는 것이 필요함
@app.route('/')
def main_get(num=None):
    return render_template('submit_test.html', num=num)

@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):
    ## 어떤 http method를 이용해서 전달받았는지를 아는 것이 필요함
    ## 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽어들이는 방식이 달라짐
    if request.method == 'POST':
        #temp = request.form['num']
        pass
    elif request.method == 'GET':
        ## 넘겨받은 숫자 
        temp = request.args.get('num')
        temp = int(temp)
        ## 넘겨받은 문자
        temp1 = request.args.get('char1')
        ## 넘겨받은 값을 원래 페이지로 리다이렉트
        return render_template('submit_test.html', num=temp, char1=temp1)
    ## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함

if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(debug=True, threaded=True)

```

- 이렇게 진행하면 잘 됩니다. 


## css 추가하기 

- 하지만 지금은 form이 너무 예쁘지 않습니다. 
- [이 포스트](https://developer.mozilla.org/ko/docs/Learn/HTML/Forms/Your_first_HTML_form)를 참고하여 css를 추가합니다. 
    - 외부 파일에서 가져오는 것이 좋지만 저는 임의로 head 내에 넣었습니다. 

```html 
<html>
<head>
    <title>
        draw star by number
    </title>
    <style>
        form {
            /* Just to center the form on the page */
            margin: 0 auto;
            width: 400px;
            /* To see the outline of the form */
            padding: 1em;
            border: 1px solid #CCC;
            border-radius: 1em;
        }
        form div + div {
            /* div div 사이에 여백 추가*/
            margin-top: 1em;
        }
        label {
            /* To make sure that all label have the same size and are properly align */
            display: inline-block;
            width: 90px;
            text-align: right;
        }
        .button {
            /* To position the buttons to the same position of the text fields */
            padding-left: 90px; /* same size as the label elements */
        }

        button {
            /* This extra margin represent roughly the same space as the space
            between the labels and their text fields */
            margin-left: .5em;
        }
    </style>
</head>
```

- 훨씬 예뻐지는군요. 

## 저의 경우는 

- 엑셀 파일을 파일명을 읽어서 데이터를 처리하고, 시각화/분석/시뮬레이션이 가능하도록 처리를 하려고 합니다. 
- 따라서 POST 방식을 쓸 필요는 없고 GET만으로 충분할 것 같긴 합니다. 
    - 파일 전체를 POST로 넘기는 것도 가능하겠지만 제 생각에 그건 너무 커뮤니케이션 오버헤드가 너무 큰 것 같고
    - 파일 이름만 넘기고 이를 활용해서 static하게 있는 것을 그대로 활용하면 되지 않을까? 싶어요

## wrap-up

- `render_template`를 사용할 때 지금은 값을 하나씩 넘기는 형태입니다만, 다른 방식으로 넘길 수 있지 않을까? 하는 생각은 해봅니다. 
- 그러니까, `context`같은 딕셔너리로 묶은 다음에 처리하면 되지 않을까? 싶어요. 다음에 알아보도록 하겠습니다. 

## reference

- <http://doorbw.tistory.com/46?category=679147>
- <https://medium.com/wasd/웹-페이지-client-에서-정보-보내기-bf3aff952d3d>
- <https://blog.outsider.ne.kr/312>

## raw code

### submit_test.html 

```html 
{% raw %}
<!DOCTYPE html>
<html>
<head>
    <title>
        draw star by number
    </title>
    <style>
        form {
            /* Just to center the form on the page */
            margin: 0 auto;
            width: 400px;
            /* To see the outline of the form */
            padding: 1em;
            border: 1px solid #CCC;
            border-radius: 1em;
        }
        form div + div {
            /* div div 사이에 여백 추가*/
            margin-top: 1em;
        }
        label {
            /* To make sure that all label have the same size and are properly align */
            display: inline-block;
            width: 90px;
            text-align: right;
        }
        .button {
            /* To position the buttons to the same position of the text fields */
            padding-left: 90px; /* same size as the label elements */
        }

        button {
            /* This extra margin represent roughly the same space as the space
            between the labels and their text fields */
            margin-left: .5em;
        }
    </style>
</head>
<body>
    <h1> 어떤 문자를 표시하실건가요</h1><br>
    <form method="GET" action="/calculate">
        <div>
            <label for="char1"> 표시할 문자 </label>
            <input type="text" name="char1">
        </div>
        <div>
            <label for="num"> 몇 번 </label>
            <input type="text" name="num">
        </div>
        <div class='button'>
            <button type="submit">숫자만큼 별 표시하기</button>
        </div>
    </form>
    <div>
        <p>
            {% if num == None %}
                <h5> 아직 아무 값도 입력이 안되었습니다. </h5>
            {% else %}
                <h5> {{num}} 를 입력받았습니다. </h5>
                {% for i in range(1, num+1) %}
                <p>
                    {% for j in range(0, i) %}
                        {{char1}}
                    {% endfor %}
                </p>
                {% endfor %}
            {% endif %}
        </p>
    </div>
</body>
</html>
{% endraw %}
```

### submit_test.py

```python
from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='/static')

## GET 방식으로 값을 전달받음. 
## num이라는 이름을 가진 integer variable를 넘겨받는다고 생각하면 됨. 
## 아무 값도 넘겨받지 않는 경우도 있으므로 비어 있는 url도 함께 mapping해주는 것이 필요함
@app.route('/')
def main_get(num=None):
    return render_template('submit_test.html', num=num)

@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):
    ## 어떤 http method를 이용해서 전달받았는지를 아는 것이 필요함
    ## 아래에서 보는 바와 같이 어떤 방식으로 넘어왔느냐에 따라서 읽어들이는 방식이 달라짐
    if request.method == 'POST':
        #temp = request.form['num']
        pass
    elif request.method == 'GET':
        ## 넘겨받은 숫자 
        temp = request.args.get('num')
        temp = int(temp)
        ## 넘겨받은 문자
        temp1 = request.args.get('char1')
        ## 넘겨받은 값을 원래 페이지로 리다이렉트
        return render_template('submit_test.html', num=temp, char1=temp1)
    ## else 로 하지 않은 것은 POST, GET 이외에 다른 method로 넘어왔을 때를 구분하기 위함

if __name__ == '__main__':
    # threaded=True 로 넘기면 multiple plot이 가능해짐
  app.run(debug=True, threaded=True)
```