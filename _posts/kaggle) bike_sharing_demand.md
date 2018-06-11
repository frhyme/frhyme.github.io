---
title: kaggle) bike sharind demand를 맞춰봅시다!
category: machin-learning 
tags: python kaggle machine-learning python-lib sklearn
---

## kaggle) bike sharind demand를 맞춰봅시다!

- 아주 행복하게도, missing value가 없습니다 개좋음!!
- Linear model로 했을때보다, randomforest를 넣었을때 훨씬 좋게 나옵니다. 사실 너무 당연한 거죠. 

## just do it. 

- 보통 저는, benchmark model로 만만한, linear model을 만듭니다. 저는 randomforest를 주로 쓰구요. 
- house price prediction을 할때는 gradient boosting method가 괜찮았는데, 여기서는 잘 먹히지 않아요. 흠. 
- 일단은 randomforest를 이용해서, 0.65정도를 찍었습니다. 
- 이제는 `MLPRegressor`를 이용해보려고 합니다. 
##


## wrap-up 

- 처음에는 시간에 따른 변화를 어떻게 트래킹할 수 있을까? 라고 생각했는데, 거시적으로 추정할 것이라면, 그냥 처음 시작부터 날짜를 하나의 변수로 집어넣으면 된다. 
- 그렇게 만들면, 시간의 흐름에 따라 증가하는 것을 알 수있고, 요일 등의 변수를 이용해서 대략 적으로 추정할 수 있음. 

## reference 

- <https://programmers.co.kr/learn/courses/21/lessons/945>