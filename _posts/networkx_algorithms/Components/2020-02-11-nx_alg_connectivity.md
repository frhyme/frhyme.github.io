---
title: networkx - connectivity
category: python-libs
tags: python python-libs networkx connectivity
---

## 3-line summary. 

- 네트워크에서 [component](https://en.wikipedia.org/wiki/Component_(graph_theory))는 "connected component"라고 불리기도 하며, "집단 내 어떤 두 노드 사이에도 path가 존재하는 집단"을 보통 말한다. 

## networkx - component

- [component(connected component)](https://en.wikipedia.org/wiki/Component_(graph_theory))는 "집단 내 어떤 두 노드 사이에도 path가 존재하는 node 집단"을 말합니다. 즉, "서로 연결된 집단"이라고 이해하시면 되는데, 방향성이 있는 경우에는 다음 두 가지로 구분됩니다.
    - strong connected: 양방향으로 다 길이 있는 경우(strong connected)
    - weak connected: 최소 한 방향으로는 길이 있는 경우 
- 아래 그림을 보시면 더 명확해지죠. 

![connected component](https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Pseudoforest.svg/360px-Pseudoforest.svg.png)

## Component 뽑아내기 

- [networkx - components](https://networkx.github.io/documentation/stable/reference/algorithms/component.html)의 함수들을 사용해서 component들을 뽑아냅니다. 

### `nx.is_connected(G)`

- 현재 graph `G`가 모두 연결되어 있는지를 확인하는 함수입니다. 

```python
nx.is_connected(G)# True or False
```

### `nx.number_connected_components(G)`

- graph `G`에 존재하는 component의 수가 몇 개인지를 return합니다.

```python
if nx.number_connected_components(G)>1:
    assert nx.is_connected(G)==False
else:
    assert nx.is_connected(G)==True
```

### `nx.connected_components(G)`

- graph `G`에 존재하는 component를 생성하는 generator를 리턴합니다.

```python
for com in nx.connected_components(G):
    print(comm)
```

## Exercise: Random하게 edge를 추가하며, component 변화 보기.

- 그냥 이렇게만 알고 끝내면 재미가 없으므로, 
    - node만 존재하는 `G`에 
    - random하게 edge를 추가하면서, 
    - component의 수가 어떻게 변화하는지를 파악해보자. 

```python
import networkx as nx
import numpy as np

# random으로 node를 만들어가면서 Component가 얼마나 생기는지를 확인함.
G = nx.Graph()
N = 30
G.add_nodes_from([i for i in range(0, N)])

# insertion edge
MAX_E = len(G)*(len(G)-1)//2
EACH_E = 10 # 한번에 업데이트되는 edge의 수
for E in [EACH_E for n in range(0, MAX_E // EACH_E)]:
    #============================================
    # INSERT Edge
    for _ in range(0, E):
        while True:
            u, v = np.random.randint(0, len(G), 2)
            if u not in G[v]:  # u, v not connected
                G.add_edge(u, v)
                break
    #============================================
    print(f"== edge size: {len(G.edges())}")
    print(f"== nx.is_connected(G): {nx.is_connected(G)}")
    print(
        f"nx.number_connected_components(G): {nx.number_connected_components(G)}"
    )
    component_size_lst = [len(comp) for comp in nx.connected_components(G)]
    component_size_lst = sorted(component_size_lst, reverse=True)
    print(f"component size dist: {component_size_lst}")
    print("--"*30)
    if nx.is_connected(G)==True:
        break
    #===========================================================================

```

- edge를 10개 추가했을때로 나누어서 출력을 해 보면, 30개의 노드가 존재하미만, 60개의 edge만 추가해도 모든 노드가 하나로 연결됩니다.

```
== edge size: 10
== nx.is_connected(G): False
nx.number_connected_components(G): 21
component size dist: [5, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
------------------------------------------------------------
== edge size: 20
== nx.is_connected(G): False
nx.number_connected_components(G): 15
component size dist: [14, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
------------------------------------------------------------
== edge size: 30
== nx.is_connected(G): False
nx.number_connected_components(G): 8
component size dist: [20, 4, 1, 1, 1, 1, 1, 1]
------------------------------------------------------------
== edge size: 40
== nx.is_connected(G): False
nx.number_connected_components(G): 4
component size dist: [27, 1, 1, 1]
------------------------------------------------------------
== edge size: 50
== nx.is_connected(G): False
nx.number_connected_components(G): 2
component size dist: [29, 1]
------------------------------------------------------------
== edge size: 60
== nx.is_connected(G): False
nx.number_connected_components(G): 2
component size dist: [29, 1]
------------------------------------------------------------
== edge size: 70
== nx.is_connected(G): True
nx.number_connected_components(G): 1
component size dist: [30]
------------------------------------------------------------
```
    
## wrap-up

- community, cluster 들이 많지만, 만약 edge의 weight를 측정할 수 있다면, 약한 weight를 그저 없애는 것만으로도 많은 component들을 뽑아낼 수 있으며, 이것만으로도 꽤 의미있는 노드 집단이 되죠.


## reference 

- [networkx components](https://networkx.github.io/documentation/stable/reference/algorithms/component.html)