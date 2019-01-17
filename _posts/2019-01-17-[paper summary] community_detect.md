---
title: paper-summary - Optics - A bibliometric approach to detect emerging research domains and intellectual bases
category: paper-summary
tags: paper-summary community-detection
---

## Optics: A bibliometric approach to detect emerging research domains and intellectual bases

- journal of informetric에 2011년 10월에 게재된 논문 
- [링크](https://www.sciencedirect.com/science/article/pii/S1751157711000319)

### abstract summary 

- web이 발달하면서, community detection을 포함한 social network analysis의 중요성에 대해서 많이 인지하게 됨.
- community detection은 아래와 같은 두 가지 접근 방법으로 구분된다.
    - 첫번째는 topology-based community detection: 네트워크의 그래프 특성을 고려한 접근법
    - 두번째는 topic-based community detection approach: 네트워크 노드의 텍스트 정보를 활용한 접근법
- 본 논문은 두 가지 방법이 각각 어떤 경우에 효과적으로 적용될 수 있는지를 파악하기 위하여, coauthorship network에 대해서 topology-based community detection approach와 topic-based community detection approach를 활용한 논문들을 체계적으로 분석하여, 다음과 같은 인사이트를 발견하였음
    - topology-based community detection approach를 활용하여 도출한 community들의 경우 community 내에서도 서로 다른 주제들이 포함되는 일이 많았고 
    - topic-based community detection approach를 활용한 경우, topologically-diverse sub-communities 가 포함되어 있었다. 
- 향후 community detection 접근법에서는 커뮤니티와 토픽간의 관계만을 강조하는 것이 아니라, dynamic changes of communities and topics를 고려하는 것이 필요하다.

### insight

- 일단 keyword network에 대해서 수행한 것이 아니라, co-author network를 구성해서 진행한 것이므로 약간 차이가 있을 수 있음
- topology-based와 topic-based의 차이에 대해서 좀 더 정확하게 이해하는 것이 필요함. 
- topology-based approach
    - girvan-newman method가 가장 많이 알려진 topology-based community detection approach이며, 가장 betweenness centrality가 높은 edge를 순차적으로 자르면서 진행함. 
    - The Girvan–Newman approach is one of the most commonly used topology-based community detection approaches (Girvan & Newman, 2002), which partitions the graph by gradually removing edges with high betweenness centralities.
- topic-based approach
    - 이건, girvan-newman 메소드처럼 네트워크 기반 graph-partitioning이 아니라, clustering 기법이라고 보는 것이 정확함. 
    - 각 Node들이 만든 논문, abstract 등의 다른 정보를 활용해서 node를 vector화하고 node들을 클러스터링해준 것. 
- 본 논문의 경우 author network에 대하여 clustering을 진행했을때 차이점을 말하고 있음. 
    - 따라서, topology based community detection을 수행할 경우에는 결과로 도출된 community 내에 서로 다른 topic(연구 주제)를 가진 네트워크가 포함되는 일들이 있으며, 
    - 반대로 topic based community detection을 수행할 경우에는 topologycially 섞여 있는 sub-commnity가 나올 가능성이 높다는 것임. 
- 본 논문의 결론은 "topology"방법 만으로는 topic의 차이를 구별하지 못하고, "topic"만으로는 topologically 차이를 구별하지 못하므로, 이 둘을 잘 구분해서 만들어야 하는 것이 결론인듯 한데, 이는 author-network 의 특성으로 보임. 
    - 예를 들어서, 대학원생이 30명이 넘는 큰 연구실이 있다고 할때, topology-based method로는 이 연구실이 하나의 community로 인식될 것임. 그러나, 30명이 넘는 연구실의 경우 30명이 모두 동일한 연구를 수행하고 있다고 보기는 어렵고, 따라서 topic-based로 연구실의 커뮤니티를 추가로 수행하는 것이 필요할 것이라는 말임.