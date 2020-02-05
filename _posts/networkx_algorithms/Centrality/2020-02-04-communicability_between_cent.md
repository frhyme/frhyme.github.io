---
title: networkx - communicability betweenness centrality
category: python-libs
tags: python python-libs networkx centrality communicability betweenness-centrality
---

## Centrality - communicability betweenness centrality

- 전통적인 개념에서는 network를 분석할 때, shortest path만을 고려하게 됩니다. 하지만, 이는 실재적인 graph의 특성을 반영하지 못하죠. shortest path가 아니더라도, path는 여러개 존재하며, non-shortest path를 통해서 영향을 받게 되죠. 
- 따라서, shortest path만을 고려한 전통적인 betweenness centrality를 구하는 것이 아니라, 서로 다른 node pair 간에 존재하는 모든 path를 고려해서, betweenness centrality를 고려하는 것이 필요합니다. 
- 개념적으로는 어렵지 않습니다. 이전에는 그저 'shortest path'에 대해서만 해당 노드가 포함되었는지 확인했다면, 이제는 둘 사이의 모든 노드 path에 대해서 각 path 별로 해당 노드가 포함되는지 확인하면 됩니다. 간단하게 코드로 쓰면 다음과 같죠

```python
r_dict = {r:0 for r in inputG}
    for r in inputG:# 모든 r에 대해서
        for p in inputG: # p에서 q로 가는 모든 path중에서
            for q in inputG:
                if (p!=q) and (q!=r):
                    # path_p_q_r / path_p_r
                    r_dict[r] += len(path_p_r_q) / len(path_p_q)
```

- 물론, 진짜 이렇게 계산하면 계산의 복잡도가 매우 증가합니다. 실제로는 matrix exponential으로 처리하여 합해주는 식으로 처리되죠. 자세한 내용은 [networkx - communicability betweenness centrality](https://networkx.github.io/documentation/stable/_modules/networkx/algorithms/centrality/subgraph_alg.html#communicability_betweenness_centrality)에서 보시고, 위의 코드는 개념적으로만 이해하시면 됩니다.

## Do it using `Networkx`

- 코드는 다음과 같습니다. 간단하게, `communcation betweenness centrality`를 계산하는 함수를 만들고, `nx.communicability_betweenness_centrality(G)`와 값을 비교합니다. 
- 시간부터, 말하자면, 당연히, loop를 반복한 경우가 훨씬 많이 소요되죠.


```python
import numpy as np
import networkx as nx
import time


# Graph generation
N = 10  # node size
p = 0.5
G = nx.fast_gnp_random_graph(N, p, seed=0)
print(nx.is_connected(G))
def custom_comm_bet_cent(inputG):
    """
    - communicability betweenness centrality는 shortest path만 고려하는 것이 아니라, 
    모든 도달가능한 모든 path를 고려합니다. 
    - matrix로 푸는 방법도 있으나, 여기서는 이해가 쉽도록 다음과 같이, 일일이 path를 확인하여 게산합니다. 
    - 즉, node `r`의 communicability bet cent는 
        - 모든 node pair p부터 q까지의 모든 path중에서, 
        - r이 포함된 path의 비율을 모두 합하여 계산된다.
    """
    C = (len(inputG)-1)*(len(inputG)-2)
    r_dict = {r:0 for r in inputG}
    for r in inputG:# 모든 r에 대해서
        for p in inputG: # p에서 q로 가는 모든 path중에서
            for q in inputG:
                if (p!=q) and (q!=r):
                    #print(f"== {p}, {q}")
                    path_p_q = list(nx.all_simple_paths(inputG, p, q))
                    path_p_q_r = filter(lambda x: True if r in x else False, path_p_q)
                    path_p_q_r = list(path_p_q_r)
                    r_dict[r] += len(path_p_q_r) / len(path_p_q)
    # normalization
    r_dict = {k: v/C for k, v in r_dict.items()}
    #print(r_dict)
    return r_dict

# Compute communicability betweenness centrality
custom_cbc_time = time.time()
custom_comm_bet_cent = custom_comm_bet_cent(G)
custom_cbc_time = time.time() - custom_cbc_time

nx_cbc_time = time.time()
nx_comm_bet_cent = nx.communicability_betweenness_centrality(G)
nx_cbc_time = time.time() - nx_cbc_time

print(f"custom cbc time  : {custom_cbc_time:6.3f} sec")
print(f"networkx cbc time: {nx_cbc_time:6.3f} sec")
print(f"nx_cbc is {custom_cbc_time/nx_cbc_time} times faster than custom cbc")
print("=="*20)
# Compute np.corr
custom_cbc_np = np.array(list(custom_comm_bet_cent.values()))
custom_cbc_np /= np.linalg.norm(custom_cbc_np)

nx_cbc_np = np.array(list(nx_comm_bet_cent.values()))
nx_cbc_np /= np.linalg.norm(nx_cbc_np)

corr = np.correlate(custom_cbc_np, nx_cbc_np)[0]
print(f"corr: {corr:%}")

```

```
ustom cbc time  :  1.227 sec
networkx cbc time:  0.015 sec
nx_cbc is 83.44528754641114 times faster than custom cbc
========================================
corr: 97.839404%
```

## wrap-up

- 알것 같으면서도, 중간중간 헷갈립니다. linear algebra를 너무 멀리했어요 그동안 ㅠㅠ


## reference

- [networkx - communicability_betweenness_centrality](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.communicability_betweenness_centrality.html#networkx.algorithms.centrality.communicability_betweenness_centrality)