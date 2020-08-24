---
title: networkx Graph에서 새로운 Graph 만들기(filtering, map 등)
category: python-lib
tags: networkx python-lib python 
---

## 간단히 말해서, 네트워크 또한 데이터 구조다. 

- '어떤 노드가 어떤 노드와 연결되어 있는가?', '또한 그 노드들은 어떠한 특성을 가지고 연결되어 있는가?', '그 노드와 직접 연결된 노드들은 무엇이 있는가?' 등 네트워크를 분석하다보면 관련된 분석들이 꼬리를 물고 늘어진다. 
- 이 때 매번 기존 graph로부터 새로운 node를 만들어야 할 필요가 있는데, 아직 `nx.Graph()`에 익숙하지 못하여, 이 부분이 부족하다는 생각이 들었다. 
- 그래서, 다시 정리를 해보기로 함. 

## please do not use `add_weighted_edges_from`

- 내가 `nx.Graph()`를 사용하면서 가장 혼동스러웠던 부분이 이 부분이라고 생각되는데, 보통 나는 weighted edges를 사용한다. 따라서 대부분 `add_weighted_edges_from`을 사용하느데 이 아이와 `add_edges_from`의 input이 다르다. 
- `add_weighted_edges_from`의 경우 3-tuple의 형태지만 `(from_node, to_node, weight)`의 형태로 넘긴다. 단, 이것이 graph에 edge로 추가된 다음에는 `(from_node, to_node, {'weight':weight})`의 형태로 변경된다. 이 부분이 약간 나는 헷갈려서, 동일하게 넘길 수 있는 `add_edges_from`을 사용하는 것이 edge의 형태를 일관적으로 기억하는데 적합하다고 생각한다. 

```python
import networkx as nx
import numpy as np 

graph_size = 5
testG = nx.Graph()
testG.add_nodes_from(
    [ ("n{}".format(i), {'weight':np.random.randint(1, 5)}) for i in range(0, graph_size) ]
)
testG.add_weighted_edges_from(
    [ ("n{}".format(i), "n{}".format(j), np.random.randint(1.0, 10.0)) # (from_node, to_node, weight) 
     for i in range(0, graph_size) for j in range(0, graph_size)]
)
for e in testG.edges(data=True):
    print(e)
```

- 들어갈때는 weight가 dictionary로 넘어간 것이 아니지만, edge를 출력해보면 dictionary로 되어 있음. 혼동스러운 부분.

```
('n0', 'n0', {'weight': 3})
('n0', 'n1', {'weight': 2})
('n0', 'n2', {'weight': 9})
('n0', 'n3', {'weight': 5})
('n0', 'n4', {'weight': 9})
('n1', 'n1', {'weight': 9})
('n1', 'n2', {'weight': 3})
('n1', 'n3', {'weight': 2})
('n1', 'n4', {'weight': 6})
('n2', 'n2', {'weight': 4})
('n2', 'n3', {'weight': 2})
('n2', 'n4', {'weight': 1})
('n3', 'n3', {'weight': 1})
('n3', 'n4', {'weight': 3})
('n4', 'n4', {'weight': 7})
```

- 따라서 앞으로는 `add_edges_from`만을 쓰기로 합니다. 다음처럼 3-tuple의 마지막 원소를 `dictionary`로 넘겨주면 됩니다. 

```
graph_size = 5
testG = nx.Graph()

testG.add_nodes_from(
    [ ("n{}".format(i), {'weight':np.random.randint(1, 5)}) for i in range(0, graph_size) ]
)
testG.add_edges_from(
    [ 
        ("n{}".format(i), "n{}".format(j), {'weight': np.random.randint(1.0, 10.0)}) # (from_node, to_node, weight) for i in range(0, graph_size) for j in range(0, graph_size)
    ]
)
for e in testG.edges(data=True):
    print(e)
```


## generate or extract new graph 

- 우리가 database에서 필요한 데이터만 가져와서 분석하는 것처럼, 전체 네트워크는 그대로 두고 필요할때 일 부분만 filtering하거나 수정해서 분석하는 것이 필요합니다. 경우에 따라서는 새로운 graph를 만드는 것도 필요할 수 있구요. 

