---
title: networkx의 노드, edge의 attribute 추가 및 업데이트하기 
category: python-lib
tags: python python-lib networkx network 
---

## 아주 간단합니다. 

- 사실 너무 간단해서 굳이 이걸 포스팅할 필요가 있는가 라는 생각도 들긴 하는데.....
- 다음처럼 해당 node의 정보값(정확히는 attr dictionary)에 그대로 넣어주면 됩니다. 
- 단 edge는 tuple이 key값으로 들어감 

```python
testG.edges[('A', 'B')]['gender'] = 20
```

```python
## node, edge update

import networkx as nx 

testG = nx.Graph()
testG.add_nodes_from([('A', {'weight':5}), ('B', {'weight':3})])
testG.add_edges_from([('A', 'B', {'weight':20})])
print(testG.nodes(data=True))
print(testG.edges(data=True))
print("="*20)
## update 나 추가하기 
testG.nodes['A']['weight'] = 1000
testG.nodes['A']['gender'] = 'male'
print(testG.nodes(data=True))
testG.edges[('A', 'B')]['gender'] = 'aaa'
print(testG.edges(data=True))
print("="*20)
```

```
[('A', {'weight': 5}), ('B', {'weight': 3})]
[('A', 'B', {'weight': 20})]
====================
[('A', {'weight': 1000, 'gender': 'male'}), ('B', {'weight': 3})]
[('A', 'B', {'weight': 20, 'gender': 'aaa'})]
====================
```