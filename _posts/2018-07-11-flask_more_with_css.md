---
title: Flask로 html 상속, css 적용하기
category: python-lib
tags: html python python-lib Flask css 
---

## intro

- 지난 번에는 아주 간단한 Flask 사용법을 알아보았는데, 이번에는 좀 더 복잡한 것을 알아보려고 합니다. 
- [이 포스트](https://code.tutsplus.com/ko/tutorials/an-introduction-to-pythons-flask-framework--net-28822)의 내용을 많이 참고했습니다. 

## html 상속하기 

- 참고한 포스트에서는 html을 상속하는 형태로 html을 만들었습니다. 

### layout.html

- 문서 자체는 그냥 html 문서인데, 중간에 몇 가지 신경 쓰이는 부분이 있습니다.

#### css setting 

- html 문서는 `template`라는 폴더에 있고, css 문서는 `static/css/main.css`에 있습니다. 
- `url_for`를 이용하면 해당 폴더의 url을 자동으로 세팅해주는 것 같아요. 

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
```

#### block content, end block 

- 또 html 문서에서는 좀 낯설게 보이는 부분이 있습니다. 
- `layout.html`은 일종의 abstract class라고 생각하셔도 됩니다. 다른 html 문서들, `about.html`, `home.html`의 뼈대가 되죠. 
- 아래 부분의 경우는 다른 html 문서들이 `layout.html`을 상속받고, 저 부분만 변경하여 새로운 html문서를 만들어주게 됩니다. 

```html
{% block content %}
{% endblock %}
```

#### layout.html 코드

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Flask App</title>    
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
  </head>
  
  <body>
   
    <header>
      <div class="container">
        <h1 class="logo">Flask 앱</h1>
        <strong><nav>
            <ul class="menu">
              <li><a href="{{ url_for('home') }}">Home</a></li>
              <li><a href="{{ url_for('about') }}">About</a></li>
              <li><a href="{{ url_for('user') }}">User</a></li>
            </ul>
          </nav></strong>
      </div>
    </header> 
     
    <div class="container">
      {% block content %}
      {% endblock %}
    </div>
     
  </body>
</html>
```

### about.html 

- 따라서, 다른 html 파일에서는 `{% extends "layout.html" %}`를 사용해서 그대로 상속받고, 
- `{% block content %}`와 `{% endblock %}` 사이에만 html 부분을 넣어주면 됩니다. 

```html
{% extends "layout.html" %}
  
{% block content %}
  <h2>About</h2>
  <p>This is an About page for the Intro to Flask article. Don't I look good? Oh stop, you're making me blush.</p>
{% endblock %}
```

### home.html 

```html
{% extends "layout.html" %}
{% block content %}
  <div class="jumbo">
    <h2>Welcome to the Flask app<h2>
    <h3>This is the home page for the Flask app<h3>
  </div>
{% endblock %}
```

## main.css

- css 부분은 제가 참고한 포스트에 있는 내용을 그대로 가져왔습니다. 공부하면서 제가 원하는 형태로 변경해야 할것 같긴 합니다만, css만 잘 세팅해줘도 아주 예쁘게 나오네요. 

```css
body {
    margin: 0;
    padding: 0;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: #444;
  }
   
  /*
   * Create dark grey header with a white logo
   */
    
  header {
    background-color: #2B2B2B;
    height: 35px;
    width: 100%;
    opacity: .9;
    margin-bottom: 10px;
  }
   
  header h1.logo {
    margin: 0;
    font-size: 1.7em;
    color: #fff;
    text-transform: uppercase;
    float: left;
  }
   
  header h1.logo:hover {
    color: #fff;
    text-decoration: none;
  }
   
  /*
   * Center the body content
   */
    
  .container {
    width: 940px;
    margin: 0 auto;
  }
   
  div.jumbo {
    padding: 10px 0 30px 0;
    background-color: #eeeeee;
    -webkit-border-radius: 6px;
       -moz-border-radius: 6px;
            border-radius: 6px;
  }
   
  h2 {
    font-size: 3em;
    margin-top: 40px;
    text-align: center;
    letter-spacing: -2px;
  }
   
  h3 {
    font-size: 1.7em;
    font-weight: 100;
    margin-top: 30px;
    text-align: center;
    letter-spacing: -1px;
    color: #999;
  }
  
  .menu {
    float: right;
    margin-top: 8px;
  }
   
  .menu li {
    display: inline;
  }
   
  .menu li + li {
    margin-left: 35px;
  }
   
  .menu li a {
    color: #999;
    text-decoration: none;
  }
```

## hello2.py

- 다음의 형식으로 아주 간단하게 url과 html 문서만 매핑해주는 형식으로 만들었습니다. 

- 또한 코드를 아래처럼 작성한 경우에는 `python hello2.py`로 실행해도 잘됩니다. 

```python
from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/user')
def user():
  return render_template('user.html')


if __name__ == '__main__':
  app.run(debug=True)
```

## wrap-up

- css는 웹브라우저에서 캐시에 남아있는 경우가 많아서, css를 바꾸어도 웹페이지에서는 바로 뜨지 않는 경우를 볼 수 있어요. 
- 그럴때는 브라우저의 개발자 도구로 들어가서, 네트워크에 캐시 삭제를 누르시고 진행하시면 됩니다. 

## reference 

- <https://code.tutsplus.com/ko/tutorials/an-introduction-to-pythons-flask-framework--net-28822>