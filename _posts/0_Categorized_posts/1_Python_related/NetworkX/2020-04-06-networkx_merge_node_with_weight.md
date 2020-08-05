---
title: Networkx에서 node 합치기(MERGE node)
category: python-libs
tags: python python-libs networkx 
---

## Intro

- node의 uniqueness가 보장되지 않은 network를 대상으로 network 분석을 수행하고 있습니다. node의 uniqueness가 보장되지 않았다는 말은, "현재의 network에서 서로 다르게 표현된 두 node가 정말로 다른지 보장되지 않는다"라는 말이죠. 
- 가령, text에 존재하는 word들을 각 node로 만들었다고 해봅시다. 그런데, 이 node들이 '동일한 의미'를 가질 수도 있죠. 가령, '여성'과 '여자'라는 node가 동시에 현재 네트워크에 존재할 수 있겠죠. 그런데, 이 두 node는 의미적으로 매우 비슷하게 보입니다. 이런 경우에는, 가능하면 두 노드를 합쳐서 관리하는 것이 좋겠죠. 

## MERGE node 

- `merge`라고 쓰니까 반사적으로 마치, git을 쓰는 것 같군요. 
- 아무튼, 어떤 노드가 서로 합쳐지는지 우리가 알게 되었다고 한다면, 이 두 노드를 합쳐주는 것이 좋습니다. 가령 `A`를 `B`로 바꾸어준다고 하겠습니다.
- 이 합쳐주는 작업은 대략 다음의 순서로 진행되겠죠. 그리고 network는 기본적으로 weight가 있다고 가정합니다.
  1) `A`의 node weight를 `B`의 node weight에 더 해준다. 
  2) `A`의 neighbor가 `B`의 neighbor이기도 한 경우에는 edge의 weight만 더해준다. 
  3) 그렇지 않을 경우, 새로운 edge를 추가해주고, 같은 weight를 설정해준다. 
  4) `A`를 지운다.
- 이를 코드로 쓰면 대략 다음과 같아 지죠. 

```python
import networkx as nx 
import numpy as np 

def merge_node(G, nodeA, nodeB):
    """
    G의 nodeA를 nodeB로 변환해준다. 
    G를 shallow copy로 가져왔으며, call by reference의 형태로 바로 바꿔줌. 
    그리고, 이 과정에서 nodeA와 nodeB사이에 edge가 있었다면 이 edge는 삭제된다.
    """
    # UPDATE Node weight
    G.nodes[nodeB]['weight'] += G.nodes[nodeA]['weight']
    # UPDATE Edge weight
    
    for A_nbr in G[nodeA]:
        if G.has_edge(A_nbr, nodeB):
            # 이미 A_nbr이 nodeB와 연결되어 있다면, edge의 weight만 update하면 됨.
            G[nodeB][A_nbr]['weight'] += G[nodeA][A_nbr]['weight']
        else:
            # 연결되어 있지 않으므로 새로운 edge를 만들어주어야 함.
            if A_nbr is not nodeB: 
                # self-loop가 아닌지 확인
                G.add_edge(nodeB, A_nbr, weight=G[nodeA][A_nbr]['weight'])
            else: 
                # self-loop
                continue
    G.remove_node(nodeA)
```

- 이걸 간단히 테스트해보면 다음과 같습니다. 

```python
RG = np.random.RandomState(seed=0)
G = nx.complete_graph(4)
nx.set_node_attributes(
    G, dict(zip(G, RG.randint(1, 10, len(G)))), 'weight')
nx.set_edge_attributes(
    G, dict(zip(G.edges(), RG.randint(1, 10, len(G.edges())))), 'weight')

print(f"== BEFORE")
print(f"---- NODE attr")
for n in G.nodes(data=True): 
    print(n)
print(f"---- EDGE attr")
for e in G.edges(data=True):
    print(e)
print("=="*20)
merge_node(G, 0, 1)
print(f"== AFTER")
print(f"---- NODE attr")
for n in G.nodes(data=True):
    print(n)
print(f"---- EDGE attr")
for e in G.edges(data=True):
    print(e)
print("=="*20)
```

```plaintext
== BEFORE
---- NODE attr
(0, {'weight': 6})
(1, {'weight': 1})
(2, {'weight': 4})
(3, {'weight': 4})
---- EDGE attr
(0, 1, {'weight': 8})
(0, 2, {'weight': 4})
(0, 3, {'weight': 6})
(1, 2, {'weight': 3})
(1, 3, {'weight': 5})
(2, 3, {'weight': 8})
========================================
== AFTER
---- NODE attr
(1, {'weight': 7})
(2, {'weight': 4})
(3, {'weight': 4})
---- EDGE attr
(1, 2, {'weight': 7})
(1, 3, {'weight': 11})
(2, 3, {'weight': 8})
========================================
```

## wrap-up

- 코드로 만들어보니, 비교적 간단한 코드인데도 불구하고, 이전에는 이걸 만들지 못해서, network를 다시 raw_data로 변환하고, 다시 읽어들이는 형태의 번거로운 작업을 수행했던 기억이 납니다. 
- 그래도, 이제는 잘하게 되었으니 다행이죠 뭐.
