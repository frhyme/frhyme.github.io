---
title: selenium을 사용해봅시다. - 1편
category: python-lib
tags: python python-lib selenium web web-browser automation webdriver
---

## automate your work

- 데이터를 웹에서 긁어오고 싶은데, 너무 번거롭다는 생각이 들었습니다. 저는 좀더 게을러지고 싶고, 그러기 위해서는 저보다 컴퓨터에 일을 많이 시키는 것이 더 필요하다고 생각됩니다. 
- pycon2017에서 [[Dances with the Last Samurai] 개발자 없는 통계업무 부서에서 (Django)+(Pandas)+(Selenium)+(python-docx)으로 통계업무도구 만들기](https://www.pycon.kr/2017/program/210)라는 발표를 대충 들어본 적이 있습니다. 다시 말해서, 제가 웹에 있는 정보를 직접 긁어서(마치 웹브라우저에서 내가 직접 데이터를 가져오는 것처럼), 저장할 수 있다는 말인것 같아요. 
- 따라서, 한번 selenium을 사용해보기로 했습니다. 

## selenium

- [selenium](https://www.seleniumhq.org/)은 "**Selenium automates browsers**"이라고 합니다. 
- 뭐, 사용해보면 더 잘 알 수 있을 것 같아요. 그래서 일단 설치부터 합니다. 

```plaintext
conda install selenium
```

- 또한 selenium은 firefox와 부착이 잘 된다고 합니다. 따라서, [firefox도 설치합니다](https://www.mozilla.org/en-US/firefox/new/). 

- 그 다음 설치한 웹브라우저에 맞는 [selenium drive](https://github.com/mozilla/geckodriver/releases)를 설치해줍니다. 저의 경우는 맥 버전을 설치했습니다. 
  - 만약 geckodriver를 잘 인식하지 못할 경우 [스택오버플로우의 이 질문](https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path)을 참고하시면 좋습니다. 

## simple example 

### google search 

- 여기서는 "구글의 검색창에 일정 값을 입력하고, 그 페이지로 이동하려는 작업"을 수행합니다. [이 블로그](http://sacko.tistory.com/14)의 내용을 참고했습니다. 
- 우리가 여기서 알아야 하는 '요소'는 구글의 '검색창'이죠. 해당 요소의 html은 다음과 같습니다, 자세히 보면 눈에 띄는 몇 가지가 있죠. id, name, class 등. 
- 다행히도, selenium에서 요소를 `name`, `id`, `class`등으로 읽어들일 수 있습니다. 우리는 그 방식으로 원하는 소스를 읽으면 되구요. 

```html
<input class="gsfi" id="lst-ib" maxlength="2048" name="q" autocomplete="off" title="Search" type="text" value="" aria-label="Search" aria-haspopup="false" role="combobox" aria-autocomplete="list" dir="ltr" spellcheck="false" style="border: none; padding: 0px; margin: 0px; height: auto; width: 100%; background: url(&quot;data:image/gif;base64,R0lGODlhAQABAID/AMDAwAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw%3D%3D&quot;) transparent; position: absolute; z-index: 6; left: 0px; outline: none;">
```

```python
## google 검색
browser = webdriver.Firefox(executable_path='/Users/frhyme/Downloads/gecko/geckodriver')
## 브라우저에서서 다음 url로 접속합니다. 그럼 브라우저가 열리고, 해당 url로 접속합니다. 
browser.get('https://google.com')

## 페이지 소스에서 내가 원하는 요소는 tag_name, id, css_selector등으로 매우 다양하게 찾을 수 있습니다. 
## 일단 편하게 긁어오시고, 긁어오신다음에 만약 여러 개가 나올 경우에 더 구체적으로 찾아보면서 해보시는 게 좋아요. 
## 여기서는 일단 name으로 긁어왔습니다. 
elem = browser.find_element_by_name("q") 
## 이미 검색창에 어떤 값이 들어가있을 수 있기 때문에 해당 값을 지워줍니다. 
elem.clear()
## 값을 넣어주고, 
elem.send_keys("frhyme")## 
## 제출을 하면 해당 페이지로 이동하게 됩니다. 
elem.submit() ## 제출 
## 옮겨진 페이지에서 추가 작업을 하고 싶으면 여기서 진행하면 됩니다. 
#print(browser.page_source)
time.sleep(5)
## 브라우저 끄기
browser.quit()
```

### 메뉴읽기

- [여기](http://pythonstudy.xyz/python/article/404-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Selenium-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)의 내용을 참고했습니다. 단 이 블로그에는 다운받은 드라이버를 세팅하는 부분이 없어서 약간 고생했습니다. 

```python
from selenium import webdriver
import time
 
## 설치한 드라이버의 path를 웹드라이버에 함께 넘겨줍니다.
browser = webdriver.Firefox(executable_path='/Users/frhyme/Downloads/gecko/geckodriver')
## 브라우저에서서 다음 url로 접속합니다. 그럼 브라우저가 열리고, 해당 url로 접속합니다. 
browser.get("https://python.org")

## 브라우저에서 접근하려는 요소를 찾습니다. 
## 여기서는 css selector를 사용해서 찾았습니다. 
## 하지만 여기서 문제는, 제가 원하는 요소의 css selector가 무엇인지 어떻게 알 수 있을까요? 
menus = browser.find_elements_by_css_selector('#top ul.menu li')
for m in menus:
    print(m.text)## 해당 요소의 text를 출력합니다. 
    time.sleep(2)
browser.quit()
```

## do it

- 이제 저한테 필요한 부분을 코딩합니다. 
- 저는 웹에서 페이지의 특정 부분만을 데이터로 가져오는데, 페이지에 모든 내용이 다 뜨지는 않아서, 페이지를 넘겨가면서(1, 2, 3, 4 이렇게 되어있는 페이지넘버), 각 페이지에 있는 내용을 다 가져오려 합니다. 

### with dropdown menu

- 드롭다운이 있는 경우는 다음처럼 처리하면 됩니다.
  - [How to select a drop-down menu value with Selenium using Python?](https://stackoverflow.com/questions/7867537/selenium-python-drop-down-menu-option-value)

## wrap-up

- 웹의 데이터를 가져올때, 중요한 것은, 페이지를 서버에서 가져올만큼 충분히 여유시간을 고려해야 한다는 것입니다. 아직 서버로부터 데이터 소스를 다 받지 않았는데, 데이터를 가져오려고 할 경우에는 에러가 발생할 수 있다는 것이죠.

## reference

- [예제로 배우는 파이썬 프로그래밍 - 파이썬 selenium 사용하기](http://pythonstudy.xyz/python/article/404-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Selenium-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)
