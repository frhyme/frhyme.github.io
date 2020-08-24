---
title: python - networkx - incremental_closeness_centrality
category: python-libs
tags: python python-libs networkx centrality subgraph 
---

## networkx - closeness centrality 

- network에서 closeness centrality는 "노드 u에서 다른 모든 노드들까지의 거리의 합의 역수"를 말합니다. 즉, closeness centrality가 높으면, 다른 모든 노느들까지 접근할 수 있는 거리가 짧다고, 간단하게 설명할 수 있는 것이죠. 
- 다만, 이런 종류의 centrality를 계산하기 위해서는 모든 node pair에 대해서 shortest-path를 찾아줘야 하며, 이는 굳이 말하지 않아도, 매우 복잡한 알고리즘이 됩니다. 
- 그리고, 특히, 특정한 edge가 추가되거나, 없어지거나 할 때, 변화하는 closeness centrality를 측정하고 싶다면, 이 과정을 매번 해줘야 하죠. 

## networkx - incremental closeness centrality 

- 매우 고맙게도, [networkx - centrality - closeness centrality](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.incremental_closeness_centrality.html)를 사용하면, closeness centrality를 incremental하게 계산할 수 있습니다. 
- incremental하다는 것은, "점진적"이라는 말을 의미하며, 현재 상태에서 closeness-centrality를 저장하고 있다면, edge가 추가되거나, 삭제될 때, closeness-centrality가 어떻게 변화하는지를 알 수 있따는 이야기죠. 
- 어째서, 이렇게 되는지에 대해서는 논문 [Incremental Algorithms for Closeness Centrality](http://sariyuce.com/papers/bigdata13.pdf) 을 참고하시면 좋습니다. 
- 단, node는 변해서는 안됩니다. 항상 동일한 node set가 있어야 하니다. edge가 삽입되거나, 삭제되는 경우에 대해서만 해당 함수를 사용할 수 있습니다.

## Use nx.incremental_closeness_centrality

- 아래와 같이 사용할 수 있습니다. 
    1) edge가 추가(혹은 삭제) 되기 전의 closeness_centrality 를 미리 계산해 두어야 하며, 
    2) 한번에 하나의 edge가 추가되었을대의 cc를 계산할 수 있으며, 
    3) insertion인지, deletion인지를 넘겨줌(default는 True)
    4) Node는 절대로 변해서는 안됨. 

```python
import networkx as nx 

G = nx.Graph() 
# 현재 상태에서의 closeness_centrality를 저장하고
prev_cc = nx.closeness_centrality(G)
new_edge = (0, 1)
post_cc = nx.incremental_closeness_centrality(
    G=G, 
    edge=e,# edge => 추가되는 edge 한 개
    prev_cc=prev_cc, # prev_cc => edge가 추가되기 전의 closeness_centrality
    insertion=True # False이면, edge가 삭제되는 경우를 의미함.
)
```

### 얼마나 빠른가? 

- 간단하게, 코드를 만들어서, 얼마나 빠른지 비교해봤습니다. 
- Node의 수는 50개로 고정하고, 현재는 하나도 edge가 없는 상태죠. 
- edge가 추가될 때마다, 항상 closeness centrality를 계산해야 한다고 할때, 
- case1에서는 매번 edge를 추가할때마다 이전의 값을 고려하여 새롭게 계산해주고 
- case2에서는 매번 그냥 새롭게 계산해줍니다.

```python
import networkx as nx 
import numpy as np 
import time 
import itertools

NODE_SIZE = 50
for EDGE_SIZE in range(100, 600, 50):
    G = nx.Graph()
    G.add_nodes_from([i for i in range(0, NODE_SIZE)])
    # 추가한 EDGE들을 만들고, 섞음.
    EDGEs = list(itertools.combinations(G, 2))[:EDGE_SIZE]
    np.random.shuffle(EDGEs)

    inc_cc_time, cc_time = 0.0, 0.0

    start_time = time.time() 
    prev_cc = nx.closeness_centrality(G)
    inc_cc_time += time.time() - start_time
    for e in EDGEs:
        # CASE 1: nx.incremental_closeness_centrality
        start_time = time.time() 
        prev_cc = nx.incremental_closeness_centrality(G, edge=e,prev_cc=prev_cc, insertion=True)
        inc_cc_time += time.time() - start_time
        G.add_edge(*e)
        # CASE 2: nx.closeness_centrality(G)
        start_time = time.time()
        cc = nx.closeness_centrality(G)
        cc_time += time.time() - start_time
    print(
        f"EDGE_SIZE: {EDGE_SIZE:3d} - incremental_cc_time: {inc_cc_time:.5f} ::: cc_time: {cc_time:.5f}")
    print("--"*50)
```

- 아래를 보시면 추가하는 edge의 수가 커짐에 따라서, `incremental_cc`가 훨씬 시간을 효율적으로 쓰고 있음을 알 수 있죠.

```
EDGE_SIZE: 100 - incremental_cc_time: 0.48296 ::: cc_time: 0.97368
----------------------------------------------------------------------------------------------------
EDGE_SIZE: 150 - incremental_cc_time: 0.62988 ::: cc_time: 1.63518
----------------------------------------------------------------------------------------------------
EDGE_SIZE: 200 - incremental_cc_time: 0.49914 ::: cc_time: 1.78936
----------------------------------------------------------------------------------------------------
EDGE_SIZE: 250 - incremental_cc_time: 0.62656 ::: cc_time: 2.65078
----------------------------------------------------------------------------------------------------
EDGE_SIZE: 300 - incremental_cc_time: 0.71788 ::: cc_time: 3.56669
----------------------------------------------------------------------------------------------------
EDGE_SIZE: 350 - incremental_cc_time: 1.30331 ::: cc_time: 6.24117
----------------------------------------------------------------------------------------------------
EDGE_SIZE: 400 - incremental_cc_time: 1.07049 ::: cc_time: 5.80284
----------------------------------------------------------------------------------------------------
EDGE_SIZE: 450 - incremental_cc_time: 1.14740 ::: cc_time: 7.97550
----------------------------------------------------------------------------------------------------
EDGE_SIZE: 500 - incremental_cc_time: 1.60740 ::: cc_time: 11.66063
----------------------------------------------------------------------------------------------------
EDGE_SIZE: 550 - incremental_cc_time: 1.95668 ::: cc_time: 13.81745
----------------------------------------------------------------------------------------------------
```



## reference

- [networkx - centrality - closeness centrality](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.incremental_closeness_centrality.html)
- [Incremental Algorithms for Closeness Centrality](http://sariyuce.com/papers/bigdata13.pdf)