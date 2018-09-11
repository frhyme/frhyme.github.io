---
title: scopus에서 서지정보 가져오기(fail)
category: python-lib
tags: python scopus python-lib selenium pandas html 
---

## start and fail. 

- 원래는 selenium을 이용해서 직접 scopus에서 데이터를 일일이 가져오는 식으로 처리하려고 했습니다만, 혹시나 해서 찾아보니, 이미 [scopus를 편하게 쓸 수 있는 라이브러리](https://github.com/scopus-api/scopus)가 만들어져있었습니다. 

- 일단 설치합니다. 

```bash
pip install scopus
```

- 하지만, api key를 입력해야 하는군요. 
- 또한, 웹에서 데이터를 크롤링해서 가져오려고 해도, scopus에서는 한번에 2000개밖에 읽을 수 없습니다(페이지를 넘겨도, 더이상은 넘어가지 않아요).
- 다시 말해서, db를 구축하려면, 일일이 2000개 미만으로 페이퍼를 잘라가면서, 진행해야 한다는 이야기죠. 
- 제가 직접 하루정도동안 웹에서 데이터를 일일이 가져오는 코드를 만들었는데, 실패한 이유는 위와 같이 2000개 이상 데이터를 가져오기가 힘들기 때문이었습니다. 

- 만든 코드가 아까워서, 일단 여기에 작성해두기는 하는데, 쓸모없는 코드가 되어버렸습니다. 

## raw code

```python
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd 

 
## 설치한 드라이버의 path를 웹드라이버에 함께 넘겨줍니다.
def find_title_and_url(search_terms, page_num=5):
    ## 이미 scopus에서 원하는 페이지를 검색한 다음 시작. 
    browser = webdriver.Firefox(executable_path='/Users/frhyme/Downloads/gecko/geckodriver')
    browser.get("https://scopus.com")
    time.sleep(5)
    elem = browser.find_element_by_name("searchterm1") 
    elem.clear()
    elem.send_keys(" or ".join(search_terms))
    elem.submit()
    time.sleep(10)

    paper_df = []

    ## find selected page num 
    for i in range(0, page_num):
        ## 해당 페이지의 데이터를 읽습니다. 
        print(f"page: {i}")
        for j in range(0, 20):
            a_tag = browser.find_element_by_id("resultDataRow{}".format(j))
            a_tag = a_tag.find_element_by_tag_name('td')
            a_tag = a_tag.find_element_by_tag_name('a')
            paper_df.append((a_tag.text, a_tag.get_attribute('href')))
            #print(f"title: {a_tag.text}"), print(f"text: {a_tag.get_attribute('href')}"), print("="*20)

        ## page 요소를 찾고 
        pagination = browser.find_element_by_class_name('pagination')
        ## selectedPage 클래스를 가진 요소를 찾고, 해당 data-value를 저장한 다음 
        for page in pagination.find_elements_by_tag_name('li'):
            try:
                a_tag = page.find_element_by_tag_name('a')
                if a_tag.get_attribute('class')=='selectedPage':
                    selected_num = a_tag.get_attribute('data-value')
                    #print(f"find selected num {selected_num}")
                    break
            except:
                continue
        ## move to next page 
        ## selectedPage보다 하나 큰 값을 가진 페이지를 click 
        for page in pagination.find_elements_by_tag_name('li'):
            try:
                a_tag = page.find_element_by_tag_name('a')
                if a_tag.get_attribute('data-value')==str(int(selected_num)+1):
                    #print(f"move to page {a_tag.get_attribute('data-value')}")
                    page.click()
                    time.sleep(10)
                    break
            except:
                continue
    print('complete')
    return paper_df
paper_df= find_title_and_url(['entrepreneurship', 'entrepreneur', 'sme'], 500)
paper_df = pd.DataFrame(paper_df, columns=('title', 'url'))
paper_df.to_json(f'/Users/frhyme/Dropbox/entrepreneur.json')
```