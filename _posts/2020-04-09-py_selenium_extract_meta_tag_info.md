---
title: Python - Selenium - Extract meta info. 
category: python-libs
tags: python python-libs seleinum
---

## Intro

- 우리가 보는 웹페이지는 크게 head, body로 구성되어 있죠. 그리고 head에는 `meta`로 작성된 아이들이 있는데, 보통 meta-data라고 무릅니다. 
- meta-data는 "데이터에 대한 데이터"라고 생각하시면 됩니다. 많은 경우, 우리가 보는 웹페이지에 직접 보여지지는 않지만, 현재 웹페이지에서 필요로 하는 문자인코딩 방식이라거나, 저자, 본 문서에 대한 설명 등 많은 자료들을 담고 있죠. 
- 물론, 그냥 웹서핑을 할 때는 몰라도 됩니다만, 다른 웹페이지로부터 필요한 정보들을 크롤링해서 가져올 때는 꽤 자주 필요하죠.

## Extract meta tag.

- 그러니까, 간혹 그 정보들이, meta tag에 포함되어 있는 경우들이 있습니다. 
- 저의 경우는 대략 다음과 같았습니다. 

```html
<meta property="article:published_time" content="2020-04-09T22:05:48+09:00" />
```

- 다음처럼 `browser.find_element_by_xpath`를 이용해서 긁으면 됩니다. 
- 대충 위와 아래를 비교해보면 잘 아실 것 같아서 굳이 더 설명을 추가하지는 않겠습니다. 

```python
from selenium import webdriver

# OPEN browser
browser = webdriver.Firefox()
browser.get("http://aaa.bbb.com")
x = browser.find_element_by_xpath("//meta[@property='article:published_time']")
print(x.get_attribute('content'))

browser.close()
```

## wrap-up

- 웹 크롤링을 하다보면 정말 다양한 방식으로 엉망이 되어 있는 웹페이지들을 발견하게 되는 것 같습니다. 혼돈 그 자체인것 같아요.

## reference

- [head 태그에는 무엇이 있을까? HTML의 메타데이터](https://developer.mozilla.org/ko/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML)