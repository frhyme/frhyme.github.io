---
title: PaperSummary - Community Detection via Semi-Synchronous Label Propagation Algorithms
category: paper-summary
tags: paper-summary network community-detection label-propagation 
---

## Community Detection via Semi-Synchronous Label Propagation Algorithms

- graph의 각 노드들의 label을 파악하기 위한 Label Propatation Algorithm(LPA) 방법은 처음 제시되었을 때는 "비동기적인 방법"이어서, 속도가 매우 느렸던, 반명, 본 논문에서 제시하는 방법은, "Semi-Synchronous"한 방법이어서, 훨씬 효율적이다. 라는 것을 말하고 있음.
- 2011년 3월에 나온 논문, [논문 링크](https://arxiv.org/abs/1103.4550)


## Abstract 번역

- 최근에 label-propagation algorithm에 기반한 community detection 전략이 새롭게 소개되었고, 이를 정보의 확산(diffustion of information) 측면에서 각 community를 규정하였다("가까운 사람의 community가 해당 노드의 커뮤니티가 된다는 개념을 여기서슨 정보의 확산으로 바라본듯"). 
- 실제로 Community structure를 찾는 데 있어서, LPA의 방법이 매우 효과적이라는 것이 드러났고, 병렬처리를 위한 동기적인(synchronous) 방식과, 비동기적(asynchronous) 방식도 있으나, 이 두 방식 모두, 결점을 가지고 있다. 
- synchronous 방식의 경우, algorithm의 종료 조건(termination)이 보장되지 않고(따라서 값이 진동할 수 있고), asynchoronous의 경우, 계산 시간 측면에서 매우 큰 문제가 있음. 
- 이 논문에서는 따라서, semi-synchronous LPA를 소개하며, 이는 두 모델의 강점을 모두 가진다. 
- 우리는, 항상 방식이 항상 stable을 보장하는 것을 보였고, 실험적으로도 그 계산 속도가 비동기적인 방식에 비해서 훨씬 효율적이라는 것을 보였다.

## semi-synchronous way.

- 앞서 말한 것처럼, bipartitie network에서 진동하는 "동기적 방식"과 속도에서 손해를 보는 "비동기적인 방식"의 한계를 극복하기 위해서, 우리는 다음의 방법으로 알고리즘을 진행함. 

1) **Coloring Phase**: 어떤 인접한 노드들도 같은 색깔을 가질 수 없도록, 처리함. 이 방식 자체는 병렬적으로 처리될 수 있음. 
2) **Propagation Phase**: 이 방법의 경우는 기존 방식과 거의 동일하나, 가장 많이 등장한 label들이 2개 이상일 경우, 여기서는 그냥 가장 높은 값을 가진 label을 선택함. 이 방법이 써 있으나, 귀찮아서 안 읽음.

## wrap-up 

- 아무튼, 그래서 직접 코딩하여, semi-synchronous 에 대해서 테스트를 해본 결과 훨씬 빨랐음은 물론, 다른 지표들(coverage, performance, modularity)도 딱히 떨어지지 않았다는 이야기다.