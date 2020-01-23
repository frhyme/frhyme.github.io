---
title: networkx Graph에서 reachability 확인하기 
category: python-libs
tags: python python-libs networkx graph reachability 
---

## intro 

- 저는 networkx를 활용해서 네트워크를 그리고, 분석하고, 또 만들고 아무튼 잡일을 아주 많이 합니다. 
- 그런데 네트워크를 그린 다음, 해당 네트워크에서 특정 node A와 특정 node B가 연결되어 있는지 확인하는 방법을 정리했습니다. 


## just do it

- `nx.algorithms.descendants`를 사용하면, 특정 노드로부터 reachable한 모든 노드 집단을 리턴할 수 있습니다. 
- 두 노드가 연결되어 있는지를 파악하고 싶다면, 해당 노드로부터, reachable한 모든 노드에 해당 노드가 포함되어 있는지 파악하면 됩니다. 

```python
import networkx as nx 

testG = nx.Graph()
testG.add_edges_from(
    [('a', 'b'), ('c', 'b'), ('b', 'd'), 
     ('e', 'f'), ('f', 'g')
    ]
)
print(testG.nodes())
print(testG.edges())
print("=="*20)
print("a의 reachable한 모든 노드")
print(nx.algorithms.descendants(testG, 'a'))
print("=="*20)
print("e의 reachable한 모든 노드")
print(nx.algorithms.descendants(testG, 'e'))
print("=="*20)

```


## wrap-up

- 어려울줄 알았는데 역시 networkx는 개쩌는 라이브러리라서, 다 알려주네요 쿠쿠 
- 저는 undirected network를 사용했지만, 만약 directed network를 사용한다면, 아래 두 경우를 구분해서 써줘야 합니다. 
    - `networkx.algorithms.dag.ancestors`
    - `networkx.algorithms.dag.descendants`

## reference

- <https://media.readthedocs.org/pdf/networkx/latest/networkx.pdf>