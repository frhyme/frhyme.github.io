---
title: beautifulsoup4 기본.
category: python-lib
tags: python python-lib html xml beautifulsoup http requests
---

## intro

- 웹에서 데이터를 가져오고 있습니다. 찾아보니 html문서를 파싱하는데는 `beautifulsoup4`가 매우 유용한다는 이야기가 있어서, 이 이아이를 간단하게라도 사용해보려고 합니다. 

## beautifulsoup4 

> Beautiful Soup is a Python library for pulling data out of HTML and XML files.

- 즉, 이미 제가 가지고 있는 xml, html 문서들을 잘 파싱하여, 의미있는 정보(data)로 도출해내는 작업을 `beautifulsoup4`가 도와줍니다. 

- 우선은 언제나 그렇듯이 설치부터 합니다. 

```bash
conda install beautifulsoup4
```

## do it 

- 조금 특이한 것은 `beautifulsoup4`를 설치했는데, `import bs4`를 하는군요. 


```python
## 요즘에는 웹에서 데이터를 가져와야 하는 일들이 많아졌습니다. 
## 따라서, beautifulsoup이라는 라이브러리를 사용해서 html문서를 파싱하는 작업을 해보기로 합니다. 
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
## BeautifulSoup 에 html 데이터와 파서를 넣고 인스턴스를 생성해줌
soup = BeautifulSoup(html_doc, 'html.parser')
def prettify(input_soup, indent_level = 1):    
    ## pretiffy에서는 indetation level을 조절할 수 없음
    ## 기본적으로는 1칸씩만 주어지는데, 이는 가독성이 좋지 못하여 임의로 코드를 작성해서 아래처럼 변경함.
    for s in soup.prettify().split("\n"):
        non_blank = 0 
        for i in range(0, len(s)):
            if s[i] != " ":
                non_blank = i
                break
        print(" "*(indent_level-1)*non_blank + s)
prettify(soup, 2)
```

```html
<html>
  <head>
    <title>
      The Dormouse's story
    </title>
  </head>
  <body>
    <p class="title">
      <b>
        The Dormouse's story
      </b>
    </p>
    <p class="story">
      Once upon a time there were three little sisters; and their names were
      <a class="sister" href="http://example.com/elsie" id="link1">
        Elsie
      </a>
      ,
      <a class="sister" href="http://example.com/lacie" id="link2">
        Lacie
      </a>
      and
      <a class="sister" href="http://example.com/tillie" id="link3">
        Tillie
      </a>
      ;
and they lived at the bottom of a well.
    </p>
    <p class="story">
      ...
    </p>
  </body>
</html>
```


```python
## soup는 객체처럼 hierarchical하게 값을 내려가면서 원하는 value를 찾을 수 있다. 
## 또한 다음처럼, tag를 attribute처럼 접근하는 것이 가능함은 물론, parent, children 등을 사용할 수도 있음. 
print(soup.title)
## tag name 
print(soup.title.name)
## 내부의 string
print(soup.title.string)
print("="*20)
## tag가 'p'인 것 모두 찾기 
for x in soup.find_all('p'):## tag는 그냥 스트링으로 넣어도됨. 
    if x['class'][0]=='story':
        print(x)
print("="*20)
## 전체에서 id가 link3인 것을 모두 찾고, 첫번째만 가져오기
print(soup.find_all(id='link3')[0])
print("="*20)
##텍스트만 뽑아서 출력하기 
print(soup.get_text())
```

```
<title>The Dormouse's story</title>
title
The Dormouse's story
====================
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
====================
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
====================

The Dormouse's story

The Dormouse's story
Once upon a time there were three little sisters; and their names were
Elsie,
Lacie and
Tillie;
and they lived at the bottom of a well.
...

```

## wrap-up

- 이제 `requests`로부터 html 문서를 가져오고, 거기서 파싱해서 사용하면 될 것 같습니다. 
- 하나 참고할 사실은, 해당 웹페이지에서 아무 정보나 막 가져올 경우에, 해당 서버에 과부하를 일으킬 수 있습니다. 일종의 bot으로 작동하는 것이죠. 따라서, 지나치게 큰 데이터를 웹에서 막 가져오는 것은 문제가 될 수 있으니, 지양하는 것이 좋습니다. 