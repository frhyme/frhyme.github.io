---
title: networkx - community detection - measuring partition(coverage, performance)
category: python-libs
tags: python python-libs networkx community community-detection
---

## intro - community evaluation.

- graph에서 내부에 존재하는 다양한 소그룹, 이른바 community를 뽑아내었다고 해봅시다. 가령 "방법1로 community를 도출한 경우", "방법2로 community를 도출한 경우"라는 두 가지 경우가 있고 그 결과들이 다르다고 할때, 그 두 결과를 어떻게 비교할 수 있을까요? 
- 이 글에서는, `coverage`와 `performance`를 제시합니다. 


## community quality - `coverage` 

- [coverage](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.quality.coverage.html#networkx.algorithms.community.quality.coverage)는 "community들이 기존의 Graph가 가지고 있던 edge를 얼마나 커버할 수 있느냐?"를 의미합니다. Graph를 N개의 community(혹은 subgraph)로 분화하게 되면, 자연스럽게 community간의 edge는 없어지게 되죠. 즉, "(community들 내부에 존재하는 모든 edge의 수)/ (Graph의 모든 edge의 수)"가 coverage입니다. 
- 당연하지만, community의 수가 많아질수록 작아지게 되겠죠. 코드는 다음과 같습니다.

```python
def intra_community_edges_count(G, partition):#A
    """
    A : community 내의 모든 edge의 수의 합
    """
    r = 0
    for comm in partition:
        comm_edges = nx.subgraph(G, comm).edges()
        r += len(comm_edges)
    return r
def custom_coverage(G, partition):
    """
    - A: 모든 community들의 intra edge의 수들을 합
    - B: G의 모든 edge의 수 
    - return A/B
    - girvan-newman method를 사용해서 계층적으로 분화를 진행한다고 할 때, 
    `B`는 고정되어 있는 반면, `A`는 작아지므로, 점점 값이 작아지게 됨. 
    - `nx.algorithms.community.coverage(G, partition)`와 동일함.
    """
    return intra_community_edges_count(G, partition) / len(G.edges())
```

## community quality - `performance`

- [Performance](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.quality.performance.html#networkx.algorithms.community.quality.performance)는 A(community 내의 모든 edge의 수)와 B(community간에 존재하지 않는 edge의 수) 를 더하고, 이를 C(모든 Node간에 발생가능한 모든 edge의 수)로 나눕니다. 
    - 분화가 진행되어도(community가 많아져도), 
    - `C`는 `(Node_size-1)*(Node_size)//2`로 고정되어 있습니다.
    - 반면 `A`의 경우 "community들 내에 존재하는 edge의 총 수" 이므로, 점점 작아지죠. 
    - 그러나, `B`의 경우는, "community 간에 존재하지 않는 edge의 수", 즉, "(community 간에 발생가능한 모든 edge의 수) - (실제 존재하는 community간 edge의 수)"를 말합니다. community간에 edge가 적을수록, 이는 community를 나눈 것이 합당하다는 말이 되죠. community 간에 edge가 없을수록 더해지는 값이 커지므로 `B`는 커지게 되며, node의 수만큼 나누어졌을 때, 가장 커지게 됩니다.
- 만약 `com_1`을 `com_1_1`과 `com_1_2`로 나누게 되고, `com_1_1`과 `com_1_2` 사이에는 `l`개의 edge가 있다고 합시다. 그렇다면 다음과 같이 값이 변화하죠. 
    - A' = A - `l`
    - B' = (`com_1_1`과 `com_1_2` 사이의 모든 possible edge) - `l`
- python code로 보면 다음과 같습니다.

```python
def inter_community_non_edges_count(G, partition):  #B
    """
    B : community 간에 존재하지 않는 edge의 수. 
    community간 edge의 수가 적을수록 B는 커짐.
    """
    G_complement = nx.complement(G)
    r = 0
    for comm1, comm2 in itertools.combinations(partition, 2):
        for n1 in comm1:
            for n2 in comm2:
                if n1 in G_complement[n2]:
                    # n1 and n2 adjacent
                    r += 1
    return r
def custom_performance(G, partition):
    """
    Return performance of partition.
    A: 모든 community들의 intra-edge의 수의 합 
    B: community 들 사이에 존재하지 않는 모든 edge(non-edge)의 수의 합
    C: G에서 존재 가능한 모든 edge의 수 => complete graph edge count
    return (A+B)/C
    - 분화가 진행어도 `C`는 고정되어 있고, `A`는 값이 점점 줄어들게 됨.
    반면, `B`의 경우, community들간에 edge가 많지 않을 수록 값이 커짐
    다시 말하면, 이는 community들이 서로 독립적일수록 값이 커지게 되는 것인데, 
    node가 n개일 때, n개의 community들로 분화한다고 하면, 값이 당연히 커지게 됨
    - `nx.algorithms.community.performance(G, partition)`와 동일함.
    """
    #=================================
    A = intra_community_edges_count(G, partition)
    B = inter_community_non_edges_count(G, partition)
    C = len(G)*(len(G)-1)//2
    return (A+B)/C
```


## Compute `coverage` and `performance`

- 이제 `coverage`와 `performance`를 계산해봅니다. `networkx`에서 이미 제공하기는 하지만, 직접 코딩을 해봅니다.

```python
print("==" * 20)
print("== community detection by edge betweenness centrality")
community_generator = nx.algorithms.community.girvan_newman(G=G)

print("== Coverage and its Performance")
for i, partition in enumerate(community_generator):
    # n개의 node가 있을 때, n개의 community까지 분화할 수 있으므로,
    # n개로 분화되면 loop 탈출.
    # 발생한 Partition(=community set)에 대해서 지표를 측정. 
    partition_coverage = custom_coverage(G, partition)
    partition_performance = custom_performance(G, partition)
    A = intra_community_edges_count(G, partition)
    B = inter_community_non_edges_count(G, partition)
    print(
        f"{i:2d} time :: Coverage: {partition_coverage:.4f}, Performance: {partition_performance:.4f}, A: {A:3d}, B: {B:3d}"
    )
    if False: #print all communities?
        for j, comm in enumerate(partition):
            print(f"community {j:2d} at time {i:2d} ==> {comm}")
print("==" * 20)
```

```
========================================
== community detection by edge betweenness centrality
== Coverage and its Performance
 0 time :: Coverage: 0.9677, Performance: 0.3421, A:  30, B:  35
 1 time :: Coverage: 0.8065, Performance: 0.6316, A:  25, B:  95
 2 time :: Coverage: 0.7742, Performance: 0.6842, A:  24, B: 106
 3 time :: Coverage: 0.7419, Performance: 0.7316, A:  23, B: 116
 4 time :: Coverage: 0.7097, Performance: 0.7737, A:  22, B: 125
 5 time :: Coverage: 0.6774, Performance: 0.8105, A:  21, B: 133
 6 time :: Coverage: 0.5161, Performance: 0.8632, A:  16, B: 148
 7 time :: Coverage: 0.4839, Performance: 0.8737, A:  15, B: 151
 8 time :: Coverage: 0.4516, Performance: 0.8842, A:  14, B: 154
 9 time :: Coverage: 0.4194, Performance: 0.8895, A:  13, B: 156
10 time :: Coverage: 0.3871, Performance: 0.8947, A:  12, B: 158
11 time :: Coverage: 0.3548, Performance: 0.8947, A:  11, B: 159
12 time :: Coverage: 0.2903, Performance: 0.8895, A:   9, B: 160
13 time :: Coverage: 0.2258, Performance: 0.8789, A:   7, B: 160
14 time :: Coverage: 0.1935, Performance: 0.8737, A:   6, B: 160
15 time :: Coverage: 0.1613, Performance: 0.8684, A:   5, B: 160
16 time :: Coverage: 0.0968, Performance: 0.8579, A:   3, B: 160
17 time :: Coverage: 0.0645, Performance: 0.8526, A:   2, B: 160
18 time :: Coverage: 0.0323, Performance: 0.8474, A:   1, B: 160
========================================
```

## wrap-up

- 개념적으로 보면, `coverage`는 "원래 Graph를 edge 측면에서 얼마나 커버하는가?"를 의미하고, `performance`는 "coverage를 고려하면서도, 새로운 community를 만드는 것이 얼마나 이득인지"를 평가하고 있다고 할 수 있겠네요.
- 또한, `modularity`라는 지표도 있는데, 이는 조금 내용이 길어질 수 있어서, 다른 글에서 처리하겠습니다.



## raw-code

```python
import networkx as nx
import itertools

# Generate graph
N = 20
G = nx.scale_free_graph(N, seed=0)
G = nx.Graph(G)

assert nx.is_connected(G)==True


def intra_community_edges_count(G, partition):  #A
    """
    A : community 내의 모든 edge의 수의 합
    """
    r = 0
    for comm in partition:
        comm_edges = nx.subgraph(G, comm).edges()
        r += len(comm_edges)
    return r

def inter_community_non_edges_count(G, partition):  #B
    """
    B : community 간에 존재하지 않는 edge의 수. 
    community간 edge의 수가 적을수록 B는 커짐.
    """
    G_complement = nx.complement(G)
    r = 0
    for comm1, comm2 in itertools.combinations(partition, 2):
        for n1 in comm1:
            for n2 in comm2:
                if n1 in G_complement[n2]:
                    # n1 and n2 adjacent
                    r += 1
    return r


def custom_coverage(G, partition):
    """
    - A: 모든 community들의 intra edge의 수들을 합
    - B: G의 모든 edge의 수 
    - return A/B
    - girvan-newman method를 사용해서 계층적으로 분화를 진행한다고 할 때, 
    `B`는 고정되어 있는 반면, `A`는 작아지므로, 점점 값이 작아지게 됨. 
    - `nx.algorithms.community.coverage(G, partition)`와 동일함.
    """
    return intra_community_edges_count(G, partition) / len(G.edges())

def custom_performance(G, partition):
    """
    Return performance of partition.
    A: 모든 community들의 intra-edge의 수의 합 
    B: community 들 사이에 존재하지 않는 모든 edge(non-edge)의 수의 합
    C: G에서 존재 가능한 모든 edge의 수 => complete graph edge count
    return (A+B)/C
    - 분화가 진행어도 `C`는 고정되어 있고, `A`는 값이 점점 줄어들게 됨.
    반면, `B`의 경우, community들간에 edge가 많지 않을 수록 값이 커짐
    다시 말하면, 이는 community들이 서로 독립적일수록 값이 커지게 되는 것인데, 
    node가 n개일 때, n개의 community들로 분화한다고 하면, 값이 당연히 커지게 됨
    - `nx.algorithms.community.performance(G, partition)`와 동일함.
    """
    #=================================
    A = intra_community_edges_count(G, partition)
    B = inter_community_non_edges_count(G, partition)
    C = len(G)*(len(G)-1)//2
    return (A+B)/C

#================================


print("==" * 20)
print("== community detection by edge betweenness centrality")
community_generator = nx.algorithms.community.girvan_newman(G=G)

print("== Coverage and its Performance")
"""
- coverage는 community 분화를 진행할수록 작아질 수 밖에 없음
    - community 들이 분화되면서, community 내부에 존재하는 edge의 수 또한 작아지기 때문
- performance는 
"""
for i, partition in enumerate(community_generator):
    # n개의 node가 있을 때, n개의 community까지 분화할 수 있으므로,
    # n개로 분화되면 loop 탈출.
    partition_coverage = custom_coverage(G, partition)
    partition_performance = custom_performance(G, partition)
    A = intra_community_edges_count(G, partition)
    B = inter_community_non_edges_count(G, partition)
    print(
        f"{i:2d} time :: Coverage: {partition_coverage:.4f}, Performance: {partition_performance:.4f}, A: {A:3d}, B: {B:3d}"
    )
    if False: #print all communities?
        for j, comm in enumerate(partition):
            print(f"community {j:2d} at time {i:2d} ==> {comm}")
print("==" * 20)

```