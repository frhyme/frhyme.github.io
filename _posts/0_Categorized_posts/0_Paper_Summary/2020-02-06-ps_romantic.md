---
title: PaperSummary - Romantic Partnerships and the Dispersion of Social Ties - A Network Analysis of Relationship Status on Facebook
category: paper-summary
tags: paper-summary network centrality subgraph
---

## PaperSummary - Romantic Partnerships and the Dispersion of Social Ties - A Network Analysis of Relationship Status on Facebook

- 페이스북 직원과 코넬대학교의 연구자가 같이 연구해서 발표한 저작물이군요. 
- 제목을 번역한다면, "페이스북의 'relationship status'에 대한 네트워크 분석"이 되겠군요.
- [논문 링크](https://arxiv.org/pdf/1310.6753v1.pdf)


## Abstract 번역

> A crucial task in the analysis of on-line social-networking systems is to identify important people — those linked by strong social ties — within an individual’s network neighborhood. 
- 온라인 소셜 미디어의 분석에서 가장 중요한 것은 "네트워크 상의 이웃들 중에서, 누구와 가장 강한 관계(Strong tie)를 맺고 있는지, 즉 누가 누가 중요한 사람인지" 파악하는 것이다. 

> Here we investigate this question for a particular category of strong ties, those involving spouses or romantic partners. 
- 우리는 이 질문 중, 특별한 종류의 강한 관계(particular category of strong tie)인, 배우자나 애정관계에 있는 사람들을 탐색하였다.

> We organize our analysis around a basic question: given all the connections among a person’s friends, can you recognize his or her romantic partner from the network structure alone? 
- 우리는 분석을 기본적인 질문으로부터 출발하였다: "만약, 그저 사람들과 그들간의 관계만 주어졌을 때, 당신은 네트워크 구조만으로부터, 그의 애정관계에 있는 사람을 알아차릴 수 있겠는가?"

> Using data from a large sample of Facebook users, we find that this task can be accomplished with high accuracy, but doing so requires the development of a new measure of tie strength that we term ‘dispersion’ — the extent to which two people’s mutual friends are not themselves well-connected.
- 페이스북의 아주 많은 종류의 사람들에 대한 데이터로부터, 우리는 이 일이 매우 높은 정확도로 처리될 수 있다는 것을 알았다. 이렇게 함으로써, 새로운 방식의 node strength 측정 방식을 필요로 했고, 우리는 이 측정 방식의 이름을 'dispersion'이라고 정했다. 이는 그들뿐만이 아니라, 그들 친구들간에 매우 많은 상호 친구(mutual friends)가 있는 정도를 의미한다.

> The results offer methods for identifying types of structurally significant people in on-line applications, and suggest a potential expansion of existing theories of tie strength.
- 그 결과는 on-line application에서 구조적으로 중요한 사람의 유형을 식별하는 방법을 소개하며, 기존의 측정방식의 잠재적인 확장을 제안하게 된다.

## main contribution

> We propose a new network measure, dispersion, for estimating tie strength. Given the ubiquity of embeddedness in existing analyses of tie strength, the availability of this new measure broadens the range of tools available for reasoning about tie strength, and about mechanisms for ties trength classification in on-line domains.
- 새로운 네트워크 측정 방식으로, "tie strength"를 측정할 수 있는 `dispersion`을 제안함. 이는 기존의 다른 측정방식에 그대로 심어서, 노드의 힘을 파악할 수 있는 다양한 툴과 함께 사용될 수 있을 것이며, 분류 도구에서도 사용될 수 있을 것이다.

> We provide a new substantive characterization of romantic relationships in terms of network structure, with potential consequences for our understanding of the effect that such relationships have on the underlying social network.
- 우리는 romantic relationship에 대해서 네트워크의 관점에서 새로운 잠재적 특성을 제공했다는 것.

> Given this characterization, we examine its variation across different conditions and populations. We find, for example, that there are significant gender differences in the extent to which relationship partners are recognizable from network structure, and that relationships are more likely to persist when they score highly under our dispersion measure.
- 이 특성 내에게 우리는 다양한 조건과 population을 변형해 가면서 검사해봤다. 그 결과 우리는 네트워크 구조로부터 partner를 탐색하는 것에 "성별간에 유의미한 차이"가 발생한다는 것을 발견했고, 또한 dispersion이 클 수록 그들간의 관계는 좀 더 공고하다는 것 또한 발견했다.

## Embeddedness to Dispersion

>  the standard characterization of a tie’s strength in terms of its embeddedness, the number of mutual friends shared by its endpoints. 
- 기본적으로 tie(연결))의 강함을 특성화하는 지표는 embeddedness로, 두 endpoint인 노드들간의 공유되는 상호 친구의 수로 표현된다. 본 연구에서는 이 baseline을 비교대상으로 삼고, 새롭게 제시하는 dispersion을 사용했을 때 정확도가 훨씬 높아진다는 것을 증명함.

