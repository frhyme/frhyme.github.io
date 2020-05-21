---
title: PaperSummary - Rich-club phenomenon across complex network hierarchies
category: paper-summary
tags: paper-summary rich-club density 
---

## 2-line summary 

- `rich-club coefficient`는 "k-core에 대한 density 변화율"을 의미함. 
- equivalent random network와 비교하여 normalization. 

## Rich-club phenomenon across complex network hierarchies

- 논문 [Rich-club phenomenon across complex network hierarchies](https://cseweb.ucsd.edu/~jmcauley/pdfs/apl07.pdf)은 2007년에 Applied Physics Letter에 게재된 논문.


## Abstract 초월 번역 

- 복잡계에서 "rich-club phenomenon"은 "높은 degree를 가진 node들이 lower degree를 가진 node들과 연결되기 보다, 높은 degree를 가진 node들과 연결되는 현상"을 말합니다. 그림으로 보면 좀 더 명확해지는데, 아래 그림을 보시면, higher degree를 가진 것으로 보이는 red node끼리 긴밀하게 연결되어 있는 것을 알 수 있습니다. 이런 현상, 즉 "부유층끼리 어울림"이라는 이름으로 "rich-club"라고 지은 것이죠.

![Rich club phenomenon](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Disassortative_network_demonstrating_the_Rich_Club_effect.png/220px-Disassortative_network_demonstrating_the_Rich_Club_effect.png)

- 이와 같은 현상의 존재는 네트워크에 대한 몇 가지 성질을 가리키게 되는데, 그 중 하나로 `tolerance to hub failure`를 말할 수 있습니다. 
- 본 연구에서 저자는 이 현상을 여러 real-world network의 hierarchies에서도 등장하는 것을 탐색하였다. 
- [Wikipedia: Rich-club coefficient](https://en.wikipedia.org/wiki/Rich-club_coefficient)를 참고하면, 이런 현상은 scientific collaboration network뿐만 아니라, air transportation에서도 측정되지만, 흥미롭게도, protein interaction network에서는 등장하지 않는다고 합니다.
- 이를 측정하기 위해 만들어진 지표인 rich-club coefficient는 network의 강건성(robustness)를 측정하는 heuristic measurement이며, 만약 rich-club coefficient가 높다면, 이는 hub들이 well-connected라는 것을 말하며, 어떤 hub가 만약 삭제되더라도, global connectivity는 사라지지 않는다는 것을 의미합니다(resilience to global connectivity). 또한, 이를 scientific collaboration network에 적용해보면, "elite들이 서로 협력하는 경향성이 있다"에 대한 증거로서 사용될 수 있죠.
- 또한, 해당 알고리즘은 [networkx.algorithms.richclub.rich_club_coefficient](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.richclub.rich_club_coefficient.html#networkx.algorithms.richclub.rich_club_coefficient)에 잘 구현되어 있습니다.


## but. 

- `k`는 "node degree threshold(cutoff)"를 의미하며, node degree cutoff를 점점 높여가며, 해당 노드들로만 구성된 subgraph `subG`의 density가 어떻게 변화하는지를 측정하는 것이, rich_club_coefficient입니다. 
- 즉, `k`가 올라갈수록 점점 1에 가까워지는 형식으로 변화한다면, 이는 해당 패턴(rich clube)이 등장한다, 라고 해석할 수 있는 것이죠.
- 복잡하게 쓰여져 있찌만, 사실 이게 다입니다. 그냥 k-core에 대해서 density를 보는 것이죠.

### normalization 

- 하지만 이 지표가 점점 1.0에 가까워진다고 해서 반드시 그 Graph가 rich-club이라고 할 수는 없습니다. 사실 이는 random network에서도 보통 단조 증가(monotonically increasing)하는 형태를 보이거든요. 
- 따라서, 이는 equivalent random network(degree distribution이 같지만 edge의 구성이 다른 G)에 대해서 비교하여, normalization을 하여 극복합니다. 
- 그냥, 아래와 같이 심플하게 처리하죠.

```
rich_club(G) / rich_club(equivalent_random_G)
```


## reference

- [Rich-club phenomenon across complex network hierarchies](https://cseweb.ucsd.edu/~jmcauley/pdfs/apl07.pdf)