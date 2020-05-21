---
title: paper-summary - Universal Behavior of Load Distribution in Scale-Free Networks
category: paper-summary
tags: paper-summary scale-free-network network load-centrality betweenness-centrality
---

## Universal Behavior of Load Distribution in Scale-Free Networks

- 제목을 해석한다면, "Scale-free network에서 Load 분포의 범용적 특성"정도가 되겠네요. load centrality에 대해서 정리하던 중에, betweennes centrality와의 특별한 차이가 없는 것 같아서, 자료를 찾다가 이 논문을 발견하게 되었습니다. 
- 무려, 2001년에 나온 논문이며, 서울대 이론물리학 연구소에서 작성했습니다.
- [논문링크](http://phya.snu.ac.kr/~dkim/PRL87278701.pdf)

## Abstract Summary 

> We study a problem of data packet transport in scale-free networks whose degree distribution follows a power law with the exponent `gamma`. 
- 우리는 scale-free network(degree distribution이 `gamma`의 지수를 가지는 power law를 따르는 네트워크)에서 data packet 전송 문제를 연구하고 있다.

> Load, or “betweenness centrality,” of a vertex is the accumulated total number of data packets passing through that vertex when every pair of vertices sends and receives a data packet along the shortest path connecting the pair. 
- vertex의 Load, betweenness centrality는 "모든 vertex의 pair 가 data packet을 그들간의 shortest path를 통해서 주고 받을 때, 축적되는 data packet을 말한다". 

> It is found that the load distribution follows a power law with the exponent `delta` ~= 2.2, insensitive to different values of `gamma` in the range(2, 3) and different mean degrees, which is valid for both undirected and directed cases. 
- load distribution은 `gamma`가 2, 3 사이에 어떤 값이든, `delta`가 2.2에 근사하는 power law를 따른다는 것을 발견했으며, 이는 방향성이 있는 네트워크와 없는 네트워크와 무관하다.

>  Thus, we conjecture that the load exponent is a universal quantity to characterize scale-free networks.
- 따라서, 우리는 scale-free network의 특성을 규정하는 범용적인 특성(quantity)로 load exponent를 추측한다(conjecture).

## And more.

> To be specific, we suppose that a data packet is sent from a vertex i to j, for every ordered pair of vertices i, j. For a given pair i, j, it is transmitted along the shortest path between them. If there exist more than one shortest paths, the data packet would encounter one or more branching points. In this case, we assume that the data packet is divided evenly by the number of branches at each branching point as it travels. 
- 분명히 말하자면, data packet이 i에서 j로 보내질 때, 그들간의 최단거리(shortest path)를 통해 전송된다. 하지만, 만약, 최단거리가 여러 개 있을 경우, 여러개에 따라서 나누어져 전송된다.

> Then we define the load k at a vertex k as the total amount of data packets passing through that vertex k when all pairs of vertices send and receive one unit of data packet between them.
- 이렇게 할 경우, vertex k에 있는 `load`는 그 vertext를 지난 모든 data packet이 될 것이다.


## wrap-up

- 개념상으로, 'load centrality는 패킷을 나누어 전송할때, 각 노드 혹은 엣지에 걸리는 부하를 측정한다'는 것을 목적으로 하죠. 따라서, 각 노드 등에서 전송해야 하는 packet의 크기가 다르다면, 이 node의 centrality가 다르게 측정되겠지만, 모든 node가 동일한 weight를 가지고 있다고 할때, load centrality는 betweenness centrality와 별 차이가 없는 것 같아요.