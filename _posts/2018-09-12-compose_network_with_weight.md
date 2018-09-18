---
title: 여러 network를 weight를 고려해서 합칩시다. 
category: python-lib
tags: python python-lib compose network networkx weight 
---

## compose network with weight

- 모든 네트워크를 합쳐서 관리하는 것이 아니라, 분리해서 관리하다가, 필요할때만, 네트워크를 합쳐서 관리하는 것이 더 효율적일 때가 있습니다. 
- 예를 들어서, 연도별로 네트워크를 따로 보는 것이 필요할 경우에는, 연도별 네트워크를 따로 만들어두고, 필요할때 연도별 네트워크를 하나로 합쳐서, 분석하는 것이 더 좋을 수도 있으니까요. 
- 이미 `networkx`에서 네트워크를 합치는 좋은 알고리즘들을 많이 만들어두었습니다. [operator in networkx](https://networkx.github.io/documentation/stable/reference/algorithms/operators.html)에서 보실 수 있습니다. 
- compose, union, disjoint union 등 그래프를 합치고, 분할하고 하는 다양한 네트워크가 있습니다만, 아쉬운 것은, 모두 `weight`가 없다고 가정한다는 것이죠. 

- 간단하게 두 네트워크 `A`, `B` 를 만들고 
- weight를 임의로 줍니다. 
- 그 다음 `nx.compose_all`를 하면, `weight`가 더해지는 것이 아니라, 마지막에 들어온 node의 `weight`를 참고합니다. 
- 참고하지 않을 거면, 하지 않거나, 하는게 좋지, 이렇게 애매하게 참고하는 건 이상하지 않나요? 

```python
import numpy as np 
import networkx as nx

np.random.seed(40)

A = nx.Graph()
B = nx.Graph()
A.add_nodes_from([(x, {'weight':np.random.randint(1, 4)}) for x in ['A', 'B', 'C']])
B.add_nodes_from([(x, {'weight':np.random.randint(1, 4)}) for x in ['B', 'C', 'D']])
print("nodes of A:", A.nodes(data=True))
print("nodes of B:", B.nodes(data=True))
print("nodes of union(A, B):", nx.compose_all([A, B]).nodes(data=True))
```

```
nodes of A: [('A', {'weight': 3}), ('B', {'weight': 2}), ('C', {'weight': 1})]
nodes of B: [('B', {'weight': 1}), ('C', {'weight': 3}), ('D', {'weight': 2})]
nodes of union(A, B): [('A', {'weight': 3}), ('B', {'weight': 1}), ('C', {'weight': 3}), ('D', {'weight': 2})]
```


## compose with weight

- 그래서 저는 weight를 고려하는 방식으로 `compose_all_with_weight`라는 함수를 만들어보려고 합니다. 
- 단, 모든 node, edge에는 모두 `weight`를 가지고 있다고 가정하고 진행합니다. 

```python
def compose_all_with_weight(Glst, merge_func=lambda x, y: x+y):
    ## Graph를 list로 받아서, 같은 node가 있을 경우 weight를 합하여 넣어줌
    ## 단, 우선, 모든 node, edge에 weight가 있다고 가정하고 graph를 입력받음
    def compose_with_weight(g1, g2, merge_func=merge_func):
        rG = g1.copy()
        ## add node
        for n in g2.nodes(data=True):
            if n[0] in rG.nodes():
                new_weight = merge_func(rG.nodes[n[0]]['weight'], n[1]['weight'])
                rG.nodes[n[0]]['weight'] = new_weight
            else:
                rG.add_nodes_from([n])
        ## add edge
        for e in g2.edges(data=True):
            if rG.has_edge(e[0], e[1]):
                new_weight = merge_func(rG[e[0]][e[1]]['weight'], e[2]['weight'])
                rG[e[0]][e[1]]['weight'] = new_weight
            else:
                rG.add_edges_from([e])
                
        return rG
    rG = nx.Graph()
    for subG in Glst:
        rG = compose_with_weight(rG, subG, merge_func)
    return rG
```

- 간단하게 테스트를 해보면 다음과 같습니다. 

```python
## test graph 
A = nx.Graph()
A.add_nodes_from([(x, {'weight':np.random.randint(1, 4)}) for x in ['A', 'B', 'C']])
A.add_edges_from([('A', 'B', {'weight':10})])
print("nodes of A:", A.nodes(data=True))
print("edges of A:", A.edges(data=True))
print("="*20)
## make compose A 
G_compose = compose_all_with_weight([A, A], merge_func=lambda x, y: x+y)
print('nodes of A:', G_compose.nodes(data=True))
print('nodes of A:', G_compose.edges(data=True))
```

```
nodes of A: [('A', {'weight': 1}), ('B', {'weight': 3}), ('C', {'weight': 3})]
edges of A: [('A', 'B', {'weight': 10})]
====================
nodes of A: [('A', {'weight': 2}), ('B', {'weight': 6}), ('C', {'weight': 6})]
nodes of A: [('A', 'B', {'weight': 20})]
```

## wrap-up

- 이런 코드는 networkx에 추가할 수 있을 것 같아요. 그런데, 지난번에도 느낀 것이지만, 오픈소스 프로젝트에 코드를 추가한다는 것은, 생각보다는 꽤 어려워요. 
- 해당 오픈소스 프로젝트에서 원하는 기존 코드를 오염시키지 않으면서, 다시 말해서 해당 프로젝트의 방향, 정책, 코드 수준 등을 모두 만족 시키는 수준에서 진행해야 하는데, **단순히 코드만 넣으면 되지 않을까?** 생각했던 것과는 차이가 있습니다. 

