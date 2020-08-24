---
title: networkx - chain - chain decomposition 
category: python-libs
tags: python python-libs networkx chain decomposition
---

## 1-line summary 

- "chain decomposition"은 edge partition의 방법 중 하나로, DFS의 결과로 생성된 Tree를 고려하여, Tree에 속하지 않은 nontree edge을 순차적으로 읽으면서 만들 수 있는 cycle(혹은 path)을 만들어주는 식으로 진행됨.

## chain decomposition

- 사실 다 이해하고 나니까, "chain decomposition"의 경우는 application 부분이 좀 명확하지 않아서, 왜 했나 싶은 마음도 들긴 하는데, 아무튼 chain decomposition도 graph G에 대해서 정리하였습니다. 
- graph G가 있다고 하죠. 이 때, "G에 존재하는 edge들을 어떻게 잘 분해할 수 있을까?"라는 것이 edge decomposition이고 그 중 하나가 chain decomposotion이죠. 
- 알고리즘은 비교적 간단한데, 오히려 다음 그림을 보시면 매우 명확해집니다. 

![](https://www.researchgate.net/profile/Venkatesh_Raman/publication/304547887/figure/fig1/AS:378261554122763@1467195990961/llustration-of-Chain-Decomposition-a-An-input-graph-G-b-A-DFS-traversal-of-G-and.png)

- 간단하게 말하면, 
    - Graph G에 대해서 여기서 DFS로 tree `H`를 만듭니다. 이 tree에서는 각 node들이 parent, child 정보를 가지며 동시에 모든 edge들은 `(child -> parent)` 방향으로 추가되어 있죠. 
    - 다음으로 `G`에는 속하지만, Tree에 속하지 않는 edge들을 `H`에 추가해줍니다. 이러한 node들을 non-tree-edge라고 하죠. 이 nontree-edge들을 `H`에 추가할 때, root에 가까운 노드들에서 먼 노드로 향하도록 방향성을 설정하여 넣어줍니다. 이렇게 해야, 기존의 Tree에서 만든 child->parent를 고려하여, cycle이 만들어지게 되죠. 
    - 이렇게 만들어진 `H`에 대해서 non-tree edge들을 순서대로 탐색하며 cycle을 만듭니다. 
- 이게 다dlqslek.

## Chain decomposition: python implementation 

- `nx.chain_decomposition(G, root=None)`과 유사하지만, 저는 제가 더 이해가 쉽도록 만들었다고 생각합니다. 
- `nx.chain_decomposition(G, root=None)`의 경우는 `nx.dfs_labeled_edges(G, source=root)`라는 라이브러리를 사용했습니다만, 제 생각에는 굳이 저 함수를 사용할 필요가 없을 것 같아서, 사용하지 않고 처리했습니다

```python
def chain_decomposition(G, root=None):
    ########################################
    def build_H(G, root=root): 
        """
        DFS의 결과로 발생하는 Tree 구조에 대한 정보와 NonTree의 방향을 결정하여 리턴. 
        graph H는 DFS traversal의 결과를 (child, parent)의 방향으로 저장한 DiGraph이며, 
        DFS에 포함되지 않지만, G에는 포함되어 있는 nontree edge들의 경우 
        tree의 높은 레벨에서 낮은 레벨로 향하도록 처리.
        """
        H = nx.DiGraph()
        H.add_node(root, parent=None)
        # add Tree edge and parent infor.
        for parent, child in nx.dfs_edges(G, root): 
            H.add_node(child, parent=parent)
            H.add_edge(child, parent, tree=True)
        # add NonTree and set its direction for making cycle.
        NonTreeEdges = []
        for u, v in nx.difference(G, nx.Graph(H)).edges():
            # tree의 높은 레벨(root로부터의 거리 반대)부터 낮은 레벨로 향하도록 방향 설정
            # 기존의 방향이 모두 child -> parent이므로, 높은 쪽에서 낮은 쪽으로 방향을 설정해줘야함.
            u_level = nx.shortest_path_length(H, u, root)
            v_level = nx.shortest_path_length(H, v, root)
            if u_level > v_level: 
                NonTreeEdges.append((v, u))
            else: 
                NonTreeEdges.append((u, v))
        H.add_edges_from(NonTreeEdges, tree=False)
        return H

    def build_chain(H, start_edge, visited):
        """
        - start_edge로부터 출발하는, 거치지 않은 edge로 구성된 최대한 chain을 리턴.
        """
        chain = []
        u, v = start_edge
        while True:
            chain.append((u, v))
            if v in visited:
                return chain
            else:
                visited.add(v)
                u, v = v, H.nodes[v]['parent']
    
    H = build_H(G, root=root)
    visited = set()
    for u in H:
        visited.add(u)
        u_NoneTreeEdges = [(u, v) for u, v, e_attr in H.out_edges(u, data=True) if e_attr['tree']==False]
        for u, v in u_NoneTreeEdges:
            chain = build_chain(H, (u, v), visited)
            yield chain
```

## wrap-up

- 사실, 뭔가 재밌을줄 알고 공부해봤는데, 딱히 어플리케이션 레벨에서는 도움이 될 것 같지 않아요 흠흠.


## reference

- [chain decomposition image](https://www.researchgate.net/figure/llustration-of-Chain-Decomposition-a-An-input-graph-G-b-A-DFS-traversal-of-G-and_fig1_304547887)

- [Paper: Chain decomposition of graphs](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/chain-decompositions-of-graphs/DECFD20164C022EC620EB3E89679862F)