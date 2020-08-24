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

## Make an issue in NetworkX github.

- 혼자 그 이유를 정리해보려고 했으나, 이해되지 않는 부분들이 있어서, [NetworkX](https://github.com/networkx/networkx)에 issue를 남겨봤습니다. 사실 github의 issue는 본질적으로, 해당 라이브러리에 버그나 충돌의 문제가 있을 때 남기는 것이 맞지만, 가끔 `Question:` 이라는 말을 앞에 붙이고 쓰는 경우도 있길래, 저도 그냥 써봤습니다. 같은 질문을 [stackoverflow에도 남겨봤지만](https://stackoverflow.com/questions/59960662/why-nx-subgraph-view-is-amazingly-faster-than-g-subgraph-edge-subgraph), 아무도 대답하지 않았습니다. 사실, 상대적으로 networkx가 그렇게 유명한 라이브러리는 아니니까요. 
- [질문 타래](https://github.com/networkx/networkx/issues/3802)는 링크에 들어가시면 됩니다. 

### Questions 1 and its Answer

#### Questions 1
- 어째서, `nx.subgraph_view`가 `G.subgraph().edge_subgraph()`보다 훨씬 빠른것이냐? 라는 질문을 던졌고, 그에 대한 대답은 다음과 같습니다. 

#### Questions 1 : Answer

- 일단, `G.subgraph().edge_subgraph()`는 chaining method를 사용하며, 각각 parameter로 node와 edge에 대한 list를 직접 생성하여 집어넣어줘야 한다. 이렇게 새로운 리스트를 복사하는 것 자체가 시간이 매우 오래 걸리는 일이다. 반면, `nx.subgraph_view`의 경우는 node 혹으 edge를 list로 넘겨주는 것이 아니라, lambda function으로 넘기며, 이는 이후에 다 끝났을 때 lazy evaluation을 해준다. 그러므로, 속도 측면에서 차이가 있다. 
- 그리고, 이 둘의 실행결과가 항상 같은 것은 아니다. `nx.subgraph_view`의 경우는 **filter union**으로 해석하면 되는데, node, edge에 대해서 정의한 filtering lambda function에 대해서 union으로 처리하는 반면, `G.subgraph().edge_subgraph()`의 경우는 filter serise로 처리한다. 즉, set operation처럼, 첫번째는 union, 두번째는 intersection이라고 설명할 수 있다. 정확하게는 아래 코드를 보면 더 명확하다.

```python
>>> import networkx as nx
>>> G = nx.Graph([(0, 1), (1, 2)])
>>> G.add_node(3)
# filter nodes 0, 1, 3 and filter edges to only (0, 1)
>>> union = nx.subgraph_view(G, filter_node=lambda x: True if x in [0, 1, 3] else False,
                    filter_edge=lambda e1, e2: True if (e1, e2) in [(0, 1)] else False)
# same done using stacking/chaining
>>> stack = G.subgraph(nodes=[0, 1, 3]).edge_subgraph(edges=[(0, 1)])

# filter union이므로, filter_edge, filter_node 중 하나에만 속해도 보이는 반면
>>> union.nodes()
NodeView((0, 1, 3)) 
# filter stack이므로, filter_edge, filter_node 중 둘다 속해야 처리된다.
>>> stack.nodes()
NodeView((0, 1))
```

### Questions 2 and its Answer

#### Questions 2

- 그래, 두번 연속으로 chaining method를 쓰니까, 느려지는 것이라면, 그렇다면 node에 대해서만 filtering을 하면 어떨까? 라는 생각을 해서, node에 대해서만 처리해봤다. 그래도 여전히, `nx.subgraph_view`가 빨라서, 이에 대해 추가로 질문을 남겼다.

#### Questions 2 : Answer

- 여기서, 다시, 이는 결국 lazy evaluation 이며, 각각에 저장된 내용이 다르다는 것을 말해주는데, `nx.subgraph_view`의 경우 lazy evaluation으로 처리하기 때문에, 빨라 보이지만, 필요한 값을 진짜 가져올 때는 추가의 시간이 필요하며, `G.subgraph()`의 경우는 바로 evaluation해서 처리하기 때문에, 속도가 더 빠른 것처럼 보이는 것이다.

```python
# FilterAtlas와 함께 lambda function이 존재한다.
# 이는 아직 node가 evaluation되지 못했으며, 이후 필요할 때, lazy evaluation하는 방식을 말함.
>>> nx_subG._node
FilterAtlas({0: {'weight': 0.00767033093403946}, .... 4: {'weight': 0.308129712638896}},
 <function <lambda> at 0xa495783b0>)
# 
# 이는 아직 node가 evaluation되지 못했으며, 이후 필요할 때, lazy evaluation하는 방식을 말함.
>>> subG._node
FilterAtlas({0: {'weight': 0.00767033093403946}, ... 4: {'weight': 0.308129712638896}},
<networkx.classes.filters.show_nodes object at 0xa2fa39810>)
```


## wrap-up

- 외부에서, 궁금해서 조금씩 파고 들어가다가 지금처럼 내부로 훅 가게 되는 경우들이 있죠. 그저, `subgraph`를 만드는 방법이 두 가지가 있길래 그 두가지 방법이 어떻게 다른지를 확인하던 중에, 성능의 차이가 압도적인 것을 알게 되었고, 그이유를 파다보니, core한 class까지 체크하게 되었습니다. 
- 그리고, 이는 `FilterAtlas`에 대한 이해로 넘어가는데, 같은 자료구조일지라도, 어떤 경우에느 lazy evaluation으로 존재하고, 다른 경우에는 evaluation된 상태로 존재한다. 그럴 필요가 있나? 
- 아주 높은 확률로, 결국 이건 자료구조의 문제로 보입니다. 그리고 제가 참고한 class인 `networkx.classes.coreviews`에서도, `from collections.abc import Mapping`을 참고해서 쓰고 있죠. 즉, 특정한 자료구조의 형태를 직접 설계하여 써서, 훨씬 빨라진 것처럼 보이는데요. 우선, 저는 Mapping이 뭔지부터 확인한 다음, 더 정리해보도록 하겠습니다.