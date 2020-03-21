---
title: python - networkx - centrality with weight
category: python-libs
tags: python python-libs networkx centrality weight
---

## networkx - centrality with weight

- network에서 centrality를 계산할 때, 기본적으로는 edge의 weight를 모두 1로 가정합니다. 
- 이럴 때는 상관없지만, weight 값에 따라서, centrality가 달라질 때, 그냥 아무 생각없이 weight를 그대로 넘겨주지만, 사실 이게 distance를 의미하는 건지, 아니면 중요도 를 의미하는 것인지가 centrality에 따라서 조금씩 다르게 결과가 나옵니다. 


## closeness centrality with weight

- `nx.closeness_centrality`는 `weight`가 아닌 distance를 입력받습니다. 따라서, 명쾌하죠. 이 값이 클수록 거리가 멀게 측정되죠. 

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([
    (0, 1, {'weight': 1}), 
    (1, 2, {'weight': 2}),
    (2, 0, {'weight': 1}),
])

print("== CLOSENESS centrality with weight")
print(nx.closeness_centrality(G, distance='weight'))
print("== CLOSENESS centrality without weight")
print(nx.closeness_centrality(G))
print("=="*20)
```

- 아래 실행 결과를 보시면, weight를 고려한 경우와 고려하지 않은 경우의 결과가 다르죠.

```
== CLOSENESS centrality with weight
{0: 1.0, 1: 0.6666666666666666, 2: 0.6666666666666666}
== CLOSENESS centrality without weight
{0: 1.0, 1: 1.0, 2: 1.0}
```

## betweenness centrality with weight

- `nx.betweenness_centrality`의 경우 `weight`라고 되어 있지만, distance와 동일합니다. 즉, 값이 클수록 거리를 계산할 때, 멀게 계산되고, 최단거리에 포함되지 않을 확률이 높아지죠. 

```python
G = nx.Graph() 
G.add_edges_from([
    (0, 1, {'weight':1}), 
    (0, 2, {'weight':2}), 
    (1, 9, {'weight':1}),
    (2, 9, {'weight':1}),
])

print("== BETWEENNESS centrality with weight")
print(nx.betweenness_centrality(G, weight='weight'))
print("== BETWEENNESS centrality without weight")
print(nx.betweenness_centrality(G))
print("=="*20)
```

- 결과를 보시면, weight를 함께 계산해준 경우, weight가 큰 edge를 가진 node들은 다른 노드 pair 들간의 최단거리에 포함되지 않게 되므로 값이 0이 나옵니다.

```
== BETWEENNESS centrality with weight
{0: 0.0, 1: 0.3333333333333333, 2: 0.0, 9: 0.3333333333333333}
== BETWEENNESS centrality without weight
{0: 0.16666666666666666, 1: 0.16666666666666666, 2: 0.16666666666666666, 9: 0.16666666666666666}
========================================
```

## nx.pagerank 

- `nx.pagerank`의 경우는 반대로, weight가 클수록 중요하게 계산됩니다. 그리고, 다른 centrality의 경우 default가 'weight=None'이지만, pagerank는 기본 값이 `weight='weight'`입니다. 즉, 

```python
print("== PAGERANK with same weight")
G = nx.Graph()
G.add_edges_from([
    (0, 1, {'weight': 1}),
    (0, 2, {'weight': 1}),
    (1, 9, {'weight': 1}),
    (2, 9, {'weight': 1}),
])
print(nx.pagerank(G))

print("== PAGERANK with different weight")
G = nx.Graph()
G.add_edges_from([
    (0, 1, {'weight': 1}),
    (0, 2, {'weight': 2}),
    (1, 9, {'weight': 1}),
    (2, 9, {'weight': 1}),
])
print(nx.pagerank(G))
```

- 결과를 보면, weight가 큰 edge에 포함된, 0, 2 의 centrality 값이 높은 것을 알 수 있습니다. 

```
== PAGERANK with same weight
{0: 0.25, 1: 0.25, 2: 0.25, 9: 0.25}
== PAGERANK with different weight
{0: 0.2912620886697602, 1: 0.20873791133023972, 2: 0.2912620886697602, 9: 0.2087379113302397}
```

## wrap-up

- `nx.closeness_centrality`, `nx.betweenness_centrality`는 모두 weight를 거리로 생각한다. 즉, 값이 높을수록 거리가 멀게 측정됨. 
- `nx.pagerank`는 weight가 클수록 중요한 노드로 측정함.