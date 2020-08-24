---
title: networkx - graph generator - triangular lattice
category: python-libs
tags: python python-libs networkx lattice-network triangular-lattice network-generator
---

## 1-line summary. 

- "lattice network"는 삼각형/사각형/육각형 등으로 벌집처럼 촘촘하게 만들어낸 네트워크 구조를 말합니다. 
- `nx.lattice_network(3, 2)`를 통해 간단하게 사용할 수 있습니다.

## lattice network. 

- google에서 "lattice network"를 검색하면 다음의 그림이 나옵니다. lattice는 한국말로 "격자"를 의미하며, 아래 그래프처럼 촘촘하게 쌓여진 그래프를 말하죠.
- 아래의 그림에서는 삼각형으로 쌓여 있지만, 사각형, 육각형 등으로 촘촘하게 쌓을 수도 있습니다.
- 또한, "mesh graph", "grid graph"라고 부르기도 하죠.

![triangular grid graph](https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Triangular_grid_graph.svg/1024px-Triangular_grid_graph.svg.png)

- triangular lattice network의 경우는 매우 높은 clustering coefficient를 가지게 됩니다(삼각형으로 되어 있으므로 당연한 것이기도 한데). 따라서, small-worldness를 판단할 때, reference network로 사용되기도 하죠.


## nx.triangular_lattice_graph

- 늘 그렇듯, `networkx`를 이용하면, lattice_graph를 생성할 수 있습니다.
- 아래와 같이 코드 안에 내용을 정리해두었습니다.

```python
import networkx as nx
import matplotlib.pyplot as plt

print("--" * 20)
# m: number of row
# n: number of column
(m, n) = 3, 2

# with_positions:
# if True => node_attr에 (x, y)를 추가(default)
# nx에 첨부된 다른 layout들보다, node_attr로부터 position을 가져오는 것이 훨씬 깔끔함.
G = nx.triangular_lattice_graph(
    m=m, n=n,
    with_positions=True
)
#############################################
# lattice network의 경우
# adjancemey matrix가 diagonal entry로부터
# 크게 벗어나지 않는다.
# lattice adjancecy matrix example:
print("== lattice adjacency matrix")
A = nx.to_numpy_array(G)
print(A)
print("--" * 20)
"""
[[0. 1. 1. 0. 0. 0. 0. 0.]
 [1. 0. 1. 1. 0. 0. 0. 0.]
 [1. 1. 0. 1. 1. 1. 0. 0.]
 [0. 1. 1. 0. 0. 1. 0. 0.]
 [0. 0. 1. 0. 0. 1. 1. 0.]
 [0. 0. 1. 1. 1. 0. 1. 1.]
 [0. 0. 0. 0. 1. 1. 0. 1.]
 [0. 0. 0. 0. 0. 1. 1. 0.]]
"""
#############################################

lattice_clustering_coef = nx.average_clustering(G)
print(f"== clustering: {lattice_clustering_coef}")
print("--" * 20)

#############################################
# draw triangular lattice graph.
# triangular lattice graph를 생성할 때,
# `with_positions`를 True(default)로 설정하였다면,
# node_attr에 position이 작성되어 있으므로 가져와서
# layout을 잡아주는 것이 훨씬 깔끔하다.
print("== draw network")
plt.figure()
pos = {n: G.nodes[n]['pos'] for n in G}
nx.draw_networkx(G, pos=pos)
plt.savefig('!tri_lattice_net.png')
print("--" * 20)

```

- 실행 결과는 다음과 같습니다. 

```
----------------------------------------
== lattice adjacency matrix
[[0. 1. 1. 0. 0. 0. 0. 0.]
 [1. 0. 1. 1. 0. 0. 0. 0.]
 [1. 1. 0. 1. 1. 1. 0. 0.]
 [0. 1. 1. 0. 0. 1. 0. 0.]
 [0. 0. 1. 0. 0. 1. 1. 0.]
 [0. 0. 1. 1. 1. 0. 1. 1.]
 [0. 0. 0. 0. 1. 1. 0. 1.]
 [0. 0. 0. 0. 0. 1. 1. 0.]]
----------------------------------------
 == clustering: 0.6833333333333332
----------------------------------------
== draw network
----------------------------------------
```

## reference

- [Latttice graph in wiki](https://en.wikipedia.org/wiki/Lattice_graph)
- [networkx.generators.lattice.triangular_lattice_graph](https://networkx.github.io/documentation/stable/reference/generated/networkx.generators.lattice.triangular_lattice_graph.html#networkx.generators.lattice.triangular_lattice_graph)