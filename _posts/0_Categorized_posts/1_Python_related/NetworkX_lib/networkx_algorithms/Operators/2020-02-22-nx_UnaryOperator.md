---
title: networkx - unary operator - complement and reverse
category: python-libs
tags: python python-libs networkx graph-operator complement reverse
---

## 2-line summary 

- graph `G`의 complement `GC`는 "`GC`+`G` = complemet graph"라고 생각하면 됨. 
- Directed graph `G`의 `reverse`는 방향성을 반대로 하는 것을 말함(`(u, v)` ==> `(v, u)`)

## complement of `G`

- graph `G`의 complement는 현재 존재하는 모든 edge를 없애고, 존재하지 않는 edge를 모두 생성하여 만들어지는 graph `G`를 말합니다.
- 즉, 동일한 크기의 complete graph로부터 graph `G`를 뺀, graph를 말하죠. 
- 아래의 코드를 통해, 간단하게 처리하였습니다.

```python
import networkx as nx

def is_exact_same_graph(G1, G2):
    # G1, G2의 node와 edge가 정확하게 같은지를 체크하는 함수.
    g1_nodes = set(G1)
    g2_nodes = set(G2)
    if g1_nodes==g2_nodes:
        g1_diff_g2_edges = nx.difference(G1, G2).edges()
        g2_diff_g1_edges = nx.difference(G2, G1).edges()
        if len(g1_diff_g2_edges) == 0 and len(g2_diff_g1_edges) == 0:
            return True
        else:
            return False
    else:
        return False

n = 20
CompleteG = nx.complete_graph(n=n)

G = nx.wheel_graph(n=n)

# CompleteG에서 G를 뺀 것과,
# nx.complement(G)는 같음.
G1 = nx.difference(CompleteG, G)
G2 = nx.complement(G)

assert is_exact_same_graph(G1, G2)
```

## reverse of `G`

- graph `G`에 대해서 `reverse`를 취한다는 것은 방향성을 반대로 변경한다는 말이 되겠죠. 즉, Digraph에 대해서만 말이 됩니다.
- 코드로 보여줄까 했는데, 너무 간단해서 그냥 넘어가기로 합니다.



## reference

- [networkx - operators](https://networkx.github.io/documentation/stable/reference/algorithms/operators.html)