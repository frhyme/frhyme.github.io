---
title: python - Django - CSRF protection
category: python
tags: python programming django backend server form GET POST
---

## python - Django - CSRF protection

- CSRF는 "Cross Site Request Forgery"의 약자로, 사용자의 의도와 상관없이 사용자의 요청(Request)에 다른 요청을 숨겨서 전송하도록 하는 방법을 말합니다. 가령 사용자가 특정 POST를 보낼 때, 여기에 다른 POST, GET등을 붙여서 함께 보내버릴 수 있다는 것이죠.
- 따라서, 사용자가 Request를 보낼 때 이 Request가 유효한지를 http Request에 함께 포함해서 보내버리도록 강제할 수 있습니다.
- django에서는 `csrf_token`이라는 일종의 난수를 사용해서 CSRF를 방어합니다. 아주 간단하게 설명하면 "사용자로부터 A라는 난수를 받고, 이 난수가 유효한지를 확인해서 유효할 경우 해당 Request를 진행하고, 아닐 경우 진행하지 않는다"라는 기능을 진행하죠.
- 어려워 보이지만, 그냥 다음처럼 form 요소 내에 `{% raw %}{% csrf_token %}{% endraw %}`를 처리해주면 끝납니다.

```html
<form action="/submitResult" method="post">
    {% raw %}{% csrf_token %}{% endraw %}
    <label>param1</label>
    <input name="param1Name">
    <button type="submit">Submit</button>
</form>
```

## Reference

- [djangoproject - csrf](https://docs.djangoproject.com/en/3.1/ref/csrf/)
