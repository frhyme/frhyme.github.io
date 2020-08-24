---
title: Selenium - select button
category: python-libs
tags: python selenium python-libs firefox
---

## selenium - select button 조정하기

- selenium으로 웹브라우저를 조종하면서, 그 과정에서 웹페이지를 크롤링해올 때, "10개씩 보기", "20개씩 보기", "50개씩 보기", "100개씩 보기"와 같은 버튼을 볼 때가 있습니다. 
- 당연히 이럴 때면, "100개씩 보기"를 눌러서, 한 번에 많은 양의 데이터를 긁어오는 것이 좋죠. 
- 저는 다음의 코드를 사용해서 해결했습니다.

```python
from selenium.webdriver.support.ui import Select
select_button = Select(browser.find_elements_by_name("S_ROWS")[1])
select_button.select_by_value("100")
```
