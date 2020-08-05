---
title: microframework을 알아봅시다. 
category: others
tags: flask micro-framework framework REST RESTful
---

## intro

- flask로 간단한 웹페이지를 만들어보는 작업을 하고 있습니다. 그 과정에서 다음 문장이 눈에 확 들어오더군요. 

> Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD licensed!

- 마이크로 프레임워크, 마이크로서비스 등 아키텍쳐들에 대해서 간단하게 들어본 적은 있는데 좀 제대로 개별 개념에 대해서 공부해 본 적은 적어요. 그래서 이번에 '마이크로 프레임워크'가 무엇인지 정리하면 어떨까 해서 글을 써 봤습니다. 

## micro-framework 은 무엇인가? 

- 무엇인가 를 정의하기 위해서는 반대되는 개념을 떠올리는 것이 더 좋을 때가 있습니다. 즉 micro-framework의 반대개념이 무엇인지를 보면 되는데, 반대되는 개념은 **monilithic-deployment**라고 합니다. 
![](https://docs.microsoft.com/ko-kr/dotnet/standard/microservices-architecture/architect-microservice-container-applications/media/image6.png)

- 위의 그림에서 보시면 monolitic의 경우 하나의 독립된 앱 별로 같은 기능들이 여러 개 중복 개발되어 있습니다. 이를 다르게 표현하자면 **제품 지향적 조직구조**로 볼 수도 있을 것 같아요. 
- 그러나 micro-framework 에서는 가능한 모든 서비스를 분할해서 관리하고, 필요할 때마다 서비스간의 통신으로 연결하여 거대한 서비스를 만든다, 는 개념을 가지고 있습니다. 
- 물론 개별 마이크로서비스의 범위는 어느 정도로 커야 하는가? 어떻게 만들어야 좀 더 general한 app이라고 할 수 있는가? 등의 이슈들이 뒤따르지만, 기본 개념은 서비스의 모든 시스템을 micro하게 api형태로 관리하자는 것이 마이크로서비스가 말하려는 가장 중요한 부분입니다. 

## bounded context 

- bounded context는 한국말로 한다면 **갇혀진 맥락**이라고 허접하게 번역할 수 있겠죠. 
- 앞서 말한 바와 같이 micro-service를 만들기 위해서는 개별 맥락을 명확하게 구분해주는 것이 필요합니다. 어디를 어떻게 끊어주는 것이 좋은가? 어디를 어떻게 끊어야 적절하게 context를 구분하여 표현할 수 있을까? 

## RESTful 

- 아주 간단하게는 모든 api들간에 http로 통신하는 것이라고 생각하면 될 것 같습니다. 

## flask is micro-framework 

- flask는 왜 micro-framework인가? 라고 묻는다면 
    - 개별 uri가 하나의 마이크로서비스 
    - 필요할 때 다른 마이크로서비스 `url_for`를 이용하여 통신
- 이기 때문이다, 라고 할 수도 있겠네요.

## reference 

- <https://zetawiki.com/wiki/마이크로서비스>
- <https://zetawiki.com/wiki/바운디드_컨텍스트>