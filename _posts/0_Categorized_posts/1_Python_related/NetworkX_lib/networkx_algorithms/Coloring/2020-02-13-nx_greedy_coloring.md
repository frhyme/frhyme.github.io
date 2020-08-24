---
title: networkx - coloring - greedy coloring 
category: python-libs
tags: python python-libs networkx coloring 
---

## line summary. 

## What is Graph Coloring? 

- [Graph coloring](https://en.wikipedia.org/wiki/Graph_coloring)은, 말 그대로 "Graph에 색칠을 하는 것"을 말합니다. 단, 여기서 필요한 색깔의 수 `k`를 최소화하는 것을 보통 목적으로 하죠. 그리고 node를 색칠하느냐, edge를 색칠하느냐에 따라서 조금씩 달라집니다. 

### Greedy Coloring and do it in `networkx` 

- [Greedy Coloring](https://en.wikipedia.org/wiki/Greedy_coloring)은, 그냥 node를 탐색(traversal)하는 방법만 변형하면서, 현재 상태에서 가장 적합한 색칠을 하는 겁니다. 그냥 "기존에 썻던 색깔을 쓸 수 있으면, 쓰고 없으면 새로운 색을 쓴다"라는 것이 다죠. 
- 매우 간단하므로, 알고리즘 설명은 따로 하지 않고, 근야 `networkx`에 있는 방법을 간단하게 써봤습니다. `traver stratey`만 변형해가면서, 각 전략별로 몇 개의 색깔이 필요한지를 파악해봤씁니다.

```python 
import networkx as nx

N = 500
G = nx.scale_free_graph(10)
G = nx.Graph(G)

coloring_strategy = [
    'largest_first',
    'random_sequential',
    'independent_set',
    'connected_sequential_bfs',
]
print("==" * 30)
for strategy in coloring_strategy:
    # coloring_dict: dict(node_name, node_color)
    coloring_dict = nx.greedy_color(G, strategy=strategy)
    all_used_colors = set(coloring_dict.values())
    print(f"== Required color # of {strategy:30s}:  {len(all_used_colors)}")
print("=="*30)
```

- scale-free graph에 대해서는 node의 수를 몇개로 하든, 보통 3, 4 이면 충분하더군요.

```
============================================================
== Required color # of largest_first                 :  4
== Required color # of random_sequential             :  4
== Required color # of independent_set               :  4
== Required color # of connected_sequential_bfs      :  4
============================================================
```


### Application of Graph Coloring. 

- [Graph coloring - Application](https://en.wikipedia.org/wiki/Graph_coloring#Applications)에 정리된 내용을 번역하였습니다. 

#### Scheduling

- vertex coloring model 문제의 경우는 쉽게 scheduling 문제로 변환이 가능합니다. 
- 가령, 우리에게 n개의 해야할 일(job)이 있고, 이 job이 어느 날짜에 수행되어야 하는지 assignment하는 것이 필요할 수 있습니다. 그리고, 모든 job은 동일하게, '1 day'의 작업시간이 필요하다고 할게요. 그리고, 어떤 job들끼리는, 동일한 resource를 사용하기 때문에, 같은 날에 집어넣을 수가 없습니다. 
- 이 문제를 Graph로 변환한다면, node는 job을 의미하게 되고, edge는 conflict가 발생하는(같은 resource를 사용하는) job들로 섞을 수 있습니다. 따라서, 만약 이 graph를 색칠할 수 있는 최소한의 수는 모든 job을 충돌없이 끝낼 수 있는 '시간'과 동일한 문제로 변환되죠. 

#### Register allocation

- 이 문제 자체는 앞서 말한 scheduling과 비슷한데, 분야가 다르니까 마저 정리하기는 합니다.
- compiler는 컴퓨터 언어를 다른 언어(보통 assembly와 같은 low-level lang)로 변환해주는 역할을 수행합니다. 
- 이 때, 코드 변환 시간을 단축시키기 위해서, 사용하는 compiler optimization 테크닉 중 하나가, 바로 [register allocation](https://en.wikipedia.org/wiki/Register_allocation) 입니다. 이는, processor register가 가장 속도가 빠르기 때문에, "가장 많이 사용되는 값"을 여기에 넣어두는 것이 가장 효과적이기 때문이죠. 
- textbook에서는 이 문제를 graph coloring problem처럼 푸는 방법을 소개하는데, 컴파일러가 "interference graph"라는, "node가 variable이고, edge는 두 node 동시에 사용될 경우를 의미하는 Graph"를 만듭니다. 그리고 색칠을 하였을 때 k개의 색깔이 필요하다면, 매번 register에 k개만 적재해놓으면 되는 것이죠.


## reference 

- [networkx - greedy color](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.coloring.greedy_color.html#networkx.algorithms.coloring.greedy_color)
- [Greedy Coloring](https://en.wikipedia.org/wiki/Greedy_coloring)
- [Graph coloring - Application](https://en.wikipedia.org/wiki/Graph_coloring#Applications)