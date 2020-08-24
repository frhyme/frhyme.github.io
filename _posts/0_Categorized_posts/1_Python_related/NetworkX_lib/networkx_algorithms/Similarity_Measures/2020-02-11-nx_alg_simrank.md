---
title: networkx - similarity - SimRank
category: python-libs
tags: python python-libs networkx similarity distance
---

## 3-line summary 

- [SimRank](https://en.wikipedia.org/wiki/SimRank)는 "비슷한 사람에 의해서 가리켜지면, 비슷한 사람일 것이다"라는 가정에 기반한 node, similarity 계산법. 여기서 중요한 것은 "비슷한"이라는 말로, recursive의 형태로 "비슷함"을 적용해 나간다고 보면 됨.
- 계산과정이 [Pagerank](https://en.wikipedia.org/wiki/SimRank#cite_note-simrank_plusplus-1)와 매우 유사하게 느껴짐. SimRank의 경우 "노드간의 유사도를 측정하고", PageRank의 경우 "해당 노드에서 가장 영향력이 큰 놈"을 찾는 즉, 관점이 다름.
- 다만, 다른 지표는 아무것도 고려하지 않고, "그래프에서의 구조적인 특성(Structural feature)"만을 대표함. 즉, 이 가정이 valid하지 않을 경우 해당 지표는 유효하지 못함.


## node similarity - SimRank 

- [SimRank](https://en.wikipedia.org/wiki/SimRank)는 graph에 적용할 수 있는 간단하고 직관적인 유사도 측정방식을 말합니다. SimRank는 object-to-object의 관계를 가진(다르게 말한다면, graph 형태로 표현할 수 있는) 대부분의 대상에 대해서 적용가능한데, 이 측정방식은 기본적으로 "two objects are considered to be similar if they are referenced by similar objects.(두 물체는 비슷한 다른 물체들로부터 참조될경우, 비슷하다고 가정된다)"라는 가정을 내포합니다. 
- 더 풀어서 이야기한다면, 
    - 우리가 A와 B의 유사도를 측정하려고 할때, "A_1f(A의 팔로워) set"와 "B_1f(B의 팔로워) set"들간의 유사도를 통해서 측정할 수 있다고 합시다. 
    - 다시, A_1f와 B_1f 간의 유사도는 A_2f set와 B_2f_set 간의 유사도를 측정해야 알 수 있겠죠. 
    - 이런 식으로 무한히 반복될 수 있습니다. 그 모든 과정에서 결국 이를 하나의 matrix로 보면 수렴하는 값이 있겠죠. 
- 이렇게 쓰고보니, 무슨 점화식 같군요.

## Problems in SimRank 

- 다만, 논문 [ASCOS++: An Asymmetric Similarity Measure for Weighted Networks to Address the Problem of SimRank](http://clgiles.ist.psu.edu/pubs/TKDD2015.pdf) 에서는 "두 노드가 비슷하지만, odd lenght(홀수의 길이)를 가진 path만으로 접근 가능할 때는, 유사도가 떨어지게 나온다"는 기존 SimRank의 한계를 지적하기도 했습니다. 
- 또한, [networkx - simrank similarity](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.similarity.simrank_similarity.html#networkx.algorithms.similarity.simrank_similarity)는 기존의 한계를 그대로 가지고 있는 것으로 보이는데, 이는 weight factor를 조절하거나, page-rank에 기반한 다른 대안들을 통해서 보완할 수 도 있죠.


## Compute SimRank. 

- 이제 SimRank를 게산해봅시다. `nx.simrank_similarity(G)`와 코드 실행 결과가 동일하지만, 직접 짜보는 것과 짜보지 않는 것은 이해도에서 차원이 달라서, 좀 번거로워도 직접 짜봤습니다 
- 또한 저는 matrix의 형태로 개발한 것이 아니기 때문에, 계산은 좀 느릴 수 있습니다. 그리고, 결과는 생략했습니다

```python
import networkx as nx
import itertools
import numpy as np

def custom_SimRank(G, importance_factor=0.9, max_iterations=100):
    """
    SimRank: 
    - 기본적으로 "나를 가리키는(in-degree) object들끼리 비슷할수록, 비슷하다"는 것을 가정함. 
    - 이 개념은 recursion을 내포하게 되는데, 가령 "나를 가리키는 object(A)들은 이 object(A)들을 가리키는 
    또다른 object(B)들간이 비슷할수록... 으로 무한히 연속될 수 있음. 
    - 따라서, matrix를 반복해가면서 어디로 수렴하는지를 파악해야 함. 
    - 초기 값은 diagonal matrix가 됨.
    - 또한, "이웃의 이웃의 이웃"이 반복될 수록 importance_factor로 그 영햐응ㄹ 줄여나감.
    - 아래의 코드는 `nx.simrank_similarity(G)`와 코드 실행 결과가 동일함.
    - 또한, `simrank_similarity_numpy(G)`는 matrix간에 연산을 수행하는데, 
    행렬간 연산이 더 익숙한 경우 이 쪽이 더 편할 수 있음.
    """
    prevSimRank = None
    # initial SimRank인데, 당연하지만, 그냥 diagnonal matrix
    # 사실, 엄밀히 따지면, 이 두 노드만 1이어야 하므로.
    NewSimRank = {u: {v: 1 if u == v else 0 for v in G} for u in G}
    for _ in range(0, max_iterations):
        # update하기 전에 원래 값을 `prevSimRank`에 저장하고
        prevSimRank = NewSimRank.copy()
        # UPDATE Node SimRank
        for u in NewSimRank:
            for v in NewSimRank[u]:
                if u == v:  # u, v가 같을 경우에는 1.0
                    NewSimRank[u][v]=1.0
                else:
                    # u, v 가 다를 경우에는 각각의 neighbor들간의 모든 조합으로부터
                    # 기존 w_x_similarity의 평균을 구하여, 업데이트해줌.
                    u_neighbors, v_neighbors = G[u], G[v]
                    neighbors_product = list(itertools.product(u_neighbors, v_neighbors))
                    u_v_SimRank = 0.0
                    if len(neighbors_product)==0:
                        NewSimRank[u][v] = u_v_SimRank
                    else:
                        for w, x in neighbors_product:
                            #
                            w_x_SimRank = NewSimRank[w][x]
                            u_v_SimRank += w_x_SimRank
                        # u_v_SimRank average
                        u_v_SimRank /= len(neighbors_product)
                        # u_v_SimRank decay
                        u_v_SimRank *= importance_factor
                        NewSimRank[u][v] = u_v_SimRank
    return NewSimRank

########################################################################
N = 3
G = nx.scale_free_graph(N, seed=0)
G = nx.Graph(G)
assert nx.is_connected(G)==True

c_SimRank = custom_SimRank(G)
nx_SimRank = nx.simrank_similarity(G)
for u in c_SimRank:
    for v in c_SimRank[u]:
        assert round(c_SimRank[u][v], 8)==round(nx_SimRank[u][v], 8)
        #print(u, v, custom_node_SimRank, nx_node_SimRank)
print("=="*30)
print("Assertion complte")
print("=="*30)
```

- 다만, 위 과정을 통해서 나오는 SimRank matrix의 변화를 보면 다음과 같습니다.

```python
print("=="*30)
for i in range(0, 5):
    print(f"Simrank at iteration time {i:3d}")
    simrank_dict = custom_SimRank(G, max_iterations=i)
    np_arr = np.array(
        [[simrank_dict[u][v] for v in simrank_dict[u]] for u in simrank_dict]
    )
    print(np_arr)
    print("--"*30)
print("==" * 30)
```

- 처음에는 diagonal matrix에서 점점 값이 달라져가며 수렴하는 것을 볼 수 있습니다.

```
============================================================
Simrank at iteration time   0
[[1 0 0]
 [0 1 0]
 [0 0 1]]
------------------------------------------------------------
Simrank at iteration time   1
[[1.         0.225      0.225     ]
 [0.32625    1.         0.275625  ]
 [0.38826563 0.41104688 1.        ]]
------------------------------------------------------------
Simrank at iteration time   2
[[1.         0.44778164 0.47825156]
 [0.52584302 1.         0.50559618]
 [0.54711661 0.56468042 1.        ]]
------------------------------------------------------------
Simrank at iteration time   3
[[1.         0.58017506 0.59346901]
 [0.61612301 1.         0.60569372]
 [0.625351   0.63343929 1.        ]]
------------------------------------------------------------
Simrank at iteration time   4
[[1.         0.64061274 0.64685549]
 [0.65720419 1.         0.65236568]
 [0.66146263 0.66519571 1.        ]]
------------------------------------------------------------
============================================================
```


## wrap-up 

- 기본적으로, 많은 시스템들은 object들간의 similarity를 필요로 하죠. 다만, 이 지표는 "Graph의 구조적인 특성"에 기반한 유사도를 제시하였다는 점에서 의미가 있습니다. 물론 그러함에도 이 논문은 2001년도로 아주 먼 과거의 논문일 뿐이죠. 
- 개념적으로 PageRank와 매우 유사하나, 이를 node간의 유사도로 보느냐, 노드의 영향력으로 보느냐 등 관점에 따라서 조금씩 다릅니다. 
- 또한, SimRank는 다른 지표는 아무것도 고려하지 않고, "그래프에서의 구조적인 특성만을 고려하였다"는 한계를 가집니다. 이 지표를 가지고, 유사도를 측정하려면 해당 도메인에서 "이 가정"이 유효해야겠죠.


## reference 

- [SimRank in wikipedia](https://en.wikipedia.org/wiki/SimRank)
- [networkx - simrank similarity](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.similarity.simrank_similarity.html#networkx.algorithms.similarity.simrank_similarity)
- [SimRank: A Measure of Structural-Context Similarity](http://ilpubs.stanford.edu:8090/508/1/2001-41.pdf)