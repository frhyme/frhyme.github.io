---
title: networkx - centrality - Eigenvector centrality
category: python-libs
tags: python python-libs networkx centrality eigenvector
---

## Centrality - Eigenvector Centrality

- [Eigenvector centrality](https://en.wikipedia.org/wiki/Eigenvector_centrality)는 일반적으로 네트워크 내 노드들의 영향력을 측정하기 위해 사용되는데, 직접적인 영향력만을 반영하며, 노드간의 차이를 구별하지 않는 degree cetrality와 다르게, "중요한 노드(네트워크 내에서 영향력이 큰 노트)가 가리킬 경우, 그 영향력을 더 크게 반영한다"라는 관점을 가지고 있습니다. 
- 마코브 체인을 배워보신 적이 있으시면 이해가 쉬우실텐데, "네트워크가 stationary distribution을 가진다고 할때(수렴한다고 할떄, 마코브체인의 n이 무한으로 가면 결국 수렴"하게 되죠. 이와 마찬가지로, 방향이 있는 네트워크에서 어떤 흐름 하나를 랜덤하게 돌리면서 새로운 path를 만들어간다고 합시다. 이때, 그 공이 유독 많이 흘러가는 곳이 있다면, 그곳은 네트워크 내에서 중요한 노드라고 할 수 있겠죠? 즉, 이러한 관점을 반영하여 만들어진 것이 eigenvector centrality를 말합니다.
- 일반적으로 이 지표는 network 상에서 각 노드의 영향력을 측정하기 위해서 사용되는데, 만약,  `Node A`가 Eigenvector centrality가 높은 다른 노드들로부터 directed로 연결된다면, `Node A` 또한, eigen vector가 높게 됩니다. 쉽게 말하자면, "연예인들의 연예인"같은 느낌으로 이해하셔민 되죠.
- 또한, PageRank, Katz centrality 등도 Eigenvector Centrality의 변종입니다.

## How to measure it. 

- 구하는 방법은 그냥 Graph의 adjancency matrix에 대해서 eigen vector를 구하면 됩니다. 
- 그렇다면, "왜 adjacency matrix의 eigen vector가 어떻게 앞서 말한 영향력을 반영할 수 있느냐?"와 같은 질문이 뒤따라오죠. 매우 타당한 지적이지만, 이 부분은 이 글에서 커버하려는 내용을 넘습니다. 간단히 말하자면, `np.dot(A, eigenvector) = np.multiply(eigenvalue, eigenvector)`의 모양이, 약간 마코브 체인을 공부할 때, 배웠던 무엇과 비슷하다....정도밖에 말할 수 없겠네요 호호호호호호. 
- 아무튼, 이게 그냥 adjancency matrix에 대해서 eigen value를 찾으면 되는데, 이걸 풀려면 꽤 복잡해집니다. 그래서 보통 power iteration method를 사용하죠. 네, 물론 저는 이미 남들이 만들어 놓은 함수를 고대로 사용할 것입니다. 
- 그냥 `nx.eigenvector_centrality()`를 사용해서 바로 구할 수도 있지만, 이해를 돕기 위해서, 직접 코딩을 해봤습니다. 
- 앞서 말한 것처럼 iteratorion method는 어느 정도 초기값을 random하게 설정하여 시작하기 때문에, 실행시마다 약간 값이 달라져요. `np.random.seed(0)`를 사용해봤지만, 잘 고정되는 것 같지는 않더라고요.

```python
import networkx as nx
import numpy as np

import scipy as sp
from scipy.sparse import linalg

np.random.seed(0)

# Generate GN graph.
G = nx.gn_graph(n=10, seed=0)

MAX_ITER = 500

# nx.eigenvector_centrality() 와 의미적으로 동일한 함수를 numpy를 사용해서 만듬.
def custom_eigen_centrality(inputG, weight=None, max_iter=MAX_ITER, tol=0):
    """
    - 주어진 Graph에서 adjacency matrix M를 가져오고
    - scipy.linalg.eigs 를 사용해서 M의 eigen vector, value를 뽑고 
    - eigen vector를 normalization하여 결과를 출력 
    """
    M = nx.to_numpy_matrix(G).T
    #############################################
    # linalg.eigs
    # 주어진 Matrix로부터 eigen_value, eigen_vector를 구하는 scipy 함수
    # A: eigen value, vector를 구할 matrix
    # k: 구하려는 eigen value에 대한 차수(degree)와 가까운 개념인데, 일단은 그냥 1이라고 생각하면 됨
    # which: LR 은 Largest Real part를 의미함. 즉, 가장 큰 real value를 찾겠다는 것(optional)
    # maxiter: iteration을 몇 번 할 것인가?
    # tol: 어느정도의 차이가 발생하면 converge 했다고 결정하고 iteration을 멈출 것인가?
    #############################################
    
    # eigen vector를 뽑아냄. eigenvalue는 반드시 필요하지는 않음.
    eigenvalue, eigenvector = linalg.eigs(M.T,
                                          k=1,
                                          which='LR',
                                          maxiter=max_iter,
                                          tol=tol)
    # real part만 뽑아내고
    eigenvector = eigenvector.real
    # 정말 같은지 살짝 비교해봄.
    if True:
        # floating value이고, iteration method를 사용하여 오차가 발생하므로
        # 특정 소수점에서 rounding
        ROUNT_n = 10
        LEFT = np.dot(M.T, eigenvector).real
        RIGHT = np.multiply(eigenvalue, eigenvector).real
        LEFT, RIGHT = np.round(LEFT, ROUNT_n), np.round(RIGHT, ROUNT_n)
        print(f"LEFT == RIGHT :: {np.all(LEFT==RIGHT)}")
    print("==")

    # normalization
    eigenvector_norm = np.sign(eigenvector.sum()) * np.linalg.norm(eigenvector)
    eigenvector = eigenvector / eigenvector_norm
    # flatten() : (n, 1) ==> (n)
    eigenvector = eigenvector.flatten()
    return dict(zip(G, eigenvector))
# FUNCTION END
################################################

print(f"== custom eigen centrality ")
for n, eig_cent in custom_eigen_centrality(G).items():
    print(f"{n:2d} = eigen centrality: {eig_cent:10.7e}")
print("===")

```

- 결과는 다음과 같습니다. power iteration method가 exact method가 아니므로, `nx.eigenvector_centrality()`와 값이 조금씩 달라질 때는 있습니다. 

```
== custom eigen centrality
LEFT == RIGHT :: True
==
 0 = eigen centrality: 1.0000000e+00
 1 = eigen centrality: 5.2878984e-05
 2 = eigen centrality: -1.1195401e-10
 3 = eigen centrality: -4.2412712e-13
 4 = eigen centrality: 2.9085300e-09
 5 = eigen centrality: -1.3869673e-13
 6 = eigen centrality: 4.1828635e-13
 7 = eigen centrality: -1.1592913e-13
 8 = eigen centrality: 1.5379795e-13
 9 = eigen centrality: -1.3433694e-13
===
```


## wrap-up

- 오랜만에, 약간은 좀 공대생다운 정리를 한 것 같아요. 꽤 오랫동안 `eigenvector centrality`를 그냥, 거의 외우다시피 해서 썼었는데, 시간이 지나니까 내가 답답해서라도 정확하게 정리를 하게 되는 것 같네요. 
- 저는, 사람이 처음부터 모든 것을 다 탄탄히 하게 가려면 지치는 것 같아요. 어떤 경우에는 그냥 답만 보고 가고, 시간이 지나면 알아서 답만 보지 않고 지금처럼 조금 더 파고들어가게 되겠죠. 
- 아무튼, 오랜만에 정확하게 이해하니까 기분이 좋습니다 헤헤헤.



## reference

- [Eigenvector Centrality](https://en.wikipedia.org/wiki/Eigenvector_centrality)
- [Eigenvalues and eigenvectors in Wikipeia](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)
- [데이터사이언스 스쿨 - 고유값 분해](https://datascienceschool.net/view-notebook/7fd58178d9e64be682058db7e024d8b5/)
- [What is the importance of eigenvalues/eigenvectors?](https://math.stackexchange.com/questions/23312/what-is-the-importance-of-eigenvalues-eigenvectors)