---
title: [paper-summary] A domain keyword analysis approach extending Term Frequency-Keyword Active Index with Google Word2Vec model
category: paper-summary
tags: bibliometric keyword
---

## A domain keyword analysis approach extending Term Frequency-Keyword Active Index with Google Word2Vec model

- scientometric에 2018년 초에 실린 논문. 
- [링크](https://link.springer.com/article/10.1007/s11192-017-2574-9)

### abstract summary 

- 그동안의 bibliometric research에서 키워드 분석은 해당 연구 분야의 지식 구조를 도출했을 뿐만 아니라(investigate the knowledge structure of research domain), 해당 분야의 연구 동향을 분석하는 것에도 많은 도움을 주었다. 
- 가장 대표적인 키워드를 식별하기 위해서, 많은 연구들이 수행되었다. 
    - 그러나 대부분의 연구들은 statistical regularities, syntax, grammar, network-based characteristic을 이용하여 대표 키워드를 선정하였다. 
- 본 연구에서는 Google Word2Vec model을 사용하여, 키워드의 semantic meaning을 도출하였다. 이를 통해, Semantic Frequency-Semantic Active Index라는 TF-IDF와 비슷한 접근법을 만들었으며, 이를 통해 중요한 키워드들을 효과적으로 도출하였다. 
    - 적용 분야는 "natrual hazard". abstract들을 활용해서 학습을 시키고, 키워드의 word vecotr를 생성함. 
- 키워드의 semantic meaning을 활용한 본 분석 방법이 기존의 연구 방법과 어떤 면에서 장단점의 차이가 있는지를 서술하였으며, 본 연구 방법을 통해 효과적인 domain knowledge analysis를 수행할 수 있을 것으로 기대한다. 

### insight

- 키워드는 해당 연구를 대표하는 단어들을 정리하였다는 점에서 매우 의미가 있는 데이터지만, 매우 많은 단어들이 있기 때문에, 대표 키워드를 선정하는 것에 어려움을 겪어왔음
    - 실제로 대표 키워드를 선정하는 것은 어려우며, 대부분 빈도를 기반으로 높은 빈도를 가진 키워드를 선정하는데, 이 경우 빈도가 적지만 중요한 키워드들, 향후 유망한 키워드 등을 선정하는 것에 어려움을 겪을 수 있음. 
- 키워드를 선정 혹은 필터링 과정에서 발생할 수 있는 문제점들을 자세하게 서술하고 있으며, 관련 논문들에 대해서도 매우 잘 정리되어 있는 편. 참고할 수 있는 부분이 매우 많을 것으로 생각됨. 
- 직접 Word2Vec 모델을 구성하고, 학습시켜서 키워드의 semantic vector를 계산함. 또한 이를 통해 키워드 간의 semantic similarity를 계산하고, 동의어 집단을 도출함. 
    - 그러나, 이렇게 진행할 경우, 키워드의 편중 현상이 발생할 수 있음. 예를 들어, 기존의 대표하고 있는 키워드들에 더 쏠려서 모두 해당 키워드로 변형되는 현상이 발생할 수 있음. 

