---
title: networkx의 random tree 만드는 함수 정리 
category: python-lib
tags: python python-lib networkx tree matplotlib random pygraphviz 
---

## random하게 tree를 만듭니다. 

- 예전에 제가 직접 random하게 tree를 만들어주는 코드를 만들었습니다. random하게 각 level별 node의 수를 정하고 children의 수도 랜덤하게 정해서 진행했는데, 생각보다 만드는데 시간이 오래 걸렸습니다. 
- 생각해보니까 이것도 networkx에 tree를 만드는 방법이 있지 않을까? 싶어서 좀 찾아보니 어느 정도 쓸만한게 있더라구요. 

## random tree

- 아래 코드를 이용하면, 랜덤하게 tree를 만들 수 있기는 한데....이걸 tree라고 부를 수 있는지 모르겠네요. tree는 tree인데 저는 좀더 balanced tree를 만들고 싶었거든요. 

```python
g = nx.generators.trees.random_tree(n=20, seed=40)
plt.figure(figsize=(12, 5))
pos = nx.drawing.nx_agraph.graphviz_layout(g, prog='dot')
nx.draw_networkx(g, pos = pos)
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/180820_random_tree.svg')
plt.show()
```

![](/assets/images/markdown_img/180820_random_tree.svg)

## balanced tree

- 단 아래처럼 children의 수와 height를 고정해서 만들 수도 있습니다. 

```python
g1 = nx.balanced_tree(r=4, h=2) # children_node의 개수와 height 
g2 = nx.full_rary_tree(4, 15)
## node의 개수는 1 + r^1 + ... + r^h
f, axes = plt.subplots(2, 1)
f.set_size_inches(12, 8)
nx.draw_networkx(g1, pos=nx.drawing.nx_agraph.graphviz_layout(g1, prog='dot'), ax=axes[0])
nx.draw_networkx(g2, pos=nx.drawing.nx_agraph.graphviz_layout(g2, prog='dot'), ax=axes[1])
axes[0].axis('off'), axes[1].axis('off')
plt.savefig('../../assets/images/markdown_img/180820_balanced_tree.svg')
plt.show()
```

![](/assets/images/markdown_img/180820_balanced_tree.svg)

## random balanced tree

- `nx.balanced_tree`를 활용하여 조금 랜덤성을 추가한 트리를 리턴해주는 그래프를 만듭니다. 
- 지금은 uniform하게 random성을 보장하는데, 좀 더 쏠림현상이 발생하도록 만들 수도 있습니다만, 만들지 않았어요 하하핫

```python
def make_balanced_random_tree(node_size, branching, height):
    ## 최대 branching의 수, height를 정하고, node_size만큼의 tree를 만듭니다. 
    bg = nx.balanced_tree(branching, height-1)
    bg.remove_nodes_from(list(bg.nodes())[node_size:])# 정해진 node의 수를 넘는 노드는 다 삭제 
    level_node = [[0], ]## 레벨별로 들어가야 하는 노드를 리스트로 넣어둠 
    for i in range(0, height-1):
        left, right = sum([branching**j for j in range(0, i+1)]), sum([branching**(j+1) for j in range(0, i+1)])
        level_node.append([k for k in range(left, right+1)])
    ## make it random: 임의로 선을 바꿈 
    for i in range(1, len(level_node)-1):
        for j in range(0, 100):
            edges = [e for e in bg.edges() if e[0] in level_node[i] and e[1] in level_node[i+1]]
            r_e = edges[np.random.randint(0, len(edges))]
            bg.remove_edge(r_e[0], r_e[1]), bg.add_edge(np.random.choice(level_node[i]), r_e[1])
    return bg
np.random.seed(42)
bg = make_balanced_random_tree(30, 5, 3)
pos=nx.drawing.nx_agraph.graphviz_layout(bg, prog='dot')
plt.figure(figsize=(15, 6))
nx.draw_networkx(bg, pos)
plt.savefig('../../assets/images/markdown_img/180820_random_balanced_tree.svg')
plt.show()
```

![](/assets/images/markdown_img/180820_random_balanced_tree.svg)