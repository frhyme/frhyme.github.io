---
title: paper-summary - Betweenness centrality as an indicator of the interdisciplinarity of scientific journals
category: paper-summary
tags: betweeness-centrality sna
---

## Betweenness centrality as an indicator of the interdisciplinarity of scientific journals

- [Journal of the Association for Information Science and Technology](https://en.wikipedia.org/wiki/Journal_of_the_Association_for_Information_Science_and_Technology)에 2007년에 실린 논문, impact factor는 2.7 정도
- [논문 전문은 여기에서 볼 수 있음](https://onlinelibrary.wiley.com/doi/full/10.1002/asi.20614)

### abstract summary 

- 기존에도 science citation indicator는 impact, immedicacy등도 있으나, social network analysis를 활용하여 degree/betweenness, closeness centrality를 측정하는 방법도 있음. 
- betweenness centrality는 journal의 interdisciplinarity를 측정할 수 있는 지표인 것이 증명되었으나, local citation environment에서만 유효하며, degree centrality가 충분히 클 경우에는 betweenness centrality를 활용해서 측정하는 것이 유효하지 못함. 

### what is interdisciplinarity?

> Interdisciplinarity or interdisciplinary studies involves the combining of two or more academic disciplines into one activity (e.g., a research project).

- "interdisciplinarity"는 단순히 말하면, 2개 이상의 학문을 혼합하여 새로운 학문, 혹은 연구 활동을 하는 것을 의미한다. 
- 즉 앞서 논문에서는 개별 journal별로 betweenness centrality를 통해 해당 저널의 Interdisciplinarity를 측정할 수 있다고 했다.

### insight

- 그러나, 이를 키워드 등에 적용한다면, 각 키워드들의 betweenness centrality가 변화한다면(상위의 키워드는 감소하고, 다른 밑에 있는 다른 키워드들이 증가한다면) 이는 해당 분야가 interdisciplinarity가 증가하고 있다, 즉 해당 연구 분야에 다양한 연구 분야가 생성되고 있다고 말할 수 있을 것으로 보인다.