---
title:
category:
tags:
---

## MLE(Maximal Likelihood Estimation)은 무엇인가.

- 일단은 어떤 데이터가 gaussian dist(or normal dist)를 따른다고 가정합시다. 그런데, 이 아이가 따르는 평균과 분산이 무엇인지는 어떻게 알 수 있을까요? 
- 이걸 보통 Maximal Likelihood Estimation을 통해서 해결합니다. 
- **확률 밀도 함수(probability density function)**의 경우는 평균/분산이 정해진 상태에서, x가 나올 수 있는 확률을 계산합니다. 
- 반면 **Likelihood**의 경우는 x가 정해져 있는 상태에서, 평균/분산을 결정합니다. 헷갈리죠? 저도 그랬어요. pdf와 likelihood가 너무 헷갈렸습니다. 우리가 가지고 있는 것은 x, 이 데이터들이 나올 법한, 가장 그럴싸한 평균/분산을 찾는 것이 MLE입니다. 
- 구하는 방법은 일종의 optimization인데, 사실 최악으로는 가능한 모든 구간  -100 < mean < 100, -100000 < variance < 100000 같은 방법도 가능합니다만, 그렇게 하고싶지는 않네요... 

## scipy를 이용한 최적화

## reference 

- <http://rlhick.people.wm.edu/posts/estimating-custom-mle.html>