---
title: networkx - binary operator
category: python-libs
tags: python python-libs networkx graph-operator 
---

## 1-line summary 

- graph binary operator, 즉, 그래프에 대한 덧셈 뺄셉을 정리했습니다. 사실, 집합 개념과 동일해요.

## graph binary operator 

- Graph에 대해서 적용할 수 있는 operator들, 즉, 덧셈 뺄셈을 정리하였습니다.
- 사실 기본적인 set operation과 다른 것이 없어요. 
    - `compose`, `union`: '합집합'
    - `intersection`: '교집합'
    - `difference`: '차집합'
    - `symmetric_difference`: '차집합 합'
- 매우 간단한데, [nx.algorithms.operators](https://networkx.github.io/documentation/stable/reference/algorithms/operators.html)에는 추가로 조금은 미묘한 `disjoint_union`, `union`등이 있습니다. 이는, graph `G`, `H`가 각각 있고 이 두 graph에 동일한 id를 가진 node가 있다고 할때, 이들을 같다고 볼 것인가, 다르다고 볼 것인가(disjoint), 에서 기인하죠. 
- 아무튼 별 차이는 없고, 저라면 그냥 `nx.relabel`을 한 다음에, 적용하는 것이 훨씬 이롭죠.

## python implementation 

### compose

- graph G, H를 그대로 합친다고 생각하며 됩니다. 두 그래프에 이름이 같은 노드가 있다면, 같은 노드라고 인식하고 edge들도 병합됩니다

```python
#-----------------------------------
# nx.compose
# graph G, H를 그대로 합친다고 생각하면 됨.
# 따라서, node가 같은 경우가 있다면 그냥 그대로 병합함
# 그러나, nx.union의 경우 이름이 같은 node가 있다면 에러 발생.
#-----------------------------------
def compose(G, H):
    """
    - just for nx.Graph()
    compose: 
    - 그냥 두 graph, G, H를 모두 합친것이라고 생각해도 됨.
    """
    GH = G.copy()
    H_nodes = [n for n in H]
    H_edges = [e for e in H.edges()]
    # add H nodes and edges
    GH.add_nodes_from(H_nodes)
    GH.add_edges_from(H_edges)
    return GH
```

### union 

- union의 경우는 compose와 다르게, graph G, H의 node들이 동일하지 않다고 가정합니다. 즉, 항상 disjoint하다는 것이죠. 
- 따라서, node의 이름에 label을 다르게 붙여서, `rename=("G_", "H_")` 이름 앞에 prefix를 붙여준다고 생각하시면 됩니다.

```python
#-----------------------------------
# nx.union
# union의 경우는 G, H의 node이름이 동일해서는 안됨
# (정확하게는 Graph가 서로 disjoin여야 한다는 말임)
# nx.compose의 경우 node가 같을 경우 그냥 같은 노드로 인식하는데,
# nx.union은 이를 막기 위해서 존재한다고 보면 됨.
#-----------------------------------
def union(G, H, rename=("G_", "H_")):
    """
    - 본 코드에서는 G, H의 다름을 보장하기 위해서, 항상, 앞에 prefix를 넣어줌. 
    - nx.union에서는 rename의 default값이 None이며 없을 경우, error를 발생시킴.
    - 즉, node 이름을 다르게 세팅하여, G, H 가 disjoint일 경우 compose와 동일함.
    """
    G_prefix, H_prefix = rename
    G_relabeled = nx.relabel_nodes(G, {n: G_prefix+str(n) for n in G})
    H_relabeled = nx.relabel_nodes(H, {n: H_prefix+str(n) for n in H})
    return nx.compose(G_relabeled, H_relabeled)
```

### disjoint_union 

- 사실, union과 별 차이가 없는 것 같습니다. 그냥 union으로 합치고, relabel을 사용해서 node의 이름을 순서대로 붙여주면 동일한 결과가 나와요.

```python
#-----------------------------------
# nx.disjoint_union
# 사실상, rename을 argument로 넘겨준 경우, nx.union과 차이가 없다고 봐도 됩니다.
# 다만, 이 아이는 처음부터, 다르게 넘어온다는 것을 인정하고,
# 끝에 모든 노드를 동일 선상에서 보고, node_id가 0부터 순차적으로 올라간다는 것이 다르죠.
#-----------------------------------
def disjoint_union(G, H):
    """
    G, H의 node를 모두 integer id로 변형하고, 
    nx.union으로 합침.
    즉, 만약 len(G)가 10이고, len(H)가 5라면, 
    G node id: range(0, 10)
    H node id: range(10, 10+5)
    """
    G_new_relabel = {n:i for i, n in enumerate(G)}
    G_relabeled = nx.relabel_nodes(G.copy(), G_new_relabel)
    H_new_relabel = {}
    for i, n in enumerate(H):
        # G_cp에서 가장 큰 node_id부터 순차적으로 증가.
        H_new_relabel[n] = i + len(G_relabeled)
    H_relabeled = nx.relabel_nodes(H.copy(), H_new_relabel)
    return nx.union(G_relabeled, H_relabeled)
```

### intersection 

- G, H에 동일하게 존재하는 edge를 리턴합니다. 
- 단, G, H, intersection(G, H)의 node set은 동일하게 관리합니다. 
- 이는, 모든 operation에서 동일한데, 덧셈 뺄셈이 가능한 기본적인 환경을 동일하게 관리하는 것이죠.

```python
#-----------------------------------
# intersection
# G, H에서 동일하게 존재하는 edge를 리턴함.
# G, H의 node set는 동일하다는 것을 가정함.
# R = intersection(G, H) 일 때,
# 보통, G, H, R 모두 node set를 동일하게 설정함.
#-----------------------------------
def intersection(G, H):
    """
    R: intersection(G, H)의 결과 graph 
    R, G, H의 node set는 동일함. 
    즉, isolate가 존재하더라도, 제거하지 않고 남김. 
    """
    if H.number_of_edges() < G.number_of_edges():
        # H의 edge가 G의 edge의 수보다 작을 경우 swap
        G, H = H, G
    # not_both_edges: G의 edge중에서, H에 존재하지 않는 edge
    not_both_edges = []
    for u, v in G.edges():
        if not H.has_edge(u, v):
            not_both_edges.append((u, v))
    R = G.copy()
    R.remove_edges_from(not_both_edges)
    return R
```


### difference

- 차집합입니다. 이 경우에도, node set는 동일하게 관리됩니다.

```python
def difference(G, H):
    """
    G에서 H에 존재하는 edge를 뺌. 
    즉, intersection(G, H)에 존재하는 edge를 뺀다고 생각하면 됨.
    """
    R = G.copy()
    intersection_edges = [e for e in nx.intersection(G, H).edges()]
    R.remove_edges_from(intersection_edges)
    return R
```

### symmetric difference

- 차집합 합입니다. 

```python
def symmetric_difference(G, H):
    """
    G, H에 각각 존재하나, 모두 존재하지는 않는 graph
    - compose(G, H) - intersection(G, H)
    - or, difference(G, H) + difference(H, G)
    """
    G_diff_H = nx.difference(G, H)
    H_diff_G = nx.difference(H, G)
    return nx.compose(G_diff_H, H_diff_G)
```

## wrap-up

- 사실 매우 간단한 코드고 이해하기도 쉽습니다. 단, node set을 동일하게 관리한다는 것이 조금 의미가 있네요. 
- graph에 대한 어떤 high-level interface라고 생각하면 될 것 같습니다. 어떤 edge를 빼고 더하고 라는 말보다는 `difference` 등으로 이해하면 조금 더 높은 레벨에서 이해할 수 있죠.

## reference

- [nx.algorithms.operators](https://networkx.github.io/documentation/stable/reference/algorithms/operators.html)