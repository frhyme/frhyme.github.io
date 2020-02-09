---
title: networkx - community detection - greedy modularity communities
category: python-libs
tags: python python-libs networkx community community-detection optimization
---

## 1-line summary 

- girvan-newman method말고, [networkx - greedy modularity communities](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.modularity_max.greedy_modularity_communities.html#networkx.algorithms.community.modularity_max.greedy_modularity_communities)를 사용하면, 훨--씬 빠르게, 더 높은 modularity를 가지는 community 집단을 뽑아낼 수 있다. 

## networkx - greedy modularity communities

- [networkx - greedy modularity communities](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.modularity_max.greedy_modularity_communities.html#networkx.algorithms.community.modularity_max.greedy_modularity_communities)에 대해서 소개합니다. 
- 저는 보통 community detection을 위해서, [girvan-newman method](https://en.wikipedia.org/wiki/Girvan%E2%80%93Newman_algorithm)를 사용하는데요, 이 아이는 hierarchical 하게 community를 뽑아준다는 강점이 있으며, 전체 네트워크에서 edge를 하나씩 없애면서 community를 만들기 때문에, 개념적으로 이해하기도 쉽다는 강점이 있습니다. 즉, 심-플 앤 파워-풀 이라고 말할 수 있겠죠. 
- 다만, 그 과정에서 시간이 매우 많이 걸린다는 단점이 있기는 합니다. 그리고 일일이 파악하면서 진행해야 한다는 단점도 있죠. 
- 반면, `greedy modularity communities`의 경우는 시간이 매우 빠르고, 그 결과로 나오는 community의 modularity도 girvan-newman method보다 높은 경향성을 보입니다. 알고리즘 자체는, 다음으로 매우 단순합니다.
    - N개의 node가 있을 때, N개의 community부터 출발
    - 그냥 greedy하게 modularity를 올려준다고 판단될 경우 community pair를 병합(merge). 

## Do it. 

- 귀-찮으므로 직접 코딩해주지 않고, 충분히 큰 그래프에 대해서 두 가지 community detection 방법을 사용하여 비교해봅니다. 
- 결론부터 말하자면, `greedy modularity communities`의 속도가 훨-씬 빠르다. modularity도 너 크다.

```python
import networkx as nx
import time

# Generate graph
N = 300
G = nx.scale_free_graph(N, seed=0)
G = nx.Graph(G)
assert nx.is_connected(G) == True

print("==" * 30)
print("== community detection by edge betweenness centrality")
girvan_start_time = time.time()
Max_modularity = 0
Max_module_communities = None
community_generator = nx.algorithms.community.girvan_newman(G=G)
for i, comms in enumerate(community_generator):
    comm_modularity = nx.algorithms.community.modularity(G, comms)
    if Max_modularity<=comm_modularity:
        Max_modularity = comm_modularity
        Max_module_communities = comms
    gen_time = time.time() - girvan_start_time
    #print(f"{i:2d} Modularity: {comm_modularity:.5f} == times: {gen_time}")
    if comm_modularity<0.001:
        break
print(
    f"Max_modularity: {Max_modularity:.5f}, time: {time.time() - girvan_start_time:.5f}"
)
for i, comm in enumerate(Max_module_communities):
    #print(f"community {i:2d} ::: {comm}")
    continue
print("=="*30)
print("== community detection by greedy modularity community")
#================================================
# by greedy modularity community
greedy_start_time = time.time()
greedy_module_comms = nx.algorithms.community.greedy_modularity_communities(G)
print(
    f"Modularity: {nx.algorithms.community.modularity(G, greedy_module_comms):.5f}  == times: {time.time() - greedy_start_time:.5f}"
)
for i, comm in enumerate(greedy_module_comms):
    #print(f"community {i:2d} ::: {comm}")
    continue
print("== complete")
print("==" * 30)
```

```
============================================================
== community detection by edge betweenness centrality
Max_modularity: 0.47044, time: 64.24782
============================================================
== community detection by greedy modularity community
Modularity: 0.50138  == times: 0.25804
== complete
============================================================
```

## wrap-up

- 그러함에도, community간의 hierarhcical 한 관계를 뽑아주는, girvan-newman method도 나름의 강점이 있다고 생각되기는 하는데요 흠흠흠.

## reference

- [networkx.algorithms.community.modularity_max.greedy_modularity_communities](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.modularity_max.greedy_modularity_communities.html#networkx.algorithms.community.modularity_max.greedy_modularity_communities)