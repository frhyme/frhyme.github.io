---
title: networkx에서 graph를 만들고 relabeling하기 
category: python-lib
tags: python python-lib networkx graph relabel bipartite matplotlib
---

## 노드를 바꿔주기 

- networkx에는 꽤 괜찮은 random graph generator들이 많이 있습니다. 단 만들 때부터 node set를 정하고 만들기는 조금 어려워요.
- 그렇다면 일단 만든 다음에 바꿔주면 됩니다 하하핫 쉽죠. 

- 바꿔주는 방법이 숫자, 스트링 뿐만 아니라 객체로도 바꿔줄 수 있어요. 그래서 좀 유용합니다. 다음의 방법인데요. 
    - key(원래 node label), value(바뀔 node label)로 구성된 dictionary를 넘기면 됩니다. 

```python
new_bg = nx.relabel_nodes(bg1,
    {1:AAA(), 2: AAA()}
)
```

## do it

- 다음처럼 합니다. 

```python
import networkx as nx
import matplotlib.pyplot as plt 

## random으로 bipartite graph를 만들어줍니다. 
## degree list를 받아서 각 degree lst를 가지는 node들로 구성해줍니다. 
bg1 = nx.bipartite.havel_hakimi_graph([1, 2, 3, 1, 4], [3, 1,1, 2, 4])

## node로 넣어줄 클래스.
class AAA(object):
    def __init__(self, n):
        self.n = n
    def __repr__(self):
        return "kk{}".format(self.n)

## relabeling
s1, s2 = nx.bipartite.sets(bg1) ## bipartite set으로 쪼개고, 
mapping = {} ## key => 원래 node label, value => 바뀔 node, 객체여도 상관없음
mapping.update({n:AAA(n) for n in s1}), mapping.update({n:AAA(n) for n in s2})

## 아래에서 graph를 relabeling함. 
bg_lst = [bg1, nx.relabel_nodes(bg1, mapping)]
for bg in bg_lst :
    plt.figure(figsize=(12, 5))
    pos = bipartite_layout(bg)
    nx.draw_networkx_nodes(bg, pos = pos, node_size=1000)
    nx.draw_networkx_labels(bg, pos = pos)
    nx.draw_networkx_edges(bg, pos = pos)
    plt.axis('off'), 
    plt.title("label with integer" if bg==bg1 else 'label with object')
    plt.savefig('../../assets/images/markdown_img/180811_graph_relabel_{}.svg'.format(
        "label with integer" if bg==bg1 else 'label with object'))
    plt.show()
```

- 원래 graph는 다음과 같고요 

![](180811_graph_relabel_label with integer.svg)

- 바뀐 것은 다음과 같습니다. 하하 사실 별 차이 없는 것처럼 그림상에서는 보일 수 있는데 매우 큰 차이가 있습니다. 

![](180811_graph_relabel_label with object.svg)

## wrap-up

- 생각보다 이 방법이 매우 유용합니다. 경우에 따라서, 랜덤하게 그래프를 구성해서 테스트를 해볼 일들이 많이 있는데, 이전에는 일단 complete graph를 만든 다음 edge를 임의로 잘라나가면서 진행했거든요.
- 이제는 그냥 원하는 node의 크기를 가진 그래프를 만든 다음에, node들을 다 바꿔주면 됩니다. 