---
title: networkx - K-components.
category: python-libs
tags: python python-libs networkx components algorithms
---

## K - component.

- `k-component`는 graph `G`가 있을 때, 모든 node의 local node connectivity가 최소한 k인, maximal subgraph를 말한다("maximal"은 "만들 수 있는 최대의 그래프"라고 해석하면 될텐데, sub_A가 이미 2-component이라면, 그 내부의 어떤 sub_graph가 2-component이더라도, 이를 모두 표시하지는 않는 것을 말한다. 즉, 될 수 있는 최대 크기의 그래프만 고려하는 것을 보통, 'maximal'이라고 함.)
- 이전에 배웠던 것과 마찬가지로, `k-component`는 node connectivity가 k인 subgraph를 말한다. 따라서, 이 그래프를 disconnect로 만들기 위해서는 최소한 k 만큼의 node를 삭제하는 것이 필요합니다. 
- 또한 exact method가 아니라, approximation algorithm을 사용하여, `k-component` 구조를 계산합니다. 

## K - component approximation algorithm.

- 처음에는 k - component를 찾는 알고리즘을 해석하려고 했지만, 어려워서 헤헤헤. 그냥 몇 가지 개념들만 정리합니다. 아래에 정리한 간단한 그래프의 구조들은 서로 내재적인 관계(포함 관계)를 가지고 있고, 따라서 하나의 구조를 찾았을 때 거기서 출발하여, 연결하는 식으로 새로운 구조를 찾아가게 됩니다. 이를 통해 반복적으로 k - component를 찾는 알고리즘을 설계한 것이죠.
    - **k-core**: [k-core](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.core.k_core.html)는 모든 node의 degree가 k 이상인 maximal connected component를 말합니다
    - **biconnected graph**: [Biconnected graph](https://en.wikipedia.org/wiki/Biconnected_graph)는 만약 어떤 node가 없어지더라도, connected가 깨지지 않는 graph를 말합니다. 즉, 어떤 노드라도 한 개를 없앴을 때, 두 개의 connected component로 분절된다면, 그 graph는 biconnected graph가 아닌 것이죠.
    - **biconnected component**: 이는 당연히, maximal biconnected sub-graph가 되겠죠. 

## Do it. 

- 코드와 실행 결과는 다음과 같습니다. 


```python
from networkx.algorithms import approximation as apxa
import networkx as nx

# Graph Generation
G = nx.Graph()
N = 10
p = 0.2
G = nx.fast_gnp_random_graph(N, p, 0)

########################################################
# apxa.k_components(G)
# dictionary(K: compoent_lst)의 형태로 리턴.
for K, component_lst in apxa.k_components(G).items():
    # K: min connectivity in that component
    # component_lst에는 최소 node connectivity가 K인 모든 component가 들어있음.
    print(f"== K가 {K}인 모든 component:")
    for i, comp in enumerate(component_lst):
        print(f"{K}-component {i}: {comp}")
    print("=="*20)
########################################################
```

```
== K가 1인 모든 component:
1-component 0: {0, 3, 5, 6, 7, 8, 9}
1-component 1: {2, 4}
========================================
== K가 2인 모든 component:
2-component 0: {0, 3, 6, 7, 9}
========================================
```

## wrap-up

- 라이브러리 사용법이냐 사실 그대로 콜해서 그냥 쓰면 되는거고, 내부의 알고리즘들이 어떻게 흘러가는지를 아는 것이 더 중요한데, 아 그건 너무 멀고도 험한 길입니다.
- 그러나, 요즘의 저는 조급해하지 않아요(왜냐면 충분히 늦었거든요 호호호). 오늘 낯을 익힌 개념들이 있고, 아마도 다음에 볼 때는 좀 더 빠르게 이해할 수 있겠죠. 저는 좌절하지 않아요. 지금의 저는 몰라도, 내일의 저는 아마도 이해할 수 있을 거에요.

## reference

- <https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.approximation.kcomponents.k_components.html#networkx.algorithms.approximation.kcomponents.k_components>