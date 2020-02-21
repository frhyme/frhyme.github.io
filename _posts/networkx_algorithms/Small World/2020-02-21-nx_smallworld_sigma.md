---
title: network - small worldness evaluation - sigma.
category: python-libs
tags: python python-libs networkx random-network random reference-network sigma.
---

## 2-line summary. 

- `sigma`는 equivalent random network를 기준으로 clustering, 평균 최단거리를 비교하여, 만들어진 지표. 
- 1.0이 넘으면 보통 small-world라고 하지만, 그래프의 크기가 충분히 커지면 유효하지 않다는 한계를 가짐.

## small world evaluation

- [Small world network](https://en.wikipedia.org/wiki/Small-world_network)는, 네트워크의 한 유형으로, "특별히 높은 clustering 값"을 가지고, 동시에 "특별히 짧은 average shortest path length"를 가지는 네트워크를 말합니다. 
- 그리고, 특정 Graph가 얼마나 small world의 특성을 갖추고 있는지 평가하기 위해서는 보통 sigma, omega라는 두 가지 지표를 사용하고는 합니다. 
- 오늘은, sigma 라는 지표를 설명하고 python으로 간단하게 코딩하겠습니다. 

## sigma: comparison with random network. 

- 앞서 서술한 것처럼 small network는 "특별히, 높은 clustering값"과 "특별히 짧은 평균 최단거리"를 가집니다. 
- 여기서 이 "특별함"이라는 것은, 다른 대상과 비교했을 때 유효한데, `sigma`에서는 equivalent random network를 reference로 하여, 비교하게 되죠.
- 또한, 보통 `sigma`가 1보다 크면, small-world network라고 판정합니다. 다만, 그러함에도 네트워크의 크기가 충분히 커지면, 유효하지 않다는 한계를 가지고 있죠. 
- 간단하게 코드로 표현하면 다음과 같습니다. 즉, 
    - 분자: random network에 비해 clustering이 얼마나 큰지. 
    - 분모: random network에 비해 평균 최단 거리가 얼마나 짧은지. 
- 만약 해당 graph인 `G`가 small world network 라면, 
    - "random network보다 clustering이 커지므로 분자는 1보다 커집니다". 
    - "random network보다 평균 최단거리는 1보다 작아지게 됩니다"
- 따라서, 분자는 커지고 분모는 작아지죠. 보통 sigma가 1.0보다 커지면 small-worldness를 갖추고 있다고 판정하죠.

```python
# G: 연결되어 있는 어떤 graph. 
# equivalent random network: 
# 기존 graph인 G와 node degree가 동일하지만, edge가 random한 network. 
# 보통, "연결성이 끊어지지 않게, edge를 교환하면서 진행함"
eq_random_G = nx.random_reference(G)

# G의 clustering, avg_shortest_path_l을 측정 
C   = clustering_coef(G)
L   = average_shorest_path_length(G)

# eq_random_G의 clustering, avg_shortest_path_l을 측정 
C_r = clustering_coef(eq_random_G)
L_r = average_shorest_path_length(eq_random_G)

# sigma 

sigma = (C/C_r) / (L/L_r)
```


## reference

- [networkx.algorithms.smallworld.sigma](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.smallworld.sigma.html)
- [Small world network in wikipedia](https://en.wikipedia.org/wiki/Small-world_network)