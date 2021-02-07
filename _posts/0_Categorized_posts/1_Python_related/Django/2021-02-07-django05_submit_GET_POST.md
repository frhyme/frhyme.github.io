---
title: python - Django - submit by GET, POST
category: python
tags: python programming django backend server form GET POST
---

## python - Django - submit by GET, POST

- 사용자가 html 문서의 `form` tag로부터 submit한 값을 컨트롤러가 전달받아서 처리해주는 작업을 정리합니다.

### template with form submit

- `DjangoProj1 > App1 > templates > App1 > child.html`에 다음 내용을 작성해줍니다.
- 보는 것처럼, GET, POST의 방식으로 submit하는 form을 2개 만들었습니다. 
- 두 form 요소는 모두 `/submitResult`라는 url로 입력값을 전달해줍니다. 따라서, 값을 입력하는 url과 입력받은 값을 전달해주는 url인 `/submitResult`를 모두 만들어 줘야 합니다.

```html
<h3> Submit by POST </h3>
<form action="/submitResult" method="post">{% raw %}{% csrf_token %}{% endraw %}
    <label>param1</label>
    <input name="param1Name">
    <button type="submit">Submit</button>
</form>

<h3> Submit by GET </h3>
<form action="/submitResult" method="get">{% raw %}{% csrf_token %}{% endraw %}
    <label>param2</label>
    <input name="param2Name">
    <button type="submit">Submit</button>
</form>
```

### url matching

- 사용자가 값을 입력하는 form 부분은 "/" 경로에 만들고, `MainController`가 담당합니다.
- 그 값은 "/submitResult"라는 경로로 넘어가도록 해주고, `SubmitResultController`가 담당합니다.

```python
from django.contrib import admin
from django.urls import path

from App1.views import MainController, SubmitResultController


urlpatterns = [
    path('admin/', admin.site.urls),
    # 얘는 값을 입력받는 form이 포함된 view이고
    path("", MainController.as_view()),
    # 얘는 사용자가 값을 입력하고 submit을 하면 그 값이 넘어가는 url이죠.
    path("submitResult", SubmitResultController.as_view())
]
```

### Controller

- `DjangoProj1 > App1 > views.py`에 다음을 정의해줍니다.
- `post`메소드는 값을 POST로 전달받았을 때 수행되는 메소드이고
- `get`메소든느 값을 GET으로 전달받았을 때 수행되는 메소드입니다.

```python
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse


class MainController(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'App1/child.html',
            context={}
        )


class SubmitResultController(View):
    def post(self, request, *args, **kwargs):
        print("POST METHOD")
        print(request.POST)
        # <QueryDict: {'csrfmiddlewaretoken': ['wZzZqOAs3DFwZ3c5ftjABzoNOOd9L7kQIyZnFoN0MFp9NaNgpQDyoJK6nhAXJgMi'], 'param1Name': ['afads']}>
        print(request.GET)
        # <QueryDict: {}>
        param1Name = request.POST.get('param1Name')
        return HttpResponse(
            f"POST :: input String :: {param1Name}"
        )

    def get(self, request, *args, **kwargs):
        print("GET METHOD")
        print(request.GET)
        param2Name = request.GET.get('param2Name')
        return HttpResponse(
            f"GET :: input String ::{param2Name}"
        )
```

### Run server

- 그 다음 서버를 실행한 다음, GET, POST의 각각의 방식을 사용해서 전달해보면 어떻게 다른지 확인할 수 있습니다.

```plaintext
python manage.py runserver
```