### use map, filter with graph 

- 흔히들 `functional programming`에서 사용하는 것처럼 `map`, `filter`등이 그래프에서도 적용된다. 즉, iterator로 넘겨도 된다는 이야기다. 이렇게 하면 큰 데이터를 필요하지 않을 때는 realization하지 않아도 되기 때문에 훨씬 빨라질 수 있음.
- 예시는 아래 코드에서도 있으니 따로 넣어서 설명하지 않겠다. 

### 일정 weight가 되지 않는 edge 삭제하여 새로운 그래프 만들기. 

- 네트워크를 그릴 때, 모든 edge를 고려하면 굉장히 복잡해진다. 예를 들어, 논문의 키워드를 가지고 네트워크를 만들었을 때, 단 한번 등장하는(weight가 1인) edge까지 모두 고려하고 만약 그것까지 그린다면 얼마나 그림이 지저분하겠는가, 
- 따라서 일정 weight가 되지 않는 그래프는 없애고 새로운 그래프륾 만들어 주는 기능이 매우 중요하다. 

- **code의 특이사항 **
    - 아래 코드를 보면 `filter`를 사용하여 edge를 넘겼고, `add_edges_from`을 사용하여 edge를 넣었다. 
    - 또한, 그림을 그릴때 어떤 edge가 없어졌는지를 확실하게 보기 위해서 `pos`를 동일한 레이아웃으로 넘겼다. 

```python
import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt

# generate sample graph
graph_size = 10
testG = nx.Graph()
testG.add_nodes_from(
    [ ("n{}".format(i), {'weight':np.random.randint(1, 5)}) for i in range(0, graph_size) ]
)
testG.add_edges_from(
    [ ("n{}".format(i), "n{}".format(j), {'weight':np.random.randint(1.0, 10.0)}) 
     for i in range(0, graph_size) for j in range(0, graph_size)]
)

def drop_low_weighted_edge(inputG, above_weight=3):
    rG = nx.Graph()
    rG.add_nodes_from(inputG.nodes(data=True))
    edges = filter(lambda e: True if e[2]['weight']>=above_weight else False, inputG.edges(data=True))
    rG.add_edges_from(edges)
    """
    neighbor가 없는 isolated node를 모두 지운다. 
    """
    for n in inputG.nodes():
        if len(list(nx.all_neighbors(rG, n)))==0:
            rG.remove_node(n)
        #print(n, list(nx.all_neighbors(rG, n)))
    return rG
    
plt.figure(figsize=(10,5))
pos = nx.spring_layout(testG)
nx.draw_networkx(testG, pos)
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/nx_graph_control_201805091345')

plt.figure(figsize=(10,5))
nx.draw_networkx(drop_low_weighted_edge(testG, 7), pos)
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/nx_graph_control_201805091346')
```

- 원래 그래프 그림

![](/assets/images/markdown_img/nx_graph_control_201805091345.svg)

- 낮은 weight의 edge를 필터링한 다음의 그림

![](/assets/images/markdown_img/nx_graph_control_201805091346.svg)

### extract ego-network 

- 또한 개별 node와 직접 연결된 graph만 따로 도출하여 보고싶을 때가 있다. 
- 이 때는 간단하게 `nx.ego_graph`를 사용한다. 

```python
plt.close('all') 
# 가끔 figure가 너무 많으면 plt.show를 했을때 지난 figure까지 답 보여주는 경우가 있다. 이걸 쓰면 다 지워줌. 

G1 = drop_low_weighted_edge(testG, 8)
plt.figure(figsize=(10,5))
pos = nx.spring_layout(G1)
nx.draw_networkx(G1, pos)
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/nx_graph_control_201805091359.svg')

G1_ego_n5 = nx.ego_graph(G1, 'n5')
plt.figure(figsize=(10,5))
nx.draw_networkx(G1_ego_n5, pos)
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/nx_graph_control_201805091400.svg')
```

- 원래 그림 

![](/assets/images/markdown_img/nx_graph_control_201805091359.svg)

- ego network(그림의 형태는 같지만, 자동으로 확대된 부분이 있음)

![](/assets/images/markdown_img/nx_graph_control_201805091400.svg)