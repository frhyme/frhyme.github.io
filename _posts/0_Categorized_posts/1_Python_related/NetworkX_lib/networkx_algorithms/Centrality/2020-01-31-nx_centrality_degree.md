---
title: networkx - centrality - Degree
category: python-libs
tags: python python-libs networkx centrality degree-centrality
---

## networkx - Degree Centrality.

- `Degree`는 각 node에 직접 연결된 node의 수를 말한다. 아주 단순히 봤을 때, 이 값이 클수록 해당 노드가 그래프에서 가지는 직접적인 영향력이 큰 것은 자명하며, 이 값을 중심으로 node의 영향력을 평가하는 것을 `degree centrality`라고 한다. 그러나, 해당 값은 그저 `degree`를 "해당 그래프에서 가능한 최대의 degree, 즉, (node size - 1)로 나눈 것에 불가하다. 
- 또한, 방향성이 있는 Graph인 `nx.DiGraph()`에 대해서는 indegree, outdegee와 같이, 방향성을 고려한 degree centrality 또한 계산할 수 있다. 

```python
import networkx as nx
import numpy as np
import time

# GENERATE Graph size
N = 10
p = 0.6
G = nx.fast_gnp_random_graph(N, p)

##############################
# Degree Centrality
print("=="*20)
# `nx.degree_centrality` 실행 결과는 dictionary(node => deg)로 리턴됨.
for n, n_deg in nx.degree_centrality(G).items():
    # degree centrallity는 해당 graph에서 가능한 최대의 degree인 Node_size -1 로 나눈다.
    # multigraph에서도 동일하게, normalize하며, 따라서 1보다 커질 수도 있음.
    calc_by_degree = nx.degree(G, n)/(len(G)-1)
    print(f"node {n:2d} - deg cent: {n_deg:5.3f} - deg cent(calc) {calc_by_degree:5.3f}")
print("=="*20)

##############################
# In-Degree Centrality and Out-Degree Centrality.
try:
    in_deg_cent_dict  = nx.in_degree_centrality(G)
    out_deg_cent_dict = nx.out_degree_centrality(G)

except:
    # undirected type, 즉 Graph에 대해서 in-degree or out-degree centrality를 계산할 경우 에러 발생
    # networkx.exception.NetworkXNotImplemented: not implemented for undirected type
    G_dir = G.to_directed()
    in_deg_cent_dict  = nx.in_degree_centrality(G_dir)
    out_deg_cent_dict = nx.out_degree_centrality(G_dir)
for k in in_deg_cent_dict:
    in_deg = in_deg_cent_dict[k]
    out_deg = out_deg_cent_dict[k]
    print(f"node {k:2d} - indegree: {in_deg:5.3f}, outdegree: {out_deg:5.3f}")
```