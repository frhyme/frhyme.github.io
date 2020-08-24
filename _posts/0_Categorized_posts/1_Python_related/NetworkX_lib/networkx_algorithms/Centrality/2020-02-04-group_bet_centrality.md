---
title: networkx - group betweenness centrality 
category: python-libs
tags: python python-libs networkx centrality betweenness-centrality
---

## centrality - group betweenness centrality

- node betweenness centrality는 "그래프의 모든 node pair 간의 shortest path 중에서 node `N`을 지나는 최단거리의 비율"을 말하죠. 
- 그렇자면, 같은 의미로 group betweenness centrality는 "그래프의 모든 node pair 간의 shortest path 중에서 node group을 지나는 최단거리의 비율"을 말합니다. 여기서 node group은 그냥 노드의 집합을 말하는 것이죠. 만약, node group에 단 1개의 node만 존재한다면, 그냥 "node betweenness centrality"와 차이가 없죠. 
- 간단히 다음처럼 계산할 수 있습니다.

```python
import numpy as np
import networkx as nx
import time

# Graph generation
N = 10  # node size
p = 0.5
G = nx.fast_gnp_random_graph(N, p, seed=0)


"""
group betweenness centrality: 
- group에 node A, B, C가 속한다고 할 경우, 
- A, B, C를 하나의 Node로 생각하고, 
- 최단 거리가 A, B, C를 지나는 경우를 모두 합하여, betweenness centrality를 계산해주면 된다. 
- 따라서, 하나의 node만 넘길 경우에는 그냥 betweennss centrality와 차이가 없다.
"""
node_group = [1, 2, 8]
print(f"Betweenness centrality of Node Group {node_group}")
print(f"{nx.group_betweenness_centrality(G, C=node_group)}")
```

```
Betweenness centrality of Node Group [1, 2, 8]
0.023809523809523808
```


## wrap-up

- 여기서는 node group에 대한 betweenness centrality만 계산했으나, closeness centrality, degree centrality등에 대해서도, group으로 처리할 수도 있습니다. 