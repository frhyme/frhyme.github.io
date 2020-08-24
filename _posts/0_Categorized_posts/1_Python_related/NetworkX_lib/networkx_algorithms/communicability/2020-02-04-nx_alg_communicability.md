---
title: networkx - communicability
category: python-libs
tags: python python-libs networkx communicability
---

## What is communicability?

- [networkx documentation](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.communicability_alg.communicability.html#networkx.algorithms.communicability_alg.communicability)에 작성된 의미에 따르면, 다음과 같습니다. 

> The communicability between pairs of nodes in G is the sum of closed walks of different lengths starting at node u and ending at node v.

- 즉, Communicability는 Graph `G`의 모든 node pair들간에 서로 다른 길이(다양한 길이)의 closed walks의 합을 의미하죠. 이는 기존에 'shortest path'를 중심으로 node간의 관계를 측정하는 것보다 좀 더 넓은 개념을 포함하게 되죠.
    - 다만, "closed walks"는 잘못 표기된 것 같아요. closed walks는 source와 targer이 같은 walk를 말합니다(다르면, open). 그런데, 여기서 communicability는 source, target이 다른 경우에 대해서도 고려되거든요. 즉, 여기서는 그냥 walk라고 생각하면 될 것 같아요.

### paper abstract: Communicability in complex networks

- 또한, 논문 ["Communicability in complex networks"](https://arxiv.org/pdf/0707.0756.pdf)에서는 communicability의 필요성을 다음과 같이 정리하고 있습니다(간단하게 초록만을 정리하였습니다)
    - 복잡 네트워크(complex network)의 많은 위상학적(topological) 동적(dynamical) 성질들은 최단거리(shortest path)에 근거한 네트워크의 흐름을 가정하고 정의됩니다. 하지만, non-shortest path를 통해서도 네트워크의 다른 노드들에 도달할 수 있기 때문에, 무조건 최단거리만으로 전체 네트워크의 관계성(global communicability)을 제한하는 것은 합당하지 못하다.
    - 따라서, 본 논문에서는 기존의 shortest path의 개념을 확장하는 복잡계(complex network)의 관계성(communicability)에 대한 새로운 측정지표로서 제안한다. 새로운 측정 방법에 따르면, 많은 실세계의 네트워크(real-world network)는 그래프 내에서 가장 많이 연결된(most-connected node, popular)간에 communicability가 큰 경우(assortative communicability)와 "popular node"가 서로 거의 commnicate하지 않는, "disassortative communicability"로 구분된다.
    - 이러한 정보를 통해서, 우리는 실제 세계의 복잡한 시스템의 구조적/동적인 성질에 따라서, 다양한 set로 구분할 수 있을 것이다. 
    - 또한, 이 communicability measure는 네트워크의 세부 구조, 특히, 네트워크 내에 존재하는 community들을 도출하기 위해서도 사용할 수 있을 것이다. 
- 사실 타당한 지적입니다. "shortest path"는 네트워크에 대한 약간, minimum spanning tree와 유사하죠. 즉, 어느 정도 네트워크 자체를 축약해서 보는 것이기 때문에, 자체적으로 한계를 가지고 있습니다. 

## communicability vs. katz centrality.

- 이제 개념을 대략 알겠고, 이제 communicability를 계산해봅니다. 
- 앞서 말한것과 같이, `communicability`는 shortest path만을 고려하는 기존의 네트워크 유통의 한계를 넘어서기 위해서, 모든 path를 유효하다고 가정하죠. 단, 이 과정에서 path의 길이가 길어진다면 그만큼 penalty는 당연히 발생하게 됩니다. 
- 이렇게 쓰고보면, 이전에 설명했던 [katz centrality](https://en.wikipedia.org/wiki/Katz_centrality)와 매우 유사하게 느껴지기 시작합니다. **katz**의 경우, 각 노드에서 어떤 뉴스가 다른 노드로 전파된다고 할때, 그 전파될때 마다 약화되는 정도를 alpha로 고려하고, 시간 T를 증가시키면서 어떻게 정보가 퍼져나가는지를 측정하여, 해당 노드의 중요도를 측정했습니다. 
- 마찬가지로, `communicability`도 유사하게, Graph의 adjacency matrix인 `M`을 시점 T를 증가시키면서, 동시에 값을 약화시키면서 측정하게 되죠. 다만, 하나의 node의 centrality를 측정하는 것이 아니라, node to node의 communicability를 측정한다는 것이 다르죠. 
- 계산 방법은 [matrix exponential](https://en.wikipedia.org/wiki/Matrix_exponential)와 같습니다. 

## Do nx.communicability(G)

- 자, 이제 됐고, 계산을 해봅시다. 앞서 말한 것처럼 matrix `M`의 matrix exponential 을 만들면, 그 값이 결국 우리가 구하려고 하는 power series가 되는 것이죠. 이는 `scipy.linalg.expm(M)`을 통해 계산할 수 있습니다. 이걸 함수로 정의하고, `networkx`에 있는 함수와 값을 비교해봅니다. 

```python
import networkx as nx
import numpy as np

import scipy.linalg
#expA = scipy.linalg.expm(A)

def custom_communicability(inputG):
    """
    - 결국 시점 T를 증가시키면서 node to node path가 얼마나 존재하는지를 측정하는 식으로 계산
    - 단, 이는 결국 수렴하며, matrix exponential 으로 간단하게 계산할 수 있음.
    """
    expM = scipy.linalg.expm(
        nx.to_numpy_matrix(inputG)
    )
    #R /=np.linalg.norm(R)
    # dictionary representation of communicability G
    r_dict = {}
    for n1 in inputG:
        r_dict[n1] = {
            n2: v for n2, v in zip(inputG, np.array(expM[n1]))
        }
        #print(row)
    return r_dict
# ====================================
np.random.seed(0)

N = 50  # node size
p = 0.8
G = nx.fast_gnp_random_graph(N, p, seed=0)

# communicability의 return type => {n1: {n2: communicability_between_n1_and_n2}}
custom_comm_dict = custom_communicability(G)
nx_comm_dict = nx.communicability(G)
for n1 in custom_comm_dict.keys():
    custom_comm_np = np.array(
        list(custom_comm_dict[n1].values())
    )
    custom_comm_np /= np.linalg.norm(custom_comm_np)
    nx_comm_np = np.array(
        list(nx_comm_dict[n1].values())
    )
    nx_comm_np /= np.linalg.norm(nx_comm_np)
    comm_corr = np.correlate(custom_comm_np, nx_comm_np)[0]
    print(f"Node {n1} ::: correlation {comm_corr:}")
    if n1>5:
        break
print("--")
```

```
Node 0 ::: correlation 1.0
Node 1 ::: correlation 1.0
Node 2 ::: correlation 1.0
Node 3 ::: correlation 0.9999999999999999
Node 4 ::: correlation 1.0
Node 5 ::: correlation 1.0
Node 6 ::: correlation 1.0
--
```

## wrap-up

- 사실, 제가 `custom function`이라고 쓴 함수는 `communicability_exp(G)`라는 이름으로 이미 함수가 networkx에 존재합니다. 그러함에도, 굳이 풀어서 써준 것은, 이해를 돕기 위함이죠(네, 물론 저의 이해를 돕기 위함입니다 호호호). 
- 그냥 [`communicability`](https://networkx.github.io/documentation/stable/_modules/networkx/algorithms/communicability_alg.html#communicability)에서는 eigen value를 찾아서, 처리해줍니다. 지금 보니까, 이 쪽이 더 이해가 쉬웠을지도 모르겠네요. 아무튼, 결국 수렴한다는 점에서 봤을 때는 유사합니다. 
- 또한, eigen value, vector를 쓴다는 점에서 보면, 앞서 나왔던 eigen vector centrality, katz centrality와 유사한 것도 매우 타당해지죠. 즉, communicability는 eigen vector centrality, katz centrality와 유사한 점이 많아 보입니다



## reference

- [Communicability in complex networks](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.77.036111)