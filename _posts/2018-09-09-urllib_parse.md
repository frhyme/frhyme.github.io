---
title: urllib.parse
category: python-lib
tags: python python-lib urlparse urllib http
---

## url을 parsing합시다. 

- [urllib](https://docs.python.org/3/library/urllib.html)이라는 라이브러리가 있습니다. 저는 웹에서 데이터를 긁어오는 짓을 많이 하지는 않고, 해도 `requests`를 사용할때가 더 많기는 한데, 아무튼. 
- 기본적으로는 해당 url의 데이터를 가져오기 위해서 `urllib.request.urlopen`을 많이 사용합니다. 
- 여기서는 url 자체를 파싱하는 방법을 소개합니다. 매우매우매우 간단합니다. 심지어 다 [여기](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse)에 있는 내용들이구요. 

## urllib.parse

> This module defines a standard interface to break Uniform Resource Locator (URL) strings up in components (addressing scheme, network location, path etc.), to combine the components back into a URL string, and to convert a “relative URL” to an absolute URL given a “base URL.”

- url 스트링을 다양한 정보요소에 따라서 쪼갭니다.   
    - 해당 정보요소에는 scheme, network location, path 등이 포함될 수 있구요. 
    - 다만 아쉬운 것은, 결과가 dictionary의 형태로 나오는 것이 아닙니다. 따라서 각요소를 각각 출력해줘야 하죠. 

- 몇 가지 url에 대해서 다음처럼 parsing을 해봤습니다. 딱히 어려운 부분은 없어요. 

```python
from urllib.parse import urlparse

test_url_lst = [
    "https://docs.python.org/3/library/urllib.parse.html", 
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=urllib", 
    "http://localhost:5000/mine"
]

for test_url in test_url_lst:
    x = urlparse(test_url)
    print(f"url: {x.geturl()}")
    print(f"scheme: {x.scheme}")
    print(f"netloc: {x.netloc}")
    print(f"relative path: {x.path}")## relative path 
    print(f"params: {x.params}")
    print(f"query: {x.query}")
    print(f"port: {x.port}")
    print("="*50)
```

```
url: https://docs.python.org/3/library/urllib.parse.html
scheme: https
netloc: docs.python.org
relative path: /3/library/urllib.parse.html
params: 
query: 
port: None
==================================================
url: https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=urllib
scheme: https
netloc: search.naver.com
relative path: /search.naver
params: 
query: where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=urllib
port: None
==================================================
url: http://localhost:5000/mine
scheme: http
netloc: localhost:5000
relative path: /mine
params: 
query: 
port: 5000
==================================================
```

## wrap-up

- 저는 blockchain을 간단하게 만들어보다가, 중간에 `urllib.parse`가 들어가길래 내용을 정리해봤습니다. 
- 간단하게 url도 하나의 정보고, 잘 parsing해주는 것이 필요하다. 그리고 언젠가 쓰일 것 같다, 정도까지는 알겠지만, 제가 서버 작업을 하는 것도 아니고, 이 라이브러리를 사용하게 될 일이 있을까? 하는 생각은 아주 잠깐 들긴 하네요. 

## reference 

- <https://docs.python.org/3/library/urllib.parse.html>