---
title: networkx - centrality - betweenness centrality
category: python-libs
tags: python python-libs networkx centrality between-centrality
---

## Centrality - Betweenness Centrality

- `Betweeness Centrality`는 "G의 모든 node pair의 최단 거리에, node V가 얼마나 많이 포함되는지를 비율로 표현하여, node V가 전체 그래프의 흐름에 얼마나 영향을 미치는지"를 측정하는 지표입니다. 즉, 계산 방법은 다음처럼 간단하죠 
    1) 모든 node pair의 shortest path를 구하고, 
    2) 각 노드별로 얼마나 많이 포함되는지를 비율로 정리한다. 
- 다만, 그래프에서 shortest path를 찾는 것은 꽤 계산이 필요한 알고리즘이고, 이를 n^2에 대해서 모두 처리한다는 것은, 꽤나 시간이 오래 걸리게 됩니다. 따라서, `nx.betweeness_centrality`에서는 모두 체크하지 않고 approximation할수 있도록 `K`라는 파라미터도 따로 포함하고 있습니다.

## Do it. 

- 개념적으로 betweenness centrality를 계산하는 것은 쉬워서 직접 코딩하지는 않았습니다. 
- betweenness centrality는 node의 수가 커질수록 계산하기가 매우 복잡해지는데, 이를 보완하기 위해 앞서 말한 것처럼 K개의 노드를 sampling하여, 값을 유추하는 알고리즘도 `nx.betweeness_centrality`에서 처리해줍니다. 
- 여기서는, K가 변함에 따라서 어느 정도의 정확도를 반영하는지만, 보여줄게요.

```python
import networkx as nx
import numpy as np
import time

np.random.seed(0)

N = 500  # node size
p = 0.4
G = nx.fast_gnp_random_graph(N, p, seed=0)

# exact betweenness centrality
bet_time = time.time()
nx_bet_dict = nx.betweenness_centrality(G)
bet_time = time.time() - bet_time
print(f"exact betweenness cent calc time: {bet_time: .4f}")


## check its accuracy with varying K
print("== betwenness centrality with K node sampling and its estimation")
VARYING_K=True
if VARYING_K == True:
    # exact betwenness centrality
    nx_bet_np = np.array([*nx_bet_dict.values()])
    nx_bet_np /= np.linalg.norm(nx_bet_np)
    for K in range(N//10, N+1, N//10):
        # betwenness centrality with K node sampling and its estimation
        k_bet_time = time.time()
        nx_bet_dict_K = nx.betweenness_centrality(G, k=K)
        nx_bet_K_np = np.array([*nx_bet_dict_K.values()])
        nx_bet_K_np /= np.linalg.norm(nx_bet_K_np)
        k_bet_time = time.time() - k_bet_time
        bet_corr = np.correlate(nx_bet_np, nx_bet_K_np)[0]
        print(f"k: {K:4d} - corr: {bet_corr:.4f} - time: {k_bet_time:6.3f}")
print("==")
```

- 아래에서 보시는 것처럼 적은 `k`에 대해서도 꽤 정확한 correlation이 나오는 것을 알 수 있씁니다.

```
exact betweenness cent calc time:  12.1926
== betwenness centrality with K node sampling and its estimation
k:   50 - corr: 0.9886 - time:  1.240
k:  100 - corr: 0.9937 - time:  2.427
k:  150 - corr: 0.9967 - time:  3.651
k:  200 - corr: 0.9977 - time:  4.860
k:  250 - corr: 0.9984 - time:  6.262
k:  300 - corr: 0.9989 - time:  7.392
k:  350 - corr: 0.9994 - time:  8.444
k:  400 - corr: 0.9996 - time:  9.780
k:  450 - corr: 0.9998 - time: 10.827
k:  500 - corr: 1.0000 - time: 13.183
==
```



