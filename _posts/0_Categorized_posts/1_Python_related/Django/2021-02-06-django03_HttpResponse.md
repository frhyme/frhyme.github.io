---
title: python - Django - HttpResponse
category: python
tags: python programming django web backend server http
---

## python - Django - HttpResponse

- Controller에서 String을 `HttpResponse`에 묻혀서 View로 보내는 방법을 정리하였습니다.

## views.py - MainController

- 우선 Controller를 만들어 줍니다.
- `DjangoProj1 > App1 > views.py`에 새로운 컨트롤러를 추가해줍니다. 
- 컨트롤러 내부에서는 `HttpResponse(String)`의 형태로 리턴을 해줍니다. http의 응답방식에 맞게 변형해서 리턴한다는 이야기죠.

```python
from django.shortcuts import render
from django.views import View
# HttpResponse import
from django.http import HttpResponse


class MainController(View):
    def get(self, request, *args, **kwargs):
        # django에서는 get method가
        # GET request에 대응합니다.
        # 그리고 post method는 POST request에 대응되죠.
        result_str = "abcdefg"
        # string을 HttpResponse에 묻혀서 HttpResponse처럼 보내줍니다.
        return HttpResponse(result_str)
```

## urls.py - url pattern matching

- `DjangoProj1 > DjangoProj1 > urls.py`에서 다음 내용을 추가해줍니다.

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import path
from App1.views import MainController


urlpatterns = [
    # http://127.0.0.1:8000/AA
    path("AA", MainController.as_view()),
]
```

## runserver

- 그 다음 서버를 실행하고, `http://127.0.0.1:8000/AA`에 접속하면 잘 되는 것을 알 수 있습니다.

```plaintext
python manage.py runserver 
```
