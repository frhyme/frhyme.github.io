---
title: PaperSummary - Identifying a set of influential spreaders in complex networks
category: paper-summary
tags: paper-summary centrality 
---


## 2-line summary 


## Identifying a set of influential spreaders in complex networks

- 무려 "Nature - Scientific Report"에 2016년 여름에 실린 논문. 
- 해당 논문은 [여기에서](https://www.nature.com/articles/srep27823) 볼 수 있음.

## Abstract 번역 

- 복잡계(Complex network)에서 영향력 있는 사람들(influencer or influential spreader)를 식별하는 것은 효과적인 정보 흐름(effective information spreading)을 위해서 매우 중요하다.
- 가장 단순한 전략은, PageRank,ClusterRank, k-shell-decomposition 등을 통해서, 상위에 있는 노드들을 선택하는 것이며, 혹은 hill-climbing, SPIN, degree discount와 같은 다양한 방법들도 이미 제안되어 왔다. 
- 하지만, 앞서 언급한 이 모든 문제들은, 정보전달자(spreader)이 서로 가깝게 있어서, 각자의 범위가 겹칠 수 있다는 가능성을 가진다. 
- 본 리포트에서는, `VoteRank`라고 하는 비교적 단순한 방법을 사용해서, 가장 정보를 잘 전달할 수 있는 분산화된(decentralized) 정보전달자를 찾는다. 
- 이 접근 방법에서, 모든 
- 실제로, 실 세계의 네트워크들에 적용을 해보았으며, 여기서도 VoteRank는 기존의 방법들에 비해서, 전파속도(spreading rate)뿐만 아니라, 최종 전파 결과(fianl affected scale)까지 그리고, 계산 속도 자체도 훨씬 월등한 것을 파악했다.

A simple strategy is to choose top-r ranked nodes as spreaders according to influence ranking method such as PageRank, ClusterRank and k-shell decomposition. Besides, some heuristic methods such as hill-climbing, SPIN, degree discount and independent set based are also proposed. However, these approaches suffer from a possibility that some spreaders are so close together that they overlap sphere of influence or time consuming. In this report, we present a simply yet effectively iterative method named VoteRank to identify a set of decentralized spreaders with the best spreading ability. In this approach, all nodes vote in a spreader in each turn, and the voting ability of neighbors of elected spreader will be decreased in subsequent turn. Experimental results on four real networks show that under Susceptible-Infected-Recovered (SIR) and Susceptible-Infected (SI) models, VoteRank outperforms the traditional benchmark methods on both spreading rate and final affected scale. What’s more, VoteRank has superior computational efficiency.