---
title: python - Django - block
category: python
tags: python programming django web template tag
---

## python - Django - block

- `base.html`은 다음처럼 정의되어 있다고 하겠습니다.
- 내부를 자세히 보면, block으로 표시된 부분이 있죠.

```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
  </head>
  <body>
    <!--
    - 아래의 block1, block2는 base.html을 상속받는
    다른 html 문서에서 내용을 대체할 수 있도록 만들어집니다.
    - 상속받는 문서에서 아무
    -->
    <h3> Block 1</h3>
    {% raw %}{% block block1 %} hidden block1 in base(default) {% endblock %}{% endraw %}

    <h3> Block 2</h3>
    {% raw %}{% block block2 %} hidden block2 in base(default) {% endblock %}{% endraw %}
  </body>
</html>
```

- `child.html`은 다음처럼 정의됩니다. `base.html`을 extends하고, 앞서 정의한 `block1`, `block2`를 대체해 줍니다.
- `block.super`를 사용하면, block에 원래 정의되어 있는 default 를 가져옵니다.

```html
{% raw %}{% extends "./base.html" %}{% endraw %}

{% raw %}{% block title %}
This ic Child html
{% endblock %}{% endraw %}

{% raw %}{% block block1 %}
{{block.super}}
This is Block11111
{% endblock %}{% endraw %}
```
