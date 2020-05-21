---
title: [PaperSummary] Axioms for Centrality
category: paper-summary
tags: paper-summary network centrality 
---

## [PaperSummary] Axioms for Centrality

- [논문 링크](https://arxiv.org/abs/1308.2140)


## Abstract 번역. 

> Given a social network, which of its nodes are more central? This question has been asked many times in sociology, psychology and computer science, and a whole plethora of centrality measures (a.k.a. centrality indices, or rankings) were proposed to account for the importance of the nodes of a network. 
- 소셜 네트워크가 주어졌을 때, 어떤 노드들이 중심성이 높은가?를 측정하기 위해서 많은 연구들이 있었고, 많은 centrality 분석 방법들이 제안되어 왔음.

> In this paper, we try to provide a mathematically sound survey of the most important classic centrality measures known from the literature and propose an axiomatic approach to establish whether they are actually doing what they have been designed for. Our axioms suggest some simple, basic properties that a centrality measure should exhibit.
- 이 논문에서는, 고전적인 centrality 측정 방식에 대해 몇가지 axiom에 대해서 조사하여, 해당 중심성 측정 방식의 특징을 정리하였음.

> Surprisingly, only a new simple measure based on distances, harmonic centrality, turns out to satisfy all axioms; essentially, harmonic centrality is a correction to Bavelas's classic closeness centrality designed to take unreachable nodes into account in a natural way.
- 놀랍게도, 거리에 기반한, 간단하고 새로운 측정방식인 `harmonic centrality`만이 제시한 모든 axiom을 만족하는 것으로 드러났음. 특히, `harmonic centrality`는 도달불가한 노드들(unreachable node)를 고려하기 위해서 설계된 Bavelas's classic closeness centrality를 수정한 것이다. 

> As a sanity check, we examine in turn each measure under the lens of information retrieval, leveraging state-of-the-art knowledge in the discipline to measure the effectiveness of the various indices in locating web pages that are relevant to a query. 
- 검증하기 위하여(sanity check), 우리는 "우리 쿼리에 응답하는 많은 웹페이지들에 대해서 효과성을 측정하여 중요한 지식을 도출하는" "정보 검색"분야에 대해 이 측정방식을 적용하여 검증하였다.

> While there are some examples of this comparisons in the literature, here for the first time we take into consideration centrality measures based on distances, such as closeness, in an information-retrieval setting. The results match closely the data we gathered using our axiomatic approach.
- 본 연구는 "거리에 기반한 중심성 측정 방식"를 활용하여 정보 검색에 사용한 첫번째 연구이며, 우리가 수집한 데이터는 우리의 axiomatic approach에서 수행되었다.

> Our results suggest that centrality measures based on distances, which have been neglected in information retrieval in favour of spectral centrality measures in the last years, are actually of very high quality; moreover, harmonic centrality pops up as an excellent general-purpose centrality index for arbitrary directed graphs.
- 우리의 연구는 거리에 기반한 centrality 측정방식, 특히, 오랫동안 'spectral centrality measure'에 의해 오랫동안 무시되어 온, 이런 측정방식들이 실제로는 더 높은 품질을 가지고 있음을 증명합니다. 특히, 이러한 연구는 정보 검색 분야에서 쓰이는 `arbitrary directed graphs`에서 매우 탁월하게 사용되었다.
- 여기서 말하는 spectral centrality measure는 "eigen vector에 기반한, 혹은 매트릭의 형태로 decomposition하여 처리한" 측정 지표에를 말합니다.

## wrap-up

- axiom에 무엇들이 있는지 확인을 해보면 더 정확할 것으로 생각됩니다만, 그러함에도 harmonic centrality가 다른 지표들에 비해서 월등하다는 것은 좀 충격적입니다. 특히, harmonic centrlaity의 계산법이 너무 단순하니까요. 