---
title: python - Django - Start Django Project
category: python
tags: python programming django web backend 
---

## python - Django - Start Django Project

- Django, Spring, ROR(Ruby On Rails)는 모두 MVC(Model - View - Controller)라는 패턴을 따릅니다. MVC는 특정 언어에 국한된 것이 아니라, 소프트웨어 설계적인 접근인데 각각 다음과 같은 의미를 가지죠.
  - M(Model): DB와 같은 데이터적인 부분을 칭하며
  - V(View): 사용자에게 보여지는 부분, 아주 간단하게는 html 문서를 말하는 것이고
  - C(Controller): Model로부터 View까지의 데이터를 컨트롤하죠.

## Start django project

- django를 설치한 다음, `django-admin startproject projectName`를 사용해서 새로운 django 프로젝트를 만들어 줍니다.
- 그리고, 프로젝트 내부에서 새로운 어플리케이션을 만들어주기 위해서는 `django-admin startapp appName`을 사용하죠. 하나의 프로젝트 내에는 여러 App이 존재할 수 있습니다.
- 이를 순서대로 진행해보면 다음과 같이 진행되죠.

```plaintext
$ django-admin startproject DjangoProj1
$ ls                                               
DjangoProj1 main.py
$ cd DjangoProj1                                                                   
$ ls
DjangoProj1 manage.py
$ django-admin startapp App1
$ ls
App1        DjangoProj1 manage.py
```

### Model 

- 각 App마다 `models.py`에 DB operation과 관련된 모든 내용이 저장됩니다. `django.contrib.auth.models`에 존재하는 `User`, `Group`을 사용할 수도 있죠.

### View

- View는 template에 저장되며, Django/Jinja2 template language를 사용해서 정의됩니다. 일단은 그냥 html 문서라고 생각해도 상관이 없죠.
- 얘는 `models.py`와 다르게 바로 만들어지는 것이 아니라, 직접 만들어줘야 합니다. 저는 app 내에 `templates`라는 폴더를 만들어줍니다. 이 폴더 내에 html 문서를 모두 저장할 거에요.
- 다만, 좀 특이하게도 구조가 `appName/template/appName`의 방식으로 `appName`이 중복으로 들어가도록 되어 있죠. 이건 선택이 아니라, django template loader가 저렇게 되어야만 돌아가기 때문입니다. 일단은 외우도록 하죠.

```plaintext
$ cd App1
$ ls
__init__.py admin.py    apps.py     migrations  models.py   tests.py    views.py
$ mkdir templates
$ ls
__init__.py admin.py    apps.py     migrations  models.py   templates   tests.py    views.py
$ cd templates
$ mkdir App1
$ ls
App1
$ cd App1
```

### Controller

- Controller에는 `DjangoProj1/App1` 폴더 내에 있는 `views.py` 파일과, `DjangoProj1/DjangoProj1` 폴더내에 있는 `urls.py`로 구분됩니다.
  - `views.py`: 이름이 View라고 되어 있어서 헷갈릴 수 있지만, 여기서 Model, View간의 데이터 흐름을 제어합니다.
  - `urls.py`: 여기서는 사용자의 요청에 따라서 적합한 파일을 routing해주는 부분을 처리합니다.

## Wrap-up

- 사실 이렇게 말로 풀면 몰라요. 근데 몇 번 슥슥 코딩해보면 금방 무슨 말인지 이해됩니다 호호.
