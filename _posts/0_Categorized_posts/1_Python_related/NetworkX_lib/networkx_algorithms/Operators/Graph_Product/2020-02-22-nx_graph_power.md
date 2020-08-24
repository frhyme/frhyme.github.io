---
title: networkx - graph product - power
category: python-libs
tags: python python-libs networkx graph-operator power
---

## 1-line summary 

- `nx.power(G, k)`를 사용해서, power of graph를 만들 수 있다. 

## power of graph `G`

- k power of graph `G`는 마코브체인처럼, 노드들이 `k`번만에 도달할 수 있으면, 서로 인접하다고 보는 것이죠. 
- 물론, 그러함으로, adjacency matrix를 제곱하여 얻는 것 또한 가능합니다.
- 코드는 대략 다음과 같죠.

```python
import networkx as nx
import numpy as np

n = 10
G = nx.scale_free_graph(n=n)
G = nx.Graph(G)
assert nx.is_connected(G)

# connected graph `G`인 경우
# `G`의 diameter만큼 power를 먹이면,
# 같은 크기의 complete graph와 같아짐.
G_power_diameter = nx.power(G, nx.diameter(G))
assert nx.is_isomorphic(nx.complete_graph(n=n),G_power_diameter)
```

