---
title: networkx - load centrality
category: python-libs
tags: python python-libs networkx centrality betweenness-centrality load-centrality
---

## what is load centrality? 

- [networkx documentation에 작성된 "load centrality"](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.load_centrality.html#networkx.algorithms.centrality.load_centrality)는 다음과 같습니다. 
> The load centrality of a node is the fraction of all shortest paths that pass through that node.

- 그리고, [networkx documentation에 작성된 "betweenness centrality"](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.betweenness_centrality.html#networkx.algorithms.centrality.betweenness_centrality)는 다음과 같습니다. 
> Betweenness centrality of a node 𝑣 is the sum of the fraction of all-pairs shortest paths that pass through 𝑣.

- 그러니까, 문서상으로는 load centrality와 betweenness centrality가 비슷해보입니다. 그리고, 그 결과도 실제로 비슷하죠. 
- 다만, 논문 [Universal Behavior of Load Distribution in Scale-Free Networks](http://phya.snu.ac.kr/~dkim/PRL87278701.pdf)을 보면, 등장배경이 조금 다른데요, load centrality(부하 중심성)은 "네트워크에서 데이터 전송시에 노드별로 걸리는 부하를 측정"하기 위해서 만들어졌습니다. 여기서, 노드 u로부터 노드 v로 데이터가 전송되어야 할때, 데이터는 둘 사이의 최단거리의 수만큼 나누어져 전달됩니다. 이 때, 발생하는 "데이터들의 크기에 변동성이 있다면", load centrality와 betweenness centrality에 차이가 발생하겠지만, 그렇지 않은 경우는 똑같습니다. 
- 다른 문서들에서도 비슷하게, "결과값은 비슷해도, 배경이 다르다"는 식으로 표현하고 있습니다.


## Compare it using `NetworkX`

- 그러니까, 정말, 둘이 비슷한지 확인해 봅시다. 

```python
import networkx as nx
import numpy as np
import itertools

"""
# betweenness centrality 
- bet centrality의 경우 node pair 간의 최단거리들(shortest paths)에 해당 노드가 포함되는 비율을 계산했다면, 
# load centrality
- load centrality의 경우는 개념상으로, vertex `u`에서 vertex `v`로 어떤 물건 `d`(데이터 등)를 전송할 때, 
둘 사이에 여러 최단거리가 존재할 경우, `d`를 최단거리들로 나누어 보내는 것을 말합니다. 
- 개념상으로는 조금 달라 보이지만, 사실 이 둘의 값은 거의 차이가 없음.
- 다만, 네트워크의 특성(가령 scale-free network)에 따라서 값이 조금씩 달라지는 경우가 있으나, 무시해도 되는 정도로 보임.
"""

np.random.seed(0)

def custom_load_centrality(G):
    """
    load centrality: 노드 u 에서 발생한 데이터를 다른 노드 v로 전송해야할 때, 
    최단거리의 수만큼 나누어서 데이터를 전송하게 된다. 그리고 그 최단거리에 포함된 노드에는 그 값들이 포함된다.
    데이터 패킷이 나누어진 만큼 노드와 엣지에는 부하(load)가 걸리게 되고, 그 부하를 더한 값이 load centrality
    """
    r_dict = {n:0 for n in G}
    # all node pairs
    for n1, n2 in itertools.combinations(G, 2):
        # find all shortest path
        all_shrt_paths = list(nx.all_shortest_paths(G, n1, n2))
        # load is divided by shortest path count
        l = len(all_shrt_paths)
        for n1_n2_shrt_pt in all_shrt_paths:
            for r in n1_n2_shrt_pt[1:-1]:
                upated_x = 1.0/l
                r_dict[r]+=upated_x
    r_dict = np_normalize_dict(r_dict)
    return r_dict

def np_normalize_dict(input_dict):
    """
    input_dict: {node_name: centrality_float}에서 
    value를 normalize하여 리턴.
    """
    vs = np.array(list(input_dict.values()))
    vs /= np.linalg.norm(vs)
    return {k: v for k, v in zip(input_dict.keys(), vs)}

def print_load_between_centrality(inputG):
    """
    inputG에 대해서 custome_load_cent, load_cent, bet_cent를 출력함.
    """
    # normalization by norm.
    custom_load_cent = custom_load_centrality(G)
    nx_load_cent = np_normalize_dict(nx.load_centrality(G))
    nx_bet_cent = np_normalize_dict(nx.betweenness_centrality(G))

    # node별로 load centrality, betweenness centrality 출력.
    for i, n in enumerate(G):
        c_load  = custom_load_cent[n]
        nx_load = nx_load_cent[n]
        nx_bet  = nx_bet_cent[n]
        print(
            f"Node: {n:3d}, custom_load: {c_load:.6f}, nx_load: {nx_load:.6f}, nx_bet: {nx_bet:.6f}"
        )
        if i>5:
            break
#============================================
# Graph generation
N = 200  # node size
p = 0.5
G = nx.fast_gnp_random_graph(N, p, seed=0)
print("== random graph ")
print_load_between_centrality(inputG=G)
# scale-free network인 경우 가끔 load centrality와 betweenness centrality가 달라지는 경우가 있음.
G = nx.scale_free_graph(N)
G = nx.Graph(G)
print("== scale-free graph ")
print_load_between_centrality(inputG=G)
```

- 아래에서 보시는 것처럼, 직접 만든 `custom-load centrality`나, `nx.load_centrality`나, `nx.betweenness_centrality`나 별 차이가 없습니다. 다만, scale-free graph에서는 종종 달라지는 경우가 있기는 합니다.

```
== random graph
Node:   0, custom_load: 0.061781, nx_load: 0.061781, nx_bet: 0.061781
Node:   1, custom_load: 0.063924, nx_load: 0.063924, nx_bet: 0.063924
Node:   2, custom_load: 0.058781, nx_load: 0.058781, nx_bet: 0.058781
Node:   3, custom_load: 0.075727, nx_load: 0.075727, nx_bet: 0.075727
Node:   4, custom_load: 0.071445, nx_load: 0.071445, nx_bet: 0.071445
Node:   5, custom_load: 0.074909, nx_load: 0.074909, nx_bet: 0.074909
Node:   6, custom_load: 0.063930, nx_load: 0.063930, nx_bet: 0.063930
== scale-free graph
Node:   0, custom_load: 0.463166, nx_load: 0.462559, nx_bet: 0.463166
Node:   1, custom_load: 0.638801, nx_load: 0.638973, nx_bet: 0.638801
Node:   2, custom_load: 0.602436, nx_load: 0.602692, nx_bet: 0.602436
Node:   3, custom_load: 0.051489, nx_load: 0.051535, nx_bet: 0.051489
Node:   4, custom_load: 0.000000, nx_load: 0.000000, nx_bet: 0.000000
Node:   5, custom_load: 0.000000, nx_load: 0.000000, nx_bet: 0.000000
Node:   6, custom_load: 0.000000, nx_load: 0.000000, nx_bet: 0.000000
```


## wrap-up

- "load centrality"가 계산상으로는 "betweenness centrality"와 유사하지만, 개념적으로, "데이터 전송 네트워크"라는 점에서 시작했다는 면에서 좀 더 generalization같은 거라고 생각해요. edge, node에 걸리는 contraint-free한 네트워크에 대한 것이고, 만약 발생하는 data packet의 분포를 모델링해서 적용한다면, 좀더 일반적인 load centrality를 계산할 수 있게 되겠죠.


## reference

- [networkx - load centrality](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.load_centrality.html#id3)
- [centiserver - load centrality](https://www.centiserver.org/centrality/Load_Centrality/)
- [Paper: Universal Behavior of Load Distribution in Scale-Free Networks](http://phya.snu.ac.kr/~dkim/PRL87278701.pdf)