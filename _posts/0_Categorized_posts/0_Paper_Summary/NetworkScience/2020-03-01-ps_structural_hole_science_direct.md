---
title: PaperSummary - About Structural Hole vs. bewteennss centrality.
category: paper-summary
tags: paper-summary structural-hole betweenness-centrality centrality 
---

## Structual Hole vs. bet centrality.

- structural hole은 이른바 "구조적 구멍"이라고 많이 말해지는데요, 어떤 네트워크 내에서 서로 다른 두 클러스터의 중간에서, 중간자로서의 역할을 하게 될 경우, 해당 노드는 양쪽에서 오는 모든 정보를 통제할 수 있으므로, 많은 이득을 취할 수 있다, 라는 것이 이 내용의 핵심입니다. 
- 이를 계산하기 위한 몇 가지 방법들, `bridge`, `effective size`, `constraint`등이 있는데, 이 계산법들은 상대적으로 직관적이지도 않을 뿐더러, betweenness centrality가 더 좋은 측정법이라는 생각도 들었습니다. 

### Twitter: Information flows, influencers, and organic communities 초월번역

- degree centrality metric은 vertex의 중심성을 network의 connection의 수로서 정의한다. 따라서, 많은 노드와 연결되어 있을 수록, network상에서 중심에 위치해 있다고 정의한다. 
- betweenness centrality의 경우, 해당 노드가 네트워크 내에서 얼마나 '다리'역할을 많이 하는지를 통해 정의되며, 많은 노드가 해당 노드가 포함된 "최단 거리"를 사용할 수록 betweenness centrality는 높아진다.
- structural hole은 말 그대로 "구조적인 구멍"을 말하며, 해당 네트워크 내의 bridge처럼 이른바 "취약점"을 말한다고 보면 된다. 하지만, 이로 인해서 어떤 social actor가 이 "취약점"을 채우고 있을 때, 이 취약점에서 중개자로서 역할을 수행하며 많은 이점을 얻을 수 있게 된다는 것을 지적하였습니다. 이 actor들은 non-redundant한, edge들을 가지고 있죠.
- 다만, 이 내용을 읽다보니, 여기서는 betweenness centrality와 structural hole에 대해서 큰 구별을 두고 있지 않은 것 같습니다. 오히려, betwenness centrality가 structural hole을 대체할 수 있는 것처럼 말하고 있죠. 

## wrap-up

- 사실, 이 두가지 관점이 아무리 봐도 비슷하게 느껴져서, 분명히, 이를 비교한 문헌이 있어야할 것 같은데, 아직도 찾지를 못했습니다.
- 심지어, structural hole은 공학 베이스가 아니라, 인문학적인 개념에 불과한 것이 아닌가, 싶기도 해요. 의미하는 바는 알겠지만, 이것이 정확히 어떻게 측정되어야 하고, 왜 그렇게 측정되는지에 대해서 설명이 충분하지 못하다, 랄까요. 흠
- 혹시 이 글을 보시는 분들중에서 내용을 좀 더 자세하게 알고 계시는 분들이 있으시다면 알려주시면 감사하겠습니다.


## reference

- [structural hole](https://www.sciencedirect.com/topics/computer-science/structural-hole)