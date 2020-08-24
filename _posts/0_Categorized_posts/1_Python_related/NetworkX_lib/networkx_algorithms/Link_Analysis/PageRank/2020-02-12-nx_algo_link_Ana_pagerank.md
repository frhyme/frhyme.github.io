---
title: networkx - Link Analysis - PageRank
category: python-libs
tags: python python-libs networkx centrality Pagerank 
---

## 2-line summary for PageRank

- [pagerank](https://en.wikipedia.org/wiki/PageRank)는 "(web)Page의 순위(Rank)를 매기는 방법"을 말하며, page를 노드로 in-link, out-link를 edge로 고려하여 그래프를 만들고, 그래프에 기반해 node의 순위를 매기는 방식.
- 계산적으로 보면 [SimRank](https://en.wikipedia.org/wiki/SimRank) 비슷해보이지만, 관점이 다름. 아무튼 "방향성이 있는 네트워크"에서 노드의 영향력을 측정하는 방법.

## What is Page Rank. 

- PageRank 알고리즘의 기본 가정은 "중요한 object일수록 다른 (object)들로부터 follow를 많이 받을 것이며, 중요한 object들로부터 가치있는 follow를 받을 수록 중요한 노드이다" 정도로 말할 수 있습니다.
- 요즘은 인스타그램을 많이 해서 이를 통해서 설명을 하자면, 
    - 지드래곤은 아주 많은 사람들로부터 팔로우를 받지만, 아무도 팔로우하지 않는다.
    - 만약, 지드래곤이 극소수의 몇명을 팔로우한다면, 지드래곤의 팔로워들 또한, 그 사람을 알게 될 가능성이 높다. 
    - 이처럼, 마치 "물이 흐르는 것"처럼, 중요한 노드가 팔로우 할수록 많은 사람들이 그 노드로 향하게 된다. 
- 즉, 인스타그램 계정, 웹페이지 등을 모두 노드로 표현하고, 그 팔로윙 관계를 edge로 표현한다고 했을 때, 그 위를 어떤 random walk들이 마구 걸어다니고, 지나간 node의 비율, 그것이 바로 pagerank입니다. 

### Some assumption in PageRank 

- 앞서 말한 것과 같이, 그냥 "graph에서 random한 walk가 마구 발생한다고 할때, walk에 node들이 포함될 비율"이 pagerank인 셈이죠. 다만, 다음과 같은 몇 가지 가정, 혹은 설정이 있습니다. 
- `Damping factor(alpha)`: "사람 A가 웹페이지들을 마구 돌아다니다가, 어떤 페이지를 찾고, 멈출 수 있다"를 가정하고, (1-alpha)의 확률로 해당 노드에서 멈춤. 즉, (1-alpha)의 확률로 random walk가 중단됨. 
- `Personalization`: Random walk를 발생할 때, 어떤 노드로부터 walk가 발생하는지, 확률로 정의. 가령 `{"n1": 0.5}`와 같은 식으로. 
- `Dangling`: graph `G`에서 어떤 노드의 경우 in-edge는 있지만, out-edge는 없는 경우가 있음. 즉, 이런 경우에는 random walk가 진행되다가 `Damping factor`와 관계없이 멈춰야 함. 이런 노드를 dangling node라고 하며, 이 때, random walk를 멈추는 것이 아니라, 다른 node로 random하게 움직인다고 생각함. 
    - 이는 마치 "위키피디아에 막 돌아다니다가, 더이상 하이퍼링크가 없는 페이지(dangling node)에 도달했을 때, 다시 아무 페이지로 랜덤하게 접근한다"라고 생각해도 상관없음.
    - 보통 이 값은 `Personalization`과 동일하게 세팅.

## Compute PageRank.

- 자, 계산을 해보겠습니다. 
- 우선, 사실 더 빠르고 효율적으로 계산하려면 power iteration을 쓰거나, matrix 연산으로 하는 것이 더 빠르지만, 저는 아주 쉽게 설명하기 위해서, 그냥 random walk를 만들어서, 그 비율을 직접 계산하는 방식으로 처리했습니다. 그래서, 이해가 더 쉬울 것 같아요. 
- 자세한 내용은 아래 python code에 주석으로 처리하였습니다.

```python 
import networkx as nx
import numpy as np


np.random.seed(0)

def custom_pagerank(G, alpha, personalization, num_random_walks=10**3, dangling=None):
    # pagerank value.
    node_pg_dict = {n: 0.0 for n in G}
    #------------------------------------
    # alpha: range(0, 1), damping factor
    # "A라는 사람이 어떤 node에 도달했을 때, 이탈율".
    # 가령, 0.85라면 85%의 확률로 다른 노드로 움직이고, 15%의 확률로 walk를 멈춤.
    #------------------------------------
    # personlaization:
    # pagerank를 예측하기 위해서, random walk를 만든다고 할 때,
    # 어떤 node에서부터 출발하게 되는지 확률을 의미함.
    # 합이 1.0이 되도록 normalization
    personalization_norm = list(personalization.values())
    personalization_norm = np.array(personalization_norm) / np.sum(
        personalization_norm)
    #------------------------------------
    # dangling: dict(node: probablity)
    # 여기서는 구현하지 않았지만, dangling은 {node: probability}로 표현됨.
    # Graph의 경우, in-edge는 있지만, out-edge는 없는 경우들이 있음.
    # 이런 경우에 대해서, random하게 다른 모든 노드들로부터 다시 출발하도록 하는 경우를 의미함.
    # default => personlaization과 동일함
    if dangling is None:
        dangling_norm = personalization_norm
    else:
        dangling_norm = list(dangling.values())
        dangling_norm = np.array(dangling_norm) / np.sum(dangling_norm)

    #------------------------------------
    # num_random_walks:
    # random walk를 몇 개나 만들 것인지, 당연히 높을수록 converge.
    for _ in range(0, num_random_walks):  # each walk
        # personalization에 따라서, walk의 시작 node를 결정함.
        start_node = np.random.choice(G.nodes(),
                                      size=1,
                                      p=personalization_norm)[0]
        ########################################
        # Path from start_node generation
        new_path = [start_node]
        current_node = start_node
        while True:
            # alpha(damping factor)에 따라서, 계속 walk를 만들거나, 멈춤.
            move_to_nbrs_prob = np.random.random(1)
            if move_to_nbrs_prob < alpha:  # move to nbrs
                nbrs = G[current_node]
                if len(nbrs)==0:
                    # 들어오기만 하고 나가지 못하므로, dangling node
                    # 이 때는 다른 노드로부터 무작위로 시작함.
                    current_node = np.random.choice(G.nodes(),
                                                    size=1,
                                                    p=dangling_norm)[0]
                    new_path.append(current_node)
                else:
                    # 나가는 edge가 있으므로 uniform하게 선택하여 이동.
                    current_node = np.random.choice(list(nbrs), size=1)[0]
                    new_path.append(current_node)
            else:# stop
                break
        # Path generation done.
        ########################################
        #print(new_path)
        for n in new_path:
            node_pg_dict[n]+=1
    # value normalization
    norm = np.sum(list(node_pg_dict.values()))
    return {k: v/norm for k, v in node_pg_dict.items()}
##################################################################

N = 10
DG = nx.scale_free_graph(N, seed=0)
DG = nx.DiGraph(DG)

assert nx.is_weakly_connected(DG)==True

# Argument setting.
PESONALIZATION = {n: np.random.random(1)[0] for n in DG}
DANGLING = {n: np.random.random(1)[0] for n in DG}

print("==" * 20)
print("== nx.pagerank")
########################################
# nx.pagerank
pagerank_dict = nx.pagerank(G=DG,
                            alpha=0.85,
                            personalization=PESONALIZATION,
                            dangling=DANGLING)
print(pagerank_dict)
########################################
print("--"*20)
print("== custom pagerank")
cus_pg_dict = custom_pagerank(DG,
                              alpha=0.85,
                              personalization=PESONALIZATION,
                              dangling=DANGLING)
print(cus_pg_dict)
print("==" * 20)

```

- 위 코드의 실행결과는 다음과 같습니다. 
- 언뜻 보기에도, 대충 값이 비슷하죠.

```
========================================
== nx.pagerank
{0: 0.14954891677385104, 1: 0.2517095442222257, 2: 0.44756224741098555, 3: 0.020159092331299568, 4: 0.010848644049264344, 5: 0.01638209222679602, 6: 0.010809987947279236, 7: 0.04790292721282132, 8: 0.029263667007773095, 9: 0.01581288081770378}
----------------------------------------
== custom pagerank
{0: 0.14557620817843867, 1: 0.2533828996282528, 2: 0.451003717472119, 3: 0.01888475836431227, 4: 0.009516728624535316, 5: 0.015613382899628252, 6:0.012788104089219331, 7: 0.049516728624535315, 8: 0.028401486988847584, 9: 0.015315985130111525}
========================================
```

## wrap-up

- PageRank algorithm은 구글의 초기 알고리즘입니다만, 물론 지금은 훨씬 개선되고 복잡하겠죠. 그리고, harmonic centrality와 같이 local structure에 기반한 좋은 지표들도 요즘에는 많이 나오고 있습니다. 


## reference

- [networkx - pagerank](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html#networkx.algorithms.link_analysis.pagerank_alg.pagerank)
- [PageRank in wikipedia](https://en.wikipedia.org/wiki/PageRank)
- [Pagerank and HITS](https://lovit.github.io/machine%20learning/2018/04/16/pagerank_and_hits/)