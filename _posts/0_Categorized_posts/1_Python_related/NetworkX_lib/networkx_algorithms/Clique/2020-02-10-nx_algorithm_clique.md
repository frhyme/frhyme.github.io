---
title: networkx - algorithms - cliques
category: python-libs
tags: python python-libs networkx 
---

## 3 line-summary 

- `networkx`에서 제공하는 clique 관련 함수들을 정리하였습니다. 
- clique는 graph내에 존재하는 complete-subgraph를 말함. 매우 기본적인 graph의 특성이며, 각 노드가 어떤, 그리고 몇 개의 clique에 속하는지를 활용해서 지표를 만들어낼 수도 있음. 
- 또한, 속한 clique를 기준으로 clique-graph를 만들어서 보다 의미있는 관계를 뽑아내는 것도 가능함. 


## About CLIQUE.

- clique의 경우 사실, 수학자나 물리학자들에게는 마치 fractal처럼 구조적인 의미를 연쇄적으로 파악할 수 있을지 모르지만, 저 같은 해석 중심의 연구를 하는 사람에게는 상대적으로 그 중요도가 떨어지기는 합니다. 
- 다만, 그래도 bioinformatics 분야에서는 clique를 이용하여, gene expression, evoltionary tree, protein structure 등을 모델링하는 일이 많고, electrical engineering 분야에서는 communication network를 분석하기 위해 clique를 쓴거나, 효과적인 circuit을 설계하기 위해서, clique를 만들고, 혹은 "clique"를 기본 단위로 자동으로 패턴(or 그래프, 회로)를 생성하는 방법을 통해, fault-robustness를 측정하기 위한 null model로 사용하기도 하죠. 또한, 화학 분야에서는 structure간의 유사성을 파악하기 위해 clique를 고려한 지표를 만들거나, 혹은 clique를 이용하여 새로운 protetin 모델을 만들기 위해서 사용하기도 하구요. 
- 즉, 보통은 그냥 clustering이나, community detection 방법을 많이 쓰게 되지만, clique는 가장 기본적인 그래프의 특성을 말합니다. 또한 node들이 얼마나 많은 clique에 속하는지, 어떤 clique에 속하는지를 중심으로 centrality와 같은 다양한 지표들을 만들어볼 수도 있죠. 
- 다만, clique, 그리고 maximal_clique를 만드는데는 많은 시간이 소요됩니다. 따라서, 한번 clique를 뽑아내었다면 다음부터 다른 함수에도 이를 그대로 넘겨줘서, 시간을 줄이는 것이 필요하죠. 

## Extract Clique. 

- `networkx`에 있는 clique 함수를 사용하고 그 결과를 정리하였습니다. 그외에, 특정 `node`를 중심으로 "노드가 속한 클리크만 리턴", "노드가 속한 클리크의 수 리턴"등의 함수들이 있으나, 중복되는 내용이라서 따로 정리하지는 않았어요. 