> In contrast, the links to a person’s relationship partner or other closest friends may have lower embeddedness, but they will often involve mutual neighbors from several different foci, reflecting the fact that the social orbits of these close friends are not bounded within any one focus — consider, for example, a husband who knows several of his wife’s co-workers, family members, and former classmates, even though these people belong to different foci and do not know each other. 
- embeddeness는 두 노드간의 공유되는 상호 친구(mutual friend)를 활용하여, 두 노드간의 연결의 정도를 측정한다. 즉, 보통 두 노드가 같은 클러스터에 존재하여 foci가 내부에 존재할 경우, embeddedness는 높게 나온다. 
- 하지만, 본 연구에서 대상으로 하는 romantic relation의 경우를 보면, "남편은 아내의 서로 다른 다양한 그룹의 사람들, 회사 사람 조금, 학교 동창 조금, 동네 친구 조금 등, 다양한 그룹의 사람들을 다 어느 정도 알고 있다". 실제로 이 그룹간(학교 사람과 학교 동창은 서로 모를 가능성이 높다) 의 사람들은 서로 모를 수 있으며, 단 하나의 focus가 아닌 다양한 중심에 위치해 있다.
- 여기서 말하는 "foci"는 그대로 번역할 경우, "초점"으로 번역되는데, 이는 두 노드 u, v 간의 중심이 어디에 있는지를 말한다. 가령, 두 노드 간에 관련된 노드가 매우 많이 존재할 경우, 그 클러스터의 중심이 두 노드 사이에 있을 수 있을 것이고. 반대로 두 노드간에 공유하는 노드가 없을 경우 foci가 멀리 떨어져 있을 수 있다.

> Thus, instead of embeddedness, we propose that the link between an individual u and his or her partner v should display a ‘dispersed’ structure: the mutual neighbors of u and v are not well-connected to one another, and hence u and v act jointly as the only intermediaries between these different parts of the network.
- 따라서, embeddeness를 대신하여, u, v간의 관계를 측정하기 위해서, 우리는 `dispersed structure`를 보여주는데, 이는 앞서 말한 "특별히 가까운 관계(배우자)는 그저 공유되는 사람이 많은게 다가 아니고(high enbeddedness), 서로 다른 다양한 foci의 사람들을 알고 있다"는 것을 반영한다. 따라서, u, v 사이에 존재하는 mutual neighbor 중에서, 서로 well-connected되지 않고, u, v가 그저 서로 다른 path를 가지는 정도를 고려하였다.

## wrap-up

- 페이스북은 그 자체로 사람들에 대한 무수히 많은 데이터들을 담고 있죠. 그리고, 그저 네트워크만 소유하고 있을 뿐만 아니라 사람들이 스스로 labeling까지 해줍니다(누가 배우자이고, 누가 친하고 등등). 이렇게 되어 있을 경우에는 비교적 자체적으로 이 데이터 위에서 다양한 실험을 할 수 있을 것이기 때문에, 좋은 방법론이 나올 가능성이 높죠. 또한, 페이스북 내의 데이터들은, 시간의 변화 또한 담고 있습니다. 이 논문의 컨트리뷰션 중 하나로 "dispersion 값이 클수록 그들간의 관계는 더욱 공고하게 유지되었다"라는 부분이 있는데, 이는 시간에 따른 그래프의 변화를 가지고 있지 못하면 파악하기 어렵죠. 페이스북은 이것이 가능한 서비스이구요.
