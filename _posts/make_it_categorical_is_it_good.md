---
title: pd.DataFrame의 categorical data
category: python-lib
tags: python python-lib pandas dataframe categorical 
---

## dataframe의 column을 category로 만들면 좋아지나요? 

- 저는 그냥 귀찮아서, 보통 categorical data인 것 같으면, `pd.get_dummies`를 이용해서 one-hot encoding으로 처리해버렸습니다. 어차피 random-forest를 돌릴 꺼니까, 딱히 문제가 된다는 생각은 안해 봤고요. 
- 다만, 여기서 Series의 dtype을 `category`로 선언하면 뭐 좋은 점이 따로 있나요? 

## 흐음.. 

- 일단 [pandas의 documentation](https://pandas.pydata.org/pandas-docs/stable/categorical.html)을 읽어 봤는데, 딱히 더 좋아지는지 잘 모르겠습니다. 애매하네요....
- 

## reference 

- <https://pandas.pydata.org/pandas-docs/stable/categorical.html>