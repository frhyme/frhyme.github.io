---
title: networkx - structural holes - constraint
category: python-libs
tags: python python-libs networkx structural-holes constraint
---

## 4-line summary 

- structural hole은 "그래프에서 구조적인 허점"을 말하며, 이 "구조적인 허점"에 존재하는 node들은 보통 서로 다른 클러스터의 중심에 위치하게 되므로 정보의 중개자로서 강한 이득을 얻게 된다는 것을 말합니다. 
- 어떤 노드가 structural hole인지 파악하기 위해서 constraint라는 지표를 계산할 수 있으며, 이는 "해당 노드가 다른 노드들로부터 얼마나 많은 영향을 받게 되는가"를 측정한다.
- 따라서, cosntraint의 값이 적다면 이는 전체 graph의 focal point에서 벗어나 있으며, structural hole 이라는 것을 의미한다. 
- betweenness centrality와 비슷한 경향성을 가지기는 하나, 유사도는 높다고 보기 어렵다.

## what is structural holes? 

- [structural holes](https://en.wikipedia.org/wiki/Structural_holes)은 social network 연구 분야에서 주로 쓰이는 개념이며, "두 객체(individual)간의 정보 접근에 대한 차이"로 이해될 수 있습니다. 흔히들, 그냥 "중개자"정도로 이해하죠. 실제 세계에서 많은 네트워크들은 강하게 밀집된 구조(dense cluster)로 특성화됩니다. 따라서, 보통 이 클러스터들을 중심으로 비슷한 생각이 정보들이 공유됩니다.
- 그렇다면, 
- 현실계에서 일어나는 대부분의 사회적 구조(social structure)는 강한 연결(strong connection)으로 구성된 밀집된 구조(dense cluster)로 특성화됩니다. 따라서, 보통 이 클러스터별로 비슷한 생각, 정보 등을 공유하게 되죠. 
- 그러나, 만약, 어떤 한 개인이 서로 밀집된 두 그룹(혹은 클러스터)의 중간에 위치하게 된어, 중개자(mediator)로 존재하게 된다면, 이 사람은 다른 사람들에 비해 비교적 높은 정보 획득에서의 이점을 가지게 됩니다. 이 사람은 일종의 '문지기(gatekeeper)'로서의 역할을 수행하게 되는 것이죠.
- 따라서, 양 클러스터에서 발생하는 모든 생각과 아이디어는 이 사람을 통하게 되고, 혁신적인 아이디어가 이로부터 나올 수 있게 됩니다. 아래 그림을 보시면 이 것이 어떤 의미인지 보다 명확하게 아실 수 있을 것 같아요. 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Network_Structure.jpg/330px-Network_Structure.jpg)


## Constraint

