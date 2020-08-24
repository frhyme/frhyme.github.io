---
title: networkx - community detection - girvan newman method.
category: python-libs
tags: python python-libs networkx community community-detecction
---

## networkx - community detection - girvan newman method.

- community detection 방법은 네트워크에서 보다 긴밀한 관계를 가지는, 노드 그룹을 뽑아내는 방법을 말합니다.  특히, girvan newman method는 가장 가치가 높은 edge를 순차적으로 잘라나가면서 group을 계층적으로 분화하는데, 여기서 edge의 가치는 기본적으로는 `edge_betweenenss centrality`를 통해서 평가됩니다. 
- 물론, 필요에 따라서, 직접 변경해서 처리할 수도 있구요. 

## Do girvan newman method using `NetworkX`

- 사실, 그냥 다음처럼 실행하면 되지만, 리턴되는 값이 `generator`입니다. 즉, loop를 통해서 하나하나 읽으면서 어떻게 분화되는지를 파악해야 한다는 이야기죠.

```python
# type: generator
# community_generator = nx.algorithms.community.girvan_newman(G=G)  
```

- 다음 코드에서는 edge의 평가 방법을 다르게 처리하여, 서로 다른 방식으로 community를 도출해 봤습니다.

```python
import networkx as nx
################################################
# most_valuable_edge function:
# girvan-newman method는 edge의 value를 평가하여,
# 가장 중요한 edge부터 순차적으로 자르면서 community를 생성
# default는 edge-betweenness-centrality를 평가하는 것이며,
# 아래처럼 각자 함수를 정의하여 넘겨줄 수도 있음.
def most_valuable_edge_ebc(inputG):
    # edge betweenness centrality를 계산하여 가장 높은 edge를 리턴하는 함수
    ebc = nx.edge_betweenness_centrality(inputG)
    return max(ebc, key=ebc.get)

def most_valuable_edge_dispersion(inputG):
    # edge중에서 dispersion이 높은 edge를 리턴
    r_dict = {}
    for e in inputG.edges():
        u, v = e
        r_dict[e] = nx.dispersion(inputG, u, v)
    return max(r_dict.items(), key=lambda x: x[1])[0]
################################################

"""
girvan-newman method를 사용하여 community detection을 수행함. 
- most_valuable edge를 평가하는 방법을 변경하여 그 차이를 비교함.
1) edge betweenness centrality를 사용(default)
2) dispersion을 사용하여 edge의 중요도를 평가.
"""

# Generate graph
N = 20
G = nx.scale_free_graph(N, seed=0)
G = nx.Graph(G)
assert nx.is_connected(G)==True
print("==" * 20)
print("== community detection by edge betweenness centrality")
community_generator = nx.algorithms.community.girvan_newman(
    G=G, most_valuable_edge=most_valuable_edge_ebc)  # type: generator

for i, communities_at_i in enumerate(community_generator):
    # n개의 node가 있을 때, n개의 community까지 분화할 수 있으므로,
    # n개로 분화되면 loop 탈출.
    print(f"== {i:2d} time.")
    for j, comm in enumerate(communities_at_i):
        print(f"community {j:2d} at time {i:2d} ==> {comm}")
    if i>=2:
        break
print("--" * 20)
print("--" * 20)
community_generator = nx.algorithms.community.girvan_newman(
    G=G, most_valuable_edge=most_valuable_edge_dispersion)  # type: generator
for i, communities_at_i in enumerate(community_generator):
    # n개의 node가 있을 때, n개의 community까지 분화할 수 있으므로,
    # n개로 분화되면 loop 탈출.
    print(f"== {i:2d} time.")
    for j, comm in enumerate(communities_at_i):
        print(f"community {j:2d} at time {i:2d} ==> {comm}")
    if i >= 2:
        break
print("==" * 20)
```

```
========================================
== community detection by edge betweenness centrality
==  0 time.
community  0 at time  0 ==> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18}
community  1 at time  0 ==> {19, 13}
==  1 time.
community  0 at time  1 ==> {0, 2, 3, 4, 5, 6, 7, 9, 10, 11, 14, 15, 18}
community  1 at time  1 ==> {1, 8, 12, 16, 17}
community  2 at time  1 ==> {19, 13}
==  2 time.
community  0 at time  2 ==> {0, 2, 3, 4, 5, 6, 7, 9, 10, 14, 15, 18}
community  1 at time  2 ==> {1, 8, 12, 16, 17}
community  2 at time  2 ==> {11}
community  3 at time  2 ==> {19, 13}
----------------------------------------
----------------------------------------
==  0 time.
community  0 at time  0 ==> {0}
community  1 at time  0 ==> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
==  1 time.
community  0 at time  1 ==> {0}
community  1 at time  1 ==> {1, 8, 12, 16, 17}
community  2 at time  1 ==> {2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 18, 19}
==  2 time.
community  0 at time  2 ==> {0}
community  1 at time  2 ==> {16, 1, 12, 17}
community  2 at time  2 ==> {2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 18, 19}
community  3 at time  2 ==> {8}
========================================
```

## wrap-up

- scale-free graph에 대해서 각각 dispersion, edge betweenness centrality를 적용해본 결과, community가 조금씩 다르게 형성되는 것을 알 수 있습니다. 실제 현상을 분석한다면, 이것이 왜 그런지 좀 더 자세하게 해석할 수 있겠죠.



## reference

- [networkx.algorithms.community.centrality.girvan_newman](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.centrality.girvan_newman.html#networkx.algorithms.community.centrality.girvan_newman)