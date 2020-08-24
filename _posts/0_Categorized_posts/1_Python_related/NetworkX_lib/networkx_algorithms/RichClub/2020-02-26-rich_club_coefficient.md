---
title: networkx - Rich Club coefficient
category: python-libs
tags: python-libs python networkx rich-club density 
---

## 3-line summary 

- `rich-club coefficient`는 "k-core에 대한 density 변화율"을 의미함. 
- equivalent random network와 비교하여 normalization. 
- `networkx.algorithms.richclub.rich_club_coefficient`와 동일한 코드를 다른 형태로 만들어봄.

## What is Rich Club? 

- 그림으로 보면 좀 더 직관적인데요, "degree가 높은 노드(빪간색의 노드)끼리 더 밀집해 있는 형태"를 보통 rich club이라고 합니다. "높은 degree를 가진 node들이 lower degree를 가진 node들과 연결되기 보다, 높은 degree를 가진 node들과 연결되는 현상"라고 말할 수 있죠. 

![rich club figure in wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Disassortative_network_demonstrating_the_Rich_Club_effect.png/220px-Disassortative_network_demonstrating_the_Rich_Club_effect.png)

- 계산 법 자체는 매우 간단한 편인데요, 그냥 "node degree threshold"를 의미하는 `k`를 점점 상향시키면서, 해당 노드들로만 구성된 subgraph `subG`의 density가 어떻게 변화하는지를 측정하는 것이 바로 `rich_club_coefficient`입니다. 
- 즉, degree가 높은 노드들끼리 subgraph를 구축할 수록 density가 커진다면(1.0에 가까워진다면), 이는 rich club의 특성이 발현되고 있다, 라고 결론을 내릴 수 있는 것이죠. 

### normalization 

- 다만, 이 지표가 점점 1.0에 가까워진다고 해서 반드시 그 Graph가 rich-club이라고 할 수는 없습니다. 사실 이는 random network에서도 보통 단조 증가(monotonically increasing)하는 형태를 보이거든요. 
- 따라서, 이는 equivalent random network(degree distribution이 같지만 edge의 구성이 다른 G)에 대해서 비교하여, normalization을 하여 극복합니다. 
- 그냥, 아래와 같이 심플하게 처리하죠.

```
rich_club(G) / rich_club(equivalent_random_G)
```

## python implementation 

- 동일한 코드가 이미, [networkx.algorithms.richclub.rich_club_coefficient](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.richclub.rich_club_coefficient.html#networkx.algorithms.richclub.rich_club_coefficient)에 존재합니다만, 조금 더 짧고 간결하게 작성했다고 생각합니다. 혹은, 이해가 쉽도록 코딩했다고 생각해요.

```python
import networkx as nx 


def rich_club_coefficient(G, normalized=True, Q=100, seed=0):
    """
    G: undirected, not-multi nx.Graph
    """
    def compute_RichClub(G): 
        """
        k와 같거나 보다 큰 node degree를 가진 node들에 대해서 
        subgraph를 그리고 density를 계산.
        그리고 k별로 rich_club_coefficient를 리턴 
        보통 k가 커질수록 값이 1.0에 가까워지면, rich_club라고 판단함.
        """
        def Node_k(G, k): 
            # Node_k: G에서 degree가 k보다 크거나 같은 node들
            nodes_degree_higher_or_equal_than_k = []
            for n, deg in nx.degree(G):
                if deg>=k:
                    nodes_degree_higher_or_equal_than_k.append(n)
            return nodes_degree_higher_or_equal_than_k
        
        max_k = max([deg for n, deg in nx.degree(G)])
        RichClub_k_dict = {}
        for k in range(0, max_k+1): 
            subG = nx.subgraph(G, Node_k(G, k))
            if len(subG)>=2:# 2보다 작으면, edge가 없으므로 0이 나옴 
                RichClub_k_dict[k] = nx.density(subG)
        return RichClub_k_dict

    def equivalne_random_graph(G, Q=100, seed=0):
        """
        G와 degree distribution이 같지만 
        edge의 구성이 다른 equivalent random G를 
        random하게 edge를 교환하여 생성.
        """
        R = G.copy()  # equivalent Random Graph
        nedges = len(R.edges())
        nswap = Q*nedges
        max_tries = nswap*10
        nx.double_edge_swap(
            G=R, nswap=nswap, max_tries=max_tries, seed=seed
        )
        return R
    ####################################
    
    rich_club_coef = compute_RichClub(G)
    if normalized==False:
        return rich_club_coef
    else: 
        R = equivalne_random_graph(G)
        rich_club_coef_R = compute_RichClub(R)
        return {
            k: v/rich_club_coef_R[k] for k, v in rich_club_coef.items()
        }
```



## reference

- [networkx.algorithms.richclub.rich_club_coefficient](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.richclub.rich_club_coefficient.html#networkx.algorithms.richclub.rich_club_coefficient)
- [Rich-club phenomenon across complex network hierarchies](https://cseweb.ucsd.edu/~jmcauley/pdfs/apl07.pdf)
