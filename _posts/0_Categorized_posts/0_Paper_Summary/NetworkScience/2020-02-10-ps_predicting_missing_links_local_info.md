---
title: PaperSummary - Predicting Missing Links via Local Information
category: paper-summary
tags: paper-summary network link prediction local-structure
---

## Predicting Missing Links via Local Information 

- link prediction을 위한 지표인 Resource Allocation Index는 2009년에 나온 [Predicting Missing Links via Local Information](https://arxiv.org/pdf/0901.0553.pdf)라는 논문에서 제시되었습니다. 
해당 논문의 초록은 다음과 같습니다. 

## Abstract 번역

- 현대 과학에서, 네트워크 내 missing link를 예측하는 것은 이론적인 관심뿐만 아니라, 실제적인 중요성도 모두 가지고 있다.
- 본 논문에서는 node similarity에 기반한 link prediction을 검증할 수 있는 간단한 framework를 제시하였다. 
- 잘 알려진 local similarity를 6개의 현실 네트워크에 적용하였고, 이를 통해 가장 기본적인 측정 지표인 `Common Neighbors`가 전반적으로 가장 좋은 성능(Performance)를 가지고 있음을 알 수 있었고, 두번째로는 `Adamic-Adar index`가 좋은 성능을 보였다. 
- 새로운 유사도 측정 방식으로, 네트워크에서 발생하는 "resource allocation process"에 기반한 지표를 제시하였고, 이는 `Common Neighbors`보다 높은 예측 정확도를 보였다. 특히, 그저 "nearest neighbor"라는 기본 정보만을 사용하여, 높은 정확도를 측정했고, 이후에도 이를 사용한 다양한 지표를 개발하여, 정확도를 높일 수 있을 것이다.

## What is link prediction? and why it matters? 

- link prediction은 관점에 따라서 다르게 읽힐 수 있습니다 가령, 다음 2가지로 표현할 수 있겠죠.
    1) 시간 `T` 이후 발생할 확률이 가능성이 높은 link. 예를 들어 
    2) 모든 link 데이터를 수집하는 것은 어려우며, 데이터 자체게 이미 missing link가 포함되어 있게 됨. 이 link를 메꾸는 것 
- 제가 말한 2가지 그리고 더 많은 다양한 경우에 따라서 잘 작용하는 지표들은 다를 것입니다. 가령 facebook에서 제시한 `dispersion`의 경우는 "Romantic relation"을 예측하는 데 잘 작동하죠. 
- 본 논문에서는 2)에 대한 이야기를 다룹니다. 
    - 생명 공학 분야의 네트워크들인 "단백질 상호관계 네트워크"등에서 link(or interaction)를 예측하는 일은 매우 큰 시간/금전적 비용이 소요됩니다. 따라서, 만약 실제로 존재하는 link를 실험없이, 예측할 수 있다면 많은 금전적/시간적 비용을 절약할 수 있겠죠. 
    - 또한, 친구들 사이의 관계 또한, 일종의 recommendtaion system을 통해 "아마도 당신이 이미 알 것 같은 사람들"을 추천하는 것도 비슷한 방식이죠.


## Some points.

- `Resource Allocation Index`는 "두 노드 u, v의 공통노드의 degree의 역수를 합한것"이며, 이는 "common neighbor에서 발생한 random walk들이 어디로 수렴하게 되는지"와 동일한 값을 가진다.
- 또한, 이 간단한 지표만으로도 매우 높은 의미를 발견했다는 것은, 최근의 네트워크 분석이 "global structure" 중심으로 운영되는 것과 정반대의 결과를 의미한다(이 내용은 결국 `harmonic centrality`의 중요성과도 연결됨). local structure는 시간적으로도 global structure에 비해 훨씬 적은 계산 시간이 소요되며, 필요하다면 local strucrture만으로도 충분하다 뭐 대충 그런 이야기.