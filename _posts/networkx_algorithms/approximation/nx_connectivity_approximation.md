---
title: networkx - approximation - Connectivity.
category: python-libs
tags: python python-libs networkx connectivity
---

## networkx - Fast approximation for node connectivity

- Graph는 기본적으로 빠르게 처리하는 것이 어렵습니다. 테이블과 같은 형태라면, 비교적 어느 정도 병렬적으로 처리할 수 있는데(서로 데이터가 독립적이기 때문), Graph는 모두 연결되어 있으므로 그렇지 않죠. 따라서, 필요에 따라서, approximation을 사용하는 경우들이 있습니다. 그외로, graph2vec, node2vec 등의 방법론 또한 approximation의 방법 중 하나죠.
- 본 포스트에서는 `local node connectivity`를 대략적으로 계산하기 위해 `networkx`에 내재된 approximation method를 사용합니다. 

### local node connectivity

- pairwise node connectivity 라고 말하기도 하는데, 가령 node_A, node_B가 있다고 합시다. 이 때, "이 두 노드를 disconnected로 만들기 위해 제거해야 하는 최소한의 노드 수"가 바로 local node connectivity가 됩니다. 