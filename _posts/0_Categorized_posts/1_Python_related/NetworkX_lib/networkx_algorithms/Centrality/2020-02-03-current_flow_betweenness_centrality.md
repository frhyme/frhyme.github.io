---
title: networkx - current flow betwenness centrality.
category: python-libs
tags: python python-libs networkx centrality betweenness-centrality current-flow
---

## current flow betweenness centrality. 

- 이전에, closeness centrality를 이야기할 때도, `information centrality`라는 이름으로, 측정한 것이 있었죠. 
- betwenness centrality도 마찬가지로, 전류 모형을 적용하여, graph에서 정보가 흐를 때, 각 node를 얼마나 지나가는지를 측정한, **current flow betweenness centrality**라는 것이 있습니다. 이는 다른 말로 **random-walk betweenness centrality**라고 하기도 하죠.

## Do it. 

- 늘 말하지만, `betweenness centrality`나, `current flow betwenness centrality`값 자체는 크게 다르지 않습니다. 
- 그런데, current flow의 경우 시간이 훨씬 많이 걸리네요 흠. 이건, 이전에 `current closeness centrality`가 `closeness centrality`에 비해서 훨씬 짧은 시간이 걸렸던 것에 비하면, 조금 다른 결과입니다.
- 특히, Node의 개수를 1000개까지 올리면, 더 기하급수적인 차이가 나죠.

```python
import networkx as nx
import numpy as np
import time

def Derive_CORR_from_TWO_CENT_DICT(dict_A, dict_B):
    # nx.centrality의 결과인 dictionary(nodename: cent_value) 2개를 input으로 
    # correlation을 리턴함 
    A_np = np.array([*dict_A.values()])
    A_np /= np.linalg.norm(A_np)

    B_np = np.array([*dict_B.values()])
    B_np /= np.linalg.norm(B_np)
    return np.correlate(A_np, B_np)[0]

np.random.seed(0)

N = 300  # node size
p = 0.4
G = nx.fast_gnp_random_graph(N, p, seed=0)

print("==" * 30)
# exact betweenness centrality
bet_time = time.time()
nx_bet_dict = nx.betweenness_centrality(G)
bet_time = time.time() - bet_time
print(f"exact betweenness cent calc time          : {bet_time: .4f} sec")

# current flow betweenness centrality
cur_bet_time = time.time()
nx_current_bet_dict = nx.current_flow_betweenness_centrality(G)
cur_bet_time = time.time() - cur_bet_time
print(f"current flow-between cent calc time       : {cur_bet_time: .4f} sec")

# approximation current flow betweenness centrality
aprox_cur_bet_time = time.time()
aprox_nx_current_bet_dict = nx.approximate_current_flow_betweenness_centrality(G)
aprox_cur_bet_time = time.time() - aprox_cur_bet_time
print(f"approx current flow-between cent calc time: {aprox_cur_bet_time: .4f} sec")
print("==" * 30)

# np.corr
bt_curbt_corr = Derive_CORR_from_TWO_CENT_DICT(nx_bet_dict,nx_current_bet_dict)
print(f"CORRELATION of BET and CURRENT_BET       : {bt_curbt_corr:7.5f}")
bt_aprcurbt_corr = Derive_CORR_from_TWO_CENT_DICT(nx_bet_dict, aprox_nx_current_bet_dict)
print(f"CORRELATION of BET and APPROX CURRENT_BET: {bt_aprcurbt_corr:7.5f}")

print("==" * 30)
```

- 즉, 아래에서 보시는 것처럼, approximation이 그냥 `betweeness centrality`보다 더 오래 걸립니다. 

```
============================================================
exact betweenness cent calc time          :  2.5393 sec
current flow-between cent calc time       :  19.6670 sec
approx current flow-between cent calc time:  5.1184 sec
============================================================
CORRELATION of BET and CURRENT_BET       : 0.99629
CORRELATION of BET and APPROX CURRENT_BET: 0.99044
============================================================
```

## wrap-up

- current flow 시리즈는 대상을 "전류모형"으로 모델링하여 처리합니다. 보통 이경우는 라플라스 변환을 이용해서, 계산했던 것으로 기억하는데, 하나하나 shortest_path를 찾으면서 처리해야 하는 기본적인 betweenness centrality보다 오래 걸린다는 것이 조금 이상하게 느껴지네요.


## reference

- [networkx - current flow betweenness centrality](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.current_flow_betweenness_centrality.html#id4)