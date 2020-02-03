---
title: networkx - centrality - information centrality
category: python-libs
tags: python python-libs networkx centrality closeness-centrality
---

## Centrality - Information Centrality

- [Information Centrality](https://www.centiserver.org/centrality/Current-Flow_Closeness_Centrality/) 는 "Current Flow Closeness Centrality"라고도 부릅니다. 여기서 "Current"는 "전류"를 가리키죠. 즉 "전류 흐름에 근거한 근접 중심성 분석"이라는 말이 되죠. 
- 흔히들 네트워크를 생각할 때, 도로'망', 전력'망'과 같은 예를 많이 들게 됩니다. "전력망"은 전류의 흐름을 모델링하는 것이고, "전류의 흐름을 관리/예측하는 방법"은 이미 무수하게 존재하겠죠. 그리고, 이를 그대로, 일반 네트워크에도 적용하여, 각 노드에 대한 중심성을 어느 정도 도출할 수 있습니다. 
- 따라서, information Centrality는 노드간의 "effective resistance"에 근거하여, closeness centrality를 가져옵니다만, 제가 보기에는 closeness centrality와 큰 차이가 있어 보이지는 않아요. correlation을 구해보면, 값이 거의 1.0이 나옵니다.
- 다만, closeness centrality에 비해서 훨씬 빠르게 값을 구한다는 면에서는 이득이 있고, 이는 Edge의 수가 많아짐에 따라서 더 이득이 발생하게 되죠.


## Compare them. 

- 간단히 information centrality, closeness centrality를 `networkx`를 통해서 뽑아보고, 값의 유사성과 계산에 필요한 시간의 차이를 비교합니다. 

```python
import networkx as nx
import numpy as np

import time

##################################################
np.random.seed(0)

N = 500  # node size
p = 0.6
G = nx.fast_gnp_random_graph(N, p, seed=0)
print("== Graph generated")
# closeness, information centrality를 각각 구함.
close_time = time.time()
closeness_cent = nx.closeness_centrality(G)
close_time  = time.time() - close_time

info_time = time.time()
information_cent = nx.information_centrality(G, weight=None)
info_time = time.time() - info_time

# information centrality가 closeness centrality에 비해서 훨씬 시간이 적게 걸림
print(f"close_time: {close_time:8.5f}")
print(f"info_time : {info_time:8.5f}")
print(f"Information centrality is {close_time/info_time: 6.2f} times faster than closeness centrality")
print(f"==")
for i, n in enumerate(closeness_cent.keys()):
    print(f"NODE: {n:2d} - Close cent: {closeness_cent[n]:6.4f} - info cent: {information_cent[n]: 6.4f}")
    if i>5:
        break
print(f"==")

# A, B 를 normalize하지 않으면, correlation이 1보다 크게 나올 수 있음.
A = np.array([*closeness_cent.values()])
A /= np.linalg.norm(A)

B = np.array([*information_cent.values()])
B /= np.linalg.norm(B)
print(f"== correlation: {np.correlate(A, B)[0]: 5.3%}")
```

- 결과는 다음과 같습니다. 현재의 노드의 수는 500개인데, 더 증가할 수록, information centrality가 계산 시간 상에서 가지는 이점은 커집니다. 그리고, correlation은 거의 100%죠. 차이가 별로 없다는 이야기입니다. 

```
= Graph generated
close_time: 31.96718
info_time :  2.35090
Information centrality is  13.60 times faster than closeness centrality
==
NODE:  0 - Close cent: 0.7118 - info cent:  0.2990
NODE:  1 - Close cent: 0.7008 - info cent:  0.2933
NODE:  2 - Close cent: 0.7317 - info cent:  0.3083
NODE:  3 - Close cent: 0.7048 - info cent:  0.2954
NODE:  4 - Close cent: 0.7221 - info cent:  0.3040
NODE:  5 - Close cent: 0.7263 - info cent:  0.3059
NODE:  6 - Close cent: 0.7088 - info cent:  0.2975
==
== correlation:  100.000%
```


## wrap-up

- `current flow closeness centrality(information centrality)`의 의미와 closeness centrality와의 차이, 그리고 계산상에서 가지는 이점등을 정리하였습니다.


## reference

- <https://www.centiserver.org/centrality/Current-Flow_Closeness_Centrality/>