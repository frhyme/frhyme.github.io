---
title: [PS] Communicability in complex networks
category: paper-summary
tags: paper-summary patent communicability network complex-network
---

## Communicability in complex networks

- 논문 "Communicability in complex networks"는 2008년에 journal Physical Review E에 게재된 논문입니다. 지금은 2020년이구요. 저는 10년도 전에 나온 논문을 이제서야 읽고 개념을 잡고 있는 셈이죠. 참혹합니다. 물론, "이제서라도 알았으니까 됐지!"라고 생각하려고 합니다.호호호
- [link](https://arxiv.org/pdf/0707.0756.pdf)

## Abstract summary. 

- 간단하게 abstract를 요약하여 정리합니다.

> Many topological and dynamical properties of complex networks are defined by assuming that most of the transport on the network flows along the shortest paths. However, there are different scenarios in which nonshortest paths are used to reach the network destination. Thus the consideration of the shortest paths only does not account for the global communicability of a complex network. 

- 복잡 네트워크(complex network)의 많은 위상학적(topological) 동적(dynamical) 성질들은 최단거리(shortest path)에 근거한 네트워크의 흐름을 가정하고 정의됩니다. 하지만, non-shortest path를 통해서도 네트워크의 다른 노드들에 도달할 수 있기 때문에, 무조건 최단거리만으로 전체 네트워크의 관계성(global communicability)을 제한하는 것은 합당하지 못하다.

> Here we propose a new measure of the communicability of a complex network, which is a broad generalization of the concept of the shortest path. According to the new measure, most of real-world networks display the largest communicability between the most connected (popular) nodes of the network (assortative communicability). There are also several networks with the disassortative communicability, where the most “popular” nodes communicate very poorly to each other.

- 따라서, 본 논문에서는 기존의 shortest path의 개념을 확장하는 복잡계(complex network)의 관계성(communicability)에 대한 새로운 측정지표를 제안한다. 
    - 새로운 측정 방법을 많은 실세계의 네트워크(real-world network)에 적용해본 결과, 그래프 내에서 가장 많이 연결된(most-connected node, popular)간에 communicability가 큰 경우(assortative communicability)와 "popular node"가 서로 거의 commnicate하지 않는, "disassortative communicability"로 구분할 수 있었다.

> Using this information we classify a diverse set of real-world complex systems into a small number of universality classes based on their structuredynamic correlation. In addition, the new communicability measure is able to distinguish finer structures of networks, such as communities into which a network is divided. A community is unambiguously defined here as a set of nodes displaying larger communicability among them than to the rest of nodes in the network. 

- 이러한 정보를 통해서, 우리는 실제 세계의 복잡한 시스템의 구조적/동적인 성질에 따라서, 다양한 set로 구분할 수 있을 것이다. 또한, 이 communicability measure는 네트워크의 세부 구조, 특히, 네트워크 내에 존재하는 community들을 도출하기 위해서도 사용할 수 있을 것이다. 