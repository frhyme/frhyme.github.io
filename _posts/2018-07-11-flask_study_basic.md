---
title: flask로 웹 사이트 만들기 - basic
category: python-lib
tags: python python-lib flask web html 
---

## intro

- 연구실 과제로 간단하게 분석 도구를 만들어야 하는데, PyQT로 만들수도 있겠지만 별로 모양이 예쁘지 않은 것 같고요. 가능하면 웹으로 구현을 해보는 게 저한테도 도움이 될 것 같다는 생각이 들었습니다. 
- 그래서 처음에는 django를 사용해보려고 하다가, django는 제 기준에서는 세팅하거나 좀 불편한 부분이 있더라구요. 그래서 좀 간단하게 사용할 수 있는 flask를 사용해보자! 라고 결론을 내렸습니다. 
- 그래서 간단하게 사용한 것을 정리하고, 이후에 공부하는 대로 추가할 예정입니다. 


## flask 가 뭔가요?

- flask는 무엇인가. 

## do it.

### install 

- 일단 flask를 설치합니다. 

```bash
conda install Flask 
```

### very basic code

- 일단 다음 코드를 보시죠 
- 간단하게 `Flask`라는 클래스를 가져와서 만들어주고, 
- url을 설정해주고, 
- url에 들어가면 뜰 페이지를 설정해줍니다(나중에는 html 로 렌더링해서 리턴을 하겠지만 지금은 그냥 스트링으로 리턴이 됩니다)

```python
from flask import Flask
app = Flask(__name__) ## Flask instance를 만들어주고.

@app.route('/') ## URL, 이 경우 localhost:5000/
def index():
    return 'Hello, World! page입니다'
```

- 위 코드를 `hello.py`나 혹은 마음대로 이름을 정해서 파이썬 코드 파일로 만들어주고 
- 아래 코드를 bash에서 실행해줍니다. 
    - `FLASK_DEBUG=1` 부분은 코드가 바뀌면 바로 페이지에 적용되도록 설정한 부분입니다. 
- 그 다음에 웹브라우저에서 `localhost:5000/`으로 들어가면 앞에서 리턴한 스트링이 표시되는 것을 알 수 있습니다. 

```bash
$ export FLASK_APP=main.py
$ export FLASK_DEBUG=1 
$ flask run
```

### URL에서 값 넘겨받기 

- 아래 코드에서 보시면, 이전과 다르게 `<int:userid>` 라는 부분이 있는 것을 알 수 있는데요. 이 부분은 `/user/id/`다음에 integer가 넘어온다는 것을 의미합니다. 
- 어떤 값이든 integer가 넘어온다면 그 값을 받아서 그 값에 맞춰서 처리를 해줄 수 있다는 말이죠. 
- 꼭 integer가 아니더라도 url에 값을 넘긴다면 그 값은 <>를 이용해서 정의해주고, 아래의 함수에서도 동일한 argument로 적용해줘야 합니다. 

```python
## uri에 넘어온 값을 사용 
@app.route('/user/<username>')
def show_username(username):
    return "your name is {}, right?".format(username)

## 입력받는 변수의 데이터 타입을 설정할 수 있음.
## 물론 스트링으로 입력받아서 처리해도 상관없음
@app.route('/user/id/<int:userid>')
def show_user_id(userid):
    return "your id is {}, right?".format(userid)

## 넘겨받은 숫자만큼 별을 표시하기....
## 쓸데없긴 하지만 이런식으로 페이지를 제가 재밌게 만들 수있겠죠. 
@app.route('/draw/<number>')
def draw_start(number):
    r_str = ""
    for i in range(1, int(number)):
        r_str+="*"*i
        r_str+='<br>'# html에서의 줄바꿈으로 해야함 not \n
    return r_str
```

### redirection

- 아래처럼 redirect을 이용할 수도 있는데 이 말은 `/aaa`로 이동하려고 할 경우, `/`로 재연결된다는 것을 의미합니다. 

```python
# redirect를 이용해서 제어할 수 있다.
@app.route('/aaa')
def aaa(): 
    return redirect('/')
```

### html rendering 

- 하지만, 매번 저렇게 스트링으로만 표시되면 너무 웹사이트가 예쁘지 않습니다. 
- 그래서 html로 렌더링해주는 것이 필요한데요 
- 일단 파이썬에서는 코드를 다음처럼 쓸 수 있습니다. 
    - name이라는 argument로 넘겨받고, 그 값을 사용해서 `hello.html`이라는 파일을 렌더링해줍니다. 
    - 그리고 넘겨받은 `name`를 같이 넘겨주죠. 

```python
## 아래처럼 두 개를 겹쳐 놓으면, 두 경우에 대해서 모두 수행됨. 
## 단, 이 경우에 argument의 초기값이 정해져 있는 것을 확인
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', 
    name='\n'.join([name*10 for i in range(0, 20)])
    )
```

- 이를 가능하게 하기 위해서는 우리가 만든 `hello.py`가 있는 폴더에 `templates`라는 폴더를 만들고, 그 폴더 내에 `hello.html`이라는 파일을 만들어 두어야 합니다. 

- `hello.html`이라는 파일은 다음으로 구성됩니다. 이것도 매우 간단하기는 한데, 
- 파이썬의 코드인것 같긴 한데 조금 다릅니다. `{%%}`를 이용해서 표시되고, 우리가 넘겨받은 name은 `{{}}`로 감싸져 있죠. 
    - 대략 무슨 의미인지는 쉽게아실 것 같아서 넘어갑니다. 
- 아무튼 이렇게 세팅되어 있ekaus `/hello`로 들어갔을때 우리가 이미 정의한 `html` 템플릿에 맞춰서 웹페이지가 뜨는 것을 알 수 있습니다. 

```html
<!doctype html>
<title>Hello from Flask</title>

{% if name %}
  <h1>Hello <br>{{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

## wrap-up

- 일단은 아주 간단하게 웹페이지를 만들 수 있다. 
    - 그러나 시각적으로 예쁘게 하려면 css부분도 함께 공부하는 것이 필요하고
    - 단지, url을 통해서 값을 넘겨받는 것이 아니라 다른 방식으로 넘겨받으려면 어떻게 해야 하는지에 대해서도 알아두는 것이 필요할듯 

## reference

- <https://code.tutsplus.com/ko/tutorials/an-introduction-to-pythons-flask-framework--net-28822>
- <http://bluese05.tistory.com/44>


## raw code

```python
from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! page입니다'

## uri에 넘어온 값을 사용 
@app.route('/user/<username>')
def show_username(username):
    return "your name is {}, right?".format(username)
## 입력받는 변수의 데이터 타입을 설정할 수 있음.
## 물론 스트링으로 입력받아서 처리해도 상관없음
@app.route('/user/id/<int:userid>')
def show_user_id(userid):
    return "your id is {}, right?".format(userid)

## 아래처럼 두 개를 겹쳐 놓으면, 두 경우에 대해서 모두 수행됨. 
## 단, 이 경우에 argument의 초기값이 정해져 있는 것을 확인
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', 
    name='\n'.join([name*10 for i in range(0, 20)])
    )

# redirect를 이용해서 제어할 수 있다.
@app.route('/aaa')
def aaa(): 
    return redirect('/')
# uri에 변수가 포함되어 있을 때는, 함수에서도 해당 변수가 선언되어 있어야 함 
@app.route('/draw/<number>')
def draw_start(number):
    r_str = ""
    for i in range(1, int(number)):
        r_str+="*"*i
        r_str+='<br>'# html에서의 줄바꿈으로 해야함 not \n
    return r_str
```