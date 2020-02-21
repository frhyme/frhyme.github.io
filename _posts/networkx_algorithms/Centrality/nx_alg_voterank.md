---
title: networkx - voterank
category: python-libs
tags: python python-libs networkx centrality voterank
---

## problem. 

- 원래 논문에 있는 내용대로면, voting ability가 0이 되어서는 안됨. 하지만, `nx.vote_rank`에서는 종종 0이 되는 경우들이 있음. 
- 따라서, 이거 잘못된 것 아니냐, 라고 문의를 날린 상황임.

## reference

- [Identifying a set of influential spreaders in complex networks](https://www.nature.com/articles/srep27823)
- [networkx.algorithms.centrality.voterank](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.voterank.html#networkx.algorithms.centrality.voterank)