---
title: networkx - link prediction - Adamic/Adar index
category: python-libs
tags: python python-libs networkx distance 
---

## 1-line summary 

- ["Adamic/Adar index"](https://en.wikipedia.org/wiki/Adamic/Adar_index)는 "Resource Allocation Index"와 매우 유사하나, 각 값에 log를 취해서 더해준다는 차이만 있음.

## Adamic Adar index 

- 개념이 매우 간단하므로 python 코드만 쭉 읽어도 이해될 것 같습니다.

```python 
import networkx as nx
import numpy as np

#G = np.random.seed(0)

N = 10
G = nx.scale_free_graph(N, seed=0)
G = nx.Graph(G)

def custom_resource_allocation_index(G, u, v):
    """
    # u, v 간의 link prediction 지수를 의미하는
    # resource allocation index는 둘 사이에 공통으로 존재하는 노드, w의 degree의 역수 합
    nx.resource_allocation_index(G)로 계산하는 값과 동일함.
    """
    u_v_common_neighbors = set(G[u]).intersection(G[v])
    return sum([1.0 / nx.degree(G, w) for w in u_v_common_neighbors])

def custom_adamic_adar_index(G, u, v):
    """
    resource allocation index와 유사하나, 
    각 값의 분모에 대해서 log를 취한다는 것이 다름.
    """
    u_v_common_neighbors = set(G[u]).intersection(G[v])
    # np.log를 취했음.
    return sum([1.0 / np.log(nx.degree(G, w)) for w in u_v_common_neighbors])

for n1, n2, nx_adamic_adar_ind in nx.adamic_adar_index(G):
    # custom adamic_adar idex
    custom_AA_index = custom_adamic_adar_index(G, n1, n2)
    # 값이 약간 다른 경우가 있어서, 적당힌 자리에서 rounding
    custom_AA_index_rounded = round(custom_AA_index, 8)
    nx_adamic_adar_ind_rounded = round(nx_adamic_adar_ind, 8)
    assert custom_AA_index_rounded == nx_adamic_adar_ind_rounded
print("Assertion complete")
print("=="*20)
```

## wrap-up

- `resource allocation index`와 매우 흡사한데, 조금 신기한 것은 '로그를 취한 지표"가 먼저 나오고, "로그를 없앤 지표"가 나중에 나왔다는 사실이죠. 머신러닝 분야에서도 뉴럴넷의 초기 값을 세팅할 때, 0.5를 곱해서 세팅했더니 훨씬 더 정확도가 좋더라, 뭐 이런 내용들이 있었던것 같기는 한데, 흠. 사실 그냥 값을 먼저 적용해보고, 다른 사람들이 "로그를 취해보니까 더 잘되더라"라는 식으로 지표가 고도화되는 것이 좀 더 일반적인데, 조금 묘하네요. 


## reference

- [Adamic/Adar_index](https://en.wikipedia.org/wiki/Adamic/Adar_index)

