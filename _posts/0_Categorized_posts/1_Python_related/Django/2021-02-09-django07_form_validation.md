---
title: python - Django - Form
category: python
tags: python programming django backend server form
---

## python - Django - Form

- 보통 html에서 form 요소를 작성할 때는 다음과 같이 작성합니다.
- 간단한 input의 경우는 다음처럼 작성해도 아무 문제가 없습니다만, input이 여러 개이거나, 잘못된 input에 대해서 백엔드에서 프론트엔드로 메세지를 전달해주기 위해서도, front-end단보다 backend에서 처리해주는 것이 더 좋을 때가 있죠.

```html
<form action="/submitResult" method="post">
    <label>param1</label>
    <input name="param1Name">
    <button type="submit">Submit</button>
</form>
```

## Define Form class

- 따라서, `django.forms.Form`를 사용하여 다음과 같은 새로운 class를 만들어 줍니다.
- 사용자로부터 다음의 값들을 입력받겠다, 라는 이야기죠.

```python
# DjangoProj1/App1/forms.py
from django import forms

##############################
# Form 
class StudentCardForm(forms.Form):
    """
    - field에는 label만 작성해줍니다.
    - 그리고 http Request에 들어가서 넘겨갈 때 name은 다음처럼 변경됩니다.
    Name  -> student_name
    ID    -> student_id
    email -> student_email
    - 따라서, 위 값으로 접근해서 데이터를 가져올 수 있죠.
    """
    student_name = forms.CharField(
        label="Name", min_length=3
    )
    student_id = forms.CharField(
        label="ID", max_length=20
    )
    # 얘는 email이라서 email string으로 작성하지 않으면 제출되지 않습니다.
    student_email = forms.EmailField(
        label="email"
    )
```

## Define Controller

- 이제 `views.py`에 controller를 정의해줍니다.

```python
# DjangoProj1/App1/views.py
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
# 같은 경로에 있는 forms.py로부터 해당 class를 import합니다.
from .forms import StudentCardForm

##############################
# Controller
class MainController(View):
    # 사용자가 입력을 하는 view를 렌더링해줍니다.
    # context에 StudentCardForm를 생성해서 
    # template를 렌더링할때 같이 묻혀서 보내줍니다.
    def get(self, request, *args, **kwargs):
        context = {
            'StudentCardForm': StudentCardForm()
        }
        return render(
            request,
            'App1/child.html',
            context=context
        )


class SubmitResultController(View):
    # 사용자가 입력을 하고나면 그 결과가 보여지는 페이지입니다.
    def post(self, request, *args, **kwargs):
        # request로부터 값을 읽어서 정리하고 
        # context에 정리해서 보내줍니다.
        student = {
            "id"   : request.POST.get("student_id"), 
            "name" : request.POST.get("student_name"), 
            "email": request.POST.get("student_email")
        }
        context = {
            "student": student
        }
        return render(
            request, 
            "App1/submitResult.html", 
            context=context
        )        
```

## URL mapping

- URL을 mapping해줍니다.
- MainController에서 값을 입력받고, 입력받고 나면, `/submitResult`로 넘어가도록 해줍니다.

```python
# DjangoProj1/App1/views.py
from django.contrib import admin
from django.urls import path

from App1.views import MainController, SubmitResultController


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", MainController.as_view()),  # http://127.0.0.1:8000/
    path("submitResult", SubmitResultController.as_view())
]
```

## html 문서 작성

### submit.html 

- form 문은 다음처럼 작성해줍니다.

```html
<!--
DjangoProj1/App1/templates/App1/child.html
-->
<form action="/submitResult" method="post">
    {% raw %}{% csrf_token %}{% endraw %}
    <table>
        <!--
        - MainController에서 context로 전달받은
        StudentCardForm를 table의 형태로 변환하여 보여줍니다.
        -->
        {% raw %}{{ StudentCardForm.as_table }}{% endraw %}
    </table>
    <button type="submit">Submit</button>
</form>
```

- 이 부분은 html로 변환되면 다음과 같이 바뀌죠.

```html
<form action="/submitResult" method="post"><input type="hidden" name="csrfmiddlewaretoken" value="obhSnQp2TyJcaRUnhujL3cxgeBgouQbLAKHgCqCACAtPYYvyrRDJQmTzN4DcsZDd">
    <table>
        <tr>
            <th>
                <label for="id_student_name">Name:</label>
            </th>
            <td>
                <input type="text" name="student_name" minlength="3" required id="id_student_name">
            </td>
        </tr>
        <tr>
            <th>
                <label for="id_student_id">ID:</label>
            </th>
            <td>
                <input type="text" name="student_id" maxlength="20" required id="id_student_id">
            </td>
        </tr>
        <tr>
            <th>
                <label for="id_student_email">email:</label>
            </th>
            <td>
                <input type="email" name="student_email" required id="id_student_email">
            </td>
        </tr>
    </table>
    <button type="submit">Submit</button>
</form>
```

### submitResult.html 

- 그리고 form을 제출한 다음 연결되는 페이지도 만들어 줍니다.

```html
<!--
DjangoProj1/App1/templates/App1/submitResult.html
-->
<html>
    <head>

    </head>
    <body>
        <h2>Submit Result</h2>
        <p>student: {% raw %}{{student}}{% endraw %}</p>
        <p>id: {% raw %}{{ student.id }}{% endraw %}</p>
        <p>name: {% raw %}{{student.name}}{% endraw %}</p>
        <p>email: {% raw %}{{student.email}}{% endraw %}</p>
    </body>
</html>
```

## Run Server

- 그 다음 서버를 구동하고 결과를 보면 잘 되는 것을 알 수 있습니다.

```plaintext
python manage.py runserver
```
