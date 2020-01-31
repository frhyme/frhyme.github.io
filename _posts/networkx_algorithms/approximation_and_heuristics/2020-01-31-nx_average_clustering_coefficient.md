---
title: networkx - clique, max independent set
category: python-libs
tags: python python-libs networkx clique max_independent_set
---

## Average clustering coefficient of Graph.

### background

- **local clustering of each node** 는 각 노드에 대한 clustering(밀집도)를 말하며, 해당 노드 이웃들과 구성할 수 있는 모든 triangle 수 대비 실제 존재하는 triangle의 비율을 말합니다. 
- **average clustering coefficient**는 모든 노드들의 clustering coefficient의 평균을 말하죠. 

### approximation of avg. clustering coef

- 정확한 값을 계산하기 위해서는 존재하는 모든 삼각형을 일일이 확인하면서 해도 되지만, 그냥 몬테 카를로 시뮬레이션처럼 각 노드별로 그 이웃을 랜덤하게 골라서, 삼각형이 존재하는지를 체크하면서 계산해도 됩니다. 
- 어느 정도 trial이 보장되었을 때, 충분히 node의 수가 많다면, 평균값에서 그 오차가 줄어들게 되거든요. 결국, n이 증가하면 평균으로 회귀하게 되는, 기본적인 통계에서 신뢰구간 문제와 동일합니다. 

## Do it. 

- 아무튼, 해봅시다. Node가 2000개 있는 그래프를 대상으로 
    - **exact method**: 존재하는 삼각형을 일일이 세어가면서, 각 노드의 clustering coef를 찾고, 그 평균을 구함. 
    - **approx method**: 몬테카를로 시뮬레이션처럼 랜덤하게 선택하면서 값을 계산. 
- 코드와 코드 실행 결과는 다음과 같습니다. 

```python
import networkx as nx
from networkx.algorithms.approximation import clustering_coefficient
import matplotlib.pyplot as plt
import numpy as np
import time

####################################
# local clustering coefficient:
# 해당 노드가 이웃노드들과 연계하여 만들 수 있는 모든 삼각형 대비 실제로 존재하는 삼각형 수
# ------------------------
# average clustering coefficient:
# 모든 node clustering coefficient의 평균
####################################
# 여기서는 approxmiation을 활용한 방법과 exact method를 활용한 방법을 비교. 
# 당연하지만, node의 수가 커질수록 approximation의 정확도가 증가하고, 속도 상의 이점도 커짐.

N = 2000
p = 0.4
G = nx.fast_gnp_random_graph(N, p, seed=0)
#clustering_coefficient.average_clustering(G, trials=10, seed=0)

local_node_coef_lst = []
start_time = time.time()
for n in G:
    l = len(G[n])
    actual_tri_count = nx.triangles(G, n)
    possible_tri_count = l*(l-1)//2
    local_node_coef = actual_tri_count / possible_tri_count if possible_tri_count!=0 else 0
    local_node_coef_lst.append(local_node_coef)
    #print(f"{n} :: {actual_tri_count} :: {possible_tri_count} :: {local_node_coef}")
print(f"local node coef mean  : {np.mean(local_node_coef_lst):6.4f}")
exact_method_time = time.time() - start_time
start_time = time.time()
####################################
# clustering_coefficient.average_clustering(G, trials=1000, seed=0)
# -----------------------------------
# trials를 높일수록 값이 비슷해짐.
# node size가 100개일 때, 5000으로 세팅하니까 비슷하게 나옴.
# 물론, 당연하지만, 이 값을 올릴수록 시간 상에서는 손해를 보게 됨.
approx_clustering_coef = clustering_coefficient.average_clustering(G, trials=200, seed=0)
print(f"approx_clustering_coef: {approx_clustering_coef:6.4f}")
approx_method_time = time.time() - start_time
print("--"*20)
print(f"exact_method_time : {exact_method_time:6.2f}")
print(f"approx_method_time: {approx_method_time:6.2f}")
print(
    f"approximation is {exact_method_time/approx_method_time:7.2f} times faster than exact method"
)
print("=="*20)
```

- 코드 실행 결과는 다음과 같습니다. Node가 2000개일 때에 대해서 수행했는데, exact method나, approximation이나 큰 차이가 없죠. 다만 속도 측면에서는 지나칠 정도로 approximation이 빠릅니다. 사실, 생각해보면 당연한 거죠.

```
local node coef mean  : 0.4002
approx_clustering_coef: 0.3950
----------------------------------------
exact_method_time : 164.08
approx_method_time:   0.01
approximation is 14255.15 times faster than exact method
========================================
```

## wrap-up

- 그러니까, 웬만하면 정확한 값을 계산해야 한다는 강박때문에, 너무 큰 데이터에 대해서 무리하지 말고, "어느 정도 보장되는" approximation을 쓰도록 합시다. 충분히 큰 데이터에 대해서는, 어느정도 random을 가지고 게산하면 시간 상에서 압도적인 이점을 가져올 수 있습니다.
- 물론, 여기서 말하는 "어느 정도"라는 것을 판단하려면 통계적인 백그라운드가 탄탄해야겠죠. 가령 trial을 100번으로 세팅한 experiment를 50번 수행했다면 그 결과는 어느 정도의 신뢰 구간을 가지고 있는가? 와 같은 질문들에 대답을 하기 위해서라도, 통게적 지식이 필요하죠.