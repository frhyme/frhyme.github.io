---
title: URL, URI 그리고 URN 의 차이점은?? 
category: others
tags: url uri html 
---

## what is resource?

- URI, URL, URN 모두 **uniform Resource**를 공통으로 포함하고 있습니다. 즉, 우선 Resource가 무엇을 칭하고 있는지를 명확하게 짚고 넘어가는 게 필요할 것 같은데요. 여기서 말하는 'resource'란 일단은 그냥 '파일'이라고 생각하셔도 무방합니다. 
- html, js, gif 등 브라우저를 통해서 접근하는 모든 파일들을 일단은 resource라고 생각하시면 될것 같아요. 

## URI

> A Uniform Resource Identifier (URI) is a string of characters designed for unambiguous identification of resources and extensibility via the URI scheme.

- "자원을 식별할 수 있는 문자열"이라고 해석하는 것이 가장 적합하겠네요. 
- 일단 여기서, URI와 URL과의 차이점이 있다고 하는데, 이는 일단 URL을 설명하면서 진행하겠습니다. 

## URL

- 우리가 가장 흔하게 알고 있는 웹주소의 개념인데, 

> A Uniform Resource Locator (URL), colloquially termed a web address,[1] is a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it. A URL is a specific type of Uniform Resource Identifier (URI),[2] although many people use the two terms interchangeably.

- URL은 web address라고도 칭해지는데, "컴퓨터 네트워크 상에서 해당 자원의 위치"를 의미한다고 보는 게 좋을 것 같네요.
- URL은 Uniform Resource Identifier가 특화의 형태로 볼 수도 있다는데, 따라서 다음으로 표현될 수 있습니다.
    - 모든 URL은 URI: 앞서 말한 바와 같이 URI는 "자원을 식별할 수 있는 문자열"을 말합니다. 즉, 웹주소에 쳐서 들어가지는 문자열이면 다 URI라고 할 수 있고요, 당연히 URL도 URI가 됩니다. 
    - 그러나, 어떤 URI는 URL이 아니다

## 그렇다면, URL이 아닌 URI는?? 

- 다시 정리하면
    - URL: 웹상의 자원의 위치
    - URI: 자원을 식별할 수 있는 문자열 
- 즉, URL이 아닌 URI는 "자원의 실제 위치는 아닌데, 자원을 식별할 수 있는 문자열"을 의미합니다.
- 예전에는 웹에서 새로운 페이지로 간다는 것이 "웹의 다른 자원"으로 이동한다는 것이었던 반면, 지금은 해당 주소에 임의의 다른 가상의 자원을 만들어서 배치할 수 있기 때문에, URL이 아닌 URI가 더 많이 쓰이는 것이 아닐까 싶습니다. 

- 예를 들어, 아래와 같은 주소가 있다고 할 때, 해당 주소는 특정한 자원의 주소를 말하는 것이 아니라, 가상의 자원에 대한 정보를 담고 있다고 할 수 있을 것 같습니다. 

```
https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=frhyme
```

## wrap-up

- 제대로 이해하고 있는건지 모르겠지만....큰 그림은 맞을 것 같습니다 하하핫