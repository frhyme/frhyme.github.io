---
title: networkx의 clique를 정리해봅시다.
category: python-libs
tags: networkx python-libs clique
---

## network에서 clique를 뽑고, 사용하는 방법. 

- 솔직히, 저는 clique를 잘 뽑지 않습니다. 보통의 일반적인 네트워크들은, 생각보다 dense하지 않고, girvan-newman 방법을 이용하는 것이 훨씬 효율적일 때가 많거든요. 즉 clique보다는 community가 훨씬 효과적이라는 이야기죠. 
- 그런데, community-detection 이 잘 효과적으로 되지 않을때가 있습니다. 보통 굉장히 dense한 경우, 노드들이 지독하게 밀집해 있는 경우 그런 현상들이 주로 발생하죠. 
- 그럴때는 community보다는 clique를 쓰는 것이 필요합니다. 일반적인 상황에서 clique는 많아 봐야 5정도 크기로 큰 의미를 못 가지는 반면, 밀집한 네트워크에서는 clique의 크기가 10을 넘어가곤 해서, 충분히 큰 의미를 가질 수 있거든요. 
- clique는 complete graph를 말합니다. 즉 노드의 갯수가 10개인 clique라면, 10개 간에 존재하는 45개의 edge가 빠짐없이 존재해야 하죠. 이거 쉬운거 아닙니다. 당연히 아시겠지만. 
- 말이 길어지는데, 귀찮으므로 그냥 하면서 해보겠습니다. 

## learn by doing it 

- 사실 코드 상에서 좀 상세하게 작성하였습니다. 아래를 죽 읽어보시면 이해가 될 거에요. 

### code 

