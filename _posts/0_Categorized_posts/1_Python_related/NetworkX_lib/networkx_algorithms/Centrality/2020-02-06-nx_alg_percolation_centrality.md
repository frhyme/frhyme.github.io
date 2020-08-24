---
title: networkx - percolation centrality
category: python-libs
tags: python python-libs networkx centrality betweenness-centrality percolation
---

## networkx - percolation centrality

- [Percolation](https://en.wikipedia.org/wiki/Percolation)은 한국말로 "여과"입니다. 커피를 만들때 필터에 커피를 투과시키는 것을 보통 여과라고 하죠. 
- 그리고, node `u`의 Percolation centrality는 해당 노드를 지나가는 "percolated path(여과된 길)"의 비율을 말하죠. 각 node별로 percolation state는 다르며, 0.0과 1.0 사이의 값을 가지게 되죠(값이 높을수록 여과가 잘 됨 혹은 전염을 잘 시킴 이라고 이해하시면 됩니다). 
- 따라서, percolation cnetrality는 네트워크 자체가 가지는 위상적/구조적 특성(topological, structural)은 물론, 각 노드의 percolation state를 활용하여, 각 노드의 상대적인 중요성을 측정할 수 있습니다. 만약, '전염성이 강한 노드(percolation state가 높은 노드)'들에 가까이 있다면, 이 노드들 또한 percolation centrality가 높게 나오게 되겠죠. 즉, 해당 네트워크에 전염병이 흘러들어간다면, 매우 취약한 노드ㄹ가 될 수 있다는 것을 의미합니다.
- 또한, 만약, 모든 노드들의 percolated state가 같다면, 이 값은 `betweenness centrality`와 동일하게 계산됩니다(betweenness centrality는 edge의 weight를 계산, percolation centrailty는 node의 weight(percolation state)를 고려) 

## Compute percolation centrality. 

- node의 percolation state를 모두 동일하게 세팅하여 percolation centrality를 계산하여, betweenness centrality와 같음을 확인하고, 
- 한 노드의 percolation state를 높게 변화하여, 전체 percolation state가 어떻게 달라지는지를 확인함.


```python
import networkx as nx
import numpy as np

np.random.seed(0)

# Node size
N = 10  
p = 0.5
G = nx.fast_gnp_random_graph(N, p, seed=0)

##################################################
# # Same percolation attribute
# 모든 node에게 percolation 값을 동일하게 세팅할 경우에는,
# betweenness centrality와 동일한 값이 나옴.
print("== set SAME node percolation")
nx.set_node_attributes(G, 0.1, 'percolation')
percolation_cent_dict = nx.percolation_centrality(
    G=G,
    attribute='percolation',
)
bet_cent_dict = nx.betweenness_centrality(G)
for n in G:
    p, b = percolation_cent_dict[n], bet_cent_dict[n]
    p, b = round(p, 8), round(b, 8)
    if p!=b:
        print("DIFF", n, p, b)
print("=="*20)
##################################################
# Different node percolation
print("== set DIFFERENT node percolation")
BEFORE_percolation_cent_dict = nx.percolation_centrality(
    G=G,
    attribute='percolation',
)
# node 1의 percolation(여과율))이 커졌으므로,
# 여기를 지나가는 다른 node들의 percolation 값 또한 커져야 함
G.nodes[1]['percolation'] = 0.9
print(f"= node1 의 nbr들인 {G[1].keys()}의 percolation이 커져야함.")
AFTER__percolation_cent_dict = nx.percolation_centrality(
    G=G,
    attribute='percolation',
)
for n in G:
    bp = BEFORE_percolation_cent_dict[n]
    bp = round(bp, 8)
    ap = AFTER__percolation_cent_dict[n]
    ap = round(ap, 8)
    print("DIFF", n, bp, ap, "===", "Decrease" if bp>ap else "Increase")
print("==" * 20)
```

```
== set SAME node percolation
========================================
== set DIFFERENT node percolation
= node1 의 nbr들인 KeysView(AtlasView({2: {}, 4: {}, 8: {}}))의 percolation이 커져야함.
DIFF 0 0.08796296 0.04656863 === Decrease
DIFF 1 0.06018519 0.06018519 === Increase
DIFF 2 0.12962963 0.18627451 === Increase
DIFF 3 0.07407407 0.03921569 === Decrease
DIFF 4 0.18055556 0.30147059 === Increase
DIFF 5 0.00925926 0.00490196 === Decrease
DIFF 6 0.07407407 0.03921569 === Decrease
DIFF 7 0.13888889 0.07352941 === Decrease
DIFF 8 0.01388889 0.03676471 === Increase
DIFF 9 0.00925926 0.00490196 === Decrease
========================================
```



## rerference

- [networkx.algorithms.centrality.percolation_centrality](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.percolation_centrality.html#networkx.algorithms.centrality.percolation_centrality)