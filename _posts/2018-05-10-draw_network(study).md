---
title: network를 이쁘기 위해서 공부를 합니다. 
category: python-lib
tags: python python-lib networkx matplotlib

---

## 사실 해보니까 매우 간단하네요. 

- 예전에도 이걸 정리를 해뒀던 것 같은데, 매번 여기저기 둬서 없어졌습니다. 
- 괜히 node size, edge width를 weight에 따라서 알아서 조절하려고 하지 말고, 그냥 cmap을 이용해서 간단하게 하는 편이 훨씬 좋은 것 같습니다. 

## simple graph 

- 테스트를 해보기 위해서 간단하게 `complete graph`를 만들고 그 네트워크에서 너무 작은 weight를 가지고 있는 edge는 모두 삭제했습니다.

```python
import numpy as np 
g = nx.complete_graph(15)
G = nx.Graph()
G.add_nodes_from([("node{}".format(n[0]), {'weight':np.random.randint(1, 100)}) for n in g.nodes(data=True)])
G.add_edges_from(
    ("node{}".format(e[0]), "node{}".format(e[1]), {'weight':np.random.randint(1, 100)}) for e in g.edges(data=True)
)
removed_edges = filter(lambda e: True if e[2]['weight'] > 20 else False, G.edges(data=True))
G.remove_edges_from(list(map(lambda e: (e[0], e[1]), removed_edges)))
```

## draw just one network 

- node, edge, label(node label)을 모두 각각 그려주는 것이 좋다. 눈으로 봤을 때 무엇을 그리는 지 각각 구분되기도 하고. 
- layout을 고정하고 이후에 계속 같은 layout을 넘겨주는데, 키워드 분석에서는 circular가 괜찮은 것 같다. 무엇보다 키워드 이름이 겹치지 않아서 깔끔하게 보임. 
- 크기를 조절해서 weight를 보여주지는 않고, cmap으로 weight를 볼 수 있게 해두었습니다. 
    - 이후에 node의 attr name, edge의 attr name를 argument로 받아서 이에 따라서 weight를 다르게 표시해줄 수 있을 것 같습니다. 
    - 이렇게 하면 node의 내부에 centrality 값을 저장해 두고, 필요에 따라서 색을 다르게 할 수 있으니까요.

![](/assets/images/markdown_img/draw_better_1805101529.svg)

```python
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

def draw_whole_graph(inputG, outPicFile):
    plt.figure(figsize=(16, 8))
    plt.margins(x=0.1, y=0.02)
    # 아래 layout 중에서 마음에 드는 것을 쓰면 됩니다. 
    pos = nx.spring_layout(G)
    pos = graphviz_layout(G, prog='twopi', args='')
    pos = nx.circular_layout(G)

    nx.draw_networkx_nodes(
        G, pos, node_color=[n[1]['weight'] for n in G.nodes(data=True)], node_shape='h',
        node_size=3000, cmap=plt.cm.Blues, alpha=0.9
                      )
    nx.draw_networkx_edges(
        G, pos, edge_color=[e[2]['weight'] for e in G.edges(data=True)],
        width=5, edge_cmap=plt.cm.Greys, style='dashed'
    )
    nx.draw_networkx_labels(
        G, pos, font_family='sans-serif', font_color='black', font_size=10, font_weight='bold'
    )
    plt.axis('off')
    #plt.show()
    plt.savefig('../../assets/images/markdown_img/'+outPicFile)

draw_whole_graph(G, 'draw_better_1805101529.svg')
```

## draw sequential network 

- 키워드 분석 시에는 연도별로 키워드 네트워크를 구분해서 보는 것이 필요할 때가 있다. 이럴 때를 위해서, `graph list`를 input으로 받아서, 연속으로 그림을 그리는 코드를 만들었다. 
- 여기서 문제라면, `figsize()`를 고정해두었다는 것인데, 그려야 하는 그래프의 수가 적을 때(대략 6개 이하)에서는 문제가 안되지만, 많아지면 그림이 예쁘게 안 그려질 수 있다. 그런데 이걸 하나하나 바꾸는 건 약간 무의미한 짓인 것 같고, 필요할때 바꾸는게 더 좋을 것 같음. 

![](/assets/images/markdown_img/draw_better_1805101611.svg)

```python
import matplotlib.pyplot as plt
import networkx as nx

def draw_G_lst(G_lst, outPicName):# 4개라고 생각하자 우선 
    plt.close('all')
    plt.figure(figsize=(25, 5))
    """
    make node position 
    """
    pos = nx.circular(nx.compose_all(G_lst))# 이렇게 하면 모든 그래프를 하나로 합칠 수 있음
    for i in range(0, len(G_lst)):
        this_subp = plt.subplot("{}{}{}".format(1, len(G_lst), i))
        this_subp.margins(x=0.1, y=0.1)
        nx.draw_networkx_nodes(G_lst[i], pos, node_color='Red', node_shape='h', node_size=2000)
        nx.draw_networkx_edges(G_lst[i], pos, width=10, 
                                edge_color=[e[2]['weight'] for e in G_lst[i].edges(data=True)],
                                edge_cmap=plt.cm.Greys, style='dashed')
        nx.draw_networkx_labels(G_lst[i], pos, 
                                font_family='sans-serif', font_color='black', font_size=12, font_weight='normal')
        plt.axis('off')
    #plt.savefig('../../assets/images/markdown_img/'+outPicName)
    plt.show()
g_lst = [new_complete_g(4) for i in range(0, 5)]
draw_G_lst(g_lst, 'test_draw_graph_lst_1805101611.svg')
```


## reference

- [networkx documentation](https://networkx.github.io/documentation/latest/auto_examples/basic/plot_read_write.html)


## conda install pydot

- layout 중에 괜찮은 것들은 pygraphviz에 많이 있는 것 같더라고요. 그래서 일단 pydot을 설치했습니다. 아마 이번 말고, `pydot`의 경우는 다음에 제가 좀 더 정리하는 게 좋을 것 같습니다. 