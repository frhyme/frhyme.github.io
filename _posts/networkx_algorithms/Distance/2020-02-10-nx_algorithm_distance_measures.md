---
title: networkx - distance measure
category: python-libs
tags: python python-libs networkx distance 
---

## 2-line summary 

- Graph에서 `distance`에 근거한 다양한 함수들을 정리함. 
- `diameter`, `eccentricity`, `radius` 등 매우 기본적인 graph의 기본적인 지표 및 개념들 정리.

## Do it using `NetworkX`

- 어려운 코드가 아니어서, 아래에 그대로 정리하였습니다. 

```python
import networkx as nx

N = 20
G = nx.scale_free_graph(N, seed=0)
G = nx.Graph(G)
assert nx.is_connected(G)
#===============================================================
# nx.eccentricity(G)
# node v에서 G에서, 다른 모든 노드들까지의 거리 중 가장 큰 값.
print("== nx.eccentricity(G)")
G_eccentricity = nx.eccentricity(G)
def custom_eccentricity(G):
    r_dict = {}
    for u in G:
        u_eccentricity = max([nx.shortest_path_length(G, u, v) for v in G])
        r_dict[u] = u_eccentricity
    return r_dict
assert ({'a': 2} == {'a': 3}) == False  # shallow compare check
assert nx.eccentricity(G) == custom_eccentricity(G)
print("Assertion complete")
print("=="*20)
#===============================================================
# nx.diameter
# return max eccentricity
print("== nx.diameter(G)")
def custom_diameter(G):
    return max(nx.eccentricity(G).values())
assert nx.diameter(G) == custom_diameter(G)
print("Assertion complete")
print("==" * 20)
#===============================================================
# nx.radius
# return min eccentricity
print("== nx.radius")
def custom_radius(G):
    # eccentricity: u에서 다른 모든 node V까지 필요한 distance
    # diameter: min(eccentricity)
    return min(nx.eccentricity(G).values())
assert nx.radius(G)==custom_radius(G)
print("Assertion complete")
print("==" * 20)
#===============================================================
# nx.center
# eccentricity가 nx.radius와 같은 node set
print("== nx.center(G)")
def custom_center(G):
    G_radius = nx.radius(G)
    return [u for u, ecc in nx.eccentricity(G).items() if ecc==G_radius]
assert set(nx.center(G)) == set(custom_center(G))
print("Assertion complete")
print("==" * 20)
#===============================================================
# nx.periphery,
# periphery는 "주변부"를 의미함
# eccentricity가 nx.diameter와 같은 node set
# 즉, 가장 멀리 있는 노드 집단
print("== nx.periphery(G)")
def custom_periphery(G):
    G_diameter = nx.diameter(G)
    return [u for u, ecc in nx.eccentricity(G).items() if ecc == G_diameter]

assert set(nx.periphery(G)) == set(custom_periphery(G))
print("Assertion complete")
print("==" * 20)
#===============================================================
# nx.barycenter(G)
# barycenter ==> 질량 중심. also known as "median"
# Graph의 모든 node들까지의 거리가 가장 작은, node 집합. 
# 즉 1개일 수 있고 여러 개 일수도 있다.
print("== nx.barycenter(G)")
G = nx.complete_graph(10)
# complete graph인 경우 10개가 모두 barycent(질량중심)에 속해야 함
assert nx.barycenter(G)==[i for i in range(0, 10)]
print("Assertion complete")
print("==" * 20)
```

```
== nx.eccentricity(G)
Assertion complete
========================================
== nx.diameter(G)
Assertion complete
========================================
== nx.radius
Assertion complete
========================================
== nx.center(G)
Assertion complete
========================================
== nx.periphery(G)
Assertion complete
========================================
== nx.barycenter(G)
Assertion complete
========================================
```

## reference

- [networkx - distane measures](https://networkx.github.io/documentation/stable/reference/algorithms/distance_measures.html)