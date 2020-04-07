---
title: 한국 힙합씬 피쳐링 네트워크 분석 - 1편 - Data Collection
category: python-libs
tags: python python-libs selenium data-crawling 
---

## 한국 힙합씬 피쳐링 네트워크 분석. 

- 저는 대상/현상을 네트워크로 모델링하고 네트워크 적인 분석 법을 사용하여 대상 네트워크를 분석하는 일을 주로 수행합니다. 그리고, 그러다보니, 세상의 많은 현상들을 결국 "네트워크"적으로 바라보게 되죠. 
- 동시에 저는, 한국 힙합의 오랜 팬이기도 합니다. 힙합음악의 흥미로운 점은, 여러 뮤지션들이 다른 뮤지션들의 음악에 협업의 이름으로 참가하는 일이 매우 활발하다는 것이죠. 
- 저는 궁금했습니다. 과연, 한국 힙합의 피쳐링은 어떤 형태로 구성되어 있을까? 만약 이를 네트워크로 구성한다면 어떻게 구성해야 할까? 구성된 네트워크는 어떤 분석을 하면 재미있는 결과가 나올 수 있을까? 와 같이요. 
- 그래서, 저는 그동안의 한국 힙합 데이터를 모두 웹에서 크롤링하여 네트워크를 구성하고 그 결과를 정리하였습니다. 
- 분석 결과는 [한국 힙합 피쳐링 네트워크 분석](https://docs.google.com/presentation/d/1zkOGBTD0UTaeoxYLxkPohNXaaKWYjVXfdbHgrli8xms/edit#slide=id.p) 에서 발표자료로 보실 수 있습니다.

- 이 글에는 분석 과정과 어려움에 대해서 비교적 상세하게 작성할 예정입니다. 

## Data Collection.

- 목적은 분명합니다. "한국 힙합 뮤지션들의 피쳐링 네트워크를 구축하고 분석해보자"라는 것이죠. 그리고 이를 위해서는 우선 데이터를 수집하는 것이 필요합니다. 
- 저는 [한국 음악 저작권 협회](https://www.komca.or.kr/CTLJSP)로부터 데이터를 가져왔습니다. [한국 음악 저작권 협회](https://www.komca.or.kr/CTLJSP)에서 데이터를 검색할 수있는 방법은 다음 4가지입니다. 
    - 저작물명: 노래 및 가사 단위로 텍스트 검색 
    - 앨범명: 앨범의 제목에 대해서 텍스트 검색
    - 가수명: 가수 이름에 대해서 텍스트 검색 
    - 저작자명: 가수(뮤지션)의 고유 ID를 사용하여 검색. 
- 이중에서 가장 정확하게 데이터를 수집할 수 있는 곳은 "저작자명"이죠. 저작자명은 한국 음악 저작권 협회에서 관리하는 각 가수별 고유ID라고 보시면 됩니다. 가령 박재범의 ID는 `"10000556"`입니다. 저작자별로 중복되지 않도록 데이터를 일관적으로 관리하기 위한 방법이죠. 
- 따라서, 저작자명을 정확하게 알 수 있다면, 여기서 데이터를 수집하는 것이 가장 효과적입니다. 그리고 이 저작자명은 검색결과에 "가수명(저작자명)"으로 출력되기 때문에, 쉽게 알 수 있죠. 
- 다만, 저작권협회에 등록되어 있지 않은 "비관리"가수들의 경우는 `z9999900`으로 표기됩니다. 가령 이센스의 노래 "꽐라"의 경우를 보면 이센스가 협회에 등록되어 있지 않음을 알 수 있고 `z9999900`으로 ID가 표기되어 있음을 알 수 있죠. 
- 만약 여기서 `z9999900`을 이센스의 ID로 인지하고 검색하게 되면, "협회에 등록되어 있지 않은 모든 저작권자의 노래"들이 검색되기 때문에, 데이터에 문제가 발생하게 됩니다. 

## Data crawling. 

- 우선, 저는 selenium을 사용해서 데이터를 크롤링했습니다. 해당 라이브러리의 사용법의 경우 웹을 찾아보시면 이미 아주 다양하게 존재하므로 제가 이 부분에 대해서 자세하게 설명하지는 않겠습니다. 다만, 그러함에도 대략 읽어보시면 "어떤 동작"을 하는지 유추할 수 있을 정도로 자세하게 적으려고 노력해보겠습니다. 

### Related libraries.

- 우선, 본 코드에서 사용하는 라이브러리들은 다음과 같습니다.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options

import time
import json
import os 
import itertools
import numpy as np 
from collections import Counter
import datetime 

import networkx as nx 
import pickle
```

### Open headless browser and Load page

- 아래 코드에서는 브라우저를 열고, 음반 저작권 협회에 접속하여, 저작자명의 입력 부분에 우리가 원하는 아티스트의 ID를 넘겨줍니다. 
- 다만, 이 과정은 다른 사람의 서버로부터 데이터를 긁어오는 과정입니다. 따라서, 과도하게 서버에 부담을 줄 수 있으므로 적절하게 시간 간격을 주는 것이 좋습니다. 뿐만 아니라, 너무 빠르게 데이터를 긁어오게 되면 "웹페이지가 로딩되기 전에 데이터를 긁으려고 할 수도 있으므로", 데이터가 정확하게 읽히지 않을 수 있겠죠.
- 또한, 내부 코드에서는 제가 정의한 다음 3가지 종류의 함수를 사용하고 있습니다. 이 뒤에서 다시 설명할 것이므로 여기서는 간단히 어떤 동작을 하는지에 대해서만 설명하겠습니다. 
    - `extract_song_info_from_result_article`: 검색 결과의 페이지 소스를 보면 'result_article'라는 태그가 있습니다. 이 요소로부터 song과 관련된 정보만을 뽑아서 리턴하는 함수입니다.
    - `extract_artist_info_from_result_article`: 'result_article' 요소로부터 이 요소로부터 이 노래에 참여한 가수들에 대한 정보만을 뽑아서 리턴하는 함수입니다.
    - `return_next_page_button`: 현재 페이지는 약 100개의 검색 결과만 보여줍니다. 만약 가수의 노래 검색결과가 100개를 넘는다면 2 페이지로 나누어서 출력이 되겠죠. 따라서, 이 함수는 100개까지 다 읽고 나서 다음 페이지를 눌러주는 역할을 수행합니다.
- 그리고, 수행 결과는 모두 로컬의 json 파일에 저장합니다.

```python
def extract_info_from_artistID(browser=None, artistID="10007193"):
    """
    browser로부터 저작권 협회에 artistID를 검색하여
    그 결과에 포함되는 정보들을 추출하여, 
    json 형식으로 저장해준다.
    parameter 
    --------
    browser: 내부에서 새로운 browser를 열어주고, 
    artistID: 대상으로 하는 artistID(저작자명))
    """
    # 한국 음반 저작권 협회를 열어서, 
    # https://www.komca.or.kr/srch2/srch_01.jsp
    if browser is None: 
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(options=options)
    browser.get("https://www.komca.or.kr/srch2/srch_01.jsp")
    # author(저작권자의 ID ex: 10007193)에 해당하는 Tag를 찾고
    search_by_author = browser.find_element_by_id("author")
    time.sleep(RG.random()*2)
    # 해당 page에 값을 넘겨주고 리턴을 넘겨줍니다.
    search_by_author.send_keys(artistID)
    search_by_author.send_keys(Keys.RETURN)
    time.sleep(2+RG.random()*2)
    # 넘겨주고 엔터를 쳤으므로, 검색 결과가 나옵니다. 
    # 그리고, 한 페이지에 100개씩 보도록 변경합니다.
    select_button = Select(browser.find_elements_by_name("S_ROWS")[1])
    select_button.select_by_value("100")
    time.sleep(2+RG.random())    

    song_data_dict = {}
    with open("artist_data.json", 'r') as f:
        artist_data_dict = json.loads(f.read())
    #print(f"== ArtistID: {artistID} read start")
    while True:# page 이동
        time.sleep(2+RG.random())
        # result_articles => 모든 노래별로 가져옴
        result_articles = browser.find_elements_by_class_name("result_article")
        for i, each_result_article in enumerate(result_articles):
            # UPDATE song title and id and metadata
            song_id, song_title, song_metadata = extract_song_info_from_result_article(
                each_result_article)
            song_data_dict[song_id] = {
                "title": song_title, 
                "metadata": song_metadata, 
                "artists": []
            }
            # UPDATE artists info
            for a_id, a_name, a_role in extract_artist_info_from_result_article(each_result_article):
                if a_name.strip() !="":
                    artist_data_dict[a_id] = a_name
                song_data_dict[song_id]["artists"].append((a_role, a_id)) 
        next_button = return_next_page_button()
        if next_button is not None: 
            next_button.click()
            time.sleep(4+RG.random())
        else:
            break
    # write data
    with open(f"song_data/{artistID}.json", 'w', encoding='utf-8') as f:
        json.dump(song_data_dict, f, indent=4, ensure_ascii=False)
    with open("artist_data.json", 'w', encoding='utf-8') as f:
        json.dump(artist_data_dict, f, indent=4, ensure_ascii=False)
    time.sleep(5+RG.random())
    return song_data_dict
```


### `result_article` 요소로부터 데이터 추출. 

- 다음 두 함수는 주어진 tag로부터, 필요한 정보만을 선택하여 읽어서 가져오는 함수입니다.
- `extract_artist_info_from_result_article` 함수는 해당 태그로부터 '곡 참여자(artist)'에 대항 정보를 가져옵니다.

```python
def extract_artist_info_from_result_article(each_result_article):
    """
    input으로 들어온 "result_article" 포함된 결과 에서 
    해당 곡에 참여한 모든 artist의 ID를 리스트로 가져오는 함수
    input: 
    - browser.find_elements_by_class_name("result_article")의 각 요소
    output: 
    - [artistID1, artistID2]
    """
    artist_ID_name_role_lst = []
    artists = each_result_article.find_element_by_tag_name('table')
    artists = artists.find_element_by_tag_name('tbody')
    for trow in artists.find_elements_by_tag_name('tr'):
        # role에는 A인 경우 보통 가사, C인 경우 다른 것
        artist_role, artist_name_ID = trow.find_elements_by_tag_name('td')[:2]
        artist_role, artist_name_ID = artist_role.text, artist_name_ID.text
        if artist_name_ID.count("(") == 1:
            artist_name = " ".join(artist_name_ID.split("(")[:-1]).strip()
            artist_ID = artist_name_ID.split("(")[-1].strip()[:-1]
        else:
            artist_name = "(".join(artist_name_ID.split("(")[:-1]).strip()
            artist_ID = artist_name_ID.split("(")[-1].strip()[:-1]
        artist_ID_name_role_lst.append(
            (artist_ID, artist_name, artist_role)
        )
    return artist_ID_name_role_lst
```
 
- `extract_song_info_from_result_article` 함수는 해당 태그로부터 '노래'에 대한 정보를 가져옵니다.

```python
def extract_song_info_from_result_article(each_result_article):
    """
    input으로 들어온 "result_article" 포함된 결과 에서 
    해당 곡에 대한 정보를 (songID, songTITLE, songMETADAT)를 반환 
    input: 
    - browser.find_elements_by_class_name("result_article")의 각 요소
    output: 
    - song_id, song_title, song_metadata
    """
    song_title_and_id = each_result_article.find_elements_by_class_name('tit2')[
        0].text
    temp = song_title_and_id.split("-")
    song_title = " ".join(temp[:-1]).strip()
    song_id = temp[-1].strip()
    song_metadata = each_result_article.find_element_by_class_name('metadata')
    song_metadata = song_metadata.find_elements_by_tag_name("p")
    song_metadata = [x.text for x in song_metadata]
    return song_id, song_title, song_metadata
```

- `return_next_page_button` 해당 페이지를 다 읽고 다음 페이지를 클릭하는 함수입니다. 만약 현재 페이지가 1이라면, 2페이지로 이동해주는 역할을 수행하죠.
- 다만, 해당 가수의 저작권이 1000개가 넘을 경우에는 모두 읽어주지 못합니다. 거의 모든 저작권자가 1000개를 넘기지는 못하기는 하지만, 만약 체크해보시고, 1000개가 넘는 저작권자가 있다면, 다른 방식으로 읽어주셔야 합니다.

```python
def return_next_page_button():
    """
    - next page button을 리턴합니다.
    - 단, 현재로서는, 만약 해당 Artist의 음악이 1000개가 넘는 경우. 
    즉, 1페이지에 100개씩 10 페이지를 넘기는 경우에는 소화하지 못합니다.
    """
    page_buttons = browser.find_element_by_class_name('pagination')
    page_buttons = page_buttons.find_elements_by_tag_name("a")
    current_page = None
    for page_button in page_buttons:
        if len(page_button.find_elements_by_tag_name('strong')) >= 1:
            current_page = page_button
    next_page_button = page_buttons[page_buttons.index(current_page)+1]
    print(f"---- current_page: {current_page.text} ==> {next_page_button.text}")
    if next_page_button.text.isdigit()==True:
        return next_page_button
    else:
        return None
```


## wrap-up

- 갑작스럽지만, 분량 조절을 위해 여기까지만 작성합니다. 
- 오늘은 `selenium`을 사용하여, 한국음반저작권협회로부터 데이터를 긁어오는 것에 대한 내용을 정리하였습니다. 
- 우선, 데이터를 읽어오기 이전에, 웹페이지 소스를 읽고 필요한 정보가 어떤 태그들과 함께 있는지를 파악해야 합니다. 만약, 이 부분이 제대로 되어 있지 않다면 훨씬 많은 시간이 소요되었겠지만, 다행히 관련 데이터가 잘 정리되어 있어서 비교적 효율적으로 데이터를 긁어올 수 있었죠. 
- 또한, headless browser를 사용하여, 백그라운드에서 돌아가도록 처리했고, 데이터를 긁을 때 서버에 과부하가 걸리지 않도록 적절한 시간 배분을 하여 진행하였습니다.
- 그리고, 처음에는 이렇게 코드가 깔끔하지 않았는데, 진행하면서 코드를 깔끔하게 만들었죠. 
- 다음 편에서는 우리가 원하는 대상을 명확하게 분석하기 위하여, 데이터를 효율적으로 수집하는 방법을 정리합니다.