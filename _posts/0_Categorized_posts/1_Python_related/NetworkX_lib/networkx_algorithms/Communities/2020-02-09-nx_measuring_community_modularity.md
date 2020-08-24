---
title: networkx - community detection - modularity
category: python-libs
tags: python python-libs networkx community community-detection optimization
---

## 3-line summary 

- modularity는 네트워크에서 클러스터링을 수행했을 때, 얼마나 잘 나누었는지를 측정하기 위한 지표. 
- configuration model을 null model로 하여 random할때보다 얼마나 더 차이가 있는지를 비교하는 식으로 측정하는데, 네트워크가 커질 수록 오차가 커지는 문제점을 가짐. 
- 즉, modularity matrix에서 node `n1` to `n2`에 속하는 값은 "null model에서 두 노드간에 기대할 수 있는 edge의 수(확률)"을 고려하여, 양의 값(기대값보다 크다), 음의 값(기대값보다 적다, 즉 있으면 안되는데 있다) 정도로 이해하면 됨. 
- 그리고 이를 합친 modularity는, communiy에 속하는 노드끼리 값을 모두 더하면 됨(inter-modularity의 합)

## what is modularity? 

- [modularity](https://en.wikipedia.org/wiki/Modularity_(networks))는 네트워크를 어떻게 나누었을 때, 가장 적합한지, 노드들이 서로 다른 커뮤니티에 각각 속한다고 가정했을 때, 이것이 얼마나 타당한지를 정량적으로 나타내기 위한 지표를 말한다. 
- 네트워크 상에서 modularity는 커뮤니티 내부에 펼쳐져 있는 링크들이 "무작위적인 연결"과 비교했을 때, 얼마나 더 많은지를 정량화하며, 이 때 "무작위적인 연결 네트워크"는 [Configuration model](https://en.wikipedia.org/wiki/Configuration_model)을 기본으로 한다(configuration model은 "동일한 degree sequence"를 가지는, 랜덤 네트워크를 의미한다). 
- 따라서, 높은 modularity 값을 가지고 있다면, 모듈(community, group, cluster)별로 노드들이 잘 나누어졌다고 할 수 있다(모듈 내에서는 edge가 많고, 모듈 끼리는 edge가 적을 수록 modularity 값이 높아진다). 그러나, resolution limit때문에, 작은 community에 대해서는 정확하게 측정하는 것이 어렵다(작은 community는 뽑아내는 것도 어렵다).

## modularity matrix.

- 앞서 말한 바와 같이, `modularity`는 "(실제로 존재하는 노드간 edge의 수) - (노드 간에 존재할 것으로 기대되는 edge의 수)"를 의미합니다. python으로 간단히 만들어본 코드는 다음과 같죠. "edge에 대한 기대값"은 `k[u]*k[v]/(2*m)`이구요. 코드 자체가 그리 어렵지는 않습니다

```python
def custom_modularity_dict(G):
    # A_uv = actual edges from u to v
    # k_u, k_v: degree of node
    # m: num. of total edges
    """
    - 사실 np.matrix로 표현하면 더 간단해 보일 수 있는데, 
    matrix의 형태에 익숙하지 않으실 분들이 있을 것 같아서, 딕셔너리의 형태로 표현하였습니다. 
    R = A - X
    R = A - k_u * k_v /(2*m)
    - `nx.linalg.modularity_matrix(G)`와 동일함.
    """
    # Actual edge: 1 or 0 
    A = {u:{v: 1 if u in G[v] else 0 for v in G}for u in G}
    # degree deictionary of all nodes
    k = {n: nx.degree(G, n) for n in G} # degree dict
    # all possible edge( *2 for directe graph)
    m = len(G.edges())
    # expected number of edges: (degree of each node 곱)/ (존재하는 모든 edge의 수)
    X = {u:{v: k[u]*k[v]/(2*m)  for v in G} for u in G}
    R = {u:{v: 0  for v in G} for u in G}
    for n1 in G:
        for n2 in G:
            R[n1][n2] = A[n1][n2] - X[n1][n2]
    return R
```

- 그리고, modularity matrix로부터 modularity를 뽑아내는 방식은 다음과 같습니다. 그냥 inter-modularity를 모두 더해버리면 되죠(+normalization)

```python
def custom_modularity(G, partitions):
    """
    - 복잡해보이지만, modularity matrix에서,
    서로 같은 community에 속한 경우에만 그 원소들을 모두 더한다고 생각하면 됨.
    self-loop 도 마찬가지.
    """
    modularity_dict = custom_modularity_dict(G)
    all_modularity_elements = []
    for p1 in partitions:
        # community 별로
        for n1, n2 in itertools.product(p1, repeat=2):
            # community에 속하는 모든 node to node에 대해서,
            # 즉, inter-modularity를 모두 더함.
            modularity_n1_to_n2 = modularity_dict[n1][n2] * 2
            all_modularity_elements.append(modularity_n1_to_n2)
    norm = (4*len(G.edges()))
    return sum(all_modularity_elements) / norm
```

## 큰 네트워크에서 modularity의 문제점: Resolution limit 

- 네트워크의 크기가 커질수록, 기본적인 null model을 이용하여 modularity를 측정하는 것에 문제가 생길 수 있습니다.
- "Modulartiy"는 비교를 위한 null model인 configuration model(node, edge, node degree가 동일한 random network)과 "cluster 내의 노드들간의 edge의 수"를 비교하여, 측정됩니다. 하지만, 이 때, edge는 degree sequence에 따라서 아주 랜덤하게 생성된다는 것을 가정하죠. 
- 즉, null model에서는 네트워크 내의 모든 노드가 다른 노드에 자유롭게 연결될 수 있음을 "가정"하게 됩니다. 하지만, 이 가정은 네트워크가 커질수록 타당해지지 못합니다. 가령, 네트워크의 크기가 매우 커지게 된다면, "서로 다른 클러스터 간에 기대할 수 있는 edge의 수"라는 값, 즉 비교를 위한 null model에서의 값(`degree(n1) * degree(n2) / (2* (all_edges))`의 합)이 작아지게 되죠. 충분히 큰 커뮤니티 간에서, 이 값이 만약 "1"보다 작아진다면, 두 클러스터 간에 단 하나의 edge만 존재하더라도, 이 단 하나의 edge는 modularity에 의해서 두 클러스터 간의 강한 관련성을 의미하는 신호로 해석될 수 있습니다(null model에서 기대 값 합이 1보다 작기 때문에, 단 하나의 edge도 이미 타당하다고 결론이 내려지기 때문).
- 가령, 만약 complete graph 2개가 서로 약하게 상호 연결되어 있을 경우에, 그리고 이들은 각각 complete graph이므로 내부적으로 아주 높은 밀도의 edge들을 가지고 있어서, 분명한 개별적인 community로 보일지라도, 이 네트워크가 충분히 클 경우, 이 두 네트워크는 modularity optimization에 의해서는 하나의 community로 통합되어 보여질 수 있다는 것이죠(다시 말하지만, 두 클러스터 간에 기대할 수 있는 edge의 수가 매우 작게 기대되므로, 단 1개의 edge도 충분히 의미있다고 보여질 수 있음.)
- 따라서, 매우 큰 네트워크에서 modularity를 최적화는 방식은, 비록 실제로는 그 small community들이 매우 잘 구축되어 있다고 할 지라도, 실패할 수 있습니다. 이를 피하기 위해서는 global null model에 기반하여 modularity optimization을 수행하는 것이 아니라, localized null model을 따로 세워서 수행하는 것이 필요하죠.
- 물론, 여기서 말하는 문제는 진짜 말도 안되게 graph가 클 때 발생합니다(일반적으로, 우리가 다루는 네트워크에서는 이런 일이 발생하지 않으므로, 안심하고 해도 됩니다). 

## evaluate `modularity` 

- 간단한 graph로부터 community detection(girvan-newman)을 수행하면서, 그 분화의 적합성을 측정해보겠습니다. 
    - `coverage`: "community들이 기존의 Graph가 가지고 있던 edge를 얼마나 커버할 수 있느냐?"
    - `performance`: `covearge`는 분화를 할수록 값이 적어지기만, 함. 따라서, "community간에 edge가 적을수록, bonus를 얻는 지표"
    - `modularity`: configuration model이라는 random model을 기준으로, 이에 비해서 얼마나 edge가 있는 것이 exceptional한지를 고려해서 평가하는 지표. 쉽게, 높을수록, 잘 분화된 편. 이라고 생각하면 좋음.

```python
import networkx as nx
import itertools

# Generate graph
N = 20
G = nx.scale_free_graph(N, seed=0)
G = nx.Graph(G)

assert nx.is_connected(G) == True
#================================

print("==" * 20)
print("== community detection by edge betweenness centrality")
community_generator = nx.algorithms.community.girvan_newman(G=G)

print("== Coverage, Performance and Modularity")

for i, partition in enumerate(community_generator):
    # n개의 node가 있을 때, n개의 community까지 분화할 수 있으므로,
    # n개로 분화되면 loop 탈출.
    partition_coverage = nx.algorithms.community.coverage(G, partition)
    partition_performance = nx.algorithms.community.performance(G, partition)
    partition_modularity = nx.algorithms.community.modularity(G, partition)
    print(
        f"{i:2d} time :: Coverage: {partition_coverage:.4f}, Performance: {partition_performance:.4f}, Modularity: {partition_modularity:.4f}"
    )
    if False:  #print all communities?
        for j, comm in enumerate(partition):
            print(f"community {j:2d} at time {i:2d} ==> {comm}")
print("==" * 20)
```

- `coverage`의 경우, 당연히, 분화할수록 community edge를 커버할 수 없으므로 작아지는 것이 맞고 
- `performance`의 경우, 모두 분화했을 때, 0.8474를 가지므로, 이 값보다는 커야, 그나마 의미가 있는 것이죠. 
- `modularity`의 경우, 6 time 이후버트는 점차 감소되어 음의 값까지 떨어지는 것을 알 수 있습니다.

```
========================================
== community detection by edge betweenness centrality
== Coverage, Performance and Modularity
 0 time :: Coverage: 0.9677, Performance: 0.3421, Modularity: 0.0598
 1 time :: Coverage: 0.8065, Performance: 0.6316, Modularity: 0.2097
 2 time :: Coverage: 0.7742, Performance: 0.6842, Modularity: 0.2008
 3 time :: Coverage: 0.7419, Performance: 0.7316, Modularity: 0.1915
 4 time :: Coverage: 0.7097, Performance: 0.7737, Modularity: 0.1816
 5 time :: Coverage: 0.6774, Performance: 0.8105, Modularity: 0.1712
 6 time :: Coverage: 0.5161, Performance: 0.8632, Modularity: 0.2347
 7 time :: Coverage: 0.4839, Performance: 0.8737, Modularity: 0.2086
 8 time :: Coverage: 0.4516, Performance: 0.8842, Modularity: 0.1998
 9 time :: Coverage: 0.4194, Performance: 0.8895, Modularity: 0.1733
10 time :: Coverage: 0.3871, Performance: 0.8947, Modularity: 0.1545
11 time :: Coverage: 0.3548, Performance: 0.8947, Modularity: 0.1275
12 time :: Coverage: 0.2903, Performance: 0.8895, Modularity: 0.0858
13 time :: Coverage: 0.2258, Performance: 0.8789, Modularity: 0.0656
14 time :: Coverage: 0.1935, Performance: 0.8737, Modularity: 0.0380
15 time :: Coverage: 0.1613, Performance: 0.8684, Modularity: 0.0328
16 time :: Coverage: 0.0968, Performance: 0.8579, Modularity: -0.0109
17 time :: Coverage: 0.0645, Performance: 0.8526, Modularity: -0.0369
18 time :: Coverage: 0.0323, Performance: 0.8474, Modularity: -0.0682
========================================
```

## wrap-up

- 매번 community detection을 그냥 별생각없이 쓰기만 했지, 정작, 적합성을 평가하지는 못했씁니다 하하하. 
- 다만, clustering이 매번 그렇듯, 그냥 이렇게 분화해서 이정도가 적절한 것 같다, 는 것은 맞더라도, 결국 값이 아니라, 실생활에 쓰기 위해서는 그 결과를 면밀히 분석했을 때, 의미있는게 더 중요하긴 합니다.


## reference

- [[네트워크이론] Network Modularity (네트워크의 모듈성)](https://mons1220.tistory.com/93)
- [Modularity in wikipedia](https://en.wikipedia.org/wiki/Modularity_(networks)#Modularity)