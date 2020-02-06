---
title: networkx - algorithms - clustering
category: others
tags: python python-libs clustering triangle
---

## networkx - algorithms - clustering

- [networkx - clustering](https://networkx.github.io/documentation/stable/reference/algorithms/clustering.html)의 내용들을 정리합니다.

### triangles

- `G`에서 node `n`을 포함한 삼각형의 수를 말합니다.

### transitivity

- 번역이 조금 어려운데, '이행성, 전달성, 전이성'정도로 이해하시면 됩니다. 오히려 이 개념은 다음의 수식을 보면 쉬워요. 보통 전이성(transitivity)를 가진다고 하면 다음 3 조건을 만족합니다.
    - A -> B
    - B -> C
    - C -> A
- 따라서, 이를 Graph `G`에 적용한다면, 다음을 물어보고 있는 것이죠. 
    - if node `A`와 node `B`가 연결되어 있고, `B`와 `C`가 연결되어 있다면, `A`와 `C`가 연결되어 있을 가능성은? 
- 따라서, 보통 완성된 삼각형(edge가 3개인 삼각형) / 미완성된 삼각형(edge가 2개인 삼각형) 으로 나누어 계산합니다. 
- 보통 complext network나 small-world network의 경우 높은 transitivity를 가지며, 반대로 diameter는 낮게 나타나죠.
- 그리고, 여기서는 삼각형에 대해서 적용했지만, 길이가 4, 5인 경우에 대해서도 비슷하게 적용하여 transitivity를 확인할 수 있습니다. 

### clustering

- node `u`의 clustering coeffcient는 "(`u`를 포함하여 이웃노드들간에 존재하는 삼각형의 수)/(가능한 삼각형의 수)"를 말합니다. 

## Compute it using `networkx`

- 고맙게도 `networkx`에 이미 함수들이 다 있고, 사용법과 결과들은 다음과 같습니다.

```python
import networkx as nx
import numpy as np

np.random.seed(0)

N = 50
G  = nx.fast_gnp_random_graph(n=N, p=0.5)
#G = nx.scale_free_graph(N)
G = nx.Graph(G)
##################################
# nx.triangles(G, n)
# node `n`을 포함한 삼각형의 수를 리턴
print("== nx.trianbles(G, n)")
for i, n in enumerate(G):
    print(f"Node {n} triangle count: {nx.triangles(G, n)}")
    if i>2:
        break
print("=="*20)
##################################
# Transitivity는 완성된 삼각형의 수 / 미완성 삼각형(edge2개)
# 전이성(A=>B=>C)가 그래프에 있음을 파악하며, 보통 복잡한 네트워크, small-world에서는 높게 나타남.
print("== nx.transitivity(G)")
print(f"nx.transitivity(G): {nx.transitivity(G):0.4f}")
print("==" * 20)
##################################
# clustering
def custom_clustering(G, target_node):
    # node clustering:
    # target_node의 nbr들에 의해 발생할 수 있는 triangle과 실제 존재하는 triangle의 비율
    triangle_count = nx.triangles(G, target_node)
    target_node_nbr_count = len(G[target_node])
    possible_triangle_count = (target_node_nbr_count-1)*(target_node_nbr_count)/2
    if possible_triangle_count == 0:
        return 0
    else:
        return triangle_count/possible_triangle_count
print("== nx.clustering(G, n)")
for n in G:
    # custom_clusgering과 nx.clustering은 동일함.
    print(f"nx.clustering(G, n): {nx.clustering(G, n):0.4f}")
    break
print("==" * 20)
##################################
# average clustering
# 모든 node clustering coef의 평균.
print(f"nx.average_clustering(G): {nx.average_clustering(G):0.5f}")
avg_clustering = sum([nx.clustering(G, n) for n in G])/len(G)
print(f"avg_clustering          : {avg_clustering:0.5f}")
print("=="*20)
```

```
== nx.trianbles(G, n)
Node 0 triangle count: 142
Node 1 triangle count: 111
Node 2 triangle count: 178
Node 3 triangle count: 162
========================================
== nx.transitivity(G)
nx.transitivity(G): 0.4951
========================================
== nx.clustering(G, n)
nx.clustering(G, n): 0.4733
========================================
nx.average_clustering(G): 0.49588
avg_clustering          : 0.49588
```

## wrap-up

- 여기서는, triangle을 최소단위로 하여, triangle에 기반한 clustering coefficient를 계산하였지만, 경우에 따라서, square, 혹은 그 이상의 cycle을 기본 단위로 하여, 계산하는 경우도 있습니다. 물론, 저는 거기까지는 알 필요 없다고 생각해서 그 내용을 보완하지는 않았습니다.


## reference

- [transitivity in a graph](https://transportgeography.org/?page_id=6171)