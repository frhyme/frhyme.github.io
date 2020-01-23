---
title: networkx graph tree 구조 예쁘게 그리기 
category: python-lib
tags: python python-lib networkx tree matplotlib layout graphviz 
---

## tree에 적합한 layout을 찾습니다. 

- networkx에는 다양한 layout이 있습니다만, tree 구조에 적합한 레이아웃은 없어요(정확히는 없다고 생각했습니다). 그런데 사실 없다는게, 제 입장에서는 말이 안되서 한참 찾았는데, 찾다보니 있습니다 하핫. 조금 부족한 부분이 있지만 이정도면 충분한 것 같아요. 

## make random tree

- 우선은 random하게 tree를 만들어주는 함수를 정의합니다. 

```python
import networkx as nx 
import numpy as np 
import matplotlib.pyplot as plt 

def partition(number):
    ## number로 나눌 수 있는 모든 파티션 종류를 리턴
    answer = set() ## 일단 현재 number도 partition 중 하나 이므로 tuple로 넘겨주고 
    answer.add((number, )) 
    for x in range(1, number):## binary partition: increase x and partition y 
        for y in partition(number - x):## new partition of x 
            answer.add(tuple(sorted((x, ) + y)))## like this
    return answer

def list_partition(input_lst, split_size):
    if sum(split_size)==len(input_lst):
        r_lst = [input_lst[sum(split_size[:i-1]):sum(split_size[:i])] for i in range(1, len(split_size)+1)]
        return r_lst
    else:
        print('sum(split_size)!=len(input_lst)')
        return None

def make_random_tree(node_set, level=3):
    ## node set으로부터 random하게 tree를 만듬 
    rG = nx.Graph()    
    ## 만약 시간이 오래 걸린다면, partition에서 시간이 많이 소요되는 것임. 
    ## 각 레벨별로 몇 명의 node가 있을지 정하고 
    level_node_size = [1 for i in range(1, level)]
    for i in range(0, len(node_set)-level):
        level_node_size[np.random.randint(0, len(level_node_size))]+=1
    level_node_size = sorted(level_node_size)
    rG.add_node('l0_u1', level=0) ## 탑노드 
    for each_level, children_size in enumerate(level_node_size):
        each_level = each_level+1
        parent_node_set = [ n[0] for n in rG.node(data=True) if n[1]['level'] == each_level-1]
        children_node_set = [('l{}_u{}'.format(each_level, i), {'level':each_level}) for i in range(0, children_size)]
        rG.add_nodes_from(children_node_set)
        ## children_node_set을 parent_node_set에 맞춰 나누어야 함 
        children_ps = [p for p in partition(len(children_node_set)) if len(p)==len(parent_node_set)]
        children_ps = children_ps[np.random.randint(0, len(children_ps))]
        children_ps = list_partition(children_node_set, children_ps)
        for j, par_n in enumerate(parent_node_set):
            rG.add_star([par_n]+[ c[0] for c in children_ps[j]])
    ## relabel 
    new_node_label = np.random.choice(node_set, len(node_set), replace=False)
    return nx.relabel_nodes(rG, {n: new_n for n, new_n in zip(rG.nodes(), new_node_label)})

def tree_position(inputG):
    ## tree 구조인 graph의 포지션을 만들어줌
    pos_dict = {}
    levels = {n[1]['level'] for n in inputG.nodes(data=True)}
    for i, l in enumerate(range(min(levels), max(levels)+1)):
        nodes = [n for n in inputG.nodes(data=True) if n[1]['level']==l]
        y = 1.0 - (1.0/(len(levels)+1)*(i+1))
        pos_dict.update({n[0]:(1.0/(len(nodes)+1)*(j+1), y) for j, n in enumerate(nodes)})
    return pos_dict
```

- 그리고 아래처럼 그림을 그려줍니다. 
- 제가 임의로 만들어준 `tree_position`이라는 레이아웃을 사용했는데, 별로 마음에 들지 않네요 흠. 

```python
np.random.seed(1111)
g = make_random_tree(["n{:0>2d}".format(i) for i in range(0, 20)], level=3)
plt.figure(figsize=(12, 5))
nx.draw_networkx(g, tree_position(g))
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/180820_tree_layout_default.svg')
plt.show()
```

![](/assets/images/markdown_img/180820_tree_layout_default.svg)



- 아래처럼 방사형으로 그려주는 방식도 있구요 

```python
# top_node는 정해져야 함. 이게 정해지지 않을 경우에는 같은 tree라도 다르게 보일 수 있음 
## graphviz layout을 사용하는게 더 좋을 것 같은데 흠. 
plt.figure(figsize=(12, 6))
nx.draw_networkx(g, pos=nx.drawing.nx_agraph.pygraphviz_layout(g))
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/180820_tree_layout_pygraphviz_layout.svg')
plt.show()
```

![](/assets/images/markdown_img/180820_tree_layout_pygraphviz_layout.svg)

- 하지만 아래 방식이 제일 마음에 드네요. 

```python
plt.figure(figsize=(15, 5))
nx.draw_networkx(g, pos=nx.drawing.nx_agraph.graphviz_layout(g, prog='dot'))
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/180820_tree_layout_graphviz_layout.svg')
plt.show()
```

![](/assets/images/markdown_img/180820_tree_layout_graphviz_layout.svg)

## wrap-up

- 찾아보니까, graph에 대해서 적절한 layout을 찾아주는 것도 알고리즘으로 어느 정도 연구되고 있는 분야더라구요. 
- 아무튼, 저는 직접 코딩하는 건 귀찮아서 위처럼 만들어서 처리했습니다 하하핫
- 또한 igraph라는 라이브러리가 있던데, 얘를 사용하면 몇 가지를 좀 더 편하게 할 수 있지 않을까? 싶어요. 
- 그리고 허탈하지만, networkx에 이미 random하게 tree를 만들어주는 함수가 있네요 

```python
g = nx.generators.trees.random_tree(10, 42)
```