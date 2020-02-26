---
title: python - networkx - multigraph to graph. 
category: python-libs
tags: python python-libs networkx multigraph graph 
---

## 2-line summary 

- `nx.MultiGraph`를 그냥 `nx.Graph()`으로 변환해주면 weight를 고려하지 못한다는 문제가 있음. 
- 따라서, weight를 고려하여 `nx.Graph()`를 만들어주는 함수를 정의.


## MultiGraph to Graph 

- MultiGraph는 보통 노드 `u`에서 노드 `v`로 가는 direct path가 한 개 이상 존재하는 것을 허용한 graph를 말합니다. 
- 간혹, MultiGraph를 Graph로 변환해야 할 때가 있는데, 다음처럼 코딩하시는 분들이 계시죠. 
- 그러나, 이렇게 할경우 weight를 전혀 고려하지 않고, 그냥 "가장 최근에 업데이트한 edge"만 남기고 모두 삭제하게 됩니다.

```python 
# MG: type => nx.MultiGraph()
G = nx.Graph(MG)
```

- 하지만, 여러 edge가 동시에 존재할 때는 어떤 weight를 `G`의 edge의 weight로 할지가 중요해지죠. 관점에 따라서, `max`, `sum`, `min` 등 다양한 aggregate function을 사용하여 weight를 합쳐주는 것이 좋습니다.
- 저는 다음처럼 코드를 작성하였고, `aggr_func`에 따라서, multiG_to_G로 효과적으로 변환해주는 함수를 정의하였습니다.

```python
import networkx as nx

def multiG_to_G(MG, aggr_func=max):
    rG = nx.Graph()
    # add nodes
    rG.add_nodes_from([n for n in MG.nodes()])
    # extract edge and their weights
    edge_weight_dict = {}
    for u, v, e_attr in MG.edges(data=True):
        e, weight = (u, v), e_attr['weight']
        if e in edge_weight_dict:
            edge_weight_dict[e].append(weight)
        else:
            edge_weight_dict[e] = [weight]
    # add edges by aggregating their weighy by `aggr_func`
    for e, e_weight_lst in edge_weight_dict.items():
        rG.add_edge(*e, weight=aggr_func(e_weight_lst))
    return rG
```

```python 
MG = nx.MultiGraph()
MG.add_edge(0, 1, weight=10)
MG.add_edge(1, 0, weight=3)
MG.add_edge(0, 1, weight=5)

print("== MG edges with weight ")
print(MG.edges(data=True))

print("== nx.Graph(MG) edges ")
# nx.Graph(MG)의 형태로 변환하면, "가장 최근에 add한 edge만 추가됨"
G = nx.Graph(MG)
print(G.edges(data=True))


print("== MG to G by max weight ")
MG_max_weight = multiG_to_G(MG, aggr_func=max)
print(MG_max_weight.edges(data=True))

print("== MG to G by sum weight ")
MG_sum_weight = multiG_to_G(MG, aggr_func=sum)
print(MG_sum_weight.edges(data=True))

print("== MG to G by min weight ")
MG_min_weight = multiG_to_G(MG, aggr_func=min)
print(MG_min_weight.edges(data=True))
```

- 코드의 실행 결과는 다음과 같죠. 

```
== MG edges with weight
[(0, 1, {'weight': 10}), (0, 1, {'weight': 3}), (0, 1, {'weight': 5})]
== nx.Graph(MG) edges
[(0, 1, {'weight': 5})]
== MG to G by max weight
[(0, 1, {'weight': 10})]
== MG to G by sum weight
[(0, 1, {'weight': 18})]
== MG to G by min weight
```


## reference

- [Networkx : Convert multigraph into simple graph with weighted edge](https://stackoverflow.com/questions/15590812/networkx-convert-multigraph-into-simple-graph-with-weighted-edges)
