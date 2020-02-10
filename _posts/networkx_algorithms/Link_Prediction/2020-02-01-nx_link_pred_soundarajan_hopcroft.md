---
title: networkx - link prediction - CN, RA with cluster info. 
category: python-libs
tags: python python-libs networkx link-prediction 
---

## line summary 

- 각 node가 어떤 community에 속하는지를 고려하여 CN(Common neighbor)와 RA(Resource Allocation Index)를 보정함. 
- 2012년 프로시딩에서 발표했던 논문인 [Using community information to improve the precision of link prediction methods](https://dl.acm.org/doi/10.1145/2187980.2188150)에서 제시함.

## CN, RA with cluster info. 

- [Using community information to improve the precision of link prediction methods](https://dl.acm.org/doi/10.1145/2187980.2188150)에서 "네트워크 데이터는 불완전하여, link prediction 문제를 풀고 있는데, 대부분 community infor를 고려하지 않아서, 우리는 이를 고려했을 때 더 잘 예측할 수 있음"을 보였습니다. 
- 저자들인 "soundarajan", "hopcroft"를 뒤에 붙여서, 각각 `cn_index_soundarajan_hopcroft`와 `ra_index_soundarajan_hopcroft`로 이름이 붙습니다.
- 계산은, 그다지 복잡하지 않고, "그냥 같은 커뮤니티에 속하는 값들만 더해주다"로 이해하시면 됩니다. 

## Compute it. 

- `cn_index_soundarajan_hopcroft`와 `ra_index_soundarajan_hopcroft` 함수를 각각 직접 만들어보고 그게 `networkx`에 포함된 기존의 함수의 결과와 동일한지를 확인해봤습니다.

```python
import networkx as nx
import numpy as np

#G = np.random.seed(0)

N = 10
G = nx.scale_free_graph(N, seed=0)
G = nx.Graph(G)
print("==" * 20)


def custom_CN_with_comm_info(G, u, v):
    # Common neighbor와 comm infor를 업데이트.
    common_nbrs = list(nx.common_neighbors(G, u, v))
    comm_info = 0
    for w in common_nbrs:
        # u, v, w 의 community가 동일하면 1을 더함.
        u_comm = G.nodes[u]['community']
        v_comm = G.nodes[v]['community']
        w_comm = G.nodes[w]['community']
        if u_comm==v_comm==w_comm:
            comm_info+=1
    return len(common_nbrs) + comm_info


# community 정보를 node_attr에 업데이트해야 함.
nx.set_node_attributes(G, {u:np.random.randint(0, 3, 1)[0] for u in G}, 'community')

print("== nx.cn_soundarajan_hopcroft(G, community='community')")
for u, v, nx_cn_soun_hop in nx.cn_soundarajan_hopcroft(G, community='community'):
    assert nx_cn_soun_hop == custom_CN_with_comm_info(G, u, v)
print("Assertion complete")
print("=="*20)
#============================================================================
#============================================================================
#============================================================================
def custom_RA_with_comm_info(G, u, v):
    # Resource allocation index with comm info.
    xs = []
    for w in nx.common_neighbors(G, u, v):
        # u, v, w 의 community가 동일하면 1을 더함.
        u_comm = G.nodes[u]['community']
        v_comm = G.nodes[v]['community']
        w_comm = G.nodes[w]['community']
        if u_comm == v_comm == w_comm:
            xs.append(
                1.0/nx.degree(G, w)
            )
    return sum(xs)

nx.ra_index_soundarajan_hopcroft
print("== nx.ra_index_soundarajan_hopcroft(G, community='community')")
for u, v, nx_ra_soun_hop in nx.ra_index_soundarajan_hopcroft(G, community='community'):
    assert nx_ra_soun_hop == custom_RA_with_comm_info(G, u, v)
print("Assertion complete")
print("==" * 20)
```

```
========================================
== nx.cn_soundarajan_hopcroft(G, community='community')
Assertion complete
========================================
== nx.ra_index_soundarajan_hopcroft(G, community='community')
Assertion complete
========================================
```

## wrap-up

- 사실, 그냥 1.0이라는 값으로 간단하게 넣었지만, 각 community별로 힘을 다르게 준다면, 그 결과는 좀 더 정확해질 수도 있겠죠 호호.


## reference 

- [Using community information to improve the precision of link prediction methods](https://dl.acm.org/doi/10.1145/2187980.2188150)
- [networkx.algorithms.link_prediction.cn_index_soundarajan_hopcroft](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_prediction.cn_soundarajan_hopcroft.html#networkx.algorithms.link_prediction.cn_soundarajan_hopcroft)
- [networkx.algorithms.link_prediction.ra_index_soundarajan_hopcroft](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_prediction.ra_index_soundarajan_hopcroft.html#networkx.algorithms.link_prediction.ra_index_soundarajan_hopcroft)
