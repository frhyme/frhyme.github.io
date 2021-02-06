---
title: python - Django - Run superbasic Server
category: python
tags: python programming django web backend MVC server
---

## python - Django - Run superbasic Server

- MVC니 다 필요 없고 일단 server를 띄워보도록 하겠습니다.

## View - index.html

- view는 사용자에게 보여지는 문서를 말합니다. 그냥 html 문서라고 생각해도 문제가 없죠.
- `DjangoProj1 > App > template > App1 > index.html`을 다음처럼 만들어 줍니다. 

```html
<!DOCTYPE html>
<head>
    <title>This is Title</title>
</head>
<body>
    <!--
    - Controller(Views.py)에서 View로 parameter를 전달할 수 있습니다.
    이 때, parameter는 dictionary로 넘어오는데 그 때 'param1'을 key로 쓰는 애를 가져옵니다.
    -->
    <h2> param1 {%raw%}{{param1}}{%endraw%} </h2>
    <p>index.html DjangoProj1 > App1 > templates > App1</p>
    <ul>
    <!--
    - for 문은 다음처럼 쓸 수 있습니다.
    -->
    {%raw%}{% for x in paramLst %}{%endraw%}
        <li>x: {{ x }}</li>
    {%raw%}{% endfor %}{%endraw%}
    </ul>
</body>
```

## Controller - views.py

- view를 정의해줬으니까, 이제는 view에 데이터를 전달해줄 수 있는 controller를 만들어 줍니다. 근데, controller의 이름이 `views.py` 라서 헷갈리기는 하죠.
- `DjangoProj1 > App1 > views.py`에 다음처럼 어떤 html template에 어떤 parameter를 전달해줄 것인지 정해줍니다.

```python
from django.shortcuts import render
from django.views import View


class TestController(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            # 어떤 view를 렌더링할 것인지 정해주고
            'App1/index.html',  
            # 해당 view에 전달할 data(context)를 정의하고 
            context={
                'param1': "xx",
                'paramLst': [1, 2, 3]
            }
        )
```

## Controller - urls.py

- 이제 사용자가 입력한 url이 어떤 페이지로 연결될지를 정해줍니다.
- 이 파일은 `DjangoProj1 > DjangoProj1 > urls.py`에 있습니다.

```python
"""DjangoProj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import path
# 만들어준 controller를 여기에 작성해주고,
from App1.views import TestController

# 만들어진 controller가 어떤 path에 연결될지를 정해줍니다.
urlpatterns = [
    path('', TestController.as_view()),
    path('ABC', TestController.as_view()),
]
```

## Configure settings.py

- `DjangoProj1 > DjangoProj1 > settings.py`을 수정해줍니다.

```python
# 사용자가 접속할 수 있는 route를 열어주는 것이죠.
# '127.0.0.1'는 localhost를 말합니다.
ALLOWED_HOSTS = [
    '127.0.0.1'  
]

# 새로 만든 App1을 등록해줘야 하고요.
INSTALLED_APPS = [
    ...
    'App1'  
]

# database 설정 부분도 여기서 해주는데, 저는 따로 사용하지 않습니다.
# 그냥 기본으로 설치되는 sqlite3를 일단 사용합니다.
DATABASES = {}
```

## RunServer

- 자 이제 다음을 실행해주고, 웹브라우저에서 `http://127.0.0.1:8000/`으로 접속하면 우리가 만든 웹페이지가 뜨는 것을 알 수 있습니다.

```plaintext
python manage.py runserver
```

## Wrap-up

- 일단 따라하니까 뭐가 되긴 하는데, 이게 왜 되냐...싶지만 일단은 그렇게만 알고 가시면 됩니다. 반드시 알아야 하는 것은 다음이죠.
  - View, Controller가 구분되어 있다. 즉 보여지는 부분은 html로 다 몰고, logic이나 데이터 전달 부분은 모두 controller에서 처리해준다.
  - "아니, 간단한 걸 만드는데 왜 View에도 쓰고, Controller에도 쓰고 귀찮다"싶을 수 있지만, 이렇게 구분해두는 것이 유지보수측면에서 매우 안정적이죠.
  - View의 문법은 jinja를 사용해서 쓴다.
  - `setting.py`에서 전체 시스템에 대한 설정값을 조정한다.
- 이정도인 것 같네요. 세부적으로 어떤지는 앞으로 차츰차츰 알아보도록 합시다.
