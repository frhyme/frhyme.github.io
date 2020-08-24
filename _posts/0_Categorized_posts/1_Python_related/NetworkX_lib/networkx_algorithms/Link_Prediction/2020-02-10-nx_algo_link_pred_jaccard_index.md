---
title: networkx - link prediction - jaccard coeffcient
category: python-libs
tags: python python-libs networkx distance jaccard
---

## 2-line summary 

- jaccard coeffcient는 (두 집합간의 intersection set)/(두 집합간의 union set)임. 매우 간단하며, 네트워크뿐만 아니라 일반적인 data mining쪽에서도 "거리"등을 측정하기 위해 많이 사용함. 
- 특히 graph에서는 neighbor을 1차 2차 등으로 다양하게 정의할 수 있으므로 jaccard coefficient에 기반한 변종으로 다양하게 사용할 수 있음. 

## Jacard coefficient and its variation. 

- 앞서 말한 것과 같이 계산법은 매우 간단하죠. 다만, 오히려 graph에서 jaccard는 변종으로 정의하여 다양하게 사용할 수 있습니다. 
- 가령, 기본 세트를 distance가 1인 neighbor가 아니라, 2로 정의하는 경우, 그리고 distance에 따라서 weight를 다르게 주는 경우에 따라서 다양한 지표로 만들 수 있겠죠.
- 아래 코드에서는 jaccard coefficient를 계산해봤씁니다. 

```python 
import networkx as nx

N = 10
G = nx.scale_free_graph(N, seed=0)
G = nx.Graph(G)
assert nx.is_connected(G)==True

def custom_jaccard_index(G, u, v):
    """
    u_set: u의 neighbors
    v_set: v의 neighbors
    jaccard coeffcient: intersection의 수를 union의 수로 나눔.
    """
    u_set = set(G[u])
    v_set = set(G[v])
    uv_union = u_set.union(v_set)
    uv_intersection = u_set.intersection(v_set)
    return len(uv_intersection) / len(uv_union)

for u, v, nx_jac_coef in nx.jaccard_coefficient(G):
    assert nx_jac_coef == custom_jaccard_index(G, u, v)
print("Assertion Complete")
```