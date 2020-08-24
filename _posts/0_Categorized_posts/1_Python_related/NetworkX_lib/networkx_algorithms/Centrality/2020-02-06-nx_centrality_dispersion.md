---
title: networkx - centrality - dispersion
category: python-libs
tags: python python-libs networkx centrality dispersion
---

## centrality - dispersion

- "dispersion"은 [Romantic Partnerships and the Dispersion of Social Ties](https://arxiv.org/pdf/1310.6753v1.pdf)에서 제안한 개념으로, 기존의 embeddedness와 약간은 다른 개념입니다. 
- 해당 논문의 목적은 "사람들 네트워크 속에서 '특별한 관계'는 어떻게 찾아낼 수 있는가?"였으며, 이는 단순히 "공통된 neighbor의 수"를 의미하는 embeddedness로는 해결할 수 없다는 것을 알게 된 것이죠. 가령, 서로 대학교 동문일 경우에는 서로 공통된 많은 사람들이 있지만, 이 둘이 특별한 관계라고는 할 수 없으니까요. 
- 실생활에서 배우자들을 보면 "남편은 아내의 모든 회사 사람, 모든 학교 친구, 모든 동네친구를 알지는 못하지만, 다들 조금씩을 알고 있게 되죠". 그리고, 여기서 당연하지만, 학교 사람, 회사 사람 등은 서로 접점이 없죠. 이 관점에서 착안하여, "배우자들은 embeddedness만을 고려하는 것이 아니라, 그 common neighbor들간의 관계를 조금 더 고려하여, 그 common neighbor들이 서로 모를 수록, 가능성이 커진다"는 지표를 가져온 것이죠. 
- 쓰고 보면 참 당연하게 느껴집니다. 그리고, 이 내용은 이미 [networkx.algorithms.centrality.dispersion](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.dispersion.html#networkx.algorithms.centrality.dispersion)에 잘 구현되어 있죠. 
- 저는 제가 직접 같은 코드를 만들어보고, 비교해봤씁니다. 

## Compute dispersion

- 제가 직접 만들어보고, 기존에 있는 것도 사용해봤습니다.

```python
import networkx as nx
import itertools

def custom_node_to_node_dispersion(G, u, v):
    """
    u, v간의 dispersion을 알고자 함.
    ego_graph(G, source)에서 target으로 가는 dispersion을 확인
    dispersion: source와 target의 common_neighbor(공통으로 이웃하는 노드)
    1) common_neighbor에서 서로 다른 s, t들이, 
    2) ego_graph(G, source) 상에서 s, t가 서로 직접 연결되지 않았을 때, 
    3) ego_graph(G, source) 상에서 s, t가 connection이 없을 때(common neighbor 가 없을때)
    의 모든 수를 합해서 리턴.
    normalize: /len(common_nbrs)
    """
    u_nbrs = set(G[u])
    v_nbrs = set(G[v])
    common_nbrs = u_nbrs.intersection(v_nbrs)
    # embeddedness는 공통된 nbrs의 수를 의미함.
    embededness = len(common_nbrs)
    ego_graph_u = nx.ego_graph(G, u)
    # 이 함수에서는 distance를 1 or 0으로 처리했으나,
    # 실제 논문에서는 distance function을 변화하여 다양한 경우를 검증.
    distance_u_to_v = 0
    for (s, t) in itertools.combinations(common_nbrs, 2):
        # 1) common_neighbor에서 서로 다른 s, t에 대해서
        s_nbrs_excluding_uv = set(ego_graph_u[s]).difference(set([u, v]))
        if t not in s_nbrs_excluding_uv:
            # 2) ego_graph(G, source) 상에서 s, t가 서로 직접 연결되지 않았을 때(u, v 제외)
            t_nbrs_excluding_uv = set(ego_graph_u[t]).difference(set([u, v]))
            if s_nbrs_excluding_uv.isdisjoint(t_nbrs_excluding_uv):
                # 3) ego_graph에서 s, t가 서로 connection이 없을 때(common neighbor가 없을 때 )
                # 이럴 때, 거리를 1로, 아닐 경우, 0.
                distance_u_to_v += 1
    # normalized
    if len(common_nbrs)!=0:
        return distance_u_to_v / embededness
    else:
        return distance_u_to_v
########################

# Graph generation
N = 300  # node size
p = 0.5
G = nx.fast_gnp_random_graph(N, p, seed=0)
G = nx.scale_free_graph(N)
G = nx.Graph(G)
print(nx.is_connected(G))

if True:
    # custom_node_dispersion
    for n1, n2 in itertools.combinations(G, 2):
        custom_disp = custom_node_to_node_dispersion(G, n1, n2)
        nx_disp = nx.dispersion(G, n1, n2)
        if custom_disp!=nx_disp:
            print(f"{n1:3d} => {n2:3d} ::: {custom_disp:.5f} ::: {nx_disp:.5f}")
```

## wrap-up

- 그래도, dispersion은 좀 특별한 관점인 것 같습니다. 물론, romantic relation이 아니라, 다른 논문에서 이를 사용한다면 어떻게 해석해야 할지는 조금 애매하기는 합니다만.


## reference

- [networkx.algorithms.centrality.dispersion](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.dispersion.html#networkx.algorithms.centrality.dispersion)
- [Romantic Partnerships and the Dispersion of Social Ties](https://arxiv.org/pdf/1310.6753v1.pdf)