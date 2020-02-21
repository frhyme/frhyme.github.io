---
title: network - small worldness evaluation - omega.
category: python-libs
tags: python python-libs networkx random-network random reference-network omega.
---

## 2-line summary. 

- `omega`는 equivalent random network와 equivalent lattice network라는 두 reference network를 기준으로 평균 최단거리, clustering을 각각 비교하여 균형을 맞추고 있는지 평가하는 지표. 
- range(-1, 1)을 가지며, 0에 가까울수록 small-worldness를 갖추고 있다고 평가함.

## small world evaluation

- [Small world network](https://en.wikipedia.org/wiki/Small-world_network)는, 네트워크의 한 유형으로, "특별히 높은 clustering 값"을 가지고, 동시에 "특별히 짧은 average shortest path length"를 가지는 네트워크를 말합니다. 
- 그리고, 특정 Graph가 얼마나 small world의 특성을 갖추고 있는지 평가하기 위해서는 보통 `sigma`, `omega`라는 두 가지 지표를 사용하고는 합니다. 
- 오늘은, `omega` 라는 지표를 설명하고 python으로 간단하게 코딩하겠습니다. 

## omega: comparison with both random and latticized network. 

- 앞서 서술한 것처럼 small network는 "특별히, 높은 clustering값"과 "특별히 짧은 평균 최단거리"를 가집니다. 
- 여기서 이 "특별함"이라는 것은, 다른 대상과 비교했을 때 유효한데, `sigma`에서는 equivalent random network를 reference로 하여, 비교하게 되죠.
- 다만, 단지 random network만을 활용해서 비교하는 것에는 한계가 있습니다. `sigma`의 경우 그래프의 크기가 커지면, 그 정확도에 문제가 생기기도 하고요. 

### latticized network?

- [lattice network](https://en.wikipedia.org/wiki/Lattice_graph) 는 "격자 네트워크"로, 화장실 타일처럼 촘촘하게 구성되어 있는 네트워크를 말합니다(mesh network)라고 하기도 하지요. 보통은 '삼각형'을 기준으로 한 "triangular lattice network"를 보통 말하며, 당연하지만, clustering값이 매우 높게 측정됩니다. 그리고 또 당연하지만, average shortest path length는 매우 크게 나오게 되죠.
- 특정 graph를 latticization한다는 것은, 해당 graph의 node degree를 그대로 유지하고, 최대한 clustering을 높일 수 있고, average shortest path length를 최대로 높일 수 있도록, lattice network와 유사하게 변형한다는 것을 의미합니다.
- 이를 통해서, 현재 네트워크가 얼마나 small world에 가까운지를 비교할 수 있는 reference 대상으로 삼을 수 있다는 것이죠.

### peudo code. 

- 이를 코드로 구현하면 대략 아래와 같습니다. 
- clusering과 average shortest path length는 어느 정도 반비례같은 성질을 가지는데, lattice network를 보면, 매우 높은 clustering 값을 가지지만, 반대로 average shortest path length는 아주 크게 증가하게 되죠. 
- 따라서, `omega`는 다음 두 가지를 각각 비교하여, 균형을 이루고 있는지를 평가하는 것이죠. 
    - `A`: random network와 비교했을 때, 평균 최단거리가 유사한가? 
    - `B`: lattice network와 비교했을 때, clustering 값이 유사한가? 
- 그리고, `A - B`를 통해, 이 값이 균형을 이루고 있는지를 평가합니다. 만약, 
    - G가 Random network에 가깝다면, `A`값은 1에 가까울 것이고, B는 `0`에 가까워질 것입니다. 보통 random network는 clustering 값이 매우 낮으니까요. 
    - G가 lattice network에 가깝다면, `A`는 0에 가까워집니다(lattice network에서는 평균 최단거리가 매우 높거든요). 반면, `B`는 거의 1에 가까워지겠죠. 
- 따라서, 이를 종합하면 다음과 같아집니다. 
- `omega`는 보통 `range(-1, 1)`을 가지며, 
    - `omega = -1`: lattice-network 
    - `omega =  0`: small-network 
    - `omega = +1`: random-network

- 코드로 보면 대략 다음과 같죠.

```python
G        = "그냥 Graph"
randG    = "equivalent random G"
latticeG = "equivalent latticized G"

C = clustering(G)
L = nx.average_shortest_path_length(G)

# C_l: latticized G에 대한 clustering
C_l = clustering(latticeG)
# L_r: random network에 대한 평균 최단 거리.
L_r = nx.average_shortest_path_length(randG)

# A: "평균최단거리"가 random network와 비교해봤을 때, 어느 정도 유효한가, 를 측정함.
# Graph G의 equivalent random network의 평균 최단거리가, G에 비해 얼마나 더 짧은지, 
# 만약 lattice network라면 최단거리가 매우 커지므로 A는 거의 0에 가깝게 됨.
A = (L_r / L)

# B: "Clustering"이 latticized G에 비해서 얼마나 유효한지.  
# 만약, latticizedG와 비교해봤을 때, 값이 너무 작다면, 
# B는 0에 가까워지고, 그럴경우 A만 남으므로, 해당 G는 random-network에 가깝다고 평가할 수 있음.
B = (C / C_l)
omega =  A - B
```


## reference

- [networkx.algorithms.smallworld.omega](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.smallworld.omega.html#networkx.algorithms.smallworld.omega)
- [Small world network in wikipedia](https://en.wikipedia.org/wiki/Small-world_network)