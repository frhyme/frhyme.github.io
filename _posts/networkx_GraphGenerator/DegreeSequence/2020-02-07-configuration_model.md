---
title: networkx - Configuration model.
category: python-libs
tags: python python-libs networkx modularity configuration-model network-generator
---

## What is Configuration model. 

- [Configuration model](https://en.wikipedia.org/wiki/Configuration_model)은 Node들에 대한 **Degree sequence**가 주어졌을 때, degree sequence를 그대로 유지한 상태로, random network를 만드는 방법을 말합니다. 즉, `degree sequence`를 그대로 유지하기 때문에, 다른 network에 대한 reference model로서 사용될 수 있는 것이죠.


### real-world network와의 비교. 

- 복잡계(complex network)는 3가지의 일반적인 성질을 가지는데, 1) heterogeneous degree distribution, 2) short average path length, 3) high clustering입니다. 임의의 degree sequence를 만들게 되면, node들의 degree 분포가 달라지므로, 조건 1)은 만족하게 됩니다, 하지만, configuration model은 node의 수가 증가할수록 clustering coefficient가 증가하게 됩니다. 따라서, configuration network의 이 특성은 baseline model로서 설정하여, 다른 복잡계 네트워크와의 비교를 위해 사용될 수 있습니다.

### Configuration model for network modularity. 

- [modularity](https://en.wikipedia.org/wiki/Modularity_(networks))는 네트워크를 '커뮤니티' 혹은 '모듈'로 나눈다고 할때, 이게 얼마나 잘 나누어졌는지를 평가하는 지표입니다. 이 값을 계산할 때도, 기준을 configuration model로 두고, "Degree 분포가 같은, Configuration model"에 근거하여, "두 노드간의 edge probability를 기반으로 adjacency matrix를 비교"하게 됩니다. 이걸 수식으로 말하지 않고, 그냥 쓰려니까 말이 좀 이상한데, baseline이라고 보면 됩니다. "그냥 이 random network보다는 더 높아야 modular되어 있다고 할 수 있다"같은 것이죠. 

## networkx.generators.degree_seq.configuration_model

- 당연하지만, `networkx`에서도 configuration model을 만드는 함수를 제공합니다. 다만, degree sequence에 따라서, self-loop, parallel-edge를 허용하며 만들어질 때가 있습니다. 이는 degree sequence를 맞추기 위해서 어쩔 수 없는 경우들도 있으며, 가령 `[2, 3]`이라는 degree sequence를 넘긴다면 이를 만들기 위해서, 어쩔 수 없이, self-loop, parallel-edge를 만드는 것이 필요하게 되죠. 

```python
G = nx.generators.degree_seq.configuration_model(
    deg_sequence = deg_seq,
    create_using=nx.MultiGraph(),
    seed=0
)
```

- 간단하게, `power_law`에 맞춰서 degree sequence를 생성하고, 이 값을 가지는 `configuration_model`을 만들었습니다.

```python 
import networkx as nx

# make degree sequence
print("==" * 20)
deg_seq = nx.random_powerlaw_tree_sequence(n=20, seed=0)
deg_seq = sorted(deg_seq, reverse=True)
print("== Degree sequence")
print(deg_seq)

# make configuration model
print("== Configuration Model")
# configuration_model의 경우 
G = nx.generators.degree_seq.configuration_model(
    deg_sequence = deg_seq,
    create_using=nx.MultiGraph(),
    seed=0
)
degree_seq = [d for n, d in nx.degree(G)]
degree_seq = sorted(degree_seq, reverse=True)
print(degree_seq)
print("=="*20)
```

```
========================================
== Degree sequence
[8, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
== Configuration Model
[8, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
========================================
```

## wrap-up

- network로부터 community들을 뽑아내었을 때, 이 community가 얼마나 잘 뽑혀나온건지, 다른 community에 비해서 얼마나 잘 나온 것인지 비교하기 위해서는 평가지표들이 필요한데, 그 중 하나가 `modularity`입니다. 이 `modularity`를 공부하다가 configuration model로 넘어왔습니다. 