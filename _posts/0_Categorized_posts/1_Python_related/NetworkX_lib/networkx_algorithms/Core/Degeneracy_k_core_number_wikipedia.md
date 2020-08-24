---
title: Degeneracy(graph theory) in wikipedia(번역)
category: others
tags: network graph-theory Degeneracy
---

## line summary 

- 

## Degeneracy or k-core.

- Degeneracy는 "퇴화"를 의미합니다. ~~~ 
- graph theory에서 k-degenerate graph는 보통, "모든 subgraph는 최대 `k`의 degree만을 가진다"라는 성질을 만족하는 undirected network를 말합니다. 이는 다시 "어떤 노드도, `k`보다 큰 degree를 가질 수는 없는 것이죠"


In graph theory, a k-degenerate graph is an undirected graph in which every subgraph has a vertex of degree at most k: that is, some vertex in the subgraph touches k or fewer of the subgraph's edges. The degeneracy of a graph is the smallest value of k for which it is k-degenerate. The degeneracy of a graph is a measure of how sparse it is, and is within a constant factor of other sparsity measures such as the arboricity of a graph.

Degeneracy is also known as the k-core number,[1] width,[2] and linkage,[3] and is essentially the same as the coloring number[4] or Szekeres-Wilf number (named after Szekeres and Wilf (1968)). k-degenerate graphs have also been called k-inductive graphs.[5] The degeneracy of a graph may be computed in linear time by an algorithm that repeatedly removes minimum-degree vertices.[6] The connected components that are left after all vertices of degree less than k have been removed are called the k-cores of the graph and the degeneracy of a graph is the largest value k such that it has a k-core.

## what is k-core? 

- graph `G`의 `k-core`는 "`G`의 maximal connected subgraph이며, 모든 vertex가 최소한 `k`의 degree를 가지는 것을 말합니다. 따라서, 이는 `k`보다 degree가 작은 node를 순차적으로 삭제하면서 생성되는 connected component와 같죠. 
- 만약, 이 때, `k-core`가 존재한다면, graph `G`는 최소한 `k`의 degeneracy를 가진다고 할 수 있습니다. 그리고, 가장 크게 만들 수 있는 `k`가 바로 `G`의 degeneracy라고 할 수 있는 셈이죠. 
- 즉, 만약 graph `G1`으로 만들 수 있는 가장 큰 값의 `k-core`가 `4-core`라면, `G1`의 degeneracy는 4가 되는 것이죠.
- k-core의 개념은, 소셜 네트워크 내에서 밀집된 구조(clustering structure)를 소개하기 위해서 사용되었고, 추가로, random graph의 진화과정을 묘사하기 위해서도 사용되었습니다. 이는 이후, 생명정보학이나, 네트워크 시각화, 인터넷 구조, 경제 위기의 전파, 영향력있는 influencer의 식별, 등 매우 다양한 분야에서 사용되었죠. 
- 즉, clustering, community등도 있지만, graph-pruning을 하는 가장 기본적인 방법이다, 라고 말씀드릴 수 있겠네요.


### what is difference with `node degree`?

- 가끔, `k-core`가 `node degree`와 무슨 차이가 있냐? 라고 생각하시는 분들이 있어서, 조금 더 써보겠습니다. 
- graph `G`에 isolated_node가 없다면, `G`는 이미 "1-core"입니다. 모든 노드가 1이상의 degree를 가지니까요. 
- 그렇다면, 이제 "2-core"를 찾아보겠습니다. 그러려면, 일단 degree가 1인 놈들을 잘라나가야겠죠. 그런데, 이를 잘라나가다보면, 다른 노드들의 degree도 작아집니다. 당연하지만, 모든 edge는 혼자 존재하는 것이 아니니까요. 어떤 노드를 삭제하면 edge도 날아가고, 당연히, 다른 노드들의 degree도 작아집니다. 따라서, 가령 node `u`의 degree가  "5"였다고 해도, 낮은 degree의 node를 잘라나가는 과정에서, node `u`의 degree는 이미 "5"가 아닐 수 있습니다. 그렇다면, 이제 이 `G`에서 `5-core`는 없다고 봐도 되는 것이죠. 
- 다시 말하지만, "`k-core`는 "graph `G`의 subgraph인 `subG`이며, `subG`의 모든 vertext의 degree는 최소한 `k`보다 커야 합니다". 


## reference 

- [Degeneracy_(graph_theory)](https://en.wikipedia.org/wiki/Degeneracy_(graph_theory))