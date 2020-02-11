---
title: networkx - PageRank
category: python-libs
tags: python python-libs networkx centrality Pagerank
---

## 3-line summary for PageRank

- 이미 [pagerank](https://en.wikipedia.org/wiki/PageRank) 매우 유명한 알고리즘이지만, 그래도 일단 쓴다. 
- 계산적으로 보면 [SimRank](https://en.wikipedia.org/wiki/SimRank) 비슷해보이지만, 관점이 다름. 아무튼 "방향성이 있는 네트워크"에서 노드의 영향력을 측정하는 방법.

## Page Rank. 

- 알고리즘의 기본 가정은 "중요한 object일수록, 다른 object들로부터 follow를 많이 받을 것이며, 중요한 object들로 부터 가치있는 follow를 받을수록 중요한 노드이다" 정도로 말할 수 있습니다. 
- 요즘은 인스타그램들을 많이 해서 설명이 참 쉬운 것 같은데, 
    - "만약, 지드래곤이 A라는 사람을 팔로우한다면, A는 아마도 매우 영향력있는 노드일 가능성이 높을 것입니다". 
    - "100명이 A라는 사람을 follow하는데, 이 100명이 '마구마구 팔로우하는 사람'이라면, A는 아마도 별로 영향력있는 노드가 아니겠죠"
- 위 두 이야기는 우리도 이미 알고 있는 내용일 것이고, 매우 타당한 가정으로 보입니다.



## reference

- [networkx - pagerank](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html#networkx.algorithms.link_analysis.pagerank_alg.pagerank)
- [PageRank in wikipedia](https://en.wikipedia.org/wiki/PageRank)
- https://en.wikipedia.org/wiki/PageRank