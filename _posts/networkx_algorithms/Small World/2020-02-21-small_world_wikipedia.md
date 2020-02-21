---
title: What is Small-world? 
category: others
tags: networkx network-theory wikipedia small-world
---

## What is small-world network 

- [Small-world Network](https://en.wikipedia.org/wiki/Small-world_network)는 대부분의 노드가 서로 이웃은 아니지만, 어떤 노드도 다른 노드들의 이웃이 될 가능성이 있고(link prediction이 높고), 대부분의 노드가 다른 노드로 짧은 거리(small number of step)만으로 도달 가능한, 네트워크를 말합니다. 
- 따라서, 특정한 network가 small-worldness를 갖추고 있다면, `L`(노드간의 평균적인 거리)는 `log(node size)`와 비례하게 됩니다. 즉, "네트워크의 노드가 아무리 많아져도, 평균 최단거리는 그에 정비례해서 증가하지 않는다"라고 해석할 수 있죠.
- 또한, 그러면서도, random한 network보다는 clustering coefficient가 높아야 합니다. 아주 욕심쟁이인 네트워크죠. "짧은 최단거리"를 가지면서도, "clustering은 높아야 해(삼각형은 많아야 해)"라는 것이니까요.
- 특정한 graph가 존재할 때, 이 graph가 small-worldness를 갖추는지 중요한 것은, 이러한 네트워크가 가지고 있는 매력때문인 것이죠. small-worldness를 갖추고 있다면, "해당 네트워크에 새로운 사람이 들어왔을 때, 다른 사람들과 연결될 가능성이 매우 커집니다". 이런 말을 쓰고 싶지는 않지만, "융합"같은 것이죠. "누구나, 누구를 만나기 쉽다"라는 것은 네트워크 자체에 큰 힘을 부여하게 되니까요. 
- 실제 세상에서의 많은 social network와, wikipedia, gene network 등은 대부분 small-worldness를 갖추고 있습니다. 그리고, 흥미로운 사실은 컴퓨터 하드웨어 중 하나인 network-on-chip 또한, 여기서 영감을 받아서 만들어졌죠.

## small-worl의 성질. 

- 앞서 비슷한 말을 하기는 했지만, small-worldness는 다음의 두 조건을 일반적으로 충족합니다. 
    1) 노드들간의 평균 최단 거리가 특별히 짧아야 하고, 
    2) clustering coefficient가 특별히 높아야 하죠. 
- 여기서, `1)`조건을 만족하려면, 네트워크를 필연적으로, 노드들은 최소한 1개 이상의 최단거리를 가져야 합니다. 즉, 여러 hub node들이 존재해야 한다는 것이죠. 허브가 존재해야만, 노드들간의 최단거리의 길이가 짧아지게 되는 것이니까요.
- 또한, 여기서, 이 "특별함"이라고 하는 모호함은 다른 reference network와 비교하여 설명됩니다. 보통 지표는 두 가지를 사용하는데, 간단히 설명하면 다음과 같습니다. 

### small-worldness evaluation: `sigma` and `omega`

- 이처럼 network가 small-world로 구축되어 있을 경우, 네트워크 자체에서 가질 수 있는 이득이 있으므로, 가령 네트워크를 구성한다면, 해당 네트워크가 small network의 특성을 갖추는지 파악하는 것이 중요합니다. 
- 이미 `sigma`라는 지표와 `omega`라는 지표가 있으며, 이 두 지표 모두 다른 reference network와 비교하여, 스몰월드의 특별함을 정의하죠.
- 그 외로, SWI(Small-World-Index)라는 지표도 있으나, 본 글에서는 제외하였습니다

#### `sigma`

- `sigma`의 경우, equivalent random network만을 기준으로 삼고, 얼마나 평균 최단거리가 짧은지, clustering이 높은지를 비교하게 됩니다. "equivalent random network"는 "동일한 node degree 를 가지지만 edge들을 랜덤으로 교환해준 graph를 말하죠. 하지만, 이 지표의 경우, "한쪽에 대해서만 비교한다는 문제가 있습니다". small-worldness는 clustering이 높고, 최단거리는 짧습니다. 그리고, clustering과 최단거리는 약간의 반비례적인 성향을 지니죠. random network는 평균 최단거리를 비교하는 것에는 적합할 수 있지만, clustering을 비교하는 것에는 적합하지 못해요. 따라서, 이를 보완하기 위해, `omega`라는 지표가 나오게 됩니다. 

```python 
C = "clustering coefficient of graph G"
C_r = "clustering coef of random network(same degree with G)"
L = "average shortest path length of graph G"
L_r = "average shortest path of random network(same degree with G)"
sigma = (C/C_r) / (L/L_r)
```

#### `omega`

- `omega`의 경우, equivalent random network와 equivalent lattice network를 둘다 기준으로 삼고, 비교합니다. lattice network의 경우 매우 높은 clustering값을 가지지만, 동시에 매우 높은 평균 최단거리를 가지는 아이죠(그냥 화장실 타일같은 구조입니다). 따라서, "lattice network만큼 clustering이 높아야 한다, 하지만 동시에 random network와 비슷한 평균 최단거리를 유지해야 small-worldness라고 할 수 있다"라는 조건을 걸어버린 것이죠. 따라서, random network와 lattice network를 각각 비교하여, 균형을 이루고 있는지를 파악하는 지표라고 할 수 있습니다

```python 
L = "average shortest path length of graph G"
L_r = "average shortest path of random network(same degree with G)"

C = "clustering coefficient of graph G"
C_l = "clustering coefficient of equivalent lattice network"
omega = (L_r/L) - (C/C_l)
```


## Small-world Network Robustness 

- 스몰월드의 특성은 자연의 많은 시스템들에서 이미 반영되어 있습니다. 특히, '스몰월드'는 무작위로 노드를 삭제한다고 해도, 급격한 clustering의 변화나, 평균 최단거리의 변화가 발생하지 않습니다. 이것이 바로 small-world가 가지는 "강건함(robustness)"죠. 그리고, 이러한 강건성이, 자연의 무수한 진화(evolution)를 가능하게 한 원인, 이라고 보기도 하죠. 물론, random하게 설정할 때만 그렇지, 오히려 hub를 정확하게 때려버리면, 더 큰 문제가 발생할 수도 있죠.


## reference

- [Small world network in wikipedia](https://en.wikipedia.org/wiki/Small-world_network)