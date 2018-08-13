---
title: DiGraph를 arrow로 그립시다. 
category: python-lib
tags: python python-lib networkx matplotlib arrow digraph
---

## DiGraph

- DiGraph는 방향성이 있는 네트워크를 말합니다. 일반적인 graph라면 edge를 그냥 그리면 되는데, 방향성이 있는 graph는 화살표를 잘 그려줘야 합니다. 
- [arrow style](https://matplotlib.org/api/_as_gen/matplotlib.patches.ArrowStyle.html)은 여기에 볼 수 있는데, 각각 어떻게 나오는지 정리해서 보여드립니다.

## arrow style 

- 그냥 `nx.draw_networkx_edges`에 `arrowstyle`의 값을 넘겨주면 됩니다. 

```python
nx.draw_networkx_edges(DG, pos=pos, width=3, 
                           arrowstyle=arrow_style, arrowsize=20, ax=ax)
```

- 꽤 다양한 종류의 arrow_style이 있는데, 아래 그림을 보시면서 이해하는 것이 더 빠를거에용. 

```python
arrow_style_lst = ['-', '->', '-[', '-|>', '<-', '<->', '<|-',
                   '<|-|>', ']-', ']-[', 'fancy', 'simple', 'wedge', '|-|']
f, axes = plt.subplots(7, 2)
f.set_size_inches((12, 16))
for i, arrow_style in enumerate(arrow_style_lst):
    ax = axes[i//2][i%2]
    DG = nx.DiGraph()
    DG.add_nodes_from([ ("A{:0>2d}".format(i)) for i in range(0, 5)])
    DG.add_edges_from([ ("A{:0>2d}".format(i), "A{:0>2d}".format(i+1)) for i in range(0, 4) ] )
    pos = { n: (1.0/len(DG.nodes())*i, 0.5) for i, n in enumerate(DG.nodes())}
    nx.draw_networkx_nodes(DG, pos=pos, node_size=500, node_color='blue', ax=ax)
    nx.draw_networkx_edges(DG, pos=pos, width=3, 
                           arrowstyle=arrow_style, arrowsize=20, ax=ax)
    ax.set_title('arrow: {}'.format(arrow_style_lst[i]), fontsize=15), 
    ax.set_axis_off()
plt.tight_layout()
plt.savefig('../../assets/images/markdown_img/180813_arrow_style_comp.svg')
plt.show()
```

![](/assets/images/markdown_img/180813_arrow_style_comp.svg)


## wrap-up

- 제 생각에는 그냥 `->`이나 `simple`이 제일 좋은 것 같습니다. 


## reference 

- <https://matplotlib.org/api/_as_gen/matplotlib.patches.ArrowStyle.html>