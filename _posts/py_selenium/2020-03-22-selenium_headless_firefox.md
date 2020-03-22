---
title: Selenium - headless firefox
category: python-libs
tags: python selenium python-libs firefox
---

## selenium with headless

- selenium은 python을 이용해서 웹브라우저를 컨트롤하는 라이브러리입니다. 즉, 웹에서 필요한 정보들을 비교적 자유롭게 크롤링해서 가져올 수 있다는 장점이 있죠. 
- 다만, 그냥 selenium을 실행하면, 컴퓨터에 웹브라우저가 떠 있게 됩니다. 뭐, 어떤 분들은 신경쓰이지 않을 수 있지만, 저는 꽤나 신경 쓰이더군요. 그래서, 브라우저를 띄우지 않고, 웹브라우징을 할 수 있는 방법을 찾아봤습니다. 
- 그리고, 이런 방법을 "Headless"라고 부르더군요. 
- 저는 파이어폭스를 사용하였고, 다음과 같이, 간단한 코드를 추가하여, 창없이 알아서 돌아가도록 처리했습니다. 

```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
```