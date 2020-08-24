---
title: networkx - equivalent random network. 
category: python-libs
tags: python python-libs networkx random-network random reference-network. 
---

## 3-line summary. 

- "어떤 네트워크가 어떠한 성질을 가진다"는 것을 증명하기 위해서는 보통 비슷한 성질을 가지는, random network를 reference로 삼는다. 
- graph의 small-worldness를 측정하기 위해서는 'equivalent random network'를 reference로 삼는다. 
- node의 degree가 똑같고, '연결성(connectedness)'를 유지하면서, edge들을 변형한 것을 equivalent random network라고 한다.

## What is Small worldness?

- [small-world network](https://en.wikipedia.org/wiki/Small-world_network)는 보통, "대부분의 노드들이 서로 이웃은 아니지만, 어떤 노드도 다른 노드들의 이웃이 될 가능성이 높고(link prediction이 높고), 대부분의 노드가 다른 노드들로 비교적 짧은 거리들만으로 도달 가능한, 네트워크를 말합니다.
- 따라서, 보통, small-world network는 "노드간의 평균적인 거리"가 `log(node size)`와 비례하게 됩니다. 즉, 네트워크의 노드가 아무리 많아져도, 평균적인 거리는 로그 펑션으로 증가하게 된다는 것이죠
- 이 특성을 갖추게 되면, 흔히 "세상 참 좁다"라고 말하는 것인, "새로운 사람이 생겼을 때, 이 사람이 내 친구의 친구일 가능성"이 매우 높아집니다. 이는 실제 세상의 많은 네트워크들의 특성들을 대표하기도 하죠.
- small network는 보통 clustering coefficient가 높고, average shortest path length가 짧은 것으로 알려져 있습니다. 그리고, 보통, equivalent random network와 이 값을 비교하죠. 

## equivalent random network. 

- "equivalent random network"는 각 node들의 degree는 변화없고, 그저 edge만 바뀐 것을 의미합니다. 
- 대략적인 알고리즘을 보면 다음과 같죠. 
    1) node의 degree에 따른 probability distribution function을 만들고, 이에 따라, 서로 다른 노드 `a`, `b`를 추출. 
    2) `a`의 이웃들, `b`의 이웃들로부터 uniform하게 하나의 이웃들을 각각 `c`, `d`를 뽑고, 이 둘을 교환. 이렇게 하면 모든 node degree가 유지되면서, edge만 변형하게 되죠.
    3) 2)를 진행했을 때, connectedness가 깨진다면, 원래대로 revert하고, 아닐 경우, 다시 1)부터 진행함. 
- 다시 말해, 'node의 degree는 유지하고, edge만 random하게 변형해준 네트워크'를 바로 equivalent random network라고 합니다. 
- 이러한 random하게 발생할 수 있는 network에 비해 특별한 성질을 갖추고 있어야만, small-worldness를 갖추고 있는 것이 되죠.

### python implementation 

- networkx 내의 `nx.random_reference(G)`를 사용해도 되지만, 이해를 위해서 직접 만들어 봤습니다. 
- 코드 내에 주석을 나름 상세하게 달았기 때문에, 읽어보시면 어느 정도 이해될 것이라고 생각해요.

