---
title: jinja2 에 대해서 알아보쟈!
category: python-libs
tags: jinja jinja2 python flask template 
---

## jinja2는 flask에서 무슨 일을 하는가? 

- flask로 웹서버를 구축하고 있습니다. flask를 통해서 웹서버를 구축하는 방식은 매우 간단합니다. 
- 일단 다음과 같은 python 코드를 만듭니다. 
    - `/test_page`라는 url로 들어오면, `test_page.html`라는 template을 렌더링해서 보여준다는 이야기겠죠. 

```python

app = Flask(__name__)

@app.route('/test_page')
def test_page():
    return render_template('test_page.html')

if __name__ == '__main__':
    # debug를 True로 세팅하면, 해당 서버 세팅 후에 코드가 바뀌어도 문제없이 실행됨. 
    app.run(host='127.0.0.1', port=8000, debug = True)
```

- 그렇다면 이제 `test_page.html`을 봅시다. 
    - 뭔가, html문서처럼 보이기는 하는데, `{퍼센트 퍼센트}`의 부분이 영 신경쓰입니다. 이걸 그대로 웹브라우저로 보내면, 제대로 이해를 못하게 되겠죠. 
- 결론부터 말씀드리면, jinja는 아래처럼 되어 있는 문서를 받아서, 해당 문서의 필요한 부분들, `content2`와 같은 부분을 변경해주고, 웹브라우저가 인식할 수 있는 html로 변환해주는 기능을 수행합니다. 참 쉽죠? 하하핫

```html
{% extends 'father.html' %}
{% block content2 %}
    <p>This is son html!!</p>
{% endblock %}
```

## what is jinja2?

- 그러니까, 대충 해석하면, jinja2는 어떤 파일, 실재하는 파일에 어떤 변수들을 집어넣어서 약간 변경시켜서 html로 만들어주는 엔진, 같은 것이다. 라고 해석할 수 있겠네요. 
- [공식 홈페이지](http://jinja.pocoo.org/docs/2.10/)에는 다음처럼 작성되어 있습니다. 

> Jinja2 is a templating engine for Python.

- 그렇다면 template engine은 무엇인가요? [위키피디아의 설명](https://en.wikipedia.org/wiki/Template_processor)에 따르면 다음과 같습니다. 

> A template processor (also known as a template engine or template parser) is software designed to combine templates with a data model to produce result documents.

- template(문서 원형)과 data model을 혼합하여, 새로운 document를 만드는 것. 이라고 해석할 수 있겠네요. 앞서 제가 말한 개념과 유사합니다. 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/TempEngGen015.svg/330px-TempEngGen015.svg.png)

## 어떻게 쓸 수 있나요? 

- 저는 jinja를 바로 사용하지는 않고, flask에 포함되어 있는 jinja를 사용합니다. 
- 즉, 일단 jinja의 template을 만드는 문법만 배우고, flask의 `render_template`을 이용해서 data를 넘겨줘서 html로 만들어줄 것입니다. 
- jinja template을 만들기 위한 기본적인 syntax, semantic은 [여기에서](http://jinja.pocoo.org/docs/2.10/templates/) 볼 수 있습니다. 
- 일단 예제를 보겠습니다. 대략 template은 다음처럼 구성됩니다. html비슷한데, 조금씩 다른 부분들이 보이죠. 
    - 예를 들어서, `for`구문이 있는데, `{% 퍼센트 퍼센트 %}`로 묶여 있고, 또 끝에는 `endfor`로 처리되어 있고요. 
    - statement는 `{퍼센트 퍼센트 }`로 표현되는 것 같고, 그냥 variable은 `{{}}`로 표현되는 것 같네요. 
    - 그리고, `navigation`, `a_variable`는 따로 값이 정의되지 않고, 바로 쓰이는 것을 보니까, templete을 rendering할때 값을 넘겨주어야 하는 것이 아닐까? 싶습니다. 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
    </ul>

    <h1>My Webpage</h1>
    {{ a_variable }}

    {# a comment #}
</body>
</html>
```

- 그래서, 값을 함께 넘겨보도록 하겠습니다. 아래처럼 만들고 `/test_template`로 접속합니다. 
    - 값은 아래처럼 그냥 dictionary의 형태로 넘겨주면 됩니다. 

```python
@app.route('/test_template')
def test_template():
    navigation = [{'href':'href1', 'caption':'caption1'}]
    a_variable = 'variable1'
    return render_template('test_template.html', navigation=navigation, a_variable=a_variable)
```

- 접속한 다음, 소스코드를 보면 다음과 같아요. 자, 앞에서, `{괄호 괄호}`로 싸여 있던 부분들이 모두 정상적인 html로 변형된 것을 볼 수 있습니다. 와 별거 아닐 수도 있는데 저한테는 개 신기하네요 와 개신기해!!

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <ul id="navigation">
    
        <li><a href="href1">caption1</a></li>
    
    </ul>

    <h1>My Webpage</h1>
    variable1

    
</body>
</html>
```


## wrap-up

- 정리해보겠습니다. 결론적으로, template을 jinja의 문법에 따라서 만들고, flask로 렌더링해주면 훨씬 간단한 코드를 예쁘게 만들 수 있습니다. 
- 거의 pythonic한 방식으로 코드를 짜게 되죠. 이제 이 방식을 받아들이면, html 코딩을 한다기보다, python 으로 웹코딩을 한다고 생각되게 됩니다. 와, 이제 좀 이해가 된다 ㅎ하ㅏ하하하핫
