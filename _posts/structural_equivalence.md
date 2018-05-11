---
title: structural equivalence를 활용해 두 노드 간의 등위성을 분석해봅시다. 
category: python-lib
tags: python python-lib networkx 

---

## 네트워크 상에서 비슷한 역할을 하는 노드를 찾아봅시다!

- structural equivalence, '구조적 등위성'으로 표현할 수 있을텐데, 네트워크 상에서의 연결성을 확인해보면, 두 노드가 '의미적으로 비슷하다'는 것을 의미하는 성질입니다. 
- 대략 다음 네트워크를 보시면, 구조적으로 n1과 n2의 네트워크 상에서의 역할이 비슷하다는 것을 대략 알 수 있습니다. 

![structural_sample_graph](/assets/images/markdown_img/structural_equi-201805111758.png)

```python
g = nx.Graph()
g.add_nodes_from(
    [("n{}".format(n), {'weight':1.0}) for n in range(1, 10) ]
)
g.add_edges_from(
    [('n1', n, {'weight':1.0}) for n in g.nodes()] + [('n2', n, {'weight':1.0}) for n in g.nodes()]
)
g.remove_edge('n1', 'n2')
for n1 in g.nodes():
    try:
        g.remove_edge(n1, n1)
    except:
        continue
nx.draw_networkx(g, nx.shell_layout(g))
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/structural_equi-201805111758.png')
```

- 이를 `node to node matrix`의 형태로 변환하면 각 node에 대한 vector가 되고, 이를 표준화한 다음 개별 node 간의 거리를 계산하면, 서로 가깝게 위치한 node 들을 찾을 수 있습니다. 
- 물론 여기서 중요한 것은 어떻게 노드 간의 거리를 측정할 것인가? 가 되겠죠. 유클리디안 이 적합하냐 자카드가 적합하냐, 코사인이 적합하냐 등등등, 가장 좋은 방법은 그냥 일단 다 해보는 것인데, 표준화를 먼저 한 다음에 하는 게 좋을 것 같습니다.
- 이제 슬슬 numpy, sklearn, scipy에 있는 scaling 기법들을 사용해주면 좋을 것 같습니다.

```python
import pandas as pd

node_to_node_mat = {}
for n1 in g.nodes():
    node_to_node_mat[n1] = {}
    for n2 in g.nodes():
        try:
            node_to_node_mat[n1][n2] = g[n1][n2]['weight']
        except:
            node_to_node_mat[n1][n2] = 0
node_to_node_mat = pd.DataFrame(node_to_node_mat)
print(node_to_node_mat)
```
```
     n1   n2   n3   n4   n5   n6   n7   n8   n9
n1  0.0  0.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0
n2  0.0  0.0  1.0  1.0  1.0  1.0  1.0  1.0  1.0
n3  1.0  1.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
n4  1.0  1.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
n5  1.0  1.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
n6  1.0  1.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
n7  1.0  1.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
n8  1.0  1.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
n9  1.0  1.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0
```

## by bipartite network 

- 또한 이후에는 node to node 가 아닌, bipartite한 구조를 만들어서 측정할 수도 있을 것 같습니다. 