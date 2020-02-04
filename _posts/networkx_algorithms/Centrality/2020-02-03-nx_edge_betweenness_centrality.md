---
title: networkx - centrality - edge betweennss centrality
category: python-libs
tags: python python-libs networkx centrality betweenness-centrality
---

## edge betweennss centrality

- "edge betwenness centrality"는 node betweenness centrality와 유사한데, "node"를 shortest path의 비율을 계산하는 것이 아니라, **edge를 지나는 shortest path의 길이**를 비율로 계산합니다. 
- 가끔, edge의 betweenness centrality를 계산하는 것이므로, Node를 Edge로, 그리고 Edge를 Node로 변경하여 만들어지는 Line Graph에 대해서 node betweenness centrality를 계산하는 것인줄 아시는 분들이 있는데, 다릅니다. 물론 갑 자체는 어느 정도 비슷하게 나온다고 하더라도, 계산 방법이 달라요. 
- `networkx`의 함수를 그대로 사용하여 다음과 같이 사용하면 됩니다.

```python
import networkx as nx 
nx_bet_cent = nx.edge_betweenness_centrality(G)
```




## reference

- [networkx - edge betweenness centrality](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.edge_betweenness_centrality.html#networkx.algorithms.centrality.edge_betweenness_centrality)