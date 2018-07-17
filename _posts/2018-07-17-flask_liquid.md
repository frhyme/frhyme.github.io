---
title: 지킬로 만든 블로그에서 {%%} 표시하기
category: others
tags: flask liquid jekyll blog python-lib python 
---

## flask로 공부한 내용을 마크다운으로 작성하고, 지킬로 렌더링을 하려는데.

- 자꾸 안되는 겁니다. 발생하는 에러는 대략 다음과 같아요. 
- {% raw %}{%%} {% endraw %}를 표시하려고 하면 자꾸 에러가 발생하는 것이죠. 

```bash
Liquid Exception: Liquid syntax error (line 111): Tag {% raw %} {%%} {% endraw %} was not properly terminated with regexp: /\%\}/ in /Users/frhyme/frhyme.github.io/_posts/2018-07-11-flask_study_basic.md
```

## liquid 

- liquid는 지킬에서 페이지를 렌더링할 때 이해하기 위해서 표현된 언어입니다. 
- 대략 다음의 형태로 표현되는데, 이를 자세히보면, `heading`이라는 변수가 미리 선언되어 있고, 이를 html에 합치기 위해서는 {% raw %} {%%} {% endraw %} 나 {% raw %} {} {% endraw %}를 이용해야 합니다. 
- 따라서, 해당 특수문자를 그대로 마크다운에 작성하면 liquid에 포함되는 언어라고 생각하고 지킬에서 에러가 발생할 수 있습니다. 

```html 
{% raw %}
---
heading: I like cupcakes
---
<!doctype html>

<html lang="en">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>{{ page.heading }}</h1>
  </body>
</html>
{% endraw %}
```

## how to solve 

- 비교적 간단합니다만, 여기에 작성하기는 어려워서 [제가 질문한 스택오버플로우 링크](https://stackoverflow.com/questions/51372587/how-can-i-render-of-markdown-in-jekyll/51372642#51372642)를 링크합니다. 


