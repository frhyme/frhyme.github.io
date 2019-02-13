---
title: Flask template에서 연속 상속하기. 
category: python-libs
tags: python python-libs flask template inheritance
---

## 왜 연속상속을 해야 하는가. 

- flask를 이용해서 웹서버를 구축하시는 분이 얼마나 계신지는 잘 모르겠습니다만, 저는 flask를 이용해서, html페이지를 동적으로 rendering하는 작업을 수행하고 있습니다. 
- 아무튼, `/templates`에 기본 골격이 되는 html 문서를 만들어 두고, jinja 문법에 맞춰서, 변형할 수 있도록 한 다음 `render_template`등으로 해당 html 문서의 골격을 변경해 줍니다.
- 처음에는 `base_layout.html`만으로 충분했는데, 작업을 하다보니까 html을 연속으로 상속받아서 처리해야하는 일들이 있더라구요. 
    - 예를 들어서, 할아버지 html에는 navigation bar가 포함되어 있고, 
    - 그런데, 특정 html에서는 sidebar가 추가되어야 해서, sidebar는 아버지 html에 만들고, 
    - 아들 html은 결국, 할아버지 html, 아버지 html을 모두 상속받아야 하는것이죠. 
- 사실 너무나 흔한 상속방법이고, 너무 당연한 것이기는 한데, 바보같은 저는 몰랐기 때문에 허허허 이걸 정리합니다. 

## do it. 

- 우선 `grandfather.html`을 만들어줍니다. 아주 간단하죠. 
- 단 중간에 `{% block content1 %}{% endblock %}`라는 부분이 있습니다. 즉, `grandfather.html`을 상속받는 `father.html`에서는 해당 부분을 작성해줘야겠죠. 
- 제가 처음에 연속상속이 안되지 않을까? 라고 생각했던 이유중 하나는 `content1`과 같은 부분이 마음대로 적용될 수 있는 것인지 몰랐기 떄문입니다. jinja template engine에서 기본적으로 그냥 `{% block content %}`로 정의되고 있는줄 알았는데 그게 아니라 마음대로 변수를 정의해도 되더군요. 

```html
<!DOCTYPE HTML>
<html>
    <head>
    </head>
    <body>
        <h1>This is grand father html</h1>
        <div>
            {% block content1 %}{% endblock %}
        </div>
    </body>
 </html>
```

- `father.html`을 만들어줍니다. 
- 비슷하지만, 맨 위에 `{% extends 'grandfather.html %}` 이라는 문서가 작성해주면, 해당 html을 상속받습니다. 
    - 그 다음 `{% block content1 %} ~~ {% endblock%}` 부분에 필요한 부분을 작성해주고
    - 이 아이가 또 다른 아이로부터 상속될 필요가 있기 때문에, 다시 새로운 block `{% block content2 %} {% endblock %}`를 만들어줍니다.

```html
{% extends 'grandfather.html' %}
{% block content1 %}
    <p>This is father html!!</p>
    {% block content2 %}
    {% endblock%}
{% endblock %}
```

- 이제 `son.html`을 만들어줍니다. 
    - 아래처럼, 작성해주면 됩니다. 

```html
{% extends 'father.html' %}
{% block content2 %}
    <p>This is son html!!</p>
{% endblock %}
```

- 그리고 flask에서 아래처럼 실행해주면 됩니다. 

```python
@app.route('/test')
def test():
    return render_template('son.html')
```

- 그 결과로 만들어지는 소스코드는 다음과 같습니다. 들여쓰기는 제대로 안되어있지만, 구조는 제가 의미한 바와 같죠. 

```html
<!DOCTYPE HTML>
<html>
    <head>
    </head>
    <body>
        <h1>This is grand father html</h1>
        <div>
    <p>This is father html!!</p>
    <p>This is son html!!</p>
        </div>
    </body>
 </html>
```

## wrap-up

- 사실, 너무 당연한 이야기이기는 했습니다. 단일상속만 가능하다면 template을 관리하는 측면에서 아주 큰 귀찮음들이 막 발생할 수 있을테니까요. 
- 추가로, jinja template engine에 대해서 더 정리할 필요성이 있을 것 같습니다. 여기서 제공하는 문법들을 제가 명확하게 알게되면, template들을 더 효과적으로 관리할 수 있을 것 같습니다.