```python 
#################################################################
# directed graph와 undirected graph는 다름. 
# 몇 가지 의문점
## edge betweenness centrality를 계산할 때 방향성을 고려해서 모두 처리되는가? 
#################################################################
import networkx as nx 
#################################################################
# nx.relabel_nodes: copy 가 True이면, 복사, False이면, replace
#################################################################
def main():
    print(f"-- start")
    # make clique1 
    cliq1 = nx.complete_graph(4)
    nx.relabel_nodes(cliq1, {n: f"c1_{n}" for n in cliq1.nodes()}, copy=False)
    print(cliq1.nodes())
    # make clique2
    cliq2 = nx.complete_graph(3)
    nx.relabel_nodes(cliq2, {n: f"c2_{n}" for n in cliq2.nodes()}, copy=False)
    print(cliq2.nodes())
    # make clique3
    cliq3 = nx.complete_graph(3)
    nx.relabel_nodes(cliq3, {n: f"c3_{n}" for n in cliq3.nodes()}, copy=False)
    print(cliq3.nodes())
    
    # make graph 
    G = nx.Graph()
    for cliq in [cliq1, cliq2, cliq3]:
        for n in cliq.nodes():
            G.add_node(n)
        for n1, n2 in cliq.edges():
            G.add_edge(n1, n2)
    print(G.nodes())
    print(G.edges())
    print(f"is connected? : {nx.is_connected(G)}")
    # cliq1과 cliq2를 2선으로 연결 
    G.add_edges_from([('c1_0', 'c2_0'), ("c1_1", "c2_1")])
    G.add_edges_from([('c2_1', 'c3_1'), ("c2_2", "c3_2")])
    print(f"is connected? : {nx.is_connected(G)}")
    # cliq2와 cliq3을 2선으로 연결 
    # 현재는 클리크만 있으므로 연결을 해보자.
    ########################################################################
    # enumerate_all_cliques(G)
    ## 존재하는 모든 클리크를 읽어들이는 제너레이터입니다. 
    ## 가령, (a, b, c)라는 클리크가 있다면 여기에는 (a, b), (b, c), (a, c)라는 클리드도 있게 됩니다. 
    ## 즉, 이렇게 부분집합의 형태가 되는 클리크가 모두 읽어들이는 함수입니다
    ########################################################################
    print("-- nx.enumerate_all_cliques(G)")
    for cliq in nx.enumerate_all_cliques(G):
        print(cliq)
    print("--"*40)
    ########################################################################
    # nx.find_cliques(G)
    ## 존재하는 모든 클리크들중에서 부분집합을 없애고, maximal한 클리크만 읽어들이는 제너레이터입니다.
    ########################################################################
    print("-- nx.find_cliques(G)")
    for maximal_cliq in nx.find_cliques(G):
        print(maximal_cliq)
    print("--"*40)
    ########################################################################
    # from networkx.algorithms.clique import make_max_clique_graph
    ## 우선, 해당 함수의 경우 다른 함수에 비해 위치가 다른 곳에 있음. 위의 방식으로 읽어들여야 함 
    ## 이는 cliq를 점으로, cliq간에 중복되는 node가 있을 때 edge가 있다고 가정하고 만들어지는 graph입니다.
    ## nodes: nx.find_cliques(G)를 통해 만들어지는 노드의 수와 같습니다.
    ## edges: clique간에 중복되는 node가 있으면 무조건 생성됨.
    ########################################################################
    # 즉, 얘네는 clique를 노드로 만든 그래프죠. 
    from networkx.algorithms.clique import make_max_clique_graph
    cliq_G = make_max_clique_graph(G)
    # 원래는 그냥 0, 1, 이렇게 네이밍이 되어 있으므로 이 네이밍을 바꾸구요. 
    nx.relabel_nodes(cliq_G, {name: f'cliq_{name}' for name in cliq_G.nodes()}, copy=False)
    # 각 노드(클리크)에 있는 노드들을 attr로 넣어줍니다.
    for cliq_name, nodes_in_cliq in zip(cliq_G.copy().nodes(), nx.find_cliques(G)):
        cliq_G.nodes[cliq_name]['nodes_in_cliq'] = nodes_in_cliq
        print(cliq, nodes_in_cliq)
    # 잘 들어왔는지를 확인하구요. 
    for n in cliq_G.nodes(data=True):
        print(n)
    print("=="*40)
    # 앞서 말한바와 같이 edge는 clique간에 중복되는 노드가 있어야 하죠. 
    # 따라서, edge별로 정말 중복되는 node가 있는지 파악해봅니다. 
    # 당연히 다 있쬬 호호호 
    for cliq1, cliq2 in cliq_G.edges():
        nodes_in_cliq1 = set(cliq_G.nodes[cliq1]['nodes_in_cliq'])
        nodes_in_cliq2 = set(cliq_G.nodes[cliq2]['nodes_in_cliq'])
        intersected_nodes_in_both_cliq = nodes_in_cliq1.intersection(nodes_in_cliq2)
        print(f"{cliq1} ==> {cliq2} ::: {nodes_in_cliq1} ==> {nodes_in_cliq2} ::: {intersected_nodes_in_both_cliq}")
    print("=="*40)
    ########################################################################
    # make_clique_bipartite
    ## 얘는 maximal clique와 node를 bipartite 그래프로 만들어주는 것을 말합니다. 
    ## 이걸 활용한다면, 각 노드가 어떤 클리크에 속하는지를 알 수 있게 되고, 
    ## 서로 다른 노드가 속한 클리크를 정리하여, 비슷한 클리크가 많은 경우 겹치는 클리크가 많은 경우, 
    ## 두 노드의 특성이 비슷하다고 추론할 수 있을 것 같네요. 
    ########################################################################
    from networkx.algorithms.clique import make_clique_bipartite
    cliq_bipartite_G = make_clique_bipartite(G)
    print(type(cliq_bipartite_G))
    print(cliq_bipartite_G.nodes(data=True))
    ## 사실, 근데 이건, 그냥 만들 수 있어요. 그냥 maximal clique를 죽 읽으면서, 클리크가 생성되는 대로 번호를 붙이고,
    ########################################################################
    cliq_bipartite_G = nx.Graph()
    for cliq_i, maximal_cliq in enumerate(nx.find_cliques(G)):
        cliq_bipartite_G.add_edges_from([(cliq_i, n) for n in maximal_cliq])
    print(cliq_bipartite_G.edges())
    ########################################################################
    # clique number: the number of vertext in largest clique
    ########################################################################
    from networkx.algorithms.clique import graph_clique_number
    print(f"clique number: {graph_clique_number(G)}")
    print("=="*40)
    ########################################################################
    # graph_number_of_cliques: G에 있는 모든 클리크의 수를 말합니다. 
    ########################################################################
    from networkx.algorithms.clique import graph_number_of_cliques
    print(f"all cliques in G count: {graph_number_of_cliques(G)}")
    print("=="*40)
    ########################################################################
    # node_clique_number: 지정된 node에서 가장 큰 maximal clique의 사이즈를 말합니다.
    ########################################################################
    from networkx.algorithms.clique import node_clique_number
    target_node = 'c3_1'
    print(f"node_clique_number of {target_node}: {node_clique_number(G, target_node)}")
    print("=="*40)
    ########################################################################
    # number_of_cliques: 지정된 노드를 포함하는 모든 maximal clique의 갯수를 말합니다. 
    ########################################################################
    from networkx.algorithms.clique import number_of_cliques
    target_node = 'c3_1'
    print(f"number_of_cliques of {target_node}: {number_of_cliques(G, target_node)}")
    print("=="*40)
    ########################################################################
    # cliques_containing_node: 지정된 노드가 포함된 모드 클리크를 리턴합니다.
    ########################################################################
    from networkx.algorithms.clique import cliques_containing_node
    target_node = 'c3_1'
    print(f"all maximal cliques containing target_node ::: {target_node}")
    for cliq in cliques_containing_node(G, 'c3_1'):
        print(cliq)
    print("=="*30)
    print(f"-- end")
    return 0 
main()

```

