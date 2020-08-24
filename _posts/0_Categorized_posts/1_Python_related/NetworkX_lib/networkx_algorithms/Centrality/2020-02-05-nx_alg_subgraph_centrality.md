---
title: networkx - subgraph centrality
category: python-libs
tags: python python-libs networkx centrality subgraph
---

## What is subgraph centrality? 

- [subgraph centrality](https://www.centiserver.org/centrality/Subgraph_Centrality/)는 "node가 graph의 subgraph에 속할 비율"을 말합니다. subgraph의 크기가 커질수록, penalty를 먹입니다(즉, 작은 subgraph일수록 weight가 커진다는 이야기죠). 다만, 정확히는 subgraph라기보다, closed walk에 가깝습니다. 물론 뭐 큰 차이는 없죠.
- 다만, centrality의 경우, 계산도 계산이지만, 해석이 중요하죠. 해당 centrality를 제시한 논문인 [Subgraph Centrality in Complex Networks](https://arxiv.org/abs/cond-mat/0504730)를 읽어봐도, "어떤 단백체에서 가장 먼저 떨어질 단백질을 예측하는데 기존 degree centrality보다 뛰어남을 보였다"라고 제시하고 끝입니다. 그렇죠. 물리학에서는 이렇게 증명할 수 있지만, 저처럼 키워드 네트워크를 대상으로 분석하는 경우에는, 그 해석이 어렵습니다. 
- 뭐 아무튼, 그렇다고 하네요.

## Compute subgraph centrality.

```python
import networkx as nx
import numpy as np

np.random.seed(0)

N = 100
p = 0.6
G = nx.fast_gnp_random_graph(N, p, seed=0)


def np_normalize_dict(input_dict):
    """
    input_dict: {node_name: centrality_float}에서 
    value를 normalize하여 리턴.
    """
    vs = np.array(list(input_dict.values()))
    vs /= np.linalg.norm(vs)
    return {k: v for k, v in zip(input_dict.keys(), vs)}


def custom_subgraph_centrality(inputG):
    """
    - node subgraph_centrality는 node `n`으로부터 다시 node `n`까지 도달하는 closed walk들에 대해서
    length의 역수를 weight로 주고 그 walk들을 합한 것을 말함. 
    - 따라서, adjancency matrix을 dot product로 곱해가면서 diagonal을 계산해서 합치면 됨.
    - 단, np.matrix의 경우 **2로 해도 알아서 dot product를 해주지만, np.array의 경우는 그렇지 않음.
    """
    def np_arr_power(input_np_arr, n=2):
        # input_np_arr 의 power
        R = input_np_arr.copy()
        for i in range(0, n):
            R = np.dot(R, input_np_arr)
        return R
    ########################
    M = nx.to_numpy_array(inputG)
    R = M.copy()
    for i in range(2, 5):
        #print(f"== {i}")
        R +=np_arr_power(M, i)/i
    return {k: v for k, v in zip(inputG, np.diagonal(R))}
#=============================================
custom_subgraph_cent = np_normalize_dict(
    custom_subgraph_centrality(G)
)

nx_subgraph_cent = np_normalize_dict(
    nx.subgraph_centrality(G)
)

for i, n in enumerate(G):
    print(
        f"Node: {n:2d}, nx_subgraph_cent: {nx_subgraph_cent[n]:.5f}, custom_subgraph_cent: {custom_subgraph_cent[n]:.5f}"
    )
    if i>5:
        break

```

- 결과는 다음과 같죠. 

```
Node:  0, nx_subgraph_cent: 0.09892, custom_subgraph_cent: 0.09889
Node:  1, nx_subgraph_cent: 0.10808, custom_subgraph_cent: 0.10810
Node:  2, nx_subgraph_cent: 0.10096, custom_subgraph_cent: 0.10092
Node:  3, nx_subgraph_cent: 0.10192, custom_subgraph_cent: 0.10192
Node:  4, nx_subgraph_cent: 0.11996, custom_subgraph_cent: 0.11995
Node:  5, nx_subgraph_cent: 0.09283, custom_subgraph_cent: 0.09281
Node:  6, nx_subgraph_cent: 0.09199, custom_subgraph_cent: 0.09199
```

## wrap-up

- centrality는 해당 네트워크 내에서 각 노드가 가지는 '힘'을 말합니다. 관점에 따라서 다를 수 있지만, degree centrality의 경우는 직접적인 연결만을 고려하죠. subgraph centrality는 개별 subgraph를 일종의 "힘의 단위"로 고려해서, 이를 고려하여 직/간접적인 그래프에서의 영향력을 측정한 것이라고 보는 것이 좋겠네요.

## reference

- [networkx - subgraph centrality](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.subgraph_centrality.html#networkx.algorithms.centrality.subgraph_centrality)