- structural hole을 측정하는 방법이 다른 것들도 있지만, 여기서는 `constraint`라는 것을 설명합니다. 사실 constraint는 LP에서 "제약식"을 의미하는데, 여기서는 "강제력, 제한하는 힘" 정도로 번역하는 것이 가장 적당할 것 같아요. 
- 어떤 node `u`가 특정 클러스터에 완전히 속해 있다면 이 `u`에 대해서는 일종의 강제력, 이라는 것이 매우 크다고 할 수 있죠. 하지만, 이 노드가 structural hole이라면, 어느 한쪽의 클러스터에 속해 있는 것이 아니기 때문에, 이 "강제력"이 적게 미친다고 할 수 있는 셈이죠. 따라서, 이를 고려하여 node `u`에게 영향을 미치는 정도가 어느 정도인가, 를 의미하는 것이 바로 constraint입니다.
- 이 때, 직접적(direct), 간접적(indirect) 영향력을 고려하여 `local_constraint(u, v)`를 측정하게 됩니다. 이 local_constraint는 u가 다른 노드에 비해서 v에게 지나치게 많이 쏠려 있을 경우(가령, u는 v라는 특정 노드에게만 상대적으로 많은 영향력을 주고 받게 되면 값이 커지게 되죠.

## Constraint implementation by python

- 말로만 하면 사실 무슨 말인지 이해가 어려우므로, 간단하게 코딩을 해봤습니다. 

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

### local_constraint(u, v)

- `local_constraint(u, v)`는 "u가 v에 의해서 얼마나 많은 영향을 받는가?"를 측정합니다.
- 이는 다음 두 가지 요소로 고려됩니다
    - direct: u가 v에 의해 직접 영향을 받는 정도, `normalized_mutual_weight(u, v)`
    - indirect: u가 v에 의해 간접적으로 영향을 받는 정도, node u와 v 사이에 존재하는 모든 노드 w에 대해서 `normalized_mutual_weight(u, w)` * `normalized_mutual_weight(w, v)`
- 즉, 이 값이 클수록 node `u`는 `v`에게 직간접적으로 많은 영향을 받고 있다고 할 수 있습니다.

```python
def local_constraint(G, u, v, weight='weight'): 
    # p_uv : u가 투자하는 모든 에너지 중에서 v에 투자하는 에너지의 비율을 의미함.
    direct = normalized_mutual_weight(G, u, v, weight='weight')
    indirect = 0 
    nmw = normalized_mutual_weight
    for w in set(nx.all_neighbors(G, u)):
        indirect += nmw(G, u, w, weight=weight) * nmw(G, w, v, weight=weight)
    return (direct + indirect)**2
```

### constraint(u)

- `constraint(u)`는 노드 `u`가 다른 모든 노드들에게서 얼마나 많은 영향을 받는지를 의미합니다. 즉, 노드 `u`가 어떤 클러스터에 강하게 속해 있을수록, 노드는 다른 노드들로부터 받는 에너지가 커지므로, 값이 커지고, 반대로 벗어날 경우 더 작은 값을 가지게 되죠.

```python
def constraint(G, nodes = None, weight='weight'): 
    # node u의 다른 이웃들 v들에 대한 local constraint의 합. 
    constraint_dict = {u: float('nan') for u in G}
    lc = local_constraint
    for u in constraint_dict: 
        u_nbrs = set(nx.all_neighbors(G, u))
        if len(u_nbrs)!=0:
            constraint_dict[u]=0
            for v in u_nbrs: 
                constraint_dict[u] += lc(G, u, v, weight='weight')
    return constraint_dict
```


## Constraint: Simple toy example

- 크기가 3, 4인 clique를 만들고 `node 2`에서 교차하도록 만듭니다. 이 Graph의 structural hole은 `node 2`에 위치하게 되겠죠. 앞서 말한 바와 같이, `node 2`는 양 쪽 클리크로부터 정보를 모두 전달받게 되고, 다른 노드들에 비해 상대적인 강제력(constrain)이 적습니다

```python
# G: node 2를 중심으로 각각 서로 다른 clique가 연결되어 있는 nx.graph
C1 = nx.complete_graph(3)
C2 = nx.complete_graph(4)
C2 = nx.relabel_nodes(C2, {n:n+2 for n in C2})
G = nx.compose_all([C1, C2])
nx.set_edge_attributes(G, 1, 'weight')
print(f"== Nodes: {G.nodes()}")
print(f"== Edges: {G.edges()}")
print("== constraint")
print(constraint(G, weight='weight'))
```

- 즉, 결과를 보면 실제로 `2` 노드에서 가장 값이 적은 것을 알 수 있죠.

```
== Nodes: [0, 1, 2, 3, 4, 5]
== Edges: [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
== constraint
{0: 0.9225, 1: 0.9225, 2: 0.5133333333333335, 3: 0.8311111111111109, 4: 0.8311111111111109, 5: 0.8311111111111109}
```

## comparison with betweenness centrality.

- 다만, 저는 structural hole이 betweenness centrality와 크게 다르지 않다는 생각이 들었습니다. 개념적으로 매우 비슷하게 느껴지거든요. 그래서 다음으로 간단하게 비교를 해본 결과, 비슷한 경향성은 있지만, 똑같지는 않네요. 물론 node의 수를 매우 크게 하면 더욱 비슷해질 수 있고, scale-free graph말고 다른 graph에 대해서 적용하면 다를 수도 있습니다만. 

```python
# GENERATE scale_free_graph
n = 300
G = nx.scale_free_graph(n=n, seed=0)
G = nx.Graph(G)
G.remove_edges_from(nx.selfloop_edges(G))
assert nx.is_connected(G)
# UPDATE edge weight
RG = np.random.RandomState(seed=0)
edge_weight_lst = RG.random(len(G.edges()))
edge_weight_dict = {e: e_w for e, e_w in zip(G.edges(), edge_weight_lst)}
nx.set_edge_attributes(G, edge_weight_dict, name='weight')
# CALCULATE constraint 
df = pd.DataFrame({
    'constraint': nx.constraint(G, weight='weight'), 
    'between_cent': nx.betweenness_centrality(G, weight='weight')
})
df['c_rank'] = df['constraint'].rank()
df['b_rank'] = df['between_cent'].rank(ascending=False)
corr, p = spearmanr(df['c_rank'], df['b_rank'])
print(f"spearman r - corr: {corr}, p: {p}")
corr, p = pearsonr(df['constraint'], df['between_cent'])
print(f"pearsone r - coef: {corr}, p: {p}")
```

- 순위를 비교하는 spearman의 경우는 그래도 좀 큰 값이 나오고, 값만을 비교한 경우는 좀 낮게 나옵니다. 다만, 여기서 spearman r의 값은 node의 수를 늘릴 수록 큰 값이 나오는 경향을 보입니다

```
spearman r - corr: 0.7321912070407661, p: 1.2453111039270024e-51
pearsone r - coef: -0.35762472849599036, p: 1.7635444770402943e-10
```

## wrap-up

- 처음에는 쉬울줄 알고 시작했는데, 생각보다 시간이 좀 오래 걸렸습니다. 다양한 이유가 있겠으나, 'constraint'라는 이름이 해당 개념을 명확하게 설명할 정도로 직관적이지 않고, [structural holes](https://en.wikipedia.org/wiki/Structural_holes)에 작성된 내용도, 좀 충실하지는 못한 것 같아요. 
- "개념"은 타당하지만, 이 개념이 유효하려면, "왜 그 계산을 해야 하는지"에 대한 내용도 충분해야 합니다. 하지만, 여기서 왜 'mutual weight"를 고려하고, "이걸 왜 normalized하고", 이런 부분들에 대해서 충실한 설명이 부족했던 것 같아요. 
- 결론적으로, "constraint는 해당 노드가 다른 녿들로부터 받는 영향을 말합니다", 특히 다른 도드들이 밀집된 클러스터로 인해 직간접적으로 해당 노드를 마치, 인력처럼 끌어당기면 이 값이 커지게 되는 것이죠". 
- 따라서, cosntraint의 값이 적다면 이는 전체 graph의 focal point에서 벗어나 있따, 라고 말할 수 있을 것 같네요. 


## reference

- [networkx - structural holes](https://networkx.github.io/documentation/stable/_modules/networkx/algorithms/structuralholes.html)

## raw-code 


```python
import networkx as nx 
import numpy as np 
import matplotlib.pyplot as plt 
import itertools 
import pandas as pd 
from scipy.stats import spearmanr
from scipy.stats import pearsonr


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
    scale = norm([mutual_weight(G, u, w, weight) for w in set(nx.all_neighbors(G, u))])
    if scale == 0:
        return 0
    else:
        return mutual_weight(G, u, v, weight=weight) / scale
    
def local_constraint(G, u, v, weight='weight'): 
    # p_uv : u가 투자하는 모든 에너지 중에서 v에 투자하는 에너지의 비율을 의미함.
    direct = normalized_mutual_weight(G, u, v, weight='weight')
    indirect = 0 
    nmw = normalized_mutual_weight
    for w in set(nx.all_neighbors(G, u)):
        indirect += nmw(G, u, w, weight=weight) * nmw(G, w, v, weight=weight)
    return (direct + indirect)**2

def constraint(G, nodes = None, weight='weight'): 
    # node u의 다른 이웃들 v들에 대한 local constraint의 합. 
    constraint_dict = {u: float('nan') for u in G}
    lc = local_constraint
    for u in constraint_dict: 
        u_nbrs = set(nx.all_neighbors(G, u))
        if len(u_nbrs)!=0:
            constraint_dict[u]=0
            for v in u_nbrs: 
                constraint_dict[u] += lc(G, u, v, weight='weight')
    return constraint_dict

# Simple toy example.
if False:     
    # G: node 2를 중심으로 각각 서로 다른 clique가 연결되어 있는 nx.graph
    C1 = nx.complete_graph(3)
    C2 = nx.complete_graph(4)
    C2 = nx.relabel_nodes(C2, {n:n+2 for n in C2})
    G = nx.compose_all([C1, C2])
    nx.set_edge_attributes(G, 1, 'weight')
    print(f"== Nodes: {G.nodes()}")
    print(f"== Edges: {G.edges()}")
    print("== constraint")
    print(constraint(G, weight='weight'))
# Comparison with Betweenness centrality. 
if True: 
    # GENERATE scale_free_graph
    n = 300
    G = nx.scale_free_graph(n=n, seed=0)
    G = nx.Graph(G)
    G.remove_edges_from(nx.selfloop_edges(G))
    assert nx.is_connected(G)
    # UPDATE edge weight
    RG = np.random.RandomState(seed=0)
    edge_weight_lst = RG.random(len(G.edges()))
    edge_weight_dict = {e: e_w for e, e_w in zip(G.edges(), edge_weight_lst)}
    nx.set_edge_attributes(G, edge_weight_dict, name='weight')
    # CALCULATE constraint 
    df = pd.DataFrame({
        'constraint': nx.constraint(G, weight='weight'), 
        'between_cent': nx.betweenness_centrality(G, weight='weight')
    })
    df['c_rank'] = df['constraint'].rank()
    df['b_rank'] = df['between_cent'].rank(ascending=False)
    corr, p = spearmanr(df['c_rank'], df['b_rank'])
    print(f"spearman r - corr: {corr}, p: {p}")
    corr, p = pearsonr(df['constraint'], df['between_cent'])
    print(f"pearsone r - coef: {corr}, p: {p}")
    
```