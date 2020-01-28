---
title: python - networkx - Make Subgraph and performance check.
category: python-libs
tags: python python-libs networkx subgraph
---

## Graph로부터 subgraph를 만들어봅시다.

- Graph를 분석하다보면, 필요에 따라서, subGraph를 만들어야 할 때가 있습니다. 이럴 때는 두 가지 방식이 있는데, `nx.subgraph_view()`와 이미 가진 graph object인 `G`의 class method로 접근하여 `G.subgraph().edge_graph()`로 처리하는 방식이 있죠. 첫번째의 경우 필터링할 node와 edge를 한번에 넘길 수 있는 반면, 두번째의 경우에는 각각을 따로 넘겨야 합니다. 그리고, 시간 측면에서 첫번째 방식이 훨씬 빠릅니다.
- 또한, 이렇게 만들어진 subgraph는 여전히 기존 Graph와 연결되어 있습니다. `nx.is_frozne(subG)`를 실행해보면, 해당 그래프는 얼려 있고, 따라서, subgraph에 새로운 노드를 넣거나, edge를 추가할 경우 에러가 발생합니다. 따라서, 만약 이 subgraph에 대해서 따로 분석을 수행하고 싶다면, `subG.copy()`를 통해 새로운 graph 객체를 만들어주어야 하죠. 

## do it. 

- 서론이 길었고, 해봅시다. 하나는 `nx.subtraph_view`를 사용해서 필터링할 node, edge를 함께 넘겨서 처리해주는 반면, 두번째는 `nx.subgraph().edge_graph()`를 통해 node와 edge를 각각 처리해주죠. 직관적으로, 아마도 첫번째가 더 빠를 것 같습니다. 노드가 1000개, 엣지는 컴플릿 네트워크 대비 60%만 존재하는 네트워크를 대상으로 수행했습니다.
- 속도의 차이는 다음과 같습니다. 똑같은 subGraph임에도 아래와 같이 처리하는 것이 훨씬, 압도적으로 빠릅니다. 11,205배 더 빠르네요. 이정도 차이라면 오히려, 뭔가 제가 코드 상에서 실수한 것이 없나? 싶기까지 해요.

```
== Graph Generation Done
========================================
subG from networkx:     0.000047
subG from method  :     0.526649
========================================
```

```python
import networkx as nx
import numpy as np
import time

# random한 weight를 가진 graph를 만들어줍니다.
N = 1000  # 3000
p = 0.6
G = nx.fast_gnp_random_graph(N, p)

node_weight_dict = {
    n: v
    for n, v in zip(G.nodes(), np.random.uniform(0, 1, len(G.nodes())))
}
edge_weight_dict = {
    e: v
    for e, v in zip(G.edges(), np.random.uniform(0, 1, len(G.edges())))
}
for n in (n for n in G.nodes()):
    G.nodes[n]['weight'] = node_weight_dict[n]
for e, v in edge_weight_dict.items():
    G.edges[e]['weight'] = edge_weight_dict[e]
print("== Graph Generation Done")
print("==" * 20)

# weight를 활용하여 특정 node, 특정 edge에 대해서만 filtering한다고 하자.
########################################
# nx.subgraph_view ####################
########################################
start_time = time.time()
nx_subG = nx.subgraph_view(G=G,
                           filter_node=lambda n_name: True
                           if G.nodes[n_name]['weight'] > 0.5 else False,
                           filter_edge=lambda n1_name, n2_name: True
                           if G.edges[
                               (n1_name, n2_name)]['weight'] > 0.5 else False)
#print(G.nodes(data=True))
print(f"subG from networkx: {time.time() - start_time:12.6f}")
#print(f"FROZEN: {nx.is_frozen(nx_subG)}")
########################################
# G.subgraph().edge_subgraph()
########################################
start_time = time.time()
# make node subg
NODE_subG = G.subgraph(
    nodes=(n for n, n_attr in G.nodes(data=True) if n_attr['weight'] > 0.5))
# make edge subg
subG = NODE_subG.edge_subgraph(
    edges=((e1, e2) for e1, e2, e_attr in NODE_subG.edges(data=True) 
           if e_attr['weight'] > 0.5))
print(f"subG from method  : {time.time() - start_time:12.6f}")
#print(f"FROZEN: {nx.is_frozen(subG)}")
print("=="*20)

assert len(nx_subG.nodes()) == len(subG.nodes())
assert len(nx_subG.edges()) == len(subG.edges())
# is_isomorphic로 체크하는 것이 훨씬 정확하지만 시간이 훨씬 오래 걸림.
# print(nx.is_isomorphic(subG, nx_subG))

```

## Why it happened??

- 속도의 차이가 너무 나서, 약간은 어이가 없어서 소스 코드를 뜯어보기로 합니다. 소스 코드에는 아래와 같이 약간은 낯선 함수들을 import 하는것을 알 수 있습니다. 

```python
from networkx.classes.coreviews import UnionAdjacency, UnionMultiAdjacency, \
    FilterAtlas, FilterAdjacency, FilterMultiAdjacency
from networkx.classes.filters import no_filter
```

- 이 내용을 github repository 에 작성된 [networkx.classes.coreviews](https://github.com/networkx/networkx/blob/master/networkx/classes/coreviews.py)를 보면, 각 클래스들의 역할을 할 수 있는데, 코드적으로 복잡한 것 같지는 않지만, 아직은 좀 낯설게 느껴집니다. 
- 또한, 대부분의 클래스의 base class로 `from collections.abc import Mapping`를 가지는데, 이 아이가 무슨 역할인지 체크하는 것이 우선 필요할 것 같아요. 


## wrap-up

- 외부에서, 궁금해서 조금씩 파고 들어가다가 지금처럼 내부로 훅 가게 되는 경우들이 있죠. 그저, `subgraph`를 만드는 방법이 두 가지가 있길래 그 두가지 방법이 어떻게 다른지를 확인하던 중에, 성능의 차이가 압도적인 것을 알게 되었고, 그이유를 파다보니, core한 class까지 체크하게 되었습니다. 
- 아주 높은 확률로, 결국 이건 자료구조의 문제로 보입니다. 그리고 제가 참고한 class인 `networkx.classes.coreviews`에서도, `from collections.abc import Mapping`을 참고해서 쓰고 있죠. 즉, 특정한 자료구조의 형태를 직접 설계하여 써서, 훨씬 빨라진 것처럼 보이는데요. 우선, 저는 Mapping이 뭔지부터 확인한 다음, 더 정리해보도록 하겠습니다.