---
title: networkx - harmonic centrality
category: python-libs
tags: python python-libs networkx centrality harmonic-centrality
---

## centrality - harmonic centrality.

- [harmonic centrality](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.harmonic_centrality.html#networkx.algorithms.centrality.harmonic_centrality)는 해당 노드 u부터 다른 모든 노드들인 v들로 향하는 "최단 거리의 길이(shortest path length)의 역수"를 모두 더한 값을 말합니다. 
- 이렇게 쓰고 보면, 마치 closeness centrality와 유사해보이지만, 다음과 같이 달라요. 
    - closeness centrality: (최단거리들의 길이 합)의 역수 
    - hormonic centrality: (최단거리의 역수)의 합
- 이라는 차이가 있죠. 이렇게 쓰고 나면, 도대체

## Why harmonic centrality matter? 

- 이렇게 쓰고 나면, **"이렇게 바꾼다고 뭐가 그렇게 달라지냐?"**, 라는 생각이 들지만, 다릅니다.
- 논문 [Axioms for Centrality](https://arxiv.org/abs/1308.2140)에 작성된 내용을 보면, "다양한 중심성 지표를 대상으로 실험을 해보 결과 `harmonic centrality`가 가장 탁월했다"라고 말하기도 하죠. 그리고 그 외로도 아래의 다양한 아티클들에서, `harmonic centrality`의 우수성을 이야기하고 있습니다.
    - [a comparison of harmonic centrality and pagerank](http://blogs.cornell.edu/info2040/2019/10/27/a-comparison-of-harmonic-centrality-and-pagerank/)
    - [harmonic centrality and pagerank](https://www.searchenginejournal.com/harmonic-centrality-pagerank/283985/#close)

## Compute harmonic centrality and compare with others.

- [a-comparison-of-harmonic-centrality-and-pagerank](http://blogs.cornell.edu/info2040/2019/10/27/a-comparison-of-harmonic-centrality-and-pagerank/)에서 다음을 주장했습니다. 
    - 작은 network에서 harmonic centrality가 pagerank보다 속도가 빠르다: 이건 그렇기는 한데, 작은 네트워크이므로 시간 상 이점이 별로 없다고 봅니다. 네트워크가 커지면, harmonic centrality가 pagerank보다 현저하게 느려집니다. 
    - 지표들로 historgram을 구성했을 때, 그 값들이 multi-modal이다: scale-free network에서, 지표들로 histogram을 만들어보면, pagerank의 경우는 거의 한쪽으로 쏠려 있는데(skeweed), harmonic centrality의 경우는 multi-modal의 형태가 나타납니다. 이는, 그래프의 노드들에 대한 특정한 특성을 말한다고 할 수 있고, 이를 이용해서 그래프를 분석해낼 수도 있겠죠. 혹은, harmonic centrality가 그래프에 대한 뚜렷한 특정을 보여주는 예라고 말할 수 있습니다. 
- 자세한 내용은 다음 코드에서 확인하시면 좋습니다. 


```python
import networkx as nx
import numpy as np
import time


def np_normalize_dict(input_dict):
    """
    input_dict: {node_name: centrality_float}에서 
    value를 normalize하여 리턴.
    """
    vs = np.array(list(input_dict.values()))
    vs /= np.linalg.norm(vs)
    return {k: v for k, v in zip(input_dict.keys(), vs)}

def custom_harmonic_centrality(G):
    """
    node `u`의 harmonic centrality는 
    다른 모든 node `v`로 향하는 모든 shortest path length의 역수를 더한다. 
    """
    r_dict = {n:0 for n in G}
    for n1 in G:
        for n2 in G:
            if n1!=n2:
                n1_n2_l = nx.shortest_path_length(G, n1, n2)
                #print(n1, n2, n1_n2_l)
                r_dict[n1]+=1/n1_n2_l
    return r_dict
########################


# Graph generation
N = 10  # node size
p = 0.5
G = nx.fast_gnp_random_graph(N, p, seed=0)

print("=="*20)
print("== custom harmonic centrality")
custom_harmonic_cent = custom_harmonic_centrality(G)

print("== nx - harmonic centrality")
nx_harmonic_cent = nx.harmonic_centrality(G)

# 만약, nx.harmonic_centrality와 다르다면 아래 코드에서 오류가 발생해야 함.
for n in G:
    # To ignore underflow rounding.
    round_c__h_cent = round(custom_harmonic_cent[n], 8)
    round_nx_h_cent = round(nx_harmonic_cent[n], 8)
    assert round_c__h_cent == round_nx_h_cent
print("=="*20)

#############################################
# Comparison with pagerank
# Graph generation
N = 100  # node size
p = 0.3
G = nx.fast_gnp_random_graph(N, p, seed=0)
G = nx.scale_free_graph(N)
G = nx.Graph(G)
print(f"nx.is_connected(G): {nx.is_connected(G)}")
print("==")
print("== computation time")

harmonic_time = time.time()
harmonic_cent = nx.harmonic_centrality(G)
harmonic_time = time.time() - harmonic_time
#harmonic_cent = np_normalize_dict(harmonic_cent) # normalize
print(f"harmonic computation time: {harmonic_time:10.6f}")

pagerank_time = time.time()
pagerank_cent = nx.pagerank(G)
pagerank_time = time.time() - pagerank_time
#pagerank_cent = np_normalize_dict(pagerank_cent)  # normalize
print(f"pagerank computation time: {pagerank_time:10.6f}")
print(f"harmonic is {pagerank_time/harmonic_time:.2f} times faster than pagerank ")
print("==")

# value distribution
print("== histogram ")
harmonic_cent_v = list(harmonic_cent.values())
pagerank_cent_v = list(pagerank_cent.values())

# np histogram
bins=30
harmonic_bin, h_edge_bin = np.histogram(harmonic_cent_v, bins=bins)
pagerank_bin, p_edge_bin = np.histogram(pagerank_cent_v, bins=bins)
print("== harmonic, pagerank histogram")
MARKER = "="
for h, p in zip(harmonic_bin, pagerank_bin):
    # left is harmonic
    # right is pagerank
    left  = f"{MARKER*h:>50s}"
    right = f"{MARKER*p:<50s}"
    row = left + "|" + right
    print(row)
print("=="*20)

```

- 그림으로 만들어서 처리하면 좋은데, 귀찮아서 그냥 아스키 아트로 히스토그램을 만들어서 넣었습니다후후후후. 

```
========================================
== custom harmonic centrality
== nx - harmonic centrality
========================================
nx.is_connected(G): True
==
== computation time
harmonic computation time:   0.052979
pagerank computation time:   0.036304
harmonic is 0.69 times faster than pagerank
==
== histogram
== harmonic, pagerank histogram
                                                ==|===================================================================================
                                                 =|=========
                                               ===|===
                                            ======|=
                                                ==|
                                     =============|
                                                  |
                                      ============|=
                                                  |=
                                                 =|
                   ===============================|
                               ===================|
                                             =====|
                                                 =|=
                                                  |
                                                  |
                                                 =|
                                                 =|
                                                  |
                                                  |
                                                  |
                                                 =|
                                                  |
                                                  |
                                                  |
                                                  |
                                                  |
                                                  |
                                                  |
                                                 =|=
========================================
```

## wrap-up

- centrality를 분석할 때, 사실 골치아픈 것중 하나가, scale-free network에서 대부분의 centrality가 쏠려 있다는 것이죠. 이렇게 할 경우에는 노드간의 차이가 크지 않아서, 해석에 어려움을 겪습니다. 
- 반대로 harmonic centrlaity의 경우는 그 차이가 뚜렷하게 나타나므로 이를 비교하여 유의미한 분석을 할 수 있지 않을까 싶습니다.

## reference

- [networkx.algorithms.centrality.harmonic_centrality](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.harmonic_centrality.html#networkx.algorithms.centrality.harmonic_centrality)