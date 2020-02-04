---
title: Definitions of walk, trail, path, cycle, circuit
category: python-libs
tags: python python-libs networkx 
---

## Definitions of walk, trail, path, cycle, circuit

- `walk`: "Node, edge가 반복되어도 상관없으며, graph에서 발생할 수 있는 
    - `Closed Walk`: walk중에서 source와 target이 같은 경우. 
    - `Open Walk`: walk 중에서 source와 target이 다른 경우. 
- `trail`: "edge가 반복되지 않는" walk
- `path`: source와 target이 다른(open) edge가 반복되지 않는 walk(trail)
- `cycle`: source와 target이 같은(closed), 그리고 어떤 node도 반복되지 않는 trail
- `circuit`: source와 target이 같은(closed), 그러나, edge만 반복되지 않아야 하고, node는 반복되어도 되는 trail


## find them from G using `Networkx`

- `networkx`를 사용해서 Graph로부터 에서 각 요소들을 뽑아보겠습니다. 

```python
# walk: node와 edge가 중복되어도 되므로, 무한하게 발생할 수 있음.

import networkx as nx
import numpy as np

np.random.seed(0)

N = 6  # node size
p = 0.5
G = nx.fast_gnp_random_graph(N, p, seed=0)

########################################
# closed walks: source와 target이 같고, node와 edge가 중복되어도 상관없음.
print("== closed walk")
for w_i in range(0, 5):
    walk = [np.random.randint(0, len(G), 1)[0]]
    while True:
        next_node_candidates = list(G[walk[-1]].keys())
        next_node = np.random.choice(next_node_candidates)
        walk.append(next_node)
        # closed walks
        if walk[0]==walk[-1]:
            break
    print(f"random close walks of Node {walk[0]} ::: {walk}")
print("==" * 20)

########################################
# trail: edge가 반복되면 안되는 walk
# 따라서, 사용한 edge를 딕셔너리에 업데이트시키면서, 더 사용할 수 있는 trail이 없을 경우 뛰쳐나옴
print("== closed trail")
n1, n2 = np.random.randint(0, len(G), 2)
for w_i in range(0, 5):
    walk = [np.random.randint(0, len(G), 1)[0]]
    used_edge_dict = {n: []for n in G}
    while True:
        next_node_candidates = []
        for nbr in G[walk[-1]].keys():
            if nbr not in used_edge_dict[walk[-1]]:
                next_node_candidates.append(nbr)
        if len(next_node_candidates)==0:
            #print("No more edge")
            break
        else:
            next_node = np.random.choice(next_node_candidates)
            walk.append(next_node)
            # 사용된 edge를 update해줌.
            used_edge_dict[walk[-2]].append(walk[-1])
            #print(used_edge_dict)
    print(f"random trail ::: {walk}")
print("==" * 20)
########################################
# path: source와 target이 다른(open) edge가 반복되지 않는 walk(trail)
# materialized된 list가 아니라, generator가 리턴됨.
# source, target을 같게 넣으면, 빈 리스트가 리턴됨.
n1, n2 = np.random.randint(0, len(G), 2)
print(f"== all path from {n1} to {n2}")
for i, path in enumerate(nx.all_simple_paths(G, source=n1, target=n2)):
    print(f"path {i:2d} ::: {path}")
print(('=='*20))

########################################
# cycle: source와 target이 같은(closed), 그리고 어떤 node도 반복되지 않는 trail
# graph 내부의 cycle을 찾는 다른 방법들도 있습니다만, 여기서는
# cycle basic: "minimal collection of cycles such that any cycle in the network can be written as a sum of cycles in the basis. "
# 즉, G의 어떤 cycle도 cycle basis의 합으로 만들 수 있는 cycle만을 리스트로 정리하여 보여줍니다.
G = nx.Graph()
nx.add_cycle(G, [0, 1, 2, 3])
nx.add_cycle(G, [0, 3, 4, 5])
nx.add_cycle(G, [0, 6, 7, 8])
nx.add_cycle(G, [0, 9, 10])
print("== cycle")
for i, cycle in enumerate(nx.cycle_basis(G, root=0)):
    print(f"cycle {i:2d} ::: {cycle}")
########################################

```


```
== closed walk
random close walks of Node 4 ::: [4, 5, 3, 2, 3, 4]
random close walks of Node 3 ::: [3, 4, 3]
random close walks of Node 4 ::: [4, 5, 4]
random close walks of Node 0 ::: [0, 4, 0]
random close walks of Node 2 ::: [2, 3, 5, 4, 0, 5, 3, 4, 1, 2]
========================================
== closed trail
random trail ::: [3, 2, 3, 5, 4, 5, 3, 4, 0, 4, 3]
random trail ::: [0, 5, 3, 5, 4, 0, 4, 3, 4, 5, 0]
random trail ::: [0, 5, 4, 0, 4, 5, 3, 5, 0]
random trail ::: [4, 3, 2, 1, 2, 3, 5, 3, 4, 5, 0, 4, 1, 4, 0, 5, 4]
random trail ::: [4, 1, 2, 1, 4, 0, 5, 3, 4, 5, 4, 3, 2, 3, 5, 0, 4]
========================================
== all path from 3 to 2
path  0 ::: [3, 2]
path  1 ::: [3, 4, 1, 2]
path  2 ::: [3, 5, 0, 4, 1, 2]
path  3 ::: [3, 5, 4, 1, 2]
========================================
== cycle
cycle  0 ::: [9, 10, 0]
cycle  1 ::: [6, 7, 8, 0]
cycle  2 ::: [3, 4, 5, 0]
cycle  3 ::: [1, 2, 3, 0]
```


## wrap-up

- 사실, 다 만들고 나니까, 이걸 굳이 만들 필요가 있었나, 싶기도 합니다. 
- 또한, path, trail등의 개념이 종종 혼재되는 경우가 있는 것 같아요. 다양한 아티클 들에서도 좀 혼동해서 쓰고 있습니다. 
- 다만, closed(source와 target이 같음), open(source와 target이 다름)의 경우는 거의 달라지지 않아요.



## reference

- [walks-trails-paths-cycles-and-circuits](http://mathonline.wikidot.com/walks-trails-paths-cycles-and-circuits)