---
title: paper-summary - Data-driven Process Prioritization in Process Networks
category: paper-summary 
tags: process bpm paper-summary
---

## Data-driven Process Prioritization in Process Networks

- Decision Support System에 2017년 8월에 게재된 논문
- [link](https://www.sciencedirect.com/science/article/pii/S0167923617300362)

### abstract summary 

- Business Process Management(BPM)은 조직의 설계에서 매우 핵심적인 패러다임이며, 동시에 조직의 성과에 영향을 미치는 중요한 요소이다. 
- BPM에서 가장 중요한 핵심 활동은 process improvement이며, process improvement에서 Critical Success Factor를 활용하여 Process의 우선순위를 매기는 것(prioritization)은 매우 중요함.
- 본 연구에서는 Data-Driven Process Prioritization(D2P2) approach를 제시함. 
    - 기존 방법들의 한계를 극복하기 위하여 로그 데이터를 활용하여, 프로세스 간의 구조적(structural), stochastic 의존관계를 고려한 방법론을 제시함. 
- 여기서 제시하는 방법론은 Improvement가 필요한 프로세스 네트워크 내의 프로세스를 발견하고, 우선순위를 만드는 것임. 
- 즉, D2P2는 프로세스 prioritization과 process decision-making에 대하여 예방적인 지식(prescriptive knowledge)에 공헌한다. 
- 또한 이를 실제로 software prototype으로 구현했으며, BPI challenge의 데이터에 실제로 적용해보았다. 

### insight 

- 우선, 기존의 process prioritization의 경우 process dependency를 고려하지 않고, 프로세스를 별개로 인지하고, 프로세스의 퍼포먼스등을 고려하여 process improvement를 결정함. 
    - 그러나, 실제 프로세스에서는 프로세스가 고립되어 수행되는 일이 없으므로 이렇게 수행해서는 안된다는 것이 논문 내 related work에서의 설명
- 여기서 말하는 Process Network는 프로세스 간의 의존관계를 말한다. 예를 들어서, P1이 수행되고, P2가 수행된다면, link(P1, P2)가 존재한다. 만약 standalone으로 수행될 수 있다면, self-link가 존재함. 
- 또한 프로세스별 Performance도 다양하게 존재할 수 있는데, P1로만 수행되고 끝나는 경우 측정해야하는 Performance와 P1==> P2로 수행되었을 경우 측정해야 하는 Performance는 서로 다름. 
- 대략보면, "프로세스 네트워크를 활용하여 performance를 측정하고, performance에 문제가 발생할 가능성을 시뮬레이션을 통해 예측하여 risky한 프로세스를 더 빠르게 발견할 수 있고. 이를 실제 시스템을 통해서 구현하였으며, 소프트웨어 프로토타입으로 만들었음"이 이 논문의 핵심인 것으로 보임. 