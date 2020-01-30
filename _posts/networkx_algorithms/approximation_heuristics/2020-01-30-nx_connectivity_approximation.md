---
title: networkx - Node Connectivity.
category: python-libs
tags: python python-libs networkx connectivity algorithms
---

## networkx - approximation for NODE connectivity

- Graph는 기본적으로 빠르게 처리하는 것이 어렵습니다. 테이블과 같은 형태라면, 비교적 어느 정도 병렬적으로 처리할 수 있는데(서로 데이터가 독립적이기 때문), Graph는 모두 연결되어 있으므로 그렇지 않죠. 따라서, 필요에 따라서, approximation을 사용하는 경우들이 있습니다. 그외로, graph2vec, node2vec 등의 방법론 또한 approximation의 방법 중 하나죠(물론, 어떤 사람들은 이 방법은 approximation이 아니라고 할 수 있습니다만, 저는 그렇게 생각해요.)
- 본 포스트에서는 `local node connectivity`를 대략적으로 계산하기 위해 `networkx`에 내재된 approximation method를 사용합니다. 

### local node connectivity

- pairwise node connectivity 라고 말하기도 하는데요. 예를 들어서 설명하는 게 더 쉬워요. 
    - 가령 `node_A`, `node_B`가 있다고 합시다(기본적으로는, 두 노드가 인접하지 않고(non-adjacent), 서로 다르다는 것을 전제합니다). 
    - 이 때, 두 노드 간의 관계를 disconnected로 만들기 위해서는 최소한 `n`개의 노드를 제거해야, 한다고 합시다.
    - 이 때, `n`이 바로 이 두 노드간의 connectivity가 됩니다. `minimum separating cutset`이라고 하기도 하죠. 
- 또한, 이 값은 메우 정확하게, Menger’s theorem에 의해서, "path 들간에 공통인 노드가 없은 source와 target간의 모든 path", 즉 `node_disjoint_path`의 수와 동일합니다. 이건 조금 생각해보면 매우 당연해서, 헷갈릴 경우 한번 그림을 그려보시면 명확해질 거에요. 
- 그리고, 모든 node pair 들간의 connectivity들 중에서 가장 작은 값은, 당연하지만, (global) node connectivity가 됩니다. 그냥 node connectivity는 "해당 Graph가 분리되기 위해 필요한 가장 적은 수의 노드를 말하니까요".

## do it. 

- 또 서론이 길었습니다. 그냥 해보면 쉽죠 늘 말하지만 쉬워요. 

```python
import networkx as nx
from networkx.algorithms.approximation import connectivity
import time

N = 40  # node size
p = 0.6 # edge proportion of Complete graph
G = nx.fast_gnp_random_graph(N, p, seed=0)

print("=="*30)
print(f"Node size: {N}, Edge size: {len(G.edges())}")
print("--" * 30)
print("== Start")
start_time = time.time()

MIN_global_node_connectivity = len(G)
WRONG_connectivity_count = 0

# G:nx.Graph 의 모든 node pair들의 local connnectivity를 approximation한다.
for n1, d1 in connectivity.all_pairs_node_connectivity(G).items():
    for n2, approx_c in d1.items():
        if MIN_global_node_connectivity>=approx_c:
            MIN_global_node_connectivity = approx_c
        # `local_node_connectivity`는 특정 source, target에 대해서만 계산해주는 함수
        # 장난 삼아 assert를 넣기는 했지만, 틀릴 리가 없다.
        assert approx_c == connectivity.local_node_connectivity(G, n1, n2)
        # 앞서 말한 것과 같이, local_node_connectivity는 두 노드간의 disjoint_path의 수와 동일해야 한다.
        disjoint_paths = nx.algorithms.connectivity.node_disjoint_paths(G, n1, n2)
        disjoint_path_count = 0
        for _ in disjoint_paths:
            disjoint_path_count+=1
        # `disjoint_path_count`가 정확한 node connectivity이므로 출력함.
        if approx_c!=disjoint_path_count:# Wrong
            print(
                f"WRONG - {n1:3d} => {n2:3d} - approx: {approx_c:3d} - disjoint_path_count: {disjoint_path_count:3d}"
            )
            WRONG_connectivity_count+=1
# graph의 node connectivity와 all_pairs_node_connectivity의 최소값은 당연히 같아야 함.
assert connectivity.node_connectivity(G) == MIN_global_node_connectivity
print("--" * 30)
print(f"Accuracy: {1-WRONG_connectivity_count/(N*(N-1)):%}")
print(f"== complete with comp. time: {time.time()-start_time:6.2f} sec")
print("==" * 30)

```

- 결과는 다음과 같습니다. 즉, approximation이기는 한데, 조금 소름 돋을 정도로 정확합니다. 

```
============================================================
Node size: 40, Edge size: 456
------------------------------------------------------------
== Start
WRONG -   7 =>  14 - approx:  21 - disjoint_path_count:  22
WRONG -  14 =>   7 - approx:  21 - disjoint_path_count:  22
------------------------------------------------------------
Accuracy: 99.871795%
== complete with comp. time:  20.81 sec
============================================================
```


## wrap-up

- local connectivity가 다른 노드들에 비해서 높다면, 그 두 노드는 아마도 좀 더 밀집된 관계라고, 설명할 수 있겠죠. 그 두 관계를 떨어뜨리려면 제거해야 하는 노드의 수가 많으니까요. 그리고, 이는 betweenness centrality와도 유사한 개념으로, 느껴지기도 해요. 