---
title: networkx의 layout 정리하기 
category: python-lib
tags: networkx python python-lib layout matplotlib
---

## 네트워크를 다양한 레이아웃에 따라서 2차원에 그리기.

- `matplotlib`에서 `scatter`, `plot`등으로 그림을 그릴 때는 이미 axis에서 어떤 좌표에 그림을 그리면 될지가 명확하게 나와 있습니다만, network에서는 개별 node에 좌표값이 없기 때문에 어디에 그려야 하는지 약간 어렵습니다. 
- 뭐 한 두개라면 대충 그리겠는데, 사실 node의 수도 엄청 많음은 물론, 해당 네트워크의 특징이 잘 보이도록 보여져야 하니까요. 
- 그래서 복잡한 네트워크에서 각 노드의 좌표를 잘 배치해서 네트워크를 예쁘게 보이게 하는 방법 또한 다양한 알고리즘으로 나오고 있습니다. 

## 임의로 node위치 배정하기 

- node의 x, y 좌표만 알려주면 edge는 알아서 잘 배치됩니다. 사실 당연한 이야기죠. 
- 이를 증명하려고 이상한 짓을 했는데요. 영문 알파벳 **QnA**를 네트워크로 표현해보려고 했습니다. 
- 똑같이 노드를 추가하고 엣지를 추가한 다음 `pos = {'Q0':[0, 0]}`의 식으로 node의 이름을 key로, node의 x, y 좌표를 tuple이나 리스트로 value로 넘겨줍니다. 
- 이렇게 넘겨주고, 그림을 그릴 때, `nx.draw_networkx_nodes(QnA, pos) `로 position을 넘겨주면 해당 포지션에 맞춰서 2차원에 잘 그려지게 됩니다. 

- 아래는 제가 임의로 노드 포지션을 만들어서 넘겨준 것입니다. 

```python
""" QnA를 네트워크로 그려줌 """
import networkx as nx

QnA = nx.Graph()
## Q
QnA.add_nodes_from(["Q{}".format(i) for i in range(0, 8)])
QnA.add_edges_from([("Q{}".format(i), "Q{}".format(i+1) ) for i in range(0, 7)]), QnA.add_edge('Q0', 'Q7')
QnA.add_nodes_from(['Q8', 'Q9']), QnA.add_edge('Q8', 'Q9') 

## A
QnA.add_nodes_from(["A{}".format(i) for i in range(0, 5)])
QnA.add_edges_from([('A0', 'A1'), ('A0', 'A2'), ('A2', 'A1'), ('A3', 'A1'), ('A2', 'A4')])

## n
QnA.add_nodes_from(['n{}'.format(i) for i in range(0, 6)])
QnA.add_edges_from([('n0', 'n1'), ('n1', 'n2'), ('n1', 'n3'), ('n3', 'n4'), ('n4', 'n5')])

## network의 좌표는 다음처럼 key=> node name, value=> (x, y) 로 넘겨주면 됨 
## 각 node의 좌표를 아래처럼 다 지정해주고 
pos = {'Q0':[0, 0], 'Q1':[1, 0], 'Q2':[1.5, -0.5], 'Q3':[1.5, -2.5], 
       'Q4':[1, -3], 'Q5':[0, -3], 'Q6':[-0.5, -2.5], 'Q7':[-0.5, -0.5],
       'Q8':[0.75, -2], 'Q9':[1.7, -3.3],
       'n0':[3.5, -1.5], 'n1':[3.5, -2.0], 'n2':[3.5, -3], 'n3':[4.0, -1.5], 'n4':[4.5, -2.0], 'n5':[4.5, -3], 
       'A0':[7.5, 0], 'A1': [7.0, -1.5], 'A2': [8.0, -1.5], 'A3':[6.5, -3], 'A4':[8.5, -3], 
      }

plt.figure(figsize=(10, 6))
plt.ylim(-4.0, 1.0)
## 그림을 그릴 때, pos로 넘겨주면 끝남. 
nx.draw_networkx_nodes(QnA, pos, node_size=400, alpha=1.0, 
                       node_shape='o', node_color='red')
nx.draw_networkx_edges(QnA, pos, width=10, alpha=0.8, edge_color='crimson')
plt.axis('off')
plt.tight_layout()
plt.savefig('../../assets/images/markdown_img/180807_qna.svg')
plt.show()
``` 