### result 

```
-- start
['c1_0', 'c1_1', 'c1_2', 'c1_3']
['c2_0', 'c2_1', 'c2_2']
['c3_0', 'c3_1', 'c3_2']
['c1_0', 'c1_1', 'c1_2', 'c1_3', 'c2_0', 'c2_1', 'c2_2', 'c3_0', 'c3_1', 'c3_2']
[('c1_0', 'c1_1'), ('c1_0', 'c1_2'), ('c1_0', 'c1_3'), ('c1_1', 'c1_2'), ('c1_1', 'c1_3'), ('c1_2', 'c1_3'), ('c2_0', 'c2_1'), ('c2_0', 'c2_2'), ('c2_1', 'c2_2'), ('c3_0', 'c3_1'), ('c3_0', 'c3_2'), ('c3_1', 'c3_2')]
is connected? : False
is connected? : True
-- nx.enumerate_all_cliques(G)
['c1_0']
['c1_1']
['c1_2']
['c1_3']
['c2_0']
['c2_1']
['c2_2']
['c3_0']
['c3_1']
['c3_2']
['c1_0', 'c1_1']
['c1_0', 'c1_2']
['c1_0', 'c1_3']
['c1_0', 'c2_0']
['c1_1', 'c1_2']
['c1_1', 'c1_3']
['c1_1', 'c2_1']
['c1_2', 'c1_3']
['c2_0', 'c2_1']
['c2_0', 'c2_2']
['c2_1', 'c2_2']
['c2_1', 'c3_1']
['c2_2', 'c3_2']
['c3_0', 'c3_1']
['c3_0', 'c3_2']
['c3_1', 'c3_2']
['c1_0', 'c1_1', 'c1_2']
['c1_0', 'c1_1', 'c1_3']
['c1_0', 'c1_2', 'c1_3']
['c1_1', 'c1_2', 'c1_3']
['c2_0', 'c2_1', 'c2_2']
['c3_0', 'c3_1', 'c3_2']
['c1_0', 'c1_1', 'c1_2', 'c1_3']
--------------------------------------------------------------------------------
-- nx.find_cliques(G)
['c1_1', 'c2_1']
['c1_1', 'c1_0', 'c1_3', 'c1_2']
['c3_0', 'c3_2', 'c3_1']
['c3_1', 'c2_1']
['c3_2', 'c2_2']
['c2_0', 'c2_2', 'c2_1']
['c2_0', 'c1_0']
--------------------------------------------------------------------------------
['c1_0', 'c1_1', 'c1_2', 'c1_3'] ['c1_1', 'c2_1']
['c1_0', 'c1_1', 'c1_2', 'c1_3'] ['c1_1', 'c1_0', 'c1_3', 'c1_2']
['c1_0', 'c1_1', 'c1_2', 'c1_3'] ['c3_0', 'c3_2', 'c3_1']
['c1_0', 'c1_1', 'c1_2', 'c1_3'] ['c3_1', 'c2_1']
['c1_0', 'c1_1', 'c1_2', 'c1_3'] ['c3_2', 'c2_2']
['c1_0', 'c1_1', 'c1_2', 'c1_3'] ['c2_0', 'c2_2', 'c2_1']
['c1_0', 'c1_1', 'c1_2', 'c1_3'] ['c2_0', 'c1_0']
('cliq_0', {'nodes_in_cliq': ['c1_1', 'c2_1']})
('cliq_1', {'nodes_in_cliq': ['c1_1', 'c1_0', 'c1_3', 'c1_2']})
('cliq_2', {'nodes_in_cliq': ['c3_0', 'c3_2', 'c3_1']})
('cliq_3', {'nodes_in_cliq': ['c3_1', 'c2_1']})
('cliq_4', {'nodes_in_cliq': ['c3_2', 'c2_2']})
('cliq_5', {'nodes_in_cliq': ['c2_0', 'c2_2', 'c2_1']})
('cliq_6', {'nodes_in_cliq': ['c2_0', 'c1_0']})
================================================================================
cliq_0 ==> cliq_1 ::: {'c1_1', 'c2_1'} ==> {'c1_2', 'c1_1', 'c1_3', 'c1_0'} ::: {'c1_1'}
cliq_0 ==> cliq_3 ::: {'c1_1', 'c2_1'} ==> {'c2_1', 'c3_1'} ::: {'c2_1'}
cliq_0 ==> cliq_5 ::: {'c1_1', 'c2_1'} ==> {'c2_2', 'c2_1', 'c2_0'} ::: {'c2_1'}
cliq_1 ==> cliq_6 ::: {'c1_2', 'c1_1', 'c1_3', 'c1_0'} ==> {'c2_0', 'c1_0'} ::: {'c1_0'}
cliq_2 ==> cliq_3 ::: {'c3_2', 'c3_0', 'c3_1'} ==> {'c2_1', 'c3_1'} ::: {'c3_1'}
cliq_2 ==> cliq_4 ::: {'c3_2', 'c3_0', 'c3_1'} ==> {'c3_2', 'c2_2'} ::: {'c3_2'}
cliq_3 ==> cliq_5 ::: {'c2_1', 'c3_1'} ==> {'c2_2', 'c2_1', 'c2_0'} ::: {'c2_1'}
cliq_4 ==> cliq_5 ::: {'c3_2', 'c2_2'} ==> {'c2_2', 'c2_1', 'c2_0'} ::: {'c2_2'}
cliq_5 ==> cliq_6 ::: {'c2_2', 'c2_1', 'c2_0'} ==> {'c2_0', 'c1_0'} ::: {'c2_0'}
================================================================================
<class 'networkx.classes.graph.Graph'>
[('c1_0', {'bipartite': 1}), ('c1_1', {'bipartite': 1}), ('c1_2', {'bipartite': 1}), ('c1_3', {'bipartite': 1}), ('c2_0', {'bipartite': 1}), ('c2_1', {'bipartite': 1}), ('c2_2', {'bipartite': 1}), ('c3_0', {'bipartite': 1}), ('c3_1', {'bipartite': 1}), ('c3_2', {'bipartite': 1}), (-1, {'bipartite': 0}), (-2, {'bipartite': 0}), (-3, {'bipartite': 0}), (-4, {'bipartite': 0}), (-5, {'bipartite': 0}), (-6, {'bipartite': 0}), (-7, {'bipartite': 0})]
[(0, 'c1_1'), (0, 'c2_1'), ('c1_1', 1), ('c2_1', 3), ('c2_1', 5), (1, 'c1_0'), (1, 'c1_3'), (1, 'c1_2'), ('c1_0', 6), (2, 'c3_0'), (2, 'c3_2'), (2, 'c3_1'), ('c3_2', 4), ('c3_1', 3), (4, 'c2_2'), ('c2_2', 5), (5, 'c2_0'), ('c2_0', 6)]
clique number: 4
================================================================================
all cliques in G count: 7
================================================================================
node_clique_number of c3_1: 3
================================================================================
number_of_cliques of c3_1: 2
================================================================================
all maximal cliques containing target_node ::: c3_1
['c3_0', 'c3_2', 'c3_1']
['c3_1', 'c2_1']
============================================================
-- end
```

