---
title: networkx - closeness centrality
category: python-libs
tags: python python-libs networkx centrality eigenvector
---

## Centrality - Closeness Centrality

- closeness centrality는 흔히, "근접 중심성"이라고 말하는데, "어떤 Node A에서 다른 모든 노드(reachable nodes)에 도달하기 위한 최단거리의 길이(shortest path length)의 합에 대해서 역수를 처리한 값입니다. 
- 또한, 해당 network 가 하나의 component로 구성된 것이 아닐 경우, 즉, 2가지 이상의 component로 구성이 되어 있다면, 노드별로 reachable node의 수가 다르므로, 이를 고려하여 보정해주는 것도 필요하죠. 

## Do it. 

- 사실, 개념적으로도 간단하므로 굳이 설명하지는 않겠습니다.

```python
import networkx as nx

def custom_closeness_cent(inputG):
    """
    - 노드별로 다른 노드까지의 최단거리의 길이를 합하고, 여기에 역수를 처리하여 계산합니다.
    """
    result_dict = {}
    for n1 in inputG:
        result_dict[n1] = 0
        for n2 in inputG:
            l = nx.shortest_path_length(G, n1, n2)
            result_dict[n1] +=l
    return {k: (len(G)-1)/ v for k, v in result_dict.items()}
##################################################

N = 10  # node size
p = 0.6
G = nx.fast_gnp_random_graph(N, p, seed=0)

print("==" * 20)

# 직접 closeness centrality 계산
custom_closeness = custom_closeness_cent(G)
# networkx의 closeness centrality를 사용하여 계산.
nx_closeness = nx.closeness_centrality(
    G,
    # edge attr dict에 distance 가 존재하면 그 이름을 넘겨주면 됩니다
    distance=None,
    # 만약 2개 이상의 connected component가 있다면, reachable한 노드의 수를 계산하여, closeness centrality를 보정합니다.
    # 당연히도, 작은 노드의 component에 있을 수록 closeness centrality는 작아집니다
    wf_improved=True)
for k in custom_closeness.keys():
    print(
        f"node: {k}, custom func: {custom_closeness[k]:7.5f}, nx.func: {nx_closeness[k]:7.5f}"
    )
print("=="*20)
```

```
========================================
node: 0, custom func: 0.60000, nx.func: 0.60000
node: 1, custom func: 0.81818, nx.func: 0.81818
node: 2, custom func: 0.75000, nx.func: 0.75000
node: 3, custom func: 0.75000, nx.func: 0.75000
node: 4, custom func: 0.56250, nx.func: 0.56250
node: 5, custom func: 0.81818, nx.func: 0.81818
node: 6, custom func: 0.69231, nx.func: 0.69231
node: 7, custom func: 0.60000, nx.func: 0.60000
node: 8, custom func: 0.56250, nx.func: 0.56250
node: 9, custom func: 0.69231, nx.func: 0.69231
========================================
```


## reference 

- <https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.closeness_centrality.html#networkx.algorithms.centrality.closeness_centrality>