---
title: python - networkx - centrality with wrong weight name.
category: python-libs
tags: python python-libs networkx centrality 
---

## networkx - centrality with weight 

- network에서 중요한 Node를 추출하기 위하여, centrality를 분석합니다. 보통은 Network 상에서 node간의 거리를 활용하여 이 centrality를 계산하게 되죠. 그리고 이 때, weight를 고려하느냐, 고려하지 않느냐에 따라서 결과가 달라질 수 있습니다. 

## Weighted/Unweighted Centrality

- 다음과 같이 간단한 graph를 만들어보겠습니다. 보시는 것처럼, 각 edge별로 weight가 존재하죠. 

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([
    (0, 1, {'weight': 0.3}), 
    (1, 2, {'weight': 0.2}), 
    (2, 0, {'weight': 0.66})])
```

- 그리고, `nx.closeness_centrality(G, distance='weight')`의 형식으로 넘겨주면 `weight`를 고려하여, closeness_centrality를 계산해줍니다. 
- 코드 실행 결과를 보시면, `distance` parameter에 'weight'를 넘겨준 경우와 그렇지 않은 경우의 결과가 다르죠. 

```python
print("== CLOSENESS CENTRALITY")
for k, v in nx.closeness_centrality(G).items():
    print(k, v)
print("== WEIGHTED CLOSENESS CENTRALITY")
# actually, key 'distance' doesn't exist in the edge attribute distionary. 
for k, v in nx.closeness_centrality(G, distance='weight').items():
    print(k, v)
print("=="*20)
```

```
== CLOSENESS CENTRALITY
0 1.0
1 1.0
2 1.0
== WEIGHTED CLOSENESS CENTRALITY
0 2.5
1 2.857142857142857
2 4.0
========================================
```

## WARNING: in Weighted Centrality

- 다만, 어쩌면 사소한, 하지만 어쩌면 큰 문제가 될 수 있는 작은 사안이 하나 있습니다.
- 다음과 같은 코드가 있습니다. 다만, 코드는 잘 보시면, Weighted Closeness Centrality를 계산할 때, distance parameter에 `'distance'`를 넘기는 것을 알 수 있습니다. 즉, `G`의 edge attribute dictionary에 존재하는 `distance`를 가져와서 weight를 설정하겠다는 것이죠. 
- 그런데, 사실, `G`의 edge attributed dictionary에는 `"distance"`라는 key가 없습니다. `"weight"`만 있죠. 

```python 
import networkx as nx

G = nx.Graph()
G.add_edges_from([
    (0, 1, {'weight': 0.3}), 
    (1, 2, {'weight': 0.2}), 
    (2, 0, {'weight': 0.66})])

print("== CLOSENESS CENTRALITY")
# Unweighted closeness centrality를 계산합니다.
for k, v in nx.closeness_centrality(G).items():
    print(k, v)
print("== WEIGHTED CLOSENESS CENTRALITY")
# 여기서는 Weighted closeness centrality를 계산합니다.
# 그리고 그때 weight는 G의 edge_attribute dictionary에 'distance'라는 이름의 값이죠. 
# 하지만, 실제로 G의 edge_attribute_dictionary에는 'distance'가 없습니다.
for k, v in nx.closeness_centrality(G, distance='distance').items():
    print(k, v)
print("=="*20)
```

- 하지만, 이렇게 실행을 해도 아무 에러도 발생하지 않습니다. 그리고 그냥 Unweighted 라고 가정하고, 계산을 해서 출력을 해버리죠. 
- 저는 이건 좀 이상하다고 생각해요. 사용자의 의도와 다르게 진행되는데, 사용자에게 아무런 정보도 주지 않고, 암묵적으로 변환을 해버립니다. 
- 또한, `nx.closeness_centrality`뿐만 아니라, `nx.betweenness_centrality`의 경우에도 마찬가지죠. 

```
== CLOSENESS CENTRALITY
0 1.0
1 1.0
2 1.0
== WEIGHTED CLOSENESS CENTRALITY
0 1.0
1 1.0
2 1.0
```

## nx.closeness_centrality

- 우선, [networkx - documentation - closeness_centrality](https://networkx.github.io/documentation/stable/_modules/networkx/algorithms/centrality/closeness.html#closeness_centrality)에서 `nx.closeness_centrality`의 소스코드를 뜯어보겠습니다.
- `nx.closeness_centrality`의 소스 코드에는 다음과 같은 코드가 있습니다. 
    - **if `distance` is not None**: `distance` parameter에 edge_attrbute_dictionary의 key를 넘겨주면,`nx.single_source_dijkstra_path_length` 를 사용해서 거리를 계산해줍니다. `functools.partial`는 그냥 함수의 부분함수를 만들어주는 것 뿐입니다.
    - **else**: `distance` parameter에 아무 것도 넘겨주지 않으면, 즉 `None`이면, `nx.single_source_shortest_path_length`을 사용해서, 모든 edge의 weight를 1로 생각해서 계산을 해줍니다.

```python
if distance is not None:
    # use Dijkstra's algorithm with specified attribute as edge weight
    path_length = functools.partial(
        nx.single_source_dijkstra_path_length, weight=distance)
else:
        path_length = nx.single_source_shortest_path_length
```

- 즉, 다시 정리하면, 이제 `nx.closeness_centrality`에 `distance` parameter를 None이 아닌 다른 값으로 넘겨주면, `nx.single_source_dijkstra_path_length`를 사용해서 그 path의 길이를 계산해준다는 이야기죠. 

### nx.single_source_dijkstra_path_length

- [networkx - algorithms - shortest_paths - single source dijkstra path length](https://testfixsphinx.readthedocs.io/en/latest/reference/generated/networkx.algorithms.shortest_paths.weighted.single_source_dijkstra_path_length.html)를 읽어보면, 다음과 같이 작성되어 있는 것을 알 수 있습니다. 

> `weight` (string or function) – If this is a string, then edge weights will be accessed via the edge attribute with this key (that is, the weight of the edge joining u to v will be G.edge[u][v][weight]). **If no such edge attribute exists, the weight of the edge is assumed to be one**.

- 즉, edge attribute에 전달받은 이름이 없다면, 그냥 1로 알아서 가정하고 넘어간다는 것이죠. 
- 저는 여전히 마음이 들지 않습니다. 어떤 일관성이 없고, 사용자로서는 이러한 "암묵적인 변환"을 미리 알 수 없죠. 

## wrap-up

- 결론, 네트워크에서 centrality를 계산하기 전에 `weight` 혹은 `distance`의 parameter로 넘겨줄 attribute_name이 모든 edge의 attribute_dict에 key로 존재하는지를 매번 확인하는 습관을 가집시다. 만약, 확인하지 않으면 알아서 1로 가정하고 계산을 해주게 되니까요.



