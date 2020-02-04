---
title: networkx - Line Graph.
category: python-libs
tags: python python-libs networkx line-graph
---

## What is Line Graph?

- [Line Graph](https://en.wikipedia.org/wiki/Line_graph)는 그냥 "Node를 Edge로 Edge를 Node로 변형한 그래프를 말합니다". 
- 가령, edge들이 `[(0, 1), (1, 2)]`로 존재하는 그래프(Node: 0, 1)의 Line Graph는 `[(Node_0_1, Node_1_2]`로, edge가 하나뿐인 graph로 변형된다는 이야기죠. 
- 개념적으로는 어려운 개념이 아니나, line graph와 graph와의 관계에 대해서는 매우 다양한, 정리들이 있습니다. 물론, 여기서는 거기까지 다루지 않습니다. 다만, `Line Graph`가 `Graph`와 역함수의 관계처럼 있는 걸로 아시는 분들이 있는데, 그렇지 않습니다.

## Do it. 

- 아주 간단히, `Graph G`, `Line Graph of G`, `Line Graph of Line Graph of G`를 만들고, node와 degree 합을 출력해봅니다. 
- Line Graph, `L(G)`의 node의 수는 `G`의 edge의 수와 같지만, degree sum은 같지 않죠. 


```python
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def draw_G(inputG, filename):
    """
    inputG를 그려서 filename에 저장함.
    """
    plt.figure()
    nx.draw_networkx(inputG)
    plt.savefig(filename)
#####
N = 5
G = nx.star_graph(N)
LG = nx.line_graph(G) # line graph of G
LLG = nx.line_graph(LG)

draw_G(G, "G.png")
draw_G(LG, "LG.png")
draw_G(LLG, "LLG.png")

print("==" * 20)
print("== G")
print(f"Node size: {len(G)}")
print(f"Edge size: {len(G.edges())}")
print(f"Degree Sum: {sum(map(lambda x: x[1], nx.degree(G)))}")
degree_sum = sum(map(lambda x: x[1], nx.degree(G)))
#print(degree_sum)

print("== LG")
print(f"Node size: {len(LG)}")
print(f"Edge size: {len(LG.edges())}")
print(f"Degree Sum: {sum(map(lambda x: x[1], nx.degree(LG)))}")

print("== LLG")
print(f"Node size: {len(LLG)}")
print(f"Edge size: {len(LLG.edges())}")
print(f"Degree Sum: {sum(map(lambda x: x[1], nx.degree(LLG)))}")
print("=="*20)
```

```
========================================
== G
Node size: 6
Edge size: 5
Degree Sum: 10
== LG
Node size: 5
Edge size: 10
Degree Sum: 20
== LLG
Node size: 10
Edge size: 30
Degree Sum: 60
========================================
```


## reference

- [wiki - line graph](https://en.wikipedia.org/wiki/Line_graph)
- [question in stackoverflow](https://stackoverflow.com/questions/30066788/networkx-edge-to-node-node-to-edge-representation)