---
title: networkx를 이용하여 기본적인 centrality 분석하기 
category: python-lib
tags: python python-lib networkx 

---

## centrality는 무엇인가요? 

- 한국말로 하면 '중심도'가 되겠네요. 네트워크가 구성되었을 때, 우리가 궁금한 것은 네트워크에서 어떤 노드가 중요한 놈인가? 라는 것입니다. `centrality`란 네트워크 상에서 중요한 노드를 찾기 위한 일종의 metric이라고 말하면 될 것 같습니다. 

## degree centrality

- `degree centrality`는 각 node별로 직접 연결된 edge의 weight만을 고려합니다. 즉, 해당 node가 직접 가진 영향력의 크기는 얼마인가? 를 측정하는 것이 해당 metric의 의미가 되겠네요.

## weighted degree centrality 

- 다만, 해당 edge의 weight는 모두 1이 아니기 때문에, weight를 

## closeness centrality

## betweenness centrality

## eigenvector centrality 