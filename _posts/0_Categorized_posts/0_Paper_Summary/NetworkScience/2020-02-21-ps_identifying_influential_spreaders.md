---
title: PaperSummary - Identifying a set of influential spreaders in complex networks
category: paper-summary
tags: paper-summary centrality voterank 
---

## 2-line summary 

- `voterank`알고리즘은, 가령 influencer들을 통해 모든 네트워크를 커버하려고 할 때, 서로 겹치지 않게 하려면 어떻게 하는 것이 제일 좋은가? 를 보여준 알고리즘. 
- 그냥 "이웃들에게 투표를 하는 알고리즘"이며, 선택되고 나면 그 영역을 약화시키며 진행한다, 는 것이 다임.

## Identifying a set of influential spreaders in complex networks

- 무려 "Nature - Scientific Report"에 2016년 여름에 실린 논문. 
- 해당 논문은 [여기에서](https://www.nature.com/articles/srep27823) 볼 수 있음.

## Abstract 번역 

- 복잡계(Complex network)에서 영향력 있는 사람들(influencer or influential spreader)를 식별하는 것은 효과적인 정보 흐름(effective information spreading)을 위해서 매우 중요하다.
- 가장 단순한 전략은, PageRank,ClusterRank, k-shell-decomposition 등을 통해서, 상위에 있는 노드들을 선택하는 것이며, 혹은 hill-climbing, SPIN, degree discount와 같은 다양한 방법들도 이미 제안되어 왔다. 
- 하지만, 앞서 언급한 이 모든 문제들은, 정보전달자(spreader)이 서로 가깝게 있어서, 각자의 범위가 겹칠 수 있다는 가능성을 가진다(이를 좀 더 설명한다면, 만약, 우리가 인스타그램을 통해서 마케팅 활동을 해야 한다고 해보자, 이 때, 이를 위해 최소한의 influencer들을 선택해야 한다면, 그들이 최대한 서로 겹치지 않는 것이 가장 효율적이다)
- 본 리포트에서는, `VoteRank`라고 하는 비교적 단순한 방법을 사용해서, 가장 정보를 잘 전달할 수 있는 분산화된(decentralized) 정보전달자를 찾는다. 
- 실제로, 실 세계의 네트워크들에 적용을 해보았으며, 여기서도 VoteRank는 기존의 방법들에 비해서, 전파속도(spreading rate)뿐만 아니라, 최종 전파 결과(fianl affected scale)까지 그리고, 계산 속도 자체도 훨씬 월등한 것을 파악했다.

## More about `VoteRank`

- `VoteRank`는 생각보다 매우 단순한, 알고리즘이며 대략 다음과 같습니다.
    1) 모든 노드에게는 `score`, `voting_ability`가 주어진다. 
    2) 노드는 자신의 이웃에게 그들의 `voting_ability`에 따라서, 투표를 한다(즉, 이웃의 `score`에 그들의 `voting_ability`를 더해준다. 나눠서 더하는 것이 아니라 그 값을 그대로 더해줌)
    3) 모든 노드들에 대해서 이를 진행하고 나면, `top_node`의 이웃들의 `voting_ability`를 감소시킨다. 
    4) 가장 높은 `score`를 가지는 node(`top_node`)를 제외하고, 다시 2)부터 돌아간다. 
    5) 모든 node가 제외되었거나, 가장 높은 score가 0이 되면, 알고리즘을 종료한다. 
- 코딩하는 것도 딱히 어렵지 않고, 개념도 명확하죠. 이미 `top_node` 이웃의 `voting_ability`를 감소하는 것이 핵심적인데, 해당 영역은 이미 `top_node`에 의해서 커버되므로, 자연스럽게 약화되고 있는 것으로 보면 됩니다. 
- 더 심플하게 보려면, 한 procedure가 끝날 때마다, `top_node` 자체를 graph에서 제거하면 더 직관적이죠.