---
title: networkx - structural holes - effective-size
category: python-libs
tags: python python-libs networkx structural-holes effective-size
---

## 2-line summary 

- effective-size는 "redundancy"를 중심 개념으로 "node u에서 v로 가는 중복된 path가 존재하는가"를 중심으로 값을 계산합니다. 
- 특히, ego-network를 중심으로 star-graph와 가까울수록 effective-size는 높게, complete graph와 가까울수록 낮게 나타나게 되죠.

## what is structural holes? 

- [structural holes](https://en.wikipedia.org/wiki/Structural_holes)은 social network 연구 분야에서 주로 쓰이는 개념이며, "두 객체(individual)간의 정보 접근에 대한 차이"로 이해될 수 있습니다. 보통 하나의 긴밀한 집단에는 공통된 하나의 생각이 존재하게 됩니다. 강한 연결일수록 서로 많은 정보를 공유하고, 생각과 가치관등이 비슷해질 수 있죠. 
- 그러나, 만약 어떤 사람이 강한 연결을 가진 두 집단의 사이에 존재한다고 해봅시다. 그렇다면 이 사람은 두 강한 집단으로부터 서로 다른 정보를 동시에 얻음으로써, 새로운 종류의 특성을 가질 수 있죠. 이러한 것을 "구조적 허점"이라고 하며, structural hole이라고 부릅니다. 개념적으로는 betweenness centrality와 유사하게 느껴질 수 있을수도 잇죠. 

## effective size

- constraint를 사용해서 계산할 수도 있지만, 여기서는 "effective size"라는 값을 설명합니다. 
- 중심이 되는 개념은 "중복성(redundancy)"와 "ego-network"로서, "ego-network가 star-network와 가까울수록" 이 값은 크게 나옵니다. 즉, star-network이면 중복되는 path가 없으며, 해당 node가 가장 강한 힘을 가진다는 말이 되니까요. 
- 다만, 왜 이름이 "effective size"인지 잘 모르겠습니다. 여전히, 좀 명확하지 않게 느껴집니다. 아쉽게도, structural hole에 관한 지표들은 이름이 매우 직관적이지 않을 뿐 아니라, 설명도 매우 부실하게 느껴지곤 해요.

### mutual_weight(u, v) 

- `mutual_weight(u, v)`는 u와 v의 상호간에 가지는 weight의 합을 의미합니다. 만약 unweighted라면 1.0+1.0으로 2.0이 되겠죠.

```python
def mutual_weight(G, u, v, weight='weight'):
    # node u와 v간의 모든 edge의 weight합.
    # unweighted일 경우 1.0으로 가정.
    # 단, 여기서는 항상 weighted라고 가정
    m_w = 0.0
    if G.has_edge(u, v):
        m_w += G[u][v][weight]
    if G.has_edge(v, u):
        m_w += G[v][u][weight]
    return m_w
```

### normalized_mutual_weight(u, v)

- `normalized_mutual_weight(u, v)`는 `u`가 자신의 모든 이웃들 `W`들에게 투자하고 있는 모든 mutual_weight들을 기준으로 `v`에 투자하고 있는 mutual_weight를 normalization한 것을 말합니다. 
- 일반적으로는 그냥 norm을 `sum`으로 고려하여, 전체 중에서 v에 대한 mutual_weight가 어느 정도인지를 측정하죠. 
- 만약, node u가 v를 제외한 다른 노드들과는 매우 적은 weight들을 가지고, v에게만 매우 "강한 연결"을 가지고 있다면, 이 값은 1.0에 가까워집니다. 
- 즉, node u의 관점에서, v와의 연결이 얼마나 비율적으로, 강하다고 할 수 있는가? 를 의미하죠.

```python
def normalized_mutual_weight(G, u, v, norm=sum, weight='weight'):
    # u가 속한 모든 edge의 mutual_weight의 sum으로
    # mutual_weight(u, v)를 scaling
    # 즉, u가 가지고 있는 모든 '에너지'중에서 v로 투자하는 비율을 의미함.
    scale = norm([mutual_weight(G, u, w, weight) for w in set(nx.all_neighbors(G, u))])
    if scale == 0:
        return 0
    else:
        return mutual_weight(G, u, v, weight=weight) / scale
```

### redundancy(u, v)

- 개념적으로는 u, v간의 연결이 얼마나 중복되느냐? 를 의미합니다. weight를 고려하지 않는다면, 직접 연결된 edge만 존재할 수록, 중복성이 적으므로 값이 작게 나오게 되죠. 
- 다만, 여기서 normalization을 `p_uw`는 `sum`으로 하고, `m_vw`는 `max`로 했습니다. 여기서, "왜 그렇게 해야 하는지"에 대한 내용이 존재하지 않아요.

```python
def redundancy(G, u, v, weight='weight'):
    """
    redundancy: "node u, v 사이에 얼마나 중복된 길이 있는지"를 측정
    즉, 값이 높을수록, u와, v 사이에는 중복된 길이 있음을 의미하며, 
    당연히, complete graph에서는 값이 높게 나타나게 됨.
    ------------------------
    w: node u의 v 사이에 common neighbor
    p_uw: u가 영향받는 전체 중에서 w와 공유하는 상대적인 비율
    m_vw: v가 영향받는 가장 큰 에너지 비율 w에게 받는 비율
    v가 투자하는 에너지 중에거 가장 큰 에너지로 w에게 투자하는 양을 나눔.
    """
    r = 0
    for w in set(nx.all_neighbors(G, u)):
        p_uw = normalized_mutual_weight(G, u, w, norm=sum, weight=weight)
        m_vw = normalized_mutual_weight(G, v, w, norm=max, weight=weight)
        r += p_uw * m_vw
    return r
```

### effective size(G)

- 1-redundancy, 즉 unredundancy를 ego-network를 기준으로 합한 것이 effective size가 됩니다. 
- node `u`를 거치지 않고는 ego-network에서 다른 노드에 도달할 수 없는 경우, effective size는 커지게 되죠. 

```python

def effective_size(G, weight='weight'):
    """
    각 node u의 ego-network를 만들고, 거기서 중복되는 edge들이 얼마나 적은지를 측정한다. 
    - 즉, 모든 이웃노드들을 대상으로 1-redundancy의 합을 측정. 
    - 즉, ego-network에 중복되는 edge가 없을 수록(star- network에 가까울수록) 이 값은 높게 나옴. 
    - 즉, 이 값이 높을수록 해당 노드 u의 경우 structur hole.
    """
    effective_size_dict = {u: float('nan') for u in G.nodes()}
    for u in G.nodes():
        u_nbrs = set(nx.all_neighbors(G, u))
        if len(u_nbrs) != 0:
            effective_size_dict[u] = 0
            for v in u_nbrs:
                effective_size_dict[u] += 1-redundancy(G, u, v, weight)
    return effective_size_dict
```

- 실제로 아래에서 complete graph와 star-graph에 대해서 effective size를 계산해보면, 아래와 같이 나오는 것을 알수 있죠. effective size는 1.0부터 len(ego_network)의 범위를 가지게 됩니다.

```python
# complete graph 
if True:
    print("== complete graph")
    G = nx.complete_graph(5)
    nx.set_edge_attributes(G, 1, 'weight')
    print(nx.effective_size(G, weight='weight'))
# star graph 
if True:     
    print("== star graph")
    G = nx.star_graph(5)
    nx.set_edge_attributes(G, 1, 'weight')
    print(nx.effective_size(G, weight='weight'))
```

- 결과는 다음과 같습니다. 

```
== complete graph
{0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0}
== star graph
{0: 5.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0}
```

## wrap-up

- 개념적으로는 대충 이해됩니다. 결국 ego-network에서 내 node의 영향력을 측정하는 것이죠. 


## reference

- [networkx.algorithms.structuralholes.effective_size](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.structuralholes.effective_size.html)
- [Structural_holes in wikipedia](https://en.wikipedia.org/wiki/Structural_holes)


## raw-code

```python
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import itertools


def mutual_weight(G, u, v, weight='weight'):
    # node u와 v간의 모든 edge의 weight합.
    # unweighted일 경우 1.0으로 가정.
    # 단, 여기서는 항상 weighted라고 가정
    m_w = 0.0
    if G.has_edge(u, v):
        m_w += G[u][v][weight]
    if G.has_edge(v, u):
        m_w += G[v][u][weight]
    return m_w

def normalized_mutual_weight(G, u, v, norm=sum, weight='weight'):
    # u가 속한 모든 edge의 mutual_weight의 sum으로
    # mutual_weight(u, v)를 scaling
    # 즉, u가 가지고 있는 모든 '에너지'중에서 v로 투자하는 비율을 의미함.
    scale = norm([mutual_weight(G, u, w, weight)
                  for w in set(nx.all_neighbors(G, u))])
    if scale == 0:
        return 0
    else:
        return mutual_weight(G, u, v, weight=weight) / scale

def redundancy(G, u, v, weight='weight'):
    """
    redundancy: "node u, v 사이에 얼마나 중복된 길이 있는지"를 측정
    즉, 값이 높을수록, u와, v 사이에는 중복된 길이 있음을 의미하며, 
    당연히, complete graph에서는 값이 높게 나타나게 됨.
    ------------------------
    w: node u의 v 사이에 common neighbor
    p_uw: u가 영향받는 전체 중에서 w와 공유하는 상대적인 비율
    m_vw: v가 영향받는 가장 큰 에너지 비율 w에게 받는 비율
    v가 투자하는 에너지 중에거 가장 큰 에너지로 w에게 투자하는 양을 나눔.
    """
    r = 0
    for w in set(nx.all_neighbors(G, u)):
        p_uw = normalized_mutual_weight(G, u, w, norm=sum, weight=weight)
        m_vw = normalized_mutual_weight(G, v, w, norm=max, weight=weight)
        r += p_uw * m_vw
    return r

def effective_size(G, weight='weight'):
    """
    각 node u의 ego-network를 만들고, 거기서 중복되는 edge들이 얼마나 적은지를 측정한다. 
    - 즉, 모든 이웃노드들을 대상으로 1-redundancy의 합을 측정. 
    - 즉, ego-network에 중복되는 edge가 없을 수록(star- network에 가까울수록) 이 값은 높게 나옴. 
    - 즉, 이 값이 높을수록 해당 노드 u의 경우 structur hole.
    """
    effective_size_dict = {u: float('nan') for u in G.nodes()}
    for u in G.nodes():
        u_nbrs = set(nx.all_neighbors(G, u))
        if len(u_nbrs) != 0:
            effective_size_dict[u] = 0
            for v in u_nbrs:
                effective_size_dict[u] += 1-redundancy(G, u, v, weight)
    return effective_size_dict

# complete graph 
if True:
    print("== complete graph")
    G = nx.complete_graph(5)
    nx.set_edge_attributes(G, 1, 'weight')
    print(nx.effective_size(G, weight='weight'))
# star graph 
if True:     
    print("== star graph")
    G = nx.star_graph(5)
    nx.set_edge_attributes(G, 1, 'weight')
    print(nx.effective_size(G, weight='weight'))

```