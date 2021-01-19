---
title: PaperSummary - Subgraph Centrality in Complex Networks
category: paper-summary
tags: paper-summary network centrality subgraph
---

## Subgraph Centrality in Complex Networks

- 2005년에 나온 논문입니다.
- [논문의 링크](https://arxiv.org/abs/cond-mat/0504730)

## Abstract 번역 

> We introduce a new centrality measure that characterizes the participation of each node in all subgraphs in a network. 

- 우리는, 네트워크 내의 모든 subgraph에 대해서, 각 node가 얼마나 참여하는지를 특성화하는, subgraph-centrality를 소개한다.

> Smaller subgraphs are given more weight than larger ones, which makes this measure appropriate for characterizing network motifs. 

- 작은 subgraph일수록, 큰 subgraph에 비해서 큰 weight를 주게 되는데, 이는 [Network motif](https://en.wikipedia.org/wiki/Network_motif)를 특성화하기 위함이다. 
- [Network motif](https://en.wikipedia.org/wiki/Network_motif)는 "반복적으로 나타나는 네트워크의 패턴"을 말합니다. vertex에 대해서도 존재할 수 있지만, subgraph간에서도 존재할 수 있죠. 이 부분은 글로 보는 것보다, [Well-Established_Motifs_and_Their_Functions](https://en.wikipedia.org/wiki/Network_motif#Well-Established_Motifs_and_Their_Functions) 부분을 읽어보시면 더 명확합니다. 예를 들어 "Feed-forward loops (FFL)", "Positive auto-regulation (PAR)" 등이 있죠.

> We show that the subgraph centrality (SC) can be obtained mathematically from the spectra of the adjacency matrix of the network. This measure is better able to discriminate the nodes of a network than alternate measures such as degree, closeness, betweenness and eigenvector centralities. 

- 우리는, subgraph centrality가 network의 adjacency matrix에서 수학적으로 획득될 수 있음을 보여줄 것이고, 이 측정 지표가 네트워크의 노드를 구분하기 위해 degree/closeness/beteenness/eigenvector cetranlity의 대안이 될 수 있을 것이다.

> We study eight real-world networks for which SC displays useful and desirable properties, such as clear ranking of nodes and scale-free characteristics. Compared with the number of links per node, the ranking introduced by SC (for the nodes in the protein interaction network of S. cereviciae) is more highly correlated with the lethality of individual proteins removed from the proteome.

- 우리는 8개의 실 세계의 Subgraph Centrality가 잘 작동하는, scale-free 특성을 갖춘 실제 세계의 8개의 real-world network를 대상으로 조사하였고, degree(links per node)와 비교해봤을 때, subgraph centrality가 더 (단백체에서 제고되는 개개인의 단백질)에 대해 correlation이 높다는 것을 발견하였다.
