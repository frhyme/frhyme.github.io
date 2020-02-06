---
title: networkx - centrality - local, global reaching centrality.
category: python-libs
tags: python python-libs networkx centrality 
---

## centrality - local reaching centrality.

- "local reaching centrality"는 말 그대로, "접근가능성"을 활용하여, node의 중심성을 평가합니다.  node `u`의 local reaching centrality는 `u`에서 그래프내 모든 다른 노드까지의 거리에 역수를 취해서 그 합을 계산하는 것이니까요. 
- 이렇게 쓰고 보면 harmonic centrality와 비슷해 보이는데, 아주 약간의 차이가 있습니다. 
    - `harmonic centrality`: 다른 모든 노드 `v`들로부터 target node `u`까지 가는데 필요한 최단거리의 역수 합
    - `local reaching centrality`: target node `u`부터 다른 모든 노드 `v`까지 가는데 필요한 최단거리의 역수 합.
- 따라서, undirected network에서는 큰 차이가 없지만, 방향성이 있는 directed network에서는 값이 반대로 나오게 됩니다. 
- 네, 물론, 뭐 그다지 큰 의미가 있는 차이는 아닙니다만.

## Compute local reaching centrality

```python
import networkx as nx
import numpy as np

def np_normalize_dict(input_dict):
    """
    input_dict: {node_name: centrality_float}에서 
    value를 normalize하여 리턴.
    """
    vs = np.array(list(input_dict.values()))
    vs /= np.linalg.norm(vs)
    return {k: v for k, v in zip(input_dict.keys(), vs)}

def custom_local_reaching_centraliyt(G, target_node):
    """
    - local reaching centrality
    - target_node에서 다른 모든 node까지의 거리에 대해서 역수를 취해서 합함.
    harmonic centrality: 다른 모든 node v부터 target_node u 까지의 거리의 역수 합. 
    """
    path_ls = [1/nx.shortest_path_length(G, target_node, n) for n in G if target_node!=n]
    return sum(path_ls)/(len(G)-1)
# Graph generation
G = nx.DiGraph()
G.add_edges_from([(0, 1), (1, 2)])

# harmonic centrality and normalization
nx_harmonic_cent = nx.harmonic_centrality(G)
nx_harmonic_cent = np_normalize_dict(nx_harmonic_cent)

# global reaching centrality and normalization
nx_node_reaching_centraliy = {n: nx.local_reaching_centrality(G, n) for n in G}
nx_node_reaching_centraliy = np_normalize_dict(nx_node_reaching_centraliy)
for n in G:
    print(
        f"{n:3d} ::: ",
        round(nx_node_reaching_centraliy[n], 8),
        round(nx_harmonic_cent[n], 8))
print("=="*20)
```

- 아래에서 보는 것처럼, `local_reaching_centrality`와 `harmonic centrality`는 순위가 반대로 나오게 됨.

```
  0 :::  0.89442719 0.0
  1 :::  0.4472136 0.5547002
  2 :::  0.0 0.83205029
```

## wrap-up

- `nx.global_reaching_centrality`도 있지만, 그냥 평균 값을 계산한 것 같아서, 제외하였습니다.



## reference

- [networkx - local_reaching_centrality](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.local_reaching_centrality.html#networkx.algorithms.centrality.local_reaching_centrality)