---
title: networkx - link prediction - Resource Allocation Index
category: python-libs
tags: python python-libs networkx link-prediction 
---

## 3-line summary 

- pagerank, katz centrality, bewteenness centrality 등 graph의 global structure에 기반한 link prediction이 많지만, common neighbor와 같은 local structure만을 통해서도 link prediction을 충분히 정확하게 예측할 수 있다는 것을 증명한 논문이 있음. 
- 실제로 `Resource Allocation Index`는 매우 간단한 지표만으로도 정확한 missing link prediction을 수행함. 
- 일반적으로 link prediction을 "T시간 이후에도 발생할 것으로 예측되는 link 예측"이라고 알고 있지만, 그냥, "실험 등을 통해서만 파악할 수 있는 단백질네트워크의 link를 미리 예측할 경우 시간/금전적 비용의 감소가 확기적"이라는 말도 하고 있음.

## Predicting Missing Links via Local Information 

- link prediction을 위한 지표인 Resource Allocation Index는 2009년에 나온 [Predicting Missing Links via Local Information](https://arxiv.org/pdf/0901.0553.pdf)라는 논문에서 제시되었습니다. 
- 해당 논문에서는 "common neighbor와 같은 node에 관한 local structure만으로도 충분히 정확한 link prediction을 진행할 수 있다"는 것을 보여줬죠. 여기서 제시한 `Resource Allocation Index`가 local structure를 활용한 지표니까요.

## What is Resource Allocation Index? 

- 개념은 매우 간단한데요, 노드 `u`와 노드 `v`의 resource allocation index는 (두 노드간의 공통된 노드들의 degree 역수의 합)입니다. 이따 파이썬 코드로 보면 더욱 명확할 거에요.

```python
import networkx as nx

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


# nx.resource_allocation_index(G)와 동일한지 확인함.
for n1, n2, nx_RA_ind in nx.resource_allocation_index(G):
    custom_R_ind = custom_resource_allocation_index(G, n1, n2)
    assert custom_R_ind == custom_R_ind
    #customer_RA_index = custom_resource_allocation_index(G, n1, n2)
    #print(n1, n2, nx_RA_index, customer_RA_index)
print("Assertion complete")
print("=="*20)
```

## wrap-up

- `Resource Allocation Index`보다는, 이와 같은 비교적 단순한 local strucrure에 기반한 지표만으로도 의미있는 결과들을 도출했다는, 논문이 좀 더 인상깊었습니다. 이는 `harmonic centrality`에서 지적하고 있는 것과 동일하거든요. 
- 또한, `link prediction`을 어떻게 적용할 수 있을지 고민해본 결과, 본 논문에서 지적한 것처럼, 데이터가 충분하지 못할 때, 퀄리티를 높이기 위해서 사용할 수도 있을 것 같네요.


## reference

- [Predicting Missing Links via Local Information](https://arxiv.org/pdf/0901.0553.pdf)