---
title: networkx - swap - double edge swap 
category: python-libs
tags: python python-libs networkx swap 
---

## 1-line summary 

- Before: (u, v) and (x, y)
- AFter : (u, x) and (v, y)

## network - double edge swap

- network의 유형, 특성들을 판단하는 지표들의 유효함을 보이기 위해서는 보통 reference network를 정의하고 차이를 보이는 식으로 진행되죠. 
- 이 때, 많이 쓰이는 reference network는 "degree distribution을 동일하게 유지하고, edge를 여러번 바꾼 네트워크"입니다. 흔히 equivalent random network라고 하죠. 
- 이 때, 한번 바꾸어주는 edge swap이 바로 [networkx.algorithms.swap.double_edge_swap](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.swap.double_edge_swap.html#networkx.algorithms.swap.double_edge_swap)이며, 그림으로 보면 다음과 같죠. 
- 이를 여러번 반복하면, degree distribution은 동일하더라도 다른 형태의 G가 나오게 됩니다. 
- 따라서, 이런 equivalent network에 대해서도 차이점이 명확하게 드러나면, 그 network는 확실한 차별점을 가지고 있다, 라고 할 수 있는 것이죠.

```
u--v            u  v
       becomes  |  |
x--y            x  y
```

## do it. 

- 코드는 간단합니다. 

```python 
import networkx as nx 

G = nx.Graph()
G.add_edges_from([
    (0, 1), 
    (2, 3)
])
print(f"Before: {G.edges()}")
# nswap: 몇 개의 edge를 바꿀 것인지, 
# maxtries: 1번 swap할 때, 시도를 몇 번인나 할것인지?
nx.double_edge_swap(G, nswap=1, max_tries=100, seed=0)
print(f"After : {G.edges()}")

```

```
Before: [(0, 1), (2, 3)]
After : [(0, 3), (1, 2)]
```

## reference

- [networkx.algorithms.swap.double_edge_swap](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.swap.double_edge_swap.html#networkx.algorithms.swap.double_edge_swap)