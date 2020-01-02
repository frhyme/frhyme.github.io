---
title: discrete choice model과 machine-learning은 뭐가 다른가? 
category: machine-learning
tags: data machine-learning logistic-regression discrete-choice-model 
---

## Discrete choice and machine learning: two peas in a pod?(번역 및 정리)

- 최근에 discrete choice model을 정리하고 있습니다. 아무튼 그러다보니, discrete choice model과 machine learning이 큰 차이가 없게 느껴지는데, 정확히 어떤어떤 포인트가 다른지에 대해서는 자세하게 정리된 것이 없더라고요. 
- 제가 [오늘 번역하고 정리하는 자료에는 그러한 내용이 좀 더 자세히 들어있습니다](http://transp-or.epfl.ch/documents/talks/2018MATTS.pdf).

### Discrete choice model a ML perspective

- ML의 관점에서 보면, discrete choice model은 다음의 특징을 가집니다. 
    - dependent variable이 discrete하고, 
    - supervised learning이고, 
    - logistic regression 을 사용한다는 것. 


### Data collection

- ML의 경우, 'dataData generation process가 무시되는 경향이 있고, 해당 데이터 자체의 일관성(representativity)이 확보되었다고 가정하고, 데이터세트의 크기가 중요하고. 
- 반면, Discrete choice model의 경우 집단(population)이 식별되고, Data 수집 전략이 설계되고, 데이터 세트가 해당 집단을 대표하기 위해서 조정되는 등의 차이가 있음 

### Summary 

- 그냥, DCM의 경우 해석력이 있고 보통 cross-validation은 무시되고, MLE등을 통해서 추정되고, 뭐 그런 차이가 있다고 합니다 호호.

