---
title: python - networkx - Don't use subgraph too much 
category: python-libs
tags: python python-libs networkx centrality subgraph 
---


## networkx - Subgraph. 

- networkx에서 어떤 현상을 Graph로 모델링한 다음, 어떤 부분만 특정하게 보고 싶을 때가 있습니다.
- 가령, "특정 노드들"만 포함되거나, "특정 Edge들"만 포함되거나, 하는 식으로 보고 싶을 때가 있죠. 
- 그럴때 보통 다음을 사용해서 subgraph를 만들어줍니다. 

```python
import networkx as nx

G = nx.complete_graph(10)
# G.subgraph: Node [0, 1, 2]가 존재하는 subgraph를 리턴 
subG = G.subgraph([0, 1, 2])
# G.edge_subgraph: Edge [(0, 1), (1, 2)]가 존재하는 subgraph를 리턴. 
EdgeSubG = G.edge_subgraph([(0, 1), (1, 2)])
```

### subgraph is FROZEN.

- 다만, 여기서 확실하게 알고 가야 하는 것은 `subgraph` method로 새롭게 생겨난 graph는 원래 graph인 G에 종속적이라는 것이죠. 분리된 Graph가 아니라, 기존 Graph인 `G`에 대해서 node, edge에 대해 filtering하여 보게 되는 `graphView`일 뿐입니다. 
- "그래서 뭐가 달라지는데?"라는 생각이 들 수 있습니다. 아래를 보시면 좀 명확해지는데요. `G.subgraph()`로 인해 만들어진 `subG`에 새로운 node를 넣어주려고 하면, error가 발생합니다. 
- `Frozen graph can't be modified`라는 메세지가 뜨는데, 이것은 현재 subgraph가 얼려 있다는 말이죠. 

```python 
subG = G.subgraph([0, 1, 2])
try: 
    subG.add_node(34234)
except Exception as e:
    print(f"== ERROR: {e}")
```
```
== ERROR: Frozen graph can't be modified
```

- 물론, 이를 해결하기 위해서는 다음처럼 그냥 `copy()`를 사용하여 graph를 분리해주면 됩니다. 그럼, 종속된 graph가 아니라, 분리된 graph가 되는 것이죠. 

```python
subG = G.subgraph([0, 1, 2]).copy()
```

## FROZEN graph is so slow. 

- 이 부분이 오늘 쓸 내용의 메인부분입니다. 
- 저는 그동안 Graph를 통해서 방대한 양의 데이터를 관리한다고 할때, 가능하면 Frozne 상태를 유지하려고 했습니다. Graph를 각각 분리하여, 저장하고 관리하면 귀찮기도 하고, 하나의 모델에서 필요할때만 filtering해서 가져오는 식으로 하는 것이 훨씬 데이터의 일관성을 유지하는 측면에서 아주 중요하다고 생각하기도 했으니까요. 
- 다만, 오늘 발견한 것을 이렇게 처리할 경우 속도가 매우느려진다는 것이죠. 
- 간단한 테스트를 위해서, node, edge의 weight를 랜덤하게 지정해준 complete graph를 만들었습니다.
- 그리고, closeness centrality를 계산해보기로 했죠.

```python
import networkx as nx
import numpy as np 
import time 

RG = np.random.RandomState(seed=0)

NODE_SIZE = 100
G = nx.complete_graph(n=NODE_SIZE)
# UPDATE node, edge weight 
nx.set_node_attributes(
    G, {nID: v for nID, v in zip(G, RG.random(len(G)))}, name='weight')
nx.set_edge_attributes(
    G, {(uID, vID): v for (uID, vID), v in zip(G.edges(), RG.random(len(G.edges())))}, 
    name='weight')

## CASE 1: subgraph를 copy하지 않고, 여러번 centrality를 계산하는 경우 
subG = nx.subgraph(
    G, [nID for nID, n_attr in G.nodes(data=True) if n_attr['weight']> 0.5])
subG = nx.edge_subgraph(
    subG, [(uID, vID) for uID, vID, e_attr in G.edges(data=True) if e_attr['weight']> 0.5])
start_time = time.time()
nx.closeness_centrality(subG)
print(f"  FROZEN GRAPH: {time.time() - start_time:.5f}")
print("=="*20)
## CASE 2: subgraph를 copy해서 centrality를 계산하는 경우 
start_time = time.time()
subG = subG.copy()
nx.closeness_centrality(subG)
print(f"UNFROZEN GRAPH: {time.time() - start_time:.5f}")
```

- 결과를 보시면, 그저 node가 100개인 경우에 대해서도, FROZEN graph가 훨씬 느린 것을 알 수 있습니다. 약 10배의 차이가 나죠. 
- 즉, 만약 graph를 반복적으로 접근하여, 데이터를 계속 가져와야 하는 algorithm과 관련된 함수에 적용하기 위해서는, subgraph를 copy한 다음 처리하는 것이 훨씬 좋다는, 사실 알고 보면 당연한 이야기입니다.

```
  FROZEN GRAPH: 0.54974
========================================
UNFROZEN GRAPH: 0.04986
```


## wrap-up

- 사실, 모든 것이 그렇듯, 알고 나면 매우 당연하게 느껴집니다. copy하지 않은 subgraph의 경우 기존 graph에 대한 VIEW일 뿐이며, 접근시마다, VIEW를 만들기 위한 filtering이 필연적이죠. 따라서, centrality와 같이, 여러 번 정보를 가져와야 하는 경우에는 이 filtering작업이 매우 반복적으로 일어나게 되고, 부하가 커지게 됩니다. 
- 따라서, 만약, 이후에도 어떤 알고리즘을 적용하는 것이 필요하다면, 그 직전에 subgraph를 copy한 다음 적용하는 것이 훨씬 효율적입니다.