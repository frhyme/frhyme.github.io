---
title: networkx - centrality - Katz centrality
category: python-libs
tags: python python-libs networkx centrality eigenvector
---

## Centrality - Katz Centrality

- [Katz Centrality](https://en.wikipedia.org/wiki/Katz_centrality)는 Network 내 Node의 중심성(centrality)를 측정하기 위한 방법 중 하나입니다. 다른 centrality measure들과는 다르게, node pair간의 path를 고려하여 영향력을 측정합니다. 
- 가령 "A에게서 어떤 영향력이 시작된다면, 시간(T)가 흐름에 따라서 다른 노드들에게 어느 정도의 힘으로 전달될 것인가?"를 측정할 수 있게 되죠. 이 때 당연하지만, 노드 A로부터 멀수록, 그 "힘"이라는 것은 작아질 텐데, 이 정도를 `alpha(attenuation factor)`로 조정합니다.
- eigen centrality와 거의 비슷하며(pagerank도 마찬가지), 다만 lower bound를 잡아준다는 차이가 있겠네요.

## Calculate Katz Centrality. 

- Katz centrality를 구하는 데는 두 가지 방식이 있습니다. 
    1) 시간 `T`를 키우면서, 영향력(alpha)가 어디로 전해지는지를 일일이 더해가면서 처리하는 방법
    2) linear equation을 풀어서, 해를 찾는 방법 
- 각각의 방법으로 함수를 만들어서 계산하고, 그 결과를 비교해봤습니다. 비교할 때는 `correation`을 계산하는 방법, 그리고 단순히 centrality순으로 비교해봤을 때, 순서가 어떻게 다른지를 비교했어요.

```python
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def CALC_katz_by_summation(G, alpha=None, beta = 0.2, normalized=True):
    """
    - katz centrality는 각 노드에서 시작된 어떤 "정보"가 시간 t가 변함에 따라, 다른 노드에 얼마나 영향을 주는지 확인하는 방법
    - 이 때 전파 강도를 alpha를 통해 조절하고, beta를 통해 lower bound를 설정함
    - 즉, 각 노드별로 얼마나 다른 노드에 파급력 있게 정보를 전달하는지를 summation을 통해서도 계산할 수 있음.
    - 물론, 다음 함수에서 설명할, 
    """
    alpha = 0.1
    A = nx.to_numpy_matrix(G)
    Sum_A = np.zeros(A.shape)
    # k degree마다 alpha**k, A**k를 곱하여 더해줌.
    for k in range(1, 100):
        Sum_A += np.multiply(alpha**k, A**k)+0.2
    # i: source, j: target
    # 즉, j에 대해서 더해줘야, k일 때, j에 남아있는 값들을 알 수 있음.
    katz_cent = Sum_A.sum(axis=0)
    # normalize
    if normalized==True:
        norm = np.sign(sum(katz_cent)) * np.linalg.norm(katz_cent)
    else:
        norm = 1
    katz_cent = katz_cent / norm
    katz_cent_dict = {n:katz_cent[i] for i, n in enumerate(G)}
    return katz_cent_dict

def CALC_katz_by_lin_eq(G):
    """
    linear eq: (I - alpha*A) = b
    를 풀어서, katz centrality를 계산하는 방법.
    """
    A = nx.adj_matrix(G).T
    n = A.shape[0]
    alpha = 0.1
    b = np.ones((n, 1)) * float(1)
    # linear equation solve
    centrality = np.linalg.solve(np.eye(n, n) - (alpha * A), b)
    norm = np.sign(sum(centrality)) * np.linalg.norm(centrality)
    centrality = centrality/norm
    centrality = {n: centrality[i][0] for i, n in enumerate(G)}
    #print(centrality)
    return centrality
########################################
# Generate Graph
G = nx.random_k_out_graph(n=200, k=2, alpha=0.5, seed=0)
G = nx.DiGraph(G.copy())  # MultiDiGraph => DiGraph

katz_by_summation = CALC_katz_by_summation(G)
katz_by_lineq = CALC_katz_by_lin_eq(G)

##########################################
# katz centrality의 corrleation값을 통해 비교함.
katz_corr = np.correlate([*katz_by_summation.values()],
                         [*katz_by_lineq.values()])
print(f"== correlation: {katz_corr[0]: 5.3%}")
##########################################
# katz centrality를 비교하여, 순위가 다른치 체크함.
# value로 보면 값이 조금씩 다른데, 최대 최소값이 조금씩 다를 수는 있어도, 순위 자체는 큰 차이가 없음
# katz by summation
katz1 = sorted(katz_by_summation.items(), key=lambda x: x[1], reverse=True)
katz1 = map(lambda x: x[0], katz1)
# katz_by_lineq
katz2 = sorted(katz_by_lineq.items(), key=lambda x: x[1], reverse=True)
katz2 = map(lambda x: x[0], katz2)
COUNT_rank_diff = 0
for n1, n2 in zip(katz1, katz2):
    if n1!=n2:
        COUNT_rank_diff+=1
print(f"== COUNT_rank_diff %: {COUNT_rank_diff}")
```

- 사실, 당연한 결과이기는 하지만, 값이 비슷하게 나오죠.

```
== correlation:  95.390%
== COUNT_rank_diff %: 0
```


## wrap-up 

- matrix에 익숙하신 분들은 matrix의 형태로 계산하시는 것이 편하겠지만, 사실 graph를 공부할 때, 그 이해를 위해서는 오히려 matrix형태로 표현되는 것이 더 헷갈리는 것일 수 있습니다. 제가 첫번째에 코딩한 함수는, 사실 매트릭스에 대한 이해는 거의 없어도, 쉽게 이해할 수 있죠(물론, 충분히 큰 그래프에 대해서는 문제가 발생할 수 있지만요). 속도도 중요하지만, 저는 "누구나 이해할 수 있는 코드", 가 더 중요하다고 생각해요. 그런 명세어, 사람들이 가급적, 코드를 죽죽 따라 읽으면서 직관적으로 이해할 수 있는 코드도 많이 만들어주면 좋겠습니다.
- 또한, 결과적으로 `katz centrality`, `PageRank`, `eigenvector centrality`와 유사합니다. 앞서 말한 것과 같이, lower bound를 잡아준다는 것 정도가 eigenvector centrality와의 차이라고 할 수 있겠죠.