## wrap-up

- dense한 네트워크에서는 girvan-newman 메소드와 같은 community detection 방법이 잘 안됩니다. 사실 이게 안되면, 다른 clustering 기법도 잘 안되는 건 비슷비슷해요. 
- 따라서, 이 때는, community을 뽑는것 보다는 clique를 뽑아보면서, 해당 집단의 밀집 정도를 보는게 좋습니다. 
- 다만, 이 때 clique들 또한, 모두 maximal clique라고는 하지만, 비슷비슷할 때가 많거든요. 가령, 21개 짜리 클리크가 10개 있다고 해도, 16개의 노드는 동일하고, 나머지 5개의 노드들이 조금씩 다른 경우와 같은(묘하게, 정확한 값이 작성되어 있는 것은, 이게 제 경험담이기 때문이죠) 
- 이상적으로는 maximal clique만으로 표현하고 가장 적은 edge로 원래의 그래프를 최대한 많이 커버할 수 있도록 만들면 재밌겠죠. 가령, 클리크를 노드로 네트워크를 구성하고, 클리크별 edge는 노드가 중복될 때, 그리고, 그때 각 엣지의 weight는 중복되는 노드의 수만큼 정도로 해서, weight가 큰 놈을 없애가면서 커버리지를 찾으면 재밌을 것 같습니다만, 이것도 결국은 그냥 휴리스틱이죠. 
- 그 외로는 많은 클리크에 속할 수록 해당 노드의 소위 "인싸력"이 대단하다고도 할 수 있을 것 같습니다. 속한 모든 클리크의 사이즈(clique number)를 더해서 해당 노드의 가치를 평가할 수도 있겠죠. 
- clique라는 개념을 사실 좀 무시했는데, 좀 파보면 재밌는 짓들을 할 수 있지 않을까 하고 생각하게 됩니다.