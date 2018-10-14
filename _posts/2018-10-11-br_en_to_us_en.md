---
title: 영국식 영어단어를 미국식 영어단어로 변환하기. 
category: python-libs
tags: python python-libs english nlp natural-language-processing
---

## intro 

- 간단하게 자연어 처리를 좀 하고 있습니다. 영어를 처리하고 있는데, 이 과정에서 영국식 영어와 미국식 영어가 섞여 있는 것을 발견했어요. 
- 그러니까, 이런 식이죠. 

> organisation, organization

- 의미는 같지만, 형태는 다릅니다. 이런게 매우 성가시죠. 
- 물론 보통 한 글자만 다르니까, sequence matching을 사용해서 처리할 수도 있기는 한데, 이보다는 그냥 영국식영어 ==> 미국식 영어로 변환해주는 딕셔너리가 하나 있으면 훨씬 편할 것 같아요. 

- 그래서, 찾아봤습니다. 

## dictionary 

- [Comprehensive* list of American and British spelling differences](http://www.tysto.com/uk-us-spelling-list.html)에 영국식 영어와 미국식 영어의 차이가 있습니다. 

- 해당 텍스트를 긁어와서, 딕셔너리로 만들어주면 되죠. 
- 코드는 대략 다음과 같습니다. 

```python
f = open("british_to_english.txt", 'r')
br_to_en = f.read().split("\n")
br_to_en = list(filter(lambda x: True if x!="" else False, br_to_en))
br = br_to_en[:br_to_en.index("accessorize")]
us = br_to_en[br_to_en.index("accessorize"):]
br_to_dict = {br_w:us_w for br_w, us_w in zip(br, us)}


```



## wrap-up

- 어렵지 않습니다 하하핫. 