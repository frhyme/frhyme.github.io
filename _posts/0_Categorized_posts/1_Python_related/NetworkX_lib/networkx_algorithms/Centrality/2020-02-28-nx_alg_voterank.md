---
title: networkx - voterank
category: python-libs
tags: python python-libs networkx centrality voterank
---

## 2-line summary 

- `voterank`알고리즘은, 가령 influencer들을 통해 네트워크를 최대한 많이 커버하려고 할 때, 서로 겹치지 않게 influencer들을 선택하려면 어떻게 하는 것이 제일 좋은가? 를 보여준 알고리즘. 
- 그냥 "이웃들에게 반복적으로 투표를 하는 알고리즘"이며, 선택되고 나면 그 영역에서 투표하는 영향력을 약화시킨다 라는 것이 다임.


## what is voterank? 

- 무려 "Nature - Scientific Report"에 2016년 여름에 실린 논문에서 제시한 지표로서, [Identifying a set of influential spreaders in complex networks](https://www.nature.com/articles/srep27823)에서 자세한 내용을 볼 수 있습니다. 
- 복잡계(complex network)에서 영향력 있는 사람들(influencer or influential spreader)를 식별하는 것은 정보흐름을 효과적으로 제어하기 위해서 매우 중요합니다. 
- 이를 쉽게 말하자면, "만약 제가 인스타그램을 통해서 마케팅을 하고 싶고, 이미 인스타그램의 모든 following 관계를 알고 있고 이를 graph로 구현하였을 때, 어떤 influencer들을 선택하는 것이 서로 겹치지 않게 최대한 많은 영역을 커버하면서 마케팅할 수 있는 것인가?"를 해결하려고 한 것이죠. 
- 사실, 단순한 전략으로는, PageRank,ClusterRank, k-shell-decomposition 등을 통해서, 상위에 있는 노드들을 선택하는 것도 방법이 됩니다. 하지만, 이 문제들은 모두 nod들이 서로 가깝게 위치해 있을 수 있어서, 각자의 범위들이 겹칠 수 있다는 잠재적인 문제점을 가지게 되죠.
- 따라서 해당 논문에서는 서로 겹치지 않게 `voteRank`라는 비교적 단순한 알고리즘을 통해서, 분산화된 정보 전달자를 찾아나갑니다.
- 해당 논문 내에서는 실제 존재하는 다양한 네트워크를 대상으로 계산을 해봤고, 결과 뿐만 아니라, 속도도 월등한 것을 파악해냈죠.

## voteRank Algorithm. 

- `VoteRank`는 생각보다 매우 단순한, 알고리즘이며 대략 다음과 같습니다.
    1) 모든 노드에게는 `score`, `voting_ability`가 주어진다. 
    2) 노드는 자신의 이웃에게 그들의 `voting_ability`에 따라서, 투표를 한다(즉, 이웃의 `score`에 그들의 `voting_ability`를 더해준다. 나눠서 더하는 것이 아니라 그 값을 그대로 더해줌)
    3) 모든 노드들에 대해서 이를 진행하고 나면, `top_node`의 이웃들의 `voting_ability`를 감소시킨다. 
    4) 가장 높은 `score`를 가지는 node(`top_node`)를 제외하고, 다시 2)부터 돌아간다. 
    5) 모든 node가 제외되었거나, 가장 높은 score가 0이 되면, 알고리즘을 종료한다. 
- 코딩하는 것도 딱히 어렵지 않고, 개념도 명확하죠. 이미 `top_node` 이웃의 `voting_ability`를 감소하는 것이 핵심적인데, 해당 영역은 이미 `top_node`에 의해서 커버되므로, 자연스럽게 약화되고 있는 것으로 보면 됩니다. 
- 더 심플하게 보려면, 한 procedure가 끝날 때마다, `top_node` 자체를 graph에서 제거하면 더 직관적이죠.


## python implementation

- python으로 직접 코딩하였으며 코드는 다음과 같습니다.

```python
def voterank(G, number_of_nodes=None, max_iter=1000):
    """
    voteRank는 모든 노드들이 각자의 degree의 역수라는 voting ability를 가지고 
    주위의 이웃들에게 vote를 합니다 
    다만, 이 과정에서 가장 많은 투표를 받은(score가 가장 높은) top_node를 뽑고 나면,
    이 노드를 제외하고, 이웃 노드들의 voting ability를 약화시킵니다. 
    이를 반복하여, 더이상 voting이 진행되지 않을때까지 반복하여, 
    influencer들을 순차적으로 뽑아내는 알고리즘을 말하죠.
    """
    G = G.copy()
    avgDegree = sum(deg for _, deg in G.degree()) / float(len(G))
    reciprocal_avgDeg = 1.0 / avgDegree
    voteRank = []
    # step 1 - 
    # 처음에는 모든 node의 score가 0 이고, voting_ability가 1임.
    for n in G:
        G.nodes[n]['score'] = 0
        G.nodes[n]['voting_ability'] = 1
    # ITERATION Start 
    for _ in range(0, max_iter):
        # step 2: Set score zero
        # iteration이 돌고 나면 score가 변하므로 
        # 여기서 모든 node의 score를 0으로 다시 setting함.
        for n in G:
            G.nodes[n]['score'] = 0
        # step 3: Vote
        # 모든 node가 neighbor node들에게 현재의 voting ability를 줍니다.
        # 즉, nbr의 score에 node의 voting ability를 더해줍니다.
        for n in G:
            for nbr in G[n]:
                G.nodes[nbr]['score'] += G.nodes[n]['voting_ability']
        # step 4: select top node
        # 가장 score가 높은 node를 고릅니다. 
        # 그리고 top_node는 이미 선정되었으므로, 
        # top_node 이웃 노드들의 voting ability를 약화시킵니다. 
        top_node = max(list(G), key=lambda x: G.nodes[x]['score'])
        top_score = G.nodes[top_node]['score']
        for nbr in G.neighbors(top_node):
            G.nodes[nbr]['voting_ability'] -= reciprocal_avgDeg
        ####################################
        # iteration termination condition
        # 1) score가 0보다 큰 node가 없거나,
        # 2) 모든 node가 이미 voteRank에 추가되었거나.
        if top_score == 0 or (len(voteRank)==len(G)):
            return voteRank
        else:  
            # 가장 높은 score를 가진 아이를 voteRank에 넣어주고, 
            # 이제 G에서 필요없어지므로 지워줌.
            # 즉, 이 아이는 이제 투표도 하지 못하고 필요없어짐.
            voteRank.append(top_node)
            G.remove_node(top_node)
```

