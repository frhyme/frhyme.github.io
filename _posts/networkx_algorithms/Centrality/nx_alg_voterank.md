---
title: networkx - voterank
category: python-libs
tags: python python-libs networkx centrality voterank
---

## problem. 

- 원래 논문에 있는 내용대로면, voting ability가 0이 되어서는 안됨. 하지만, `nx.vote_rank`에서는 종종 0이 되는 경우들이 있음. 
- 따라서, 이거 잘못된 것 아니냐, 라고 문의를 날린 상황임. [이슈 링크](https://github.com/networkx/networkx/issues/3826)

As the vote_rank algorithm was written in the origianl paper Identifying a set of influential spreaders in complex networks, the voting ability of already elected nodes have to be zero.

But, in networkx.vote_rank, the voting ability of already elected node could be negative value.
To check if the voting ability could be negative value, I copied the code of nx.vote_rank from networkx documentation, and add simple code that print node having negative value.

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

the output of code execution is below. Some nodes have definitely negative value. And also, nodes that have negative voting ability are already elected nodes.
Therefore, the result of nx.vote_rank could be little different with the origianl vote rank algorithm.

```
1 -0.3333333333333333
1 -0.3333333333333333
1 -0.6666666666666666
2 -0.3333333333333333
7 -0.3333333333333333
```

If I am wrong, please let me know.

I always thanks for your support and networkx.





## reference

- [Identifying a set of influential spreaders in complex networks](https://www.nature.com/articles/srep27823)
- [networkx.algorithms.centrality.voterank](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.voterank.html#networkx.algorithms.centrality.voterank)