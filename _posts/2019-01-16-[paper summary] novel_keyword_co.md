---
title: [paper-summary] Novel keyword co-occurrence network-based methods to foster systematic reviews of scientific literature
category: paper-summary
tags: paper-summary
---


## Novel keyword co-occurrence network-based methods to foster systematic reviews of scientific literature

- PLOS ONE(impact factor: 2.7, open-access journal)에서 2017년에 발행된 논문
- [link](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0172778)

### abstract summary 

- 기존의 연구 논문들을 systematic review를 통해 현재 연구의 동향을 분석하고, 향후 유망 연구를 도출하는 것은 매우 유의미한 연구다. 그러나, systematic review는 반복적이고, 타임컨슈밍한 속성을 가지고 있다. 
- 최근에는 knowledge mapping을 위하여 keyword co-occurrence networks(KCNs)가 활용되고 있다. 
- KCN에서는 개별 키워드는 노드로 표현되고, 키워드의 co-occurrence는 link로서 표현된다.
    - In a KCN, each keyword is represented as a node and each co-occurrence of a pair of words is represented as a link.
    - The number of times that a pair of words co-occurs in multiple articles constitutes the weight of the link connecting the pair.
- 이렇게 구성된 네트워크는 해당 분야의 지식을 의미하며, 네트워크를 분석하여, 패턴, 의미있는 키워드 묶음 등을 도출할 수 있다. 
    - The network constructed in this manner represents cumulative knowledge of a domain and helps to uncover meaningful knowledge components and insights based on the patterns and strength of links between keywords that appear in the literature. 
- 본 연구에서는 review process를 빠르게 수행하기 위하여, KCN을 활용한 systematic review를 수행한다. 
- 본 연구의 강점은, 기존의 KCN 분석과는 다른, 새로운 지표(metric)들을 정의했다는 것이며, 이는 nano-related environmental, health, safety 등의 분야에 적용되었다. 
- KCN approach를 통해 knowledge component, knowledge structure, research trend 등을 도출하고, 기존의 분석 결과와 비교할 수 있다. 이러한 KCN 접근 법은 기존의 접근 방법에 비해서 훨씬 빠르게 적용될 수 있다는 강점이 있다.
- 또한 이러한 접근 방법은 어떤 분야의 데이터에 대해서도 동일하게 적용하여 진행할 수 있다는 강점이 있다. 
    - It can be applied to any scientific field of study to prepare a knowledge map.

### insight

- 키워드의 경우 데이터 전처리가 매우 중요한데, 데이터를 어떻게 전처리하였는지에 대해서는 전혀 작성되어 있지 않다. 
- 3년 단위로 데이터를 분할하여, 시간적인 분석을 수행했는데, 각 시간별 그래프를 보고 어떤 변화가 있었다, 라고 작성한 것에 지나지 않는다. 
- 그렇지만, 현재 진행하고 있는 연구와 구성상 유사점이 많아 보이며, 참고할 내용이 많을 것으로 생각됨.