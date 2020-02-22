---
title: PaperSummary - A model of Internet topology using k-shell decomposition
category: paper-summary
tags: paper-summary k-shell
---

## 1-line summary 

- 인터넷 구조를 파악하기 위해 k-shell decomposition, percolation theory, fractal theory등을 사용하였으며, 이를 통해 인터넷을 구성하는 3가지 요소를 도출해냄. 

## A model of Internet topology using k-shell decomposition

- 2007년 PNAS에 게재된 논문이며, 최근에 k-shell decomposition에 대해서 정리하다가 해당 논문을 보게 됨. 
- 논문은 [여기에서 볼 수 있음](https://www.pnas.org/content/104/27/11150.full#ref-12)

## Abstract 번역

- 본 논문에서는 internet 지도(a map of the interne)를 자동시스템의 관점에서(at the autonomous systems level) 분석하고 있는데, 이 때, k-shell decomposition, percolation theory, fractal gemoetry를 사용하여, internet을 가장 잘 설명할 수 있는 모델을 찾고 있음. 
- 특히, 우리의 분석에서는, 특별한 parameter 없이, network-shell에 대한 정보를 바탕으로, internet을 3가지 subcomponent로 구분하였음.
    1) nuclues: 수가 매우 작고, 전체에 분포되어 있는(globally distributed) subgraph들과 대부분 잘 연결됨.
    2) factal subcomponent: nuclues 없이도 인터넷 전체에 문제없이, 도달할 수 있으며, self-similar 성질을 가짐
    3) dendrite-like structure: "dendrite"는 fractal에서 주로 쓰이는 단어로 "나뭇가지 모양의 프랙탈"로 표현해도 됨. 보통 "고립된 노드(isolated node)"들이 이 아이를 통해서만 nuclues에 도달할 수 있음
    - (iii) dendrite-like structures, usually isolated nodes that are connected to the rest of the network through the nucleus only
- 본 논문에서 제시한 decomposition은 매우 강건하고(이는, 특정 parameter없이 자동으로 진행할 수 있는 decomposition 방법이므로), 인터넷에 내재되어 있는 구조에 대한 통찰을 제시할 수 있다. 또한, 이후의 다른 분석들에서도 다양하게 사용될 수 있을 것이다. 
- 요약하자면, 결국, "인터넷 구조

## other things. 

- 기존의 통계물리 분야에서는 이미 "인터넷은 power-law degree distribution"을 가지고 있다, 라는 것을 발견하였고, 이로 인해, 많은 사람들이 degree distribution을 중요한 요소로 바라보기 시작했다. 하지만, 같은 degree distribution을 가지고 있다고 해도, 서로 다른 구조(structure)를 가질 수 있다.
- 따라서, 본 연구에서는, node degree를 사용하지 않고, "k-shell decomposition"을 사용하여, shell에 대한 index를 사용하였다. 실제로 node degree는 노드를 몇 천개로 분류하지만, "k-shell decomposition"을 사용하면, 40, 50개로 분류될 수 있다. 물론, k-shell decomposition은 매우 올드한 테크닉이고, 보통 데이터 시각화분야에서 많이 사용되어 왔다.

## wrap-up

- k-shell decomposition은 그냥 "subgraph 내의 모든 node의 degree가 최소한 k보다 큰, subgraph"를 말합니다. 본 논문에서는, 일반적으로 많이 쓰이는 node-degree를 사용하지 않고, k-shell decomposition을 사용해서, 그래프에 대한 어떤 계층적인 구조를 파악했다는 것이 의미가 있죠. 
- 다만, k-shell decomposition만을 사용한 것은 아니고, 그외로도 몇 가지 마이너한 테크닉을 쓰기는 했는데, 아무튼 핵심은 그냥 "k-shell decomposition"을 사용해서 node 집단을 분류했으며, 나름 의미가 있더라, 라는 것이겠죠.


## reference

- [A model of Internet topology using k-shell decomposition](https://www.pnas.org/content/104/27/11150.full#ref-12)