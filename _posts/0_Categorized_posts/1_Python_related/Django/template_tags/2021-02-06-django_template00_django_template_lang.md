---
title: python - Django - basic 
category: python
tags: python programming django web template tag
---

## python - Django - basic 

- 사실 html 문서들은 서로 중복을 피해서 유지보수를 편하도록 하게 위해서 다양한 Template Langue들이 존재합니다. django는 Django Template Language(DTL)을 사용합니다.

## Passing parameter

- 백엔드인 컨트롤러에서 해당 `index.html`로 `title` 데이터를 보내서, 이 html문서에 표시되게 해주고 싶다면, 다음처럼 해주면 됩니다.

```html
<!-- index.html -->
<h2> {% raw %} {{ title }} {% endraw %}</h2>
```

## Conditional 

- 컨트롤러에서 넘긴 `boolParam`의 True, False에 따라서 동작을 제어하고 싶다면 다음처럼 해주면 됩니다.

```html
{% raw %}{% if boolParam %}
    <p> This is True </p> 
{% else %} 
    <p> This is False </p>
{% endif %}{% endraw %}
```

## for loop 

- 컨트롤러에서 paramLst라는 `list`를 전달받고 for loop를 처리하려면 다음처럼 하면 됩니다.

```html
{% raw %}{% for p in paramLst %}
    <div>{{ p }}</div>
{% endfor %}{% endraw %}
```
