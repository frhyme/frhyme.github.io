---
title: Mapping the evolution of entrepreneurship as a field of research (1990–2013) - A scientometric analysis
category: paper-summary
tags: entrepreneurship paper-summary 
---

## Mapping the evolution of entrepreneurship as a field of research (1990–2013): A scientometric analysis

- PLOS one에 2017년 5월에 게재된 논문. 
- [link](https://journals.plos.org/plosone/article/file?type=printable&id=10.1371/journal.pone.0190228)

### abstract

- 1990년부터 2013년까지의 기업가정신 분야의 진화(evolution)을 분석하기 위하여 scientometric 기법을 사용하였다. 
- topic mapping, author and journal co-citation analysis 그리고 해당 분야의 new and hot topic을 시각화하였다. 
- 이 논문은 이를 통해 24년 동안 가장 활발하게 연구된 46개의 topic을 발굴하였으며, 그들이 어떻게 나타나고, 사라지고, 재등장하고, 안정화되는지(stablize)를 시간에 따라서 정리하였다. 
- 또한, 24년동안 굳건하게 연구된, "institutions and institutional entrepreneurship", "innovation and technology management", "policy and development", "entrepreneurial process and opportunity", "new venture"를 식별하였다. 
- 전반적으로 본 분석은 분야의 convergence, divergence, diversity등의 패턴과, specialization, interdisciplinary engagement등을 보였다. 이를 통해 해당 분야의 핵심적인 통찰력을 제공한다. 

### insight and limitation

- 키워드 분석 측면에서 nlp적인 방법은 매우 간단하게, 문장에서 명사 추출, 단수화 등으로만 사용됨. 키워드를 사용한 것이 아니라, title, abstract에서 term을 추출하여 사용했음. 그리고 term의 관계는 co-occurrence를 고려하여, 계산됨. 
    - 따라서, 두 term이 많은 논문들에서 공통으로 사용될 경우 이 두 term은 강한 관계를 가지게 됨. 
    - 이렇게 만들어진 network에 대해서 girvan-newman method와 비슷한 커뮤니티 디텍션 방법인 VOS: A new method for visualizing similarities between objects 를 사용해서 커뮤니티를 찾음. 
- 완전히 같은 논문인가 생각했는데, 논문의 수가 3693이고 너무 작아서 뭔가 다르다고 생각되었음.
    - 꼼꼼히 보니까, 이 논문에서는 "entrep"로 시작하는 키워드를 포함한 article에 대해서만 분석을 수애했고, 또한, Business or management의 분야에 대해서, 1990 - 2013의 연도에 해당되는 연구만을 수행하였음.
    - 기업가정신은 다양한 분야에서 함게 연구되고 있는데, 이 분야에 대해서만 수행하였다는 한계가 있음.
- 그러나, 제한적으로 해당 연구를 바라보았다는 단점을 제외한다면, 해당 연구는 매우 높은 수준의 연구임. 해당 분야에 대해서 매우 체계적인 방식으로 분석하였음. 특히 co-citation, journal, keyword 등 다양한 분야에 대해서 모두 총정리하여 결론을 내었다는 점에서 매우 큰 의미가 있음
- 또한 여기서는 연도별로 그래프를 따로 생성하여 분석을 수행하였음. 그 과정에서 과거에는 있었는데 없어진 cluster, 점차 생겨나는 cluster를 분명하게 작성하였으며, 이를 통해 전체 연구 분야가 어떻게 변화하였는지를 명확하게 볼 수 있었음. 
- 여기서 제시한 topic은 46개로 지나치게 세부적으로 되어 있다는 단점이 있을 수 있음. 
    - 특히 몇몇 cluster는 직관적으로 서로 연결되어 있다는 느낌을 받곤 함, 코멘트가 미흡하군..ㅠㅠ