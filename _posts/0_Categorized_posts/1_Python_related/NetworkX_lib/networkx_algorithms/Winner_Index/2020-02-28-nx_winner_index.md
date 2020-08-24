---
title: networkx - Wiener index
category: python-libs
tags: python python-libs networkx topology
---

## Wiener_index

- [Wiener index](https://en.wikipedia.org/wiki/Wiener_index)는 chemical graph theory에서 등장하는데, 하나의 chemical graph 내에 등장하는 모든 node pair간의 shortest-path-length의 합을 말합니다. 
- 개념상, 복잡계에 쓰인다기보다는 단일 고분자에 대해서 해당 index를 적용하면, 각 고분자가 가지고 있는 [Topological index](https://en.wikipedia.org/wiki/Topological_index)를 추출할 수 있고, 이를 통해 고분자의 특성을 유추할 수 있는 것으로 보입니다. 
- 이미 `nx.algorithms.wiener_index(G, weight=True)`에 구현되어 있으며 공부할 겸 동일하게 구현해봤습니다.


## implementation `Wiener_index`

```python
import networkx as nx 
import itertools 

def wiener_index(G, weight=True): 
    """
    - 주어진 graph에서 모든 node pair의 shortest-path-length를 합한 것을 말합니다.
    - directed network의 경우 는 양쪽 모두를 계사하지만, 
    - undirected network의 경우는 한쪽만 계산하므로 1/2를 곱해주면 됩니다.
    - `nx.algorithms.wiener_index(G, weight=True)`와 동일.
    """
    w_index = 0 
    
    for u, v in itertools.permutations(G, 2):
        w_index += nx.shortest_path_length(G, u, v, weight=weight)
    if nx.is_directed(G)==True: 
        return w_index
    else: 
        return w_index/2.0
```

## reference

- [Wiener_index in wikipedia](https://en.wikipedia.org/wiki/Wiener_index)
- [networkx.algorithms.wiener.wiener_index](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.wiener.wiener_index.html#networkx.algorithms.wiener.wiener_index)