---
title: Query in Networkx
category: python-libs
tags: python-libs python networkx query 
---

## query in network? 

- 최근에는 GQL이라는 Graph Query Language를 정리했습니다. 결국 데이터를 Graph로서 표현하고, 이를 필요에 따라서, 필터링해서 볼 수 있는 쿼리언어 표준을 만들자! 라는 것이 해당 언어의 목적이죠. 
- 저는, 그렇게까지 대용량의 데이터를 쓰지 않기 때문에, DB를 쓰고 있지는 않습니다. 그냥 필요하면 pickle을 사용해서 임시파일로 저장을 하거나, 하는게 다죠. 
- 아무튼, 저는 networkx를 쓰는데, 여기서 필요한 데이터 혹은 sub-network를 추출하려면 어떠한 방식으로 해야 하는지를 좀 정리하면 좋을 것 같아서 정리를 해봅니다. 
- 아래에 대략 다음과 같은 것들을 정리하였습니다. 쓰고보니까 별 거 없긴 한데요. 
    - node/edge를 attribute로 구분하여 뽑아내려면?
    - 특정 node와 edge를 가진 sub-graph를 뽑아내려면? 
    - 한 노드의 이웃 노드를 찾아내는 방법은? 


```python
import networkx as nx
import numpy as np 
from itertools import combinations

np.random.seed(10)

G = nx.Graph()
# add node
NODE_SIZE=8
G.add_nodes_from([(f"n{i}", {'weight':np.random.randint(1, 7)})for i in range(0, NODE_SIZE)])
# add edge 
all_possible_edge = list(combinations(G.nodes(), 2))
selected_edge_indices = np.random.choice([i for i in range(0, len(all_possible_edge))], len(all_possible_edge)*2//3)
for edge_index in selected_edge_indices:
    f, t = all_possible_edge[edge_index]
    G.add_edges_from([(f, t, {'weight':np.random.randint(0, 10)})])
#print(G.edges())
# undirectional weighted G made
# node들만을 가져오는 경우 
print("==================================================")
## data=True를 넘겨주면, 각 node에 정의된 attribute(ex: weight)도 함께 가져온다. 
print(G.nodes(data=True))
## 여기서, 노드는 (node_name, attr_dict)로 넘어오고, 필요에 따라서, attr를 필터링해서 선택하면 됨. 
selected_nodes = [node_name for node_name, node_attr_dict in G.nodes(data=True) if node_attr_dict['weight']<5]
print(selected_nodes)
print("==================================================")
# edge를 가져오는 경우 
# edge는 from_node_name, to_node_name, edge_weight_dict 로 구성됨. 
print(G.edges(data=True))
selected_edges = [(e1, e2, edge_attr_dict) for e1, e2, edge_attr_dict in G.edges(data=True) if edge_attr_dict['weight']<5]
print(selected_edges)
# 특정 노드의 이웃노드들을 찾고 싶은 경우 
# nx.neighbors를 써서 찾으면 됨. 
print("==================================================")
target_node = 'n1'
neighbors = nx.neighbors(G, 'n1')
print(list(neighbors))
print("==================================================")
# 특정 노드의 이웃 노드만이 포함된 sub-graph를 찾고 싶은 경우 
## nx.subgraph로 그래프와 노드를 함게 넘겨주면 됩니다. 
## subG에서 특정 노드의 attr값들을 바꾸면, G에서의 값들도 바뀝니다. 
### 만약, subgraph만 그대로 가져오고 싶다면, copy method를 쓰면 되고요.
target_nodes = ['n1', 'n2']
subG = nx.subgraph(G, target_nodes)
print(subG.nodes(data=True))
print("==================================================")
# 보통 특정 node들만을 가지고 있는 sub graph를 많이 찾지만, 
# 당연히 edge를 가지고 있는 edge-sub graph도 찾을 수 있습니다. 
## nx.edge_subgraph를 쓰면 됩니다. 
## 만약에, 특정 edge관계, 어떤 edge attr를 가지고 있는 놈들만 모아서 그래프를 구성하고 싶다면 이렇게 하면  되지요. 
edge_subG = nx.edge_subgraph(G, [('n3', 'n1'), ('n1', 'n4')])
print(edge_subG.edges(data=True))
print("==================================================")
```

- 코드의 실행 결과는 다음과 같습니다. 

```
==================================================
[('n0', {'weight': 2}), ('n1', {'weight': 6}), ('n2', {'weight': 5}), ('n3', {'weight': 1}), ('n4', {'weight': 2}), ('n5', {'weight': 4}), ('n6', {'weight': 5}), ('n7', {'weight': 2})]
['n0', 'n3', 'n4', 'n5', 'n7']
==================================================
[('n0', 'n1', {'weight': 6}), ('n0', 'n5', {'weight': 9}), ('n1', 'n3', {'weight': 3}), ('n1', 'n4', {'weight': 3}), ('n1', 'n5', {'weight': 5}), ('n1', 'n6', {'weight': 8}), ('n2', 'n6', {'weight': 1}), ('n2', 'n7', {'weight': 8}), ('n2', 'n5', {'weight': 4}), ('n3', 'n5', {'weight': 9}), ('n4', 'n5', {'weight': 6}), ('n4', 'n7', {'weight': 7}), ('n5', 'n7', {'weight': 4})]
[('n1', 'n3', {'weight': 3}), ('n1', 'n4', {'weight': 3}), ('n2', 'n6', {'weight': 1}), ('n2', 'n5', {'weight': 4}), ('n5', 'n7', {'weight': 4})]
==================================================
['n3', 'n4', 'n0', 'n5', 'n6']
==================================================
[('n2', {'weight': 5}), ('n1', {'weight': 6})]
==================================================
[('n4', 'n1', {'weight': 3}), ('n3', 'n1', {'weight': 3})]
==================================================
```

## wrap-up

- 기본적으로는 그래프에서 필요한 부분을 읽고 쓰고 하는 것은 networkx에서도 다할 수 있씁니다. 
- 그러나, SQL/GQL등에서는 비교적 짧은 문법으로 샥샥 할 수 있는 반면, 여기서는 만들고, 다시 중간 산출물을 만들고 하는 번거로움들이 발생하죠. 딱 그정도의 차이점이 있습니다. 
