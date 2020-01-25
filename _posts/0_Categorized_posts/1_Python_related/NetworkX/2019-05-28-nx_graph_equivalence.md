---
title: 네트워크의 isomorphism, equivalence의 차이
category: python-libs
tags: python python-libs network networkx
---

## network equivalence, isomorphism.

- 얼마전에, network의 isomorphic을 체크한다는 글을 썼었습니다만. 
- `isomorphism`과 `equivalence`는 다릅니다. 이걸 모르고 글을 쓴 것 같네요. 

### network isomorphism 

[graph isomorphsim](https://en.wikipedia.org/wiki/Graph_isomorphism)을 참고하면 되는데요, 간단하게 말하자면. 

> isomorphism은 구조적으로 같은지를 말할 뿐이다. 

- 이게 무슨 말인가 하면 다음 코드를 보시면 알 수 있습니다. 
    - 두 그래프는 서로 다른 node를 가지고 있고, 따라서 edge의 연결도 다릅니다. 
    - 하지만, 직선의 형태라는 점에서는 같은 형태죠. 
    - 즉 구조적으로 같기 때문에 isomorphic합니다. equivalence하지는 않죠. 

```python
import networkx as nx
g1, g2 = nx.Graph(), nx.Graph()

g1.add_edges_from([('a', 'b'), ('c', 'b'), ('a', 'c')])
g2.add_edges_from([('a', 'd'), ('d', 'c'), ('a', 'c')])
print(f"g1.edges(): {g1.edges()}")
print(f"g2.edges(): {g2.edges()}")
print(f"g1==g2: {g1==g2}")
print(f"nx.is_isomorphic(g1, g2): {nx.is_isomorphic(g1, g2)}")
```

```
g1.edges(): [('a', 'b'), ('a', 'c'), ('b', 'c')]
g2.edges(): [('a', 'd'), ('a', 'c'), ('d', 'c')]
g1==g2: False
nx.is_isomorphic(g1, g2): True
```

### network equivalence

- 따라서, equivalence를 체크하기 위해서는 node와 edge를 각각 체크해주는 것이 필요합니다. 
- isomorphism을 체크하는 것보다 훨씬 간단하죠.
- 또한, 이는 방향성이 없는 graph라서 그렇고, 또 weight도 고려하지 않았기 때문에 그런 것 같습니다. 
- 만약 이들이 고려되어야 한다면, 그냥 반영하면 되죠. 어렵지 않습니다.

```python
import networkx as nx

def is_equivalent(input_g1, input_g2):
    node_check = set(input_g1.nodes())==set(input_g2.nodes())
    edge_check = set(input_g1.edges())==set(input_g2.edges())
    return node_check and edge_check

g1, g2 = nx.Graph(), nx.Graph()
g1.add_edges_from([('a', 'b'), ('c', 'b'), ('a', 'c')])
g2.add_edges_from([('a', 'b'), ('c', 'b'), ('a', 'c')])
print(is_equivalent(g1, g2))
g1.add_nodes_from(['n1'])
print(is_equivalent(g1, g2))
g2.add_nodes_from(['n1'])
print(is_equivalent(g1, g2))
```

## wrap-up

- 오랜만에 쓰는 글이군요. 앞으로 좀 더 자주 쓸 수 있도록 노력해보겠습니당 하하