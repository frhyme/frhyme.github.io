---
title: python - networkx - weighted centrality with lambda function
category: python-libs
tags: python python-libs networkx centrality 
---

## networkx - centrality with weight 

- 어떤 대상/현상을 네트워크로 모델링한 뒤, 보통 "그래서 가장 중요한 Node/Edge가 무엇인가?"를 찾는 작업을 많이 합니다. 이 작업을 보통 Centrality 분석 이라고 하죠. 
- Closeness Centrality는 "네트워크의 모든 노드까지의 거리"의 합이 작을수록 커집니다. 다만, 여기서 이 "거리"라는 것을 어떻제 정의할 것인지에 따라서 결과는 조금씩 달라지게 되죠. 

### Unweighted Centrality(default)

- 우선, edge별로 weight가 다르지 않다라고 가정하는 방법이 있습니다. 가장 보편적인 방법이죠. 모든 weight를 1로 생각하고 처리합니다. 
- 다음과 같이, 다른 parameter를 넘겨주지 않고 그냥 수행하면 weight를 1로 가정하고 계산해줍니다.

```python
# default: 모든 edge의 weight를 1로 생각하고 계산해줍니다.
CLOSENESS_DICT = nx.closeness_centrality(G)
```

### Weighted Centrality

- 하지만, 모든 edge에 동등한 weight를 주는 것이 아니라, 다른 방식으로 설정하고 싶을 때가 있죠. 
- 가령, 우리가 `G`를 다음과 같이 모델링했다고 합시다. 보시면, 모든 edge의 attribute dictionary에 `"weight"`라는 정보가 담겨 있는 것을 볼 수 있습니다.

```python
G = nx.Graph()
G.add_edges_from([
    (0, 1, {'weight': 0.5}),
    (1, 2, {'weight': 0.2}),
    (2, 0, {'weight': 0.3}),
])
```

- 따라서, edge attribute dictionary의 특정 값을 가져와서 계산을 하고 싶다면, key 값을 넘겨주면 됩니다.

```python
# distance parameter에 'weight'를 넘겨주면 
# 알아서 edge attribute dictionary에서 key 값을 찾아서 centrality를 계산해줌. 
CLOSENESS_DICT = nx.closeness_centrality(G, distance='weight')
```

### Other way???? 

- 즉, edge attribute dictionary 있는 값을 그대로 가져와서 centrality를 계산하거나 혹은 그냥 default로 모든 edge의 weight가 같다고 가정하고 계산하거나, 이 두 방식만 있다는 것이죠. 
- 하지만, 이 거리를 측정하는 방식이 다양한데, 이를 반드시 edge attribute dictionary에 값을 저장해두고 처리하도록 하는 것은 꽤 불편해 보입니다. 
- 가령, "현재 `weight`의 값이 클수록 거리(distance)는 멀다", 와 같은 방식을 집어넣으려면, 모든 edge에 대해서 `distance`라는 값을 새롭게 설정해줘야 하는 것이니까요. 불편하고 무거운 방식으로 느껴집니다 

## Calculate weighted centrality with lambda function 

- 그래서, 여기서는 lambda function을 사용해서 centrality를 계산하는 방식을 정리하였습니다.
- 아래 코드를 보시면 distance parameter에 `lambda function`이 들어가 있는 것을 알 수 있습니다. 
- 아래 코드의 의미는 "edge_attribute dictionary에 있는 `weight`값의 역수를 distance로 고려하겠다"라는 것이죠.

```python
CLOSENESS_DICT = nx.closeness_centrality(
    G, distance=lambda u, v, d: 1.0/d['weight'])
```

### closeness_centrality Documentation 

- 우선, [networkx - documentation - closeness_centrality](https://networkx.github.io/documentation/stable/_modules/networkx/algorithms/centrality/closeness.html#closeness_centrality)에서 `nx.closeness_centrality`의 소스코드를 뜯어봅니다. 
- `distance` keyword의 경우는 edge attribute key로 정의한다고 되어 있습니다. 위에서 쓴 것과 같이, lambda function을 써도 문제없이 돌아갑니다.

> If the ‘distance’ keyword is set to an edge attribute key then the shortest-path length will be computed using Dijkstra’s algorithm with that edge attribute as the edge weight.


### single source dijkstra path length

- 이는, 결국 closeness centrality에서 거리를 계산할 때, [networkx - algorithms - shortest_paths - single source dijkstra path length](https://testfixsphinx.readthedocs.io/en/latest/reference/generated/networkx.algorithms.shortest_paths.weighted.single_source_dijkstra_path_length.html)를 사용하기 때문인데요. closeness centrality에서는 `distance`가 `None`이 아니면, 그냥 바로 이 함수로 넘겨버립니다. 
- 그리고, 이 함수를 보면, 다음과 같이 작성되어 있는 것을 알 수 있죠.

> `weight` (**string or function**) – If this is a function, the weight of an edge is the value returned by the function. The function must accept exactly three positional arguments: the two endpoints of an edge and the dictionary of edge attributes for that edge. The function must return a number.

- 만약, 이 아이가 '함수'라면, `lambda u, v, d: return SOMETHING`의 형식으로 정의해서 넘겨줘야 한다. `u`, `v`는 각각 edge의 두 node를 말하고, `d`는 graph `G`에서 `u`, `v`에 대한 attribute_dictionary를 말하는 것이죠. 
- 따라서, 그냥 이렇게 처리해도 문제없이 된다는 이야기입니다.


### Usage 

- 앞서 말한것과 같이, `distance`부분에 함수를 넘겨서 처리합니다. 이렇게 처리해도 아무 문제없이 잘만 실행되죠. 
- 다만, `nx.betweenness_centrality`나, `nx.closeness_centrality`와 같이 shortest_path를 고려하는 경우에만 문제없이 진행될 것입니다.

```python
CLOSENESS_DICT = nx.closeness_centrality(
    G, distance=lambda u, v, d: 1.0/d['weight'])
```