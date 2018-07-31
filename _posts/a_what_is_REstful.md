---
title:
category:
tags: 
---

## RESTful??

- Rest(Representational State Transfer)Ful. 

- "하나의 클라이언트를 위한 하나의 서버"라는 개념은 올드함. "여러 클라이언트를 위한 하나의 서버"가 더 효율적인 방법

- URI(Uniform Resource Identifier)를 통해 리소스를 접근하는 것

- <http://www.chidoo.me/index.php/2016/06/03/what-is-restful/> 이 내용을 좀 더 파악하면 제대로 알 수 있을 것 같은데 

## 알게 된 것

- RESTful이란 
    - 정의한 함수/객체/데이터 모두 URI의 형태로 접근하고
    - 데이터를 읽고/쓰고/업데이트하는 것은 모두 CRUD와 마찬가지로 http method(POST, GET, PUT) 등을 사용하여 접근하고 
    - 현재 클라이언트의 상태를 절대로 서버에서 관리하지 않아야 한다??
        - 이전에 로그인을 했다고 해도, 여기서는 그 전의 로그인한 세션 혹은 상태에 대해서 알수 없다 라는 이야기인가? 
        - 이를 통해 개별 서비스(특히 마이크로서비스 아키텍쳐에서)는 구현이 단순화되고, 개별 단위의 마이크로서비스 들이 하나의 서버처럼 동작할 수 있다. 

- SOAP 와의 차이점 
    - SOAP : HTTP, SMTP 등을 통해 XML 기반의 메시지를 컴퓨터 네트워크 상에서 교환하는 프로토콜

- 마이크로서비스 아키텍쳐와의 연결성

## REST 

- 개별 자원은 모두 객체화되어 URI로 접근 가능함.
- http method를 사용하여 자원을 활용(DB에서의 CRUD 와 동일하다고 봐도 상관없음)

## reference

- <http://chomskychomsky.tistory.com/33>
- <https://lalwr.blogspot.com/2016/01/restful.html>
- <http://blog.remotty.com/blog/2014/01/28/lets-study-rest/>