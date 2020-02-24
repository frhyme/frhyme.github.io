---
title: PaperSummary - Semi-Supervised Learning Using Gaussian Fields and Harmonic Functions
category: paper-summary
tags: paper-summary node-clasification harmonic-function similarity
---

## 1-line summary 

- image에 대해 similarty에 기반한 graph를 만들고, 이를 통해 unlabelled data를 효과적으로 labeling하는 방법을 제시.

## Semi-Supervised Learning Using Gaussian Fields and Harmonic Functions

- 무려 [ICML(International Conference on Machine Learning)](https://en.wikipedia.org/wiki/International_Conference_on_Machine_Learning)에서 2003년에 발표된 논문이군요. ICML은 NIPS와 더불어, 머신러닝 분야에서 가장 중요한 두 학회로 인정받습니다. 물론 저랑은 아무 상관없이 없습니다만 호호호호. 그리고, 저자도, 카네기멜론입니다 호호호호.
- 물론, 2003년즈음에는 지금처럼 머신러닝 광풍이 존재하지는 않았었기 때문에, 상대적으로 저평가되어있었다, 라고 할 수도 있겠죠. 물론 그렇다고 학회의 퀄리티가 낮은 것은 아닙니다.
- [논문은 여기에서 볼 수 있습니다](http://mlg.eng.cam.ac.uk/zoubin/papers/zgl.pdf)

## Abstract 초월번역 

- 본 논문에서는 Gaussian rando field model에 기반한 semi-supervised learning을 제시하였다. 보통, graph에서 모든 node가 label이 알려져 있지는 않다. 보통은, 이 때 node의 adjacency matrix와 weight 정보를 함께 활용하여, node vector로 표현하고, 벡터간 거리를 통해 node간의 유사도를 측정하곤 합니다.
- 이와 같은 학습문제들은 Graph에 대한 Gaussian random field의 관점에서 공식화될 수 있으며, 이 때 평균은 harmonic function을 이용해 특성화될 수 있다. 그리고, 이는 matrix method와 belief propagation을 이용해서 효과적으로 획득할 수 있다, 라는 이야기죠.
- 이 학습 알고리즘은 random walk, electric entwork, spectral graph theory에서 발생하는 connection들과 긴밀하게 연결되어 있으며, 이 결과를 supervised learning을 사용한 예측 결과과 혼합해본 결과 feature selection 분야에서 유용하게 사용될 수 있음을 보였다. 

## 도대체 무슨 말인가? 

- 우선, 관련 알고리즘은 [networkx - node classification - harmonic function](https://networkx.github.io/documentation/stable/_modules/networkx/algorithms/node_classification/hmn.html#harmonic_function)에 잘 정리되어 있습니다. 
- 쭉 읽어보면 그냥 간단한 matrix 연산에 가까워요. 각 node의 degree의 역수(이웃이 많을수록 노드에게 도달하는 영향력이 작다는 가정)를 이웃들에게 전파해가면서, 가장 많이 전파된 놈이 이 node의 label이다, 라는 접근인 것이죠. 이렇게 말하고 나면, "그냥 nearest neighbor와 뭐가 다르냐?"라는 생각이 들기도 합니다.
- 단, 이 논문은 이미 생성된 graph에서 보는 것보다는 "graph가 없는 상태에서 similarlity를 기준으로 graph를 만든 다음, 존재하는 label(확실한 데이터)를 활용해서 label을 결정한 것"이라고 보면 됩니다.
- 논문 중간에 보면, digit image(0부터 9까지)가 존재하는데, similiar-graph를 활용해서 unlabelled data를 처리해준 것이죠.

## some things. 

### Belief propagation(신뢰 전파)

- 자세한 내용은 [Belief_propagation](https://en.wikipedia.org/wiki/Belief_propagation)에서 보시는 것이 좋구요. 가령, 어떤 graph가 있고 이 위로 메세지들이 흘러간다고 합시다. 이 때, 이전에 전달된 노드에게서 온 정보를 활용하고, 여기서 또 판단하여, 다음 노드로 다시 메세지를 전파하는 경우, 이런 경우를 보통 belief propagatio이라고 하죠. 즉 "상호간 신뢰에 기반하여 메세지 통신을 한다"라고 보시면 됩니다. 
- 보통은 bayesian network에서 주로 사용되며, bayesian network의 경우 보통 conditional probability를 활용하죠, 즉 "이전에 이 아이는 A라고 했다"라는 정보가 주어지고, 여기에 기반해서 "추론(inference)"을 하게 됩니다. 
- 마찬가지로, 이러한 사고의 흐름이 담긴 Graph가 있는 것이죠. 매 노드마다 새로 계산을 하는 것이 아니라, 이전에 전달된 정보를 기반하여 새로운 추론을 하는 것, 보통 이것을 belief propagation이라고 부릅니다.

## wrap-up

- 음, 사실 [networkx - node classification - harmonic function](https://networkx.github.io/documentation/stable/_modules/networkx/algorithms/node_classification/hmn.html#harmonic_function)을 공부하다가 논문을 읽게 된 것인데, 구현된 함수보다, 논문 내용 자체가 좀 도움이 된것 같습니다. 
- 논문의 내용을 다시 요약하자면 다음과 같죠.
    - 머신러닝 분야에서, unlabelled data가 많다(여기서는 image에 대해서 처리함). 여기에 비용이 너무 많이 든다. 
    - 그냥 classification을 푸는 것도 괜찮은데, 우리는 graph적인 특성을 집어넣어서 좀 더 효과적으로 만들어보려고 했다. 
    - 그래서, image간의 similarity를 활용해서 graph를 구축했다. edge의 weight는 similarity와 같고 
    - 따라서, 이렇게 하고, 대충 적절하게 edge를 없애고 아무튼 해서, belief propagation 방법으로 label을 전파함. 
    - 이 때, 영향력은 node의 이웃에 반비례하게 세팅됨. 
    - 해보니까 좋았떠라. 
- 몇몇 포인트에서는, 확실히 도움이 될만한 부분이 있습니다. 이 방법론의 전개방식을 다른 분야에 적용해 볼 수 있을 것 같아요.
- 중요합니다. graph가 가진 고유한 특성을 어떻게 하면 잘 활용할 수 있을지, 즉, 이것 자체가 새로운 feature selection이 되는 것이죠.

## reference

- [Semi-Supervised Learning Using Gaussian Fields and Harmonic Functions](http://mlg.eng.cam.ac.uk/zoubin/papers/zgl.pdf)