![](assets/images/markdown_img/180807_qna.svg)



## networkx의 layout 함수 이용하기 

- 여기서는 `networkx`에 있는 레이아웃만 보여주도록 하겠습니다. 
- 일단 적절한 네트워크를 하나 만듭니다. 임의의 `complete_graph`를 만든 다음에, edge를 임의로 몇 개 지워줍니다. 
- 그냥 `complete_graph`를 그대로 그릴 경우에는 layout별 차이가 잘 보이지 않아요. 약하게 연결된 부분, 밀집된 부분 등 그리려는 네트워크가 다양한 특성을 가지고 있어야 이 부분을 좀 더 명확하게 그릴 수 있습니다. 

```python
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 

G = nx.complete_graph(15)
for i in range(0, 150):
    ## 지울 node 쌍을 고르고 
    n1 = list(G.nodes())[np.random.randint(0, len(G.nodes()))]
    n2 = list(G.nodes())[np.random.randint(0, len(G.nodes()))]
    try:## 문제가 없다면 edge를 지움 
        G.remove_edge(n1, n2)
    except:
        continue
```

- 자 이제 그림을 그려줍니다. 일단 해당 네트워크로 부터 노드의 좌표를 도출해주는 layout을 만들어야 하는데요 `networkx`에서는 다음과 같은 총 6가지의 레이아웃을 지원합니다. 간단하게, 만든 네트워크를 그대로 넘겨주면 끝나죠. 

```python
layouts = {'spring': nx.spring_layout(G), 
           'spectral':nx.spectral_layout(G), 
           'shell':nx.shell_layout(G), 
           'circular':nx.circular_layout(G),
           'kamada_kawai':nx.kamada_kawai_layout(G), 
           'random':nx.random_layout(G)
          }
```

- 그리고 아래처럼 그림을 그려줍니다. 

```python
f, axes = plt.subplots(3, 2)
f.set_size_inches((12, 18)) 
## layout 설정 
layouts = {'spring': nx.spring_layout(G), 
           'spectral':nx.spectral_layout(G), 
           'shell':nx.shell_layout(G), 
           'circular':nx.circular_layout(G),
           'kamada_kawai':nx.kamada_kawai_layout(G), 
           'random':nx.random_layout(G)
          }
## 각 axis마다 그림을 따로 그
려줌
for i, kv in enumerate(layouts.items()):
    title, pos, ax = kv[0], kv[1], axes[i//2][i%2]
    nx.draw_networkx(G, kv[1], ax=ax)
    ax.set_title("{} layout".format(title), fontsize=20)
    ax.axis('off')
plt.tight_layout()
plt.savefig('../../assets/images/markdown_img/180807_nx_layout_comp.svg')
plt.show()
```

- 결과는 다음과 같습니다. 그냥 앞으로는 `spring_layout`이나, `kamada_kawai_layout`만 쓰면 될 것 같습니다. 

![](assets/images/markdown_img/180807_nx_layout_comp.svg)


## wrap-up

- circular layout과 shell layout은 같아 보이는데, 왜 두 개가 따로 있을까요? 

## raw code 

```python
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 

## 네트워크 생성 
G = nx.complete_graph(15)
for i in range(0, 150):
    n1 = list(G.nodes())[np.random.randint(0, len(G.nodes()))]
    n2 = list(G.nodes())[np.random.randint(0, len(G.nodes()))]
    try:
        G.remove_edge(n1, n2)
    except:
        continue
## 그림 그리기 시작 
f, axes = plt.subplots(3, 2)
f.set_size_inches((12, 18)) 
## layout 설정 
layouts = {'spring': nx.spring_layout(G), 
           'spectral':nx.spectral_layout(G), 
           'shell':nx.shell_layout(G), 
           'circular':nx.circular_layout(G),
           'kamada_kawai':nx.kamada_kawai_layout(G), 
           'random':nx.random_layout(G)
          }
## 각 axis마다 그림을 따로 그려줌
for i, kv in enumerate(layouts.items()):
    title, pos, ax = kv[0], kv[1], axes[i//2][i%2]
    nx.draw_networkx(G, kv[1], ax=ax)
    ax.set_title("{} layout".format(title), fontsize=20)
    ax.axis('off')
plt.tight_layout()
plt.savefig('../../assets/images/markdown_img/180807_nx_layout_comp.svg')
plt.show()

```