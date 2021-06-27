---
title: 한국 힙합씬 피쳐링 네트워크 분석 - 1 ~ 3편. 
category: python-libs
tags: python python-libs selenium data-crawling networkx centrality
---

## 한국 힙합씬 피쳐링 네트워크 분석 

- 저는 대상/현상을 네트워크로 모델링하고 네트워크 적인 분석 법을 사용하여 대상 네트워크를 분석하는 일을 주로 수행합니다. 그리고, 그러다보니, 세상의 많은 현상들을 결국 "네트워크"적으로 바라보게 되죠. 
- 동시에 저는, 한국 힙합의 오랜 팬이기도 합니다. 힙합음악의 흥미로운 점은, 여러 뮤지션들이 다른 뮤지션들의 음악에 협업의 이름으로 참가하는 일이 매우 활발하다는 것이죠. 
- 저는 궁금했습니다. 과연, 한국 힙합의 피쳐링은 어떤 형태로 구성되어 있을까? 만약 이를 네트워크로 구성한다면 어떻게 구성해야 할까? 구성된 네트워크는 어떤 분석을 하면 재미있는 결과가 나올 수 있을까? 와 같이요. 
- 그래서, 저는 그동안의 한국 힙합 데이터를 모두 웹에서 크롤링하여 네트워크를 구성하고 그 결과를 정리하였습니다. 

## 발표자료. 

- 분석 결과는 [한국 힙합 피쳐링 네트워크 분석](https://docs.google.com/presentation/d/1zkOGBTD0UTaeoxYLxkPohNXaaKWYjVXfdbHgrli8xms/edit#slide=id.p) 에서 발표자료로 보실 수 있습니다.
- 구글 슬라이드로 정리하였으며, 코드 없이, 결과 중심으로 구성하였습니다. 
- 해당 자료는 이미 이전에 hiphopLE 사이트에 올렸으며, [HIPHOPLE - 한국 힙합 피쳐링 네트워크 분석.](http://hiphople.com/kboard/16636435) 제가 예상했던 것보다 더 좋은 반응을 받기도 했습니다.

## 보다 자세한 분석 과정

- 코드를 포함한 보다 자세한 분석 과정은 다음의 세 편의 글들로 나누어 정리하였습니다. 
  - 1) [한국 힙합씬 피쳐링 네트워크 분석 - 1편 - Data Collection](https://frhyme.github.io/python-libs/Korean_hiphop_colab_network_anaysis_0_data_collection/)
  - 2) [한국 힙합씬 피쳐링 네트워크 분석 - 2편 - Data Collection Wisely](https://frhyme.github.io/python-libs/Korean_hiphop_colab_network_anaysis_1_data_collection_wisely/)
  - 3) [한국 힙합씬 피쳐링 네트워크 분석 - 3편 - Data Analysis](https://frhyme.github.io/python-libs/Korean_hiphop_colab_network_anaysis_2_data_analysis/)
- 혹시 글들을 읽으시고 궁금하실 경우에는 제 개인 메일로 메일을 주시면 감사하겠습니다.