## little difference with `nx.voterank.`

- 다만, 코딩을 하고 결과를 비교하는데 networkx에 이미 구현된 `nx.voterank`와 결과를 비교해보는데, 자꾸만 답이 조금씩 다르게 나오는 겁니다. 논문을 보고, 코드를 보도, 잘못된 부분이 없거든요.
- 그래서 보니까, 원래 논문에 있는 내용대로라면, voting ability가 0이 되어서는 안됩니다. 하지만, `nx.vote_rank`에서는 종종 0이 되는 경우들이 있습니다. 즉, 일단 제가 보기에는 해당 라이브러리에 오류가 있는 것이죠. 
- 따라서, 이거 잘못된 것 아니냐, 라고 이슈를 날렸습니다. 

### issue 

- [I think `nx.vote_rank` make wrong result.](https://github.com/networkx/networkx/issues/3826)로 남겼으며, 대략적인 글은 다음과 같습니다.
- 다만, 이슈를 남긴지 시간이 꽤 오래되었는데, 아직 답이 없네요ㅠㅠ


> As the `vote_rank` algorithm was written in the origianl paper Identifying a set of influential spreaders in complex networks, the voting ability of already elected nodes have to be zero.

> But, in `networkx.vote_rank`, the voting ability of already elected node could be negative value. To check if the voting ability could be negative value, I copied the code of nx.vote_rank from `networkx` documentation, and add simple code that print node having negative value.

```python
def voterank(G, number_of_nodes=None, max_iter=10000):
    voterank = []
    if len(G) == 0:
        return voterank
    if number_of_nodes is None or number_of_nodes > len(G):
        number_of_nodes = len(G)
    avgDegree = sum(deg for _, deg in G.degree()) / float(len(G))
    # step 1 - initiate all nodes to (0,1) (score, voting ability)
    for _, v in G.nodes(data=True):
        v['voterank'] = [0, 1]
    # Repeat steps 1b to 4 until num_seeds are elected.
    for _ in range(max_iter):
        # step 1b - reset rank
        for _, v in G.nodes(data=True):
            v['voterank'][0] = 0
        ####################################
        ####################################
        # this code was added by me to check if voting ability is negative
        for n in G:
            node_voting_ability = G.nodes[n]['voterank'][1]
            if node_voting_ability < 0.0:
                print(n, node_voting_ability)
        ####################################
        ####################################
        # step 2 - vote
        for n, nbr in G.edges():
            G.nodes[n]['voterank'][0] += G.nodes[nbr]['voterank'][1]
            G.nodes[nbr]['voterank'][0] += G.nodes[n]['voterank'][1]
        for n in voterank:
            G.nodes[n]['voterank'][0] = 0
        # step 3 - select top node
        n, value = max(G.nodes(data=True), key=lambda x: x[1]['voterank'][0])
        if value['voterank'][0] == 0:
            return voterank
        voterank.append(n)
        if len(voterank) >= number_of_nodes:
            return voterank
        # weaken the selected node
        G.nodes[n]['voterank'] = [0, 0]
        # step 4 - update voterank properties
        for nbr in G.neighbors(n):
            G.nodes[nbr]['voterank'][1] -= 1 / avgDegree
    return voterank

N = 10
G = nx.scale_free_graph(n=N, seed=0)
# Digraph => Graph
G = nx.Graph(G)
# remove self-loop
G.remove_edges_from([(u, v) for u, v in G.edges() if u==v])
assert nx.is_connected(G)
voterank(G)
```

> the output of code execution is below. Some nodes have definitely negative value. And also, nodes that have negative voting ability are already elected nodes. Therefore, the result of nx.vote_rank could be little different with the origianl vote rank algorithm.

```
1 -0.3333333333333333
1 -0.3333333333333333
1 -0.6666666666666666
2 -0.3333333333333333
7 -0.3333333333333333
```

> If I am wrong, please let me know. I always thanks for your support and networkx.


## reference

- [Identifying a set of influential spreaders in complex networks](https://www.nature.com/articles/srep27823)
- [networkx.algorithms.centrality.voterank](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.voterank.html#networkx.algorithms.centrality.voterank)
- [I think `nx.vote_rank` make wrong result.](https://github.com/networkx/networkx/issues/3826)