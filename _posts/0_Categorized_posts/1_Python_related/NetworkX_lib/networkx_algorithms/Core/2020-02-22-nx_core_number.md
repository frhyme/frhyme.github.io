---
title: networkx - core-number
category: python-libs
tags: python python-libs networkx k-core degeneracy core-number
---

## 2-line summary 

- core_number는 각 vertex가 속할 수 있는 가장 큰 k-core의 `k`를 말함. 
- 따라서, k-core를 찾아가면서, 속해 있으면 update하는 식으로 처리하면 됨.

## core-number

- core-number는 node `u`가 속해 있는 가장 큰 `k-core`의 `k`를 말합니다.
- 예를 들어, "node `u`가 속한 가장 큰 core가 6-core 라면 node `u`의 core-number는 6이 되는 것이죠"

### python implementation 

- 따라서, 순차적으로 k-core를 찾으면서, 각 k-core에 포함된 모든 노드의 core_number를 업데이트하는 식으로 처리하면 됩니다.

```python
import networkx as nx

def core_number(G):
    """
    k-core: ``G``의 subgraph `sG`이며, 
    `sG`의 모든 vertex는 최소한 k이상의 degree를 가져야함. 
    core-number: `G`에서 만들 수 있는 node `u`를 포함한 가장 큰 `k`
    따라서, node별로 core_number가 다름.
    - 본 알고리즘에서는, 순차적으로 k-core를 만들고 
    각 k-core에 속해있는 vertex의 경우 최소한 `k`의 core-number를 가지므로 
    모든 vertex에 대해서 업데이트함.
    """
    core_number_dict = {n:1 for n in G}
    for k in range(2, len(G)):
        k_core = nx.k_core(G, k=k)
        if len(k_core)==0:
            break
        # udpate core_number of all vertex in k_core
        for n in k_core:
            core_number_dict[n]=k
    return core_number_dict


def generate(n=100, seed=0):
    """
    - random scale-free-graph를 만들어주는 함수
    - 연결성이 깨지지 않고, self_loop가 없도록 처리함.
    """
    # n: node size 
    while True:
        G = nx.scale_free_graph(n=n, seed=seed)
        G = nx.Graph(G)
        # remove self-edge
        self_loop = [(u, v) for u, v in G.edges() if u == v]
        G.remove_edges_from(self_loop)
        if nx.is_connected(G)==False:
            seed+=1
            continue
        else:
            break
    return G

```

- 아래에서 `nx.core_number(G)`와 비교해본 결과 동일한 결과가 나오는군요.

```python 
### test 
for i in range(1, 5): 
    G = generate(n=100*i, seed=0)
    assert nx.core_number(G)==core_number(G)
print("== complete")
```