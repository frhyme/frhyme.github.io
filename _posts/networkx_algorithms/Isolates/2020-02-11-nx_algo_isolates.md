---
title: networkx - isolates.
category: python-libs
tags: python python-libs networkx isolate
---

## intro.

- [networkx - algorithms - isolates](https://networkx.github.io/documentation/stable/reference/algorithms/isolates.html)에 있는 내용을 정리합니다. 
- 사실, 우리가 다루는 네트워크에서, "어떤 노드와도 연결되어 있지 않은 node"를 "isolate"라고 합니다. 

## `nx.isolates`. 

- networkx 다음의 함수들이 있습니다.
    - `nx.number_of_isolates(G)`: `G`에 있는 모든 `isolate`의 수(int)를 리턴합니다.
    - `nx.is_isolate(G, 0)`: `G`에서 node `n`이 `isolate`인지 True or False를 리턴합니다.
    - `nx.isolates(G)`: `G`에 있는 모든 isolate를 리턴하는 generator를 리턴합니다.

```python
import networkx as nx
import numpy as np
import time 

np.random.seed(0)

N = 100
#############################################
# Graph Generation
# Scale-free Undirected graph를 만들고
# 반 정도의 edge를 대충 날려버림.
G = nx.scale_free_graph(N, seed=0)
G = nx.Graph(G)
for e in G.copy().edges():
    if np.random.normal(0, 1)>0:
        G.remove_edges_from([e])
# Graph Generation Done.
#############################################
print(f"Node size: {len(G.nodes())}")
print(f"Edge size: {len(G.edges())}")
print("=="*30)
# number_of_isolates(G): isolated의 수
print(f"== nx.number_of_isolates(G): {nx.number_of_isolates(G)}")
print("--"*30)

# is node isolate?
print(f"== nx.is_isolate: {nx.is_isolate(G, 0)}")
print("--"*30)

# all isolate generator?
print(f"== nx.isolates: ")
print([isolated_node for isolated_node in nx.isolates(G)][:10])
print("==" * 30)
```

- 결과는 다음과 같습니다.

```
Node size: 100
Edge size: 63
============================================================
== nx.number_of_isolates(G): 43
------------------------------------------------------------
== nx.is_isolate: False
------------------------------------------------------------
== nx.isolates:
[8, 10, 11, 16, 17, 19, 27, 30, 31, 34]
============================================================
```

## wrap-up

- Graph에서 비교적 병렬처리를 하기 쉬운 부분이 그래도, 이런 isolate를 찾는 것이죠.



## reference

- [networkx - algorithms - isolates](https://networkx.github.io/documentation/stable/reference/algorithms/isolates.html)