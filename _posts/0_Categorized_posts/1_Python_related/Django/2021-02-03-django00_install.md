---
title: python - Django - install 
category: python
tags: python programming django web backend install
---

## python - Django

- [Django](https://www.djangoproject.com/)는 웹프로그래밍에서 가장 많이 사용되는 python 기반 프레임워크입니다. 저는 개인적으로 [flask](https://flask.palletsprojects.com/en/1.1.x/)가 쉽게 뚝딱뚝딱 만들기 좋아하기는 하지만, flask는 유지보수 측면에서 좀 어려움이 있는 것 같아요.
- Django 프레임워크는 HTML Template, DB와의 연결, http backend 서비스 등에 대해서 API를 제공해줍니다. 간단히 말하면 그냥 웹 서버를 구축할 때 필요한 기본적인 설정을 간단한 API로 처리할 수 있다는 이야기죠. 

### Django Version 

- Django의 버전은 A.B.C로 구분됩니다. 여기서 C는 Patch Release니까 공식은 A.B로 봐야죠. 2020년 2월 4일 기준으로 Django의 latest release는 3.1.6 버전입니다. 즉 공식버전은 3.1인데 6번의 patch release가 발생했다는 이야기죠.
- 사실 일단 공부하는 측면에서는 어떤 버전을 써도 상관없기는 한데요. 그래도 가능하면 오래 AS가 되는 LTS(Long Term Support)를 사용해보기로 합니다. LTS는 "일정기간 동안 기술 지원을 약속한다"를 말하는 용어죠. 즉 LTS가 유효한 기간동안은 해당 문제에 대해서 기술 문제가 생기면 기술적 지원을 해주겠다는 이야기입니다. 반면, non-LTS 버전의 경우는 새로운 버전이 나오면 기술적 지원이 끊깁니다.
- 오늘 날짜인 2021년 02월 03일을 기준으로 2.2 LTS 버전이 있고, 얘는 2022년 4월까지 기술지원이 보장됩니다. 따라서, 저는 Django 2.2 버전을 설치하겠습니다.

### Install Django

- Django를 설치하기 전에 가능하면 virtualenv나 conda등을 사용해서 프로젝트환경을 독립적으로 설치해주는 것이 좋습니다. 특히, python의 경우 서로 다른 패키지 간 의존성 충돌 문제들이 생기곤 해서 가능하면 이걸 꼭 해주세요. 저는 pyCharm을 python IDE로 사용하고 있기 때문에 여기서 conda를 사용해서 python 3.8 버전에 대해서 독립적인 환경을 구축해 주었습니다.
- django를 다른 python package와 동일하게 `pip`를 사용하여 LTS인 2.2 버전을 설치해 줍니다.

```plaintext
$ pip install Django==2.2
Collecting Django==2.2
  Downloading Django-2.2-py3-none-any.whl (7.4 MB)
     |████████████████████████████████| 7.4 MB 951 kB/s 
Collecting pytz
  Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
     |████████████████████████████████| 510 kB 20.2 MB/s 
Collecting sqlparse
  Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 1.3 MB/s 
Installing collected packages: sqlparse, pytz, Django
Successfully installed Django-2.2 pytz-2021.1 sqlparse-0.4.1
```

- 그리고 다음 command를 통해 현재 django의 버전을 확인할 수 있습니다.

```bash
Successfully installed Django-2.2 pytz-2021.1 sqlparse-0.4.1
$ django-admin version
2.2
```