```python 
import networkx as nx
import numpy as np

def custom_equivalent_random_network(G, niter=1, connectivity=True, seed=None):
    """
    - `G`의 node degree들을 그대로 유지하고, edge만을 변경하여 리턴함. 
    """
    RandomGenerator = np.random.RandomState(seed=seed)
    G = G.copy()
    nodes, degrees = zip(*G.degree())  # keys, degree
    # degree의 값에 따라서, node를 선정함.
    # nx.random_reference 에서는 cdf를 사용했으나, 차이가 없고 더 직관적이므로 pdf를 사용함.
    # degree가 클수록 edge가 바뀔 가능성이 크며,
    pdf_by_degree = [d/sum(degrees) for d in degrees]

    # niter: niter 개의 edge exchange를 시도함.
    niter *= int(len(G.edges()))

    # ntries: 매 edge exchange 시도 때마다 몇번까지 시도할 것인가,
    # 가령, 확률적으로 어떤 경우에는 valid한 edge exchange가 없을 수 있음.
    # 1) 서로 다른 a,b,c,d,가 없거나, 2) 어떻게 잘라도 connectivity가 깨지거나.
    # 따라서, 어떤 횟수까지만 시도하고, 넘어갈 경우에는 그냥 edge를 교환하지 못해도 그냥 넘어감.
    # 이 부분은 기존 nx.random_reference에 있는 값을 그대로 참고함.
    ntries = int(len(G)*len(G.edges()))
    ntries/= int(len(G)*(len(G)-1)/2)
    ntries = int(ntries)

    # edge_exchange_count: 성공한 edge exchange의 수를 셈.
    edge_exchange_count = 0
    for i in range(0, niter):
        for j in range(0, ntries):
            # degree dist에 따라, 클수록 확률이 높도록 서로 다른 두 노드를 선택함.
            # 엄밀히 따지면, 이렇게 2개를 뽑을 때의 확률은 각각 뽑을 때의 확률과 다름.
            # 하지만 귀찮으므로 그냥 이렇게 함.
            a, b = RandomGenerator.choice(nodes,
                                          size=2,
                                          p=pdf_by_degree,
                                          replace=False)
            # new_b_nbr: uniform하게 선정된 a의 neighbor
            new_b_nbr = RandomGenerator.choice(list(G[a]), size=1)[0]
            # new_a_nbr: uniform하게 선정된 b의 neighbor
            new_a_nbr = RandomGenerator.choice(list(G[b]), size=1)[0]
            # 따라서, 이 과정에서 문제가 없기 위해서는, a, b, c, d 모두 서로 달라야 함.
            # 이미 a!=b, a!=c, b!=d 의 조건은 만족하며,
            # a!=d, b!=c, c!=d 인지 체크하는 것이 필요함.
            if (a != new_a_nbr) and (b != new_b_nbr) and (new_b_nbr != new_a_nbr):
                # 또한, 이미 연결되어 있는 것이 아닐때, edge exchange가 가능함.
                if (new_a_nbr not in G[a]) and (new_b_nbr not in G[b]):
                    # a, b, c, d가 모두 다르고, 이미 연결되어 있는 것이 아니므로, edge exchange가 가능함.
                    # edge를 교환함:
                    # (a - new_a_nbr) ==> (a - new_b_nbr),
                    # (b - new_b_nbr) ==> (b - new_a_nbr)
                    G.add_edge(a, new_a_nbr)
                    G.add_edge(b, new_b_nbr)
                    G.remove_edge(a, new_b_nbr)
                    G.remove_edge(b, new_a_nbr)

                    # argument에서 connectivity가 유지되도록 설정한 경우
                    if connectivity==True and nx.is_connected(G) is True:
                        # edge를 exchange해도 connectivity가 유지되므로 valid G
                        edge_exchange_count+=1
                        break
                    else:
                        # connectivity가 유지되지 않으므로, edge exchange에 실패함.
                        # 따라서 기존의 G로 돌아감.
                        G.remove_edge(a, new_a_nbr),
                        G.remove_edge(b, new_b_nbr),
                        G.add_edge(a, new_b_nbr),
                        G.add_edge(b, new_a_nbr)
                        continue
        ### each exchange range(0, ntri)
    ### edge exchange range(0, ntries)
    # print(f"{niter} exchange try, {edge_exchange_count} edge exchange success")
    return G

########################
# small-world graph
# 엄밀히 따지면, small-world는 아니지만 그냥 씁니다.
small_world_G = nx.karate_club_graph()
assert nx.is_connected(small_world_G) == True

########################
# random_network 
clustering_coef_lst = []
shrt_pth_l_lst = []
for i in range(0, 10):
    # equivalent random network를 만들고,
    equiv_random_G = custom_equivalent_random_network(small_world_G, seed=i)
    assert nx.is_connected(equiv_random_G) == True
    clustering_coef_lst.append(nx.average_clustering(equiv_random_G))
    shrt_pth_l_lst.append(nx.average_shortest_path_length(equiv_random_G))
print("--" * 20)
print("== small world")
print(f"average clustering : {nx.average_clustering(small_world_G)}")
print(f"average shrt path l: {nx.average_shortest_path_length(small_world_G)}")
print("--" * 20)
print("== average from random networks")
print(f"avg clustering   from random networks: {np.mean(clustering_coef_lst)}")
print(f"avg short path l from random networks: {np.mean(shrt_pth_l_lst)}")
print("--" * 20)
```

- 위 코드의 실행 결과를 보면, 기존의 small world에 비해서, random network들의 경우 clustering 값이 크게 떨어지는 것을 알 수 있습니다. 
- 평균 최단거리의 경우, 큰 오히려 random network들의 평균이 더 적은데, 이는 제가 처음에 설정한 small-world G가 진정한 의미에서 small-world graph가 아니기 때문이겠죠.

```
----------------------------------------
== small world
average clustering : 0.5706384782076823
average shrt path l: 2.408199643493761
----------------------------------------
== average from random networks
avg clustering   from random networks: 0.3520240030058369
avg short path l from random networks: 2.2395721925133687
----------------------------------------
```


## wrap-up

- 오늘 한 것은, equivalent random network를 만들어 본 것입니다. 
- 여담이지만, small-worldness를 갖춘 네트워크는 `networkx`에 있는 generator를 사용한다고 해도, 생각만큼 좋은 small-world network로 나오는 것 같지는 않아요.

## reference

- [Small-world_network](https://en.wikipedia.org/wiki/Small-world_network)