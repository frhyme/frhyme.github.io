---
title: what is wsgi?
category: others
tags: wsgi protocol web flask django
---

## intro

- 요즘은 python의 web framework인 flask를 이용해서 웹서버를 구축해보고 있습니다.
- 그런데 flask를 이용하다 보면, wsgi라는 말이 나옵니다. 뭐 굳이 몰라도 서버 세팅하고 돌리는 데는 큰 문제가 없습니다. 하지만 블로그를 운영하게 된 다음부터는 잘 모르는 개념이 나오면 꼭 정리를 해서 블로그에 써야겠다는 생각을 많이 하게 되더라고요. 
- 그래서 다음 가지에 대해서 정리를 해보려고 합니다. 
    - WSGI의 개념과 유래 
    - flask와 WSGI와의 관계성

## 그래서 wsgi는 무엇인가요? 

- 풀어서 보면 Web Server Gateway Interfact(WSGI)입니다. 
    - 음, 정확히는 몰라도, web server를 구축할 때 web server와 통신하기 위한 일종의 규약 정도로 해석하면 될것 같네요. 
- [wsgi.org](https://wsgi.readthedocs.io/en/latest/what.html)에서는 다음처럼 정리하고 있습니다. 

>  It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request. WSGI is a Python standard described in detail in PEP 3333.

- 웹서버와 웹 어플리케이션이 서로 통신하기 위한 명세이며, request를 처리하기 위해서 web application이 어떻게 연결되어 있는지를 기술하는 방식, 정도로 설명할 수 있겠네요. 또한, python PEP 3333에서 파이썬의 표준으로 채택되기도 했습니다. 

- [위키피디아에 작성된 내용](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)을 보면 좀 더 명확해질 수 있습니다. 
- 정리하면, 웹서버가 있고(apache 등으로 구성된), 어플리케이션이 있을때(파이썬으로 구동되는), 웹서버와 어플리케이션을 연결해주는 규약이 WSGI라고 생각할 수 있습니다. 


## 정리 

- 우리가 흔히 말하는 웹서비스는 유저(client)로부터 url과 특정 명령을 받아서, 유저가 원하는 내용을 브라우저 상에서 뿌려주는 것을 말합니다. 이 측면에서 해당 내용을 다시 정리해보면 다음과 같습니다. 
    - http 리퀘스트가 들어옴: 유저가 브라우저에서 http request를 서버로 전송함
    - 웹 서버는 그 리퀘스트를 받아서 처리하기 위해서 wsgi 미들웨어와 연결됨
    - wsgi 미들웨어는 파이썬 어플리케이션으로 해당 내용을 전달
    - 파이썬 어플리케이션에서 해당 내용을 적절히 처리하고, 
    - wsgi 미들웨어, 웹서버로 전달하게 됨 

## wrap-up

- 제가 대략 정리를 하기는 했는데, 제 글보다는 [여기의 내용](https://brownbears.tistory.com/350)이 더 상세하게 작성되어 있는 것 같습니다. 
    - 과거의 개념에서는 서버와 웹 어플리케이션을 구분해서 설명했는데 요즘에는 웹서버 = 서버 + 웹 어플리케이션이라는 것. 
- WSGI는 파이썬에 종속되어 있는 개념으로 보는 것이 좋다. [wsgi를 이용한 프레임워크들](https://wsgi.readthedocs.io/en/latest/frameworks.html)은 대부분 python을 활용한 프레임워크들이라는 것
