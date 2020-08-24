---
title: networkx - shortest path and length. 
category: python-libs
tags: python python-libs networkx shortest-path 
---

## 2-line summary 

- 

## shortest path with weight. 

- 오늘 이야기할 것은 사실 좀 사소한 것일 수도 있습니다. 
- 보통 `networkx`를 이용해서 분석을 할 때, `weight`를 고려하고 싶은 경우에는 `weight=True`의 형태로 argument를 넘겨줍니다. 보통 이렇게 하면 알아서, weight를 고려해서 처리해주니까요. 
- 하지만, `nx.shortest_path`를 계산할 때는 이렇게 argument를 넘겨주면 weight를 고려해주지 않습니다.

### USE `nx.shortest_path(G, weight=True)`

- `nx.shortest_path(G, weight=True)`와 같이, arugment `weight`에 대해서 `True`를 넘겨줍니다.

```python 
import networkx as nx 
import numpy as np 
import itertools 

"""
shortest_path_length(weight=True) doesn't mean weight sum.
"""

np.random.seed(0) 
G = nx.complete_graph(3)

# UPDATE edge attr with 'weight'
edge_weight_dict = {(0, 1): 1.5, (0, 2): 3.5, (1, 2): 5.5}
nx.set_edge_attributes(G, edge_weight_dict, name='weight')

for u, v in itertools.combinations(G, 2): 
    # weight에 True를 넘겨줬습니다.
    s_p = nx.shortest_path(G, u, v, weight=True)
    print(f"== shortest path        from node {u} to node {v} :: {s_p}")
    s_p_l = nx.shortest_path_length(G, u, v, weight=True)
    print(f"== shortest path length from node {u} to node {v} :: {s_p_l}")
```

- 해당 graph `G`는 node 1에서 node 2로 갈 때, weight를 고려한다면, shortest path가 `(0, 1, 2)`로 가는게 맞습니다만, 결과가 그렇게 나오지 않죠. 그냥 weight를 고려하지 않은 경우와 동일한 결과가 나옵니다.

```
== shortest path        from node 0 to node 1 :: [0, 1]
== shortest path length from node 0 to node 1 :: 1
== shortest path        from node 0 to node 2 :: [0, 2]
== shortest path length from node 0 to node 2 :: 1
== shortest path        from node 1 to node 2 :: [1, 2]
== shortest path length from node 1 to node 2 :: 1
```

### USE `nx.shortest_path(G, weight='weight')`

- 사실, 이 부분은 `networkx`에 좀 아쉽기도 한데요, 다음과 같이, 정확한 edge attribute 내의 key를 넘겨줘야 합니다.

```python 
nx.shortest_path(G, weight='weight')
```

- 자, 이제 이렇게 해서 실행을 하면 잘 되는 것을 알 수 있죠. 


```python
import networkx as nx 
import numpy as np 
import itertools 

"""
shortest_path_length(weight=True) doesn't mean weight sum.
shortest_path_length(weight='weight') mean weight sum.
"""

np.random.seed(0) 
G = nx.complete_graph(3)

# UPDATE edge attr with 'weight'
edge_weight_dict = {(0, 1): 1.5, (0, 2): 3.5, (1, 2): 5.5}
nx.set_edge_attributes(G, edge_weight_dict, name='weight')

for u, v in itertools.combinations(G, 2): 
    s_p = nx.shortest_path(G, u, v, weight='weight')
    print(f"== shortest path        from node {u} to node {v} :: {s_p}")
    s_p_l = nx.shortest_path_length(G, u, v, weight='weight')
    print(f"== shortest path length from node {u} to node {v} :: {s_p_l}")
```

- 결과를 보시면 weight를 정확하게 고려하여 shortest_path를 계산하는 것을 알 수 있습니다.

```
== shortest path        from node 0 to node 1 :: [0, 1]
== shortest path length from node 0 to node 1 :: 1.5
== shortest path        from node 0 to node 2 :: [0, 2]
== shortest path length from node 0 to node 2 :: 3.5
== shortest path        from node 1 to node 2 :: [1, 0, 2]
== shortest path length from node 1 to node 2 :: 5.0
```

## wrap-up

- 사실, 저는 이 부분이 조금 아쉽다고 느껴지기도 합니다. 다른 많은 함수들에서는 쉽게 `weight=True`를 사용하면서, 여기서만, 정확한 `attr_key`를 넘기도록 된 건 좀 아쉬워요. 
- 오히려, True로 argument가 넘어왔을 때도 알아서 label을 인식해서 처리해주었으면 얼마나 좋았을까, 싶네요.


## reference

- [networkx.algorithms.shortest_paths.generic.shortest_path](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.shortest_path.html#networkx.algorithms.shortest_paths.generic.shortest_path)