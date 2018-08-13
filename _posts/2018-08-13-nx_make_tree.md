---
title: networkx로 random tree 만들기 
category: python-lib
tags: python python-lib tree networkx random partition
---

## random tree 만들기 

- random tree를 만들거에요. tree라는 것은 parent, children를 가지는 스트럭쳐죠. 저는 parent, children로 node를 접근하는 건 만들지 않았습니다만, random 하게 tree를 만들어주는 알고리즘을 만들고 싶었어요. 

- 아래처럼 node_size를 입력받고, 몇 층의 tree를 만들 것인지를 입력하면, 적합한 tree를 `nx.Graph()`로 만들어 리턴하는 함수를 만듭니다. 

```python
def make_random_tree(node_size, level=3):
    pass
```

## random integer and list partition 

- 예를 들어서, 총 10개짜리 node가 포함되어 있고, level이 3인 graph를 만든다고 할 경우, 가능한 graph는 아주 많죠.
- 이를 위해서는 10개의 node가 층별로 몇 개씩 배치되어야 하는지를 정해야 합니다. 
- 10을 3개의 그룹으로 어떻게 쪼갤 수 있는가, 즉 integer-partition 문제가 됩니다. 
- integer partition도 만들고, list를 정해진 split_size에 맞춰서 쪼개주는 함수도 만들었습니다. 

```python
def partition(number):
    ## number로 나눌 수 있는 모든 파티션 종류를 리턴
    answer = set()
    ## 일단 현재 number도 partition 중 하나 이므로 tuple로 넘겨주고 
    answer.add((number, ))
    ## binary partition: increase x and partition y 
    for x in range(1, number):
        for y in partition(number - x):## new partition of x 
            answer.add(tuple(sorted((x, ) + y)))## like this
    return answer

def list_partition(input_lst, split_size):
    ## input_lst를 split_size에 맞춰서 쪼개서 리턴해줌
    ## [1,2,3,4,5], [2, 2, 1] ==> [[1,2], [3, 4], 5]
    if sum(split_size)==len(input_lst):
        r_lst = [input_lst[sum(split_size[:i-1]):sum(split_size[:i])] for i in range(1, len(split_size)+1)]
        return r_lst
    else:
        print('sum(split_size)!=len(input_lst)')
        return None


```

## make random tree

- 이제 node_size와 level을 입력하면 알아서 랜덤하게 층별 노의 수와 각 노드의 자식의 수까지 알아서 잘 나눠서 아래 `make_random_tree`에서 그래프를 만들어서 리턴해줍니다. 
- 또한 tree를 예쁘게 보여주기 위해서 `tree_position`라는 노드의 포지션을 만들어주는 함수도 정의하였습니다. 

```python
def make_random_tree(node_size, level=3):
    ## node set으로부터 random하게 tree를 만듬 
    rG = nx.Graph()
    ## 각 레벨별로 몇 명의 node가 있을지 정하고 
    ps = [p for p in partition(node_size-1) if len(p)==level-1]
    selected_p = ps[np.random.randint(0, len(ps))]
    rG.add_node('l0_u1', level=0) ## 탑노드 
    for level, children_size in enumerate(selected_p):
        level = level+1
        parent_node_set = [ n[0] for n in rG.node(data=True) if n[1]['level'] == level-1]
        children_node_set = [('l{}_u{}'.format(level, i), {'level':level}) for i in range(0, children_size)]
        rG.add_nodes_from(children_node_set)
        ## children_node_set을 parent_node_set에 맞춰 나누어야 함 
        children_ps = [p for p in partition(len(children_node_set)) if len(p)==len(parent_node_set)]
        children_ps = children_ps[np.random.randint(0, len(children_ps))]
        children_ps = list_partition(children_node_set, children_ps)
        for j, par_n in enumerate(parent_node_set):
            rG.add_star([par_n]+[ c[0] for c in children_ps[j]])
    return rG

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

## do it

- 이제 아래처럼 코드를 실행하면 알아서 tree를 만들어줍니다.

```python
np.random.seed(30)
g = make_random_tree(12, level=4)

plt.figure(figsize=(12, 4))
nx.draw_networkx(g, pos=tree_position(g), node_size=1000)
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/180813_random_tree.svg')
plt.show()
```

![](/assets/images/markdown_img/180813_random_tree.svg)

## raw code 

```python
## networkx로 tree를 만드려고 하는데, 몇 가지 유용한 것들이 좀 

def partition(number):
    ## number로 나눌 수 있는 모든 파티션 종류를 리턴
    answer = set()
    ## 일단 현재 number도 partition 중 하나 이므로 tuple로 넘겨주고 
    answer.add((number, ))
    ## binary partition: increase x and partition y 
    for x in range(1, number):
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

def make_random_tree(node_size, level=3):
    ## node set으로부터 random하게 tree를 만듬 
    rG = nx.Graph()
    ## 각 레벨별로 몇 명의 node가 있을지 정하고 
    ps = [p for p in partition(node_size-1) if len(p)==level-1]
    selected_p = ps[np.random.randint(0, len(ps))]
    rG.add_node('l0_u1', level=0) ## 탑노드 
    for level, children_size in enumerate(selected_p):
        level = level+1
        parent_node_set = [ n[0] for n in rG.node(data=True) if n[1]['level'] == level-1]
        children_node_set = [('l{}_u{}'.format(level, i), {'level':level}) for i in range(0, children_size)]
        rG.add_nodes_from(children_node_set)
        ## children_node_set을 parent_node_set에 맞춰 나누어야 함 
        children_ps = [p for p in partition(len(children_node_set)) if len(p)==len(parent_node_set)]
        children_ps = children_ps[np.random.randint(0, len(children_ps))]
        children_ps = list_partition(children_node_set, children_ps)
        for j, par_n in enumerate(parent_node_set):
            rG.add_star([par_n]+[ c[0] for c in children_ps[j]])
    return rG

def tree_position(inputG):
    ## tree 구조인 graph의 포지션을 만들어줌
    pos_dict = {}
    levels = {n[1]['level'] for n in inputG.nodes(data=True)}
    for i, l in enumerate(range(min(levels), max(levels)+1)):
        nodes = [n for n in inputG.nodes(data=True) if n[1]['level']==l]
        y = 1.0 - (1.0/(len(levels)+1)*(i+1))
        pos_dict.update({n[0]:(1.0/(len(nodes)+1)*(j+1), y) for j, n in enumerate(nodes)})
    return pos_dict
    
    ## add edge

np.random.seed(30)
g = make_random_tree(12, level=4)

plt.figure(figsize=(12, 4))
nx.draw_networkx(g, pos=tree_position(g), node_size=1000)
plt.axis('off')
plt.savefig('../../assets/images/markdown_img/180813_random_tree.svg')
plt.show()
```