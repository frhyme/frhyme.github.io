

## What is small-world network 

- [Small-world Network](https://en.wikipedia.org/wiki/Small-world_network)는 대부분의 노드가 서로 이웃은 아니지만, 어떤 노드도 다른 노드들의 이웃이 될 가능성이 있고(link prediction이 높고), 대부분의 모드가 다른 노드로 짧은 거리(small number of step)만으로 도달 가능한, 네트워크를 말합니다. 
    - 따라서, 보통 Small-world network는 `L`(노드간의 평균적인 거리)가 `log(node size)`와 비례합니다. 즉, "네트워크의 노드가 아무리 많아져도, 평균적인 거리는 로그 펑션으로 증가한다는 것이죠". 
    - 그리고, 동시에 `clustering coefficient(# of triple / # of triplet)`또한 random으로 만들어지는 graph보다 높아야 합니다.
- 따라서, small world network에서는 새로운 사람이 들어왔을 때, 다른 사람들과 연결될 가능성이 매우 크죠. 이를 small-world effect라고 하며, 실제 세상에서의 social network뿐만 아니라, wikipedia, gene network, 그리고 인터넷에서도 비슷한 모습들이 발현됩니다. 컴퓨터 하드웨어 중 하나인 network-on-chip 또한, 여기서 영감을 받아서 만들어졌죠.

## small-world Network property

- 앞서 말한 바와 같이 small-world는 다음의 두 조건을 충족합니다.
    1) 노드간의 평균적인 거리가 짧아야 하고 
    2) clustering coef가 랜덤 그래프보다 높아야 하죠. 
- 1)에 의해서 혹은, 1)을 충족한다면 자연스럽게, 대부분의 노드들은 최소한 1개 이상의 shortest path를 가지며, 매우 많은 수의 hub(degree 가 매우 높은 node)를 가지게 됩니다. 이러한 허브를 통해서 많은 노드들간의 최단거리의 길이가 짧아지는 것이죠. 이러한 네트워크의 degree distribution을 보면, 보통 fat-tailed distribution을 따릅니다.
- 또한, 2)에 의해 보통은 clique, near-clique들이 많이 존재하게 됩니다.

- 그리고, 이 성질을 얼마나 만족하는지 평가하기 위한 지표로는 다음의 지표들이 있습니다. benchmark Graph를 두고, 그 그래프와 distance, clustering coef를 비교하여 얼마나 small world ness가 높은지를 파악하죠. 이 때 benchmark graph는 다음 두 가지로 구분됩니다.
    1) **equivalent random network**: degree distribution이 같은 random graph. 기존 graph에서 edge들을 서로 교환하며 새로운 graph를 생성함(가령, `(a, b), (c, d)` ==> `(a, c), (b, d)`
    2) **equivalnet lattice network**: lattice network는 격자 그래프를 말하며, 

### Sigma: Comparing with random network(same average degree)

- graph `G`의 `sigma`는 `G`와 평균 degree가 동일한 graph와 clustering coef, path length를 비교하여 다음과 같이 측정하며, 보통 1.0이 넘는 경우(distance는 비슷한데, clustering coef가 더 높아지는 경우), small-world라고 평가합니다.
- 하지만, 이 값은 네트워크의 크기가 커짐에 따라서, 정확도가 떨어진다는 단점을 가지고 있죠. 

```python 
C = "clustering coefficient of graph G"
C_r = "clustering coef of random network(same degree with G)"
L = "average shortest path length of graph G"
L_r = "average shortest path of random network(same degree with G)"
sigma = (C/C_r) / (L/L_r)
```

### Omega: 

```python 
L = "average shortest path length of graph G"
L_r = "average shortest path of random network(same degree with G)"

C = "clustering coefficient of graph G"
C_l = "clustering coefficient of equivalent lattice network"
omega = (L_r/L) - (C/C_l)
```



Network small-worldness has been quantified by a small-coefficient, {\displaystyle \sigma }\sigma , calculated by comparing clustering and path length of a given network to an equivalent random network with same degree on average

## reference

- [Small world network in wikipedia](https://en.wikipedia.org/wiki/Small-world_network)