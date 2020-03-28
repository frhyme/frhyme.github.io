---
title: networkx에서 MultiGraph에 대해 Centrality 계산하기. 
category: python-libs
tags: python python-basic python-libs centrality networkx MultiGraph
---

## networkx - MultiGraph에 대해서 Centrality 계산하기. 

- networkx에서는 Graph를 총 4가지 방법으로 표현할 수 있습니다. 방향성(Directionality) 그리고 Multiple-Edge에 따라서 2개로 나누어 `nx.Graph()`, `nx.DiGraph()`, `nx.MultiGraph()`, `nx.MultiDiGraph`로 4가지로 구분되죠. 
- 여기서 만약 해당 Graph를 대상으로 중요한 node를 뽑아내어야 한다고 해봅시다. 일단은 closeness Centrality라고 해볼게요. 

### Graph : nx.closeness_centrality

- 자세한 내용은 [](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.closeness_centrality.html)를 읽어보시는 것이 좋구요. 
- `G`에는 대상이 되는 Graph를 넘기고 `u`에는 구하려고 하는 nodeID를 넘기지만 보통 그냥 None으로 해서 넘기면 전체에 대해서 계산해줍니다.
- `distance`는 closeness_centrality를 계산할때 거리를 어떻게 계산할 것인지를 정의해줍니다. 아무것도 없이 `None`일 경우에는 그냥 모든 edge의 weight를 1.0으로 고정하고 계산해줍니다. 만약, 모든 edge의 거리를 동일하게 세팅하지 않고, 다른 값으로 설정해주고 싶다면, edge_attribute_dictionary에 값이 존재해야 하며, 이 딕셔너리에 존재하는 key를 넘겨줍니다. 

```python
nx.closeness_centrality(G, u=None, distance=None, wf_improved=True)
```

- 예를 들면 다음과 같죠. G의 edge attribute dictionary에 특정 정보가 `key:value`로 존재해야 합니다. 만약 존재하지 않는다면, 그냥 1.0으로 암묵적으로 가정하고 계산해주죠.

```python
G = nx.Graph()
# 현재, 모든 edge의 attribute_dictionary에 
# weight, distance 정보가 포함되어 있죠.
G.add_edges_from([
    (0, 1, {'distance': 1.0, 'weight': 0.6}). 
    (1, 2, {'distance': 0.5, 'weight': 0.3})
])
# distance를 사용하여 최단 거리를 계산하여 주고 싶으면 'distance'를 넘겨주고 
nx.closeness_centrality(G, distance='distance')
# weight를 사용하여 최단 거리를 계산하여 주고 싶으면 'weight'를 넘겨주면 됩니다.
nx.closeness_centrality(G, distance='weight')
```

### MultiGraph : nx.closeness_centrality

- 즉, 기본적으로는 `Graph`에 대해서 closeness_centrality등을 계산한다고 생각합니다. 그래서, 그냥 `attr_key`정보만 넘겨주는 것이죠. 
- 그렇다면, 만약에 우리가 어떤 대상을 `nx.MultiGraph`으로 가지고 있다면 어떻게 해야 할까요? 
- 우리의 `MG`는 edge의 중복을 허용합니다. 삽입되는 edge를 보면 `(0, 1)`이 2개 포함되어 있습니다.

```python
import networkx ax nx
MG = nx.MultiGraph()

MG.add_edges_from([
    (0, 1), (0, 1), (1, 2), (2, 0)
])
```

- 만약, 그냥 "2개가 있거나 1개가 있거나 차이가 없다라고 보겠다"라면, 그냥 똑같이 계산해주면 됩니다. 즉 "연결되어 있으면 1 아니면 0"으로 계산되는 것이죠. 

```python
print(
    nx.closeness_centrality(MG))
```

- 즉, MG의 모든 edge의 weight가 동일하므로, 다음과 같은 결과가 나옵니다. 만약, 우리의 의도가 그랬다면 문제가 없죠.

```
{0: 1.0, 1: 1.0, 2: 1.0}
```

- 다만, 필요에 따라서, 우리는 MultiGraph에 존재하는 Edge가 많을 수록 두 node간의 거리를 가깝게 변경하고 싶을 수도 있겠죠. 
- 그렇다면 다음처럼 MultiGraph를 WeightGraph로 변경한 다음 처리해줘야 합니다. 

```python
import networkx ax nx
MG = nx.MultiGraph()

MG.add_edges_from([
    (0, 1), (0, 1), (1, 2), (2, 0)])

# MG를 G로 변경
# 그 과정에서 G의 edge의 weight는 MG에 존재하는 edge의 수 
G = nx.Graph()
G.add_nodes_from(MG.nodes())
for u, v, k, d in MG.edges(keys=True, data=True):
    if G.has_edge(u, v) == True: 
        G[u][v]['weight']+=1
    else:
        G.add_edge(u, v, weight=1)
# weight는 edge의 수만큼 늘어나고, distance는 그 역수. 
# 따라서, 그 역수를 다시 edge_attribute_dict로 넣어줘야 함.
for u, v, d in G.edges(data=True):
    G[u][v]['distance'] = 1.0 / G[u][v]['weight']
print(nx.closeness_centrality(G, distance='distance'))
```

- 위의 과정을 거치면 계산이 됩니다. 하지만, 좀 매우 귀찮아진다고 생각합니다. 
- 우선, 잘 관리하고 있는 MultiGraph로부터, 새로운 Graph를 만들어서 관리해줘야 하고, 
- 그리고 weight를 계산한 다음 다시 distance를 만들어서 넣어줘야 하죠. 그렇다면 만약, 계산 방법이 조금씩 달라질 때마다 매번 새로운 edge_attr을 추가해줘야 한다는 말이 되니까요. 

### better way with lambda. 

- 그래서, 저는 보다 간단하고 쉬운 방법을 사용합니다. 
- 코드 먼저 보여드리면 다음이 다죠. 새로운 `G`를 만들지도 않았고, 그 값을 edge_attr에 저장하지도 않았습니다. 
- `nx.closeness_centrality`의 parameter, `distance`는 우리가 흔히 edge_attr의 key만 넘겨준다고 알고 있지만, 다음처럼 function으로 넘겨줘도 됩니다. 그리고 그 function은 `u, v, d`라는 3가지 값을 입력받아서, float을 반환하는 구조죠. 그리고, u, v는 edge의 양 끝이며, d는 edge_attr을 말하죠.
- 따라서, 위는 `MG`에 존재하는 `u`부터, `v`까지의 존재하는 edge의 수의 역수를 거리로 잡아준다는 개념으로 생각하시면 됩니다.

```python
distance_func = lambda u, v, d: 1.0/len(MG[u][v]
print(nx.closeness_centrality(MG, distance=distance_func))
```

- betweenness_centrality의 경우는 `nx.MultiGraph`에 대해서 `not_implemented_for`가 적용되어 있어서, 안되는 것처럼 보이지만, 다음처럼 틀어서 해주면 됩니다.
- `MG`와 `G`의 Node-set는 똑같기 때문에, 변형해서 그대로 넘겨주고, 그 다음에 `weight`에 같은 함수를 적용해주면 알아서 계산해줍니다.

```python
print(
    nx.betweenness_centrality(
        nx.Graph(MG), 
        weight=lambda u, v, d: 1.0/len(MG[u][v])
    )
)
```

- 다만, pagerank는 안됩니다. 이 아이는 matrix 연산이기 때문에, 같은 방식으로 적용해서는 안되요.