```python
import networkx as nx
import matplotlib.pyplot as plt

# Generate graph
N = 10
G = nx.scale_free_graph(N, seed=0)
G = nx.Graph(G)
#================================================
# nx.enumerate_all_cliques(G):
# 그냥, 존재하는 모든 clique를 리턴함.
# generator를 리턴하는데, list(nx.enumerate_all_cliques(G))로 생각없이 변환할 경우 메모리 터질 수 있음.
print("== nx.enumerate_all_cliques(G)")
clique_num = 0
for clique in nx.enumerate_all_cliques(G):
    # clique type: list
    clique_num+=1
print(f"all cliques count: {clique_num}")
print("=="*30)
#================================================
# nx.enumerate_all_cliques(G):
# maximal_clique, 각 clique를 포함해서 만들 수 있는 쵀대 크기의 clique를 리턴
print("== nx.find_cliques(G), maximal_clqiues")
for maximal_clique in nx.find_cliques(G):
    if len(maximal_clique)>=2:# 크기가 2개짜리(즉 그냥 edge)도 clique이므로 이 아이들은 출력하지 않음.
        print(maximal_clique)
print("=="*30)
#================================================
print("== nx.make_clique_bipartite(G)")
# networkx.algorithms.clique.make_clique_bipartite(G)
# node attr: 'bipartite'가 1인 아이들은 node를 말하고, 0인 아이들은 clique를 말함.
# 즉, 0인 가상의 동일한 노드에 연결된 아이들은 모두 서로 clique라는 것을 말함.
# nx.find_cliques(G)와 의미적으로 동일함.
CliqueBiG = nx.make_clique_bipartite(G)
for n, n_attr in CliqueBiG.nodes(data=True):
    if n_attr['bipartite']==0:
        # clique를 의미하는 가상의 노드
        # bipartite가 0인 노드들의 이웃 노드들은 각각 clique가 됨.
        print(f"clique_{abs(n):2d} :: {list(CliqueBiG[n])}")
print("==" * 30)
#================================================
# networkx.algorithms.clique.make_max_clique_graph
# clique를 기본 노드로 하는 graph를 새롭게 만들어냄
print("== nx.make_max_clique_graph(G)")
# 의미적으로는 다음과 같음.
def custom_cliqueG(inputG):
    # node -- clique bipartitie graph
    CliqBiG = nx.make_clique_bipartite(inputG)
    # clique를 의미하는 node set
    clique_node_set = [n for n, n_attr in CliqBiG.nodes(data=True) if n_attr['bipartite']==0]
    # clique만 날리도록 projection
    CliqG = nx.bipartite.project(CliqBiG, clique_node_set)
    # clique남 남김
    return CliqG
assert nx.is_isomorphic(custom_cliqueG(G), nx.make_max_clique_graph(G))
print("Assertion complete")
print("==" * 30)
#================================================
# networkx.algorithms.clique.graph_clique_number
# graph의 clique number는 해당 graph에 존재하는 가장 큰 clique의 크기.
print(f"== nx.graph_clique_number(G): {nx.graph_clique_number(G)}")
def custom_graph_clique_number(G):
    max_graph_clique_number = 0
    for maximal_clique in nx.find_cliques(G):
        l = len(maximal_clique)
        if max_graph_clique_number <= l:
            max_graph_clique_number=l
    return max_graph_clique_number
assert custom_graph_clique_number(G)==nx.graph_clique_number(G)
print("Assertion complete")
print("==" * 30)
#================================================
# networkx.algorithms.clique.graph_number_of_cliques
# graph에서 maximal clique의 크기를 리턴하는 함수
print(f"== nx.graph_number_of_cliques(G): {nx.graph_number_of_cliques(G)}")

def custom_graph_number_of_clique(G):
    max_graph_clique_number = 0
    for maximal_clique in nx.find_cliques(G):
        max_graph_clique_number+=1
    return max_graph_clique_number

assert custom_graph_number_of_clique(G) == nx.graph_number_of_cliques(G)
print("Assertion complete")
print("==" * 30)
```

- 결과는 다음과 같습니다.

```
== nx.enumerate_all_cliques(G)
all cliques count: 32
============================================================
== nx.find_cliques(G), maximal_clqiues
[1, 8]
[1, 2, 0, 5]
[1, 2, 3]
[1, 2, 6]
[4, 2]
[9, 7]
[7, 5]
[7, 6]
============================================================
== nx.make_clique_bipartite(G)
clique_ 1 :: [1, 8]
clique_ 2 :: [1, 2, 0, 5]
clique_ 3 :: [1, 2, 3]
clique_ 4 :: [1, 2, 6]
clique_ 5 :: [4, 2]
clique_ 6 :: [9, 7]
clique_ 7 :: [7, 5]
clique_ 8 :: [7, 6]
============================================================
== nx.make_max_clique_graph(G)
Assertion complete
============================================================
== nx.graph_clique_number(G): 4
Assertion complete
============================================================
== nx.graph_number_of_cliques(G): 8
Assertion complete
============================================================
```

## reference 
- [networkx - algorithms - clique](https://networkx.github.io/documentation/stable/reference/algorithms/clique.html)