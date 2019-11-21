---
title: Comparison of Discrete Choice Models and Artificial Neural Networks in Presence of Missing Variables
category: machine-learning
tags: data machine-learning discrete-choice-model neural-network
---

## Comparison of Discrete Choice Models and Artificial Neural Networks in Presence of Missing Variables(번역)

- 요새 discrete choice model이라는 것을 좀 파고 들고 있습니다. 그런데, 조금 파보니까, 이게 제 기준에서는 classification 문제와 크게 다르지 않은 것처럼 보여요. 다만, 일반적으로 머신러닝에서 푸는 분류 문제는 해당 데이터 세트에 이미 '일관성'이 존재한다고 보는 반면에, discrete choice model은 보통 설문조사 등을 통해서 데이터를 획득하죠. 그 과정에서 '개개인별로 가지는 오차', '시간의 변화로 인해 발생하는 오차' 등이 있다고 가정하죠. 따라서, 이를 보완하기 위해서 다양한, 테크닉들도 있고, 이런저런 모델들이 있습니다. 
- 아무튼 간에, [그러다가 찾은 논문](https://arxiv.org/pdf/1811.02284.pdf)입니다. 간단하게 abstract만 번역해서 두겠습니다.

## abstract

> Classification, the process of assigning a label (or class) to an observation given its features, is a common task in many applications. 
- 분류 문제, 주어진 특성(feature)들을 활용해서 해당 개체(관찰)에 대한 label을 지정하는 것은, 일반적으로 다양한 분야에서 사용된다.

> Nonetheless in most real-life applications, the labels can not be fully explained by the observed features. 
- 그럼에도 불구하고, 많은 실제의 적용에서, '관측된 특성들'만으로 label이 충분히 설명되지 못한다(혹은 예측되지 못한다). 

> Indeed there can be many factors hidden to the modellers. The unexplained variation is then treated as some random noise which is handled differently depending on the method retained by the practitioner. 
- 그것은, 숨겨진 아주 많은 다양한 요소들이 있고, 설명되지 않은 변화(variation)들이, practitioner에 의해 획득된 방법에 따라서 어떤 noise로서 다르게 활용되기 때문이다.

> This work focuses on two simple and widely used supervised classification algorithms: discrete choice models and artificial neural networks in the context of binary classification.
- 이 연구에서는 두 간단하고, 광범위하게 사용되는 교사학습(supervised classification algorithm)인 discrete choice model과 artificial nerual network를 2중 분류 문제에 사용하였다. 

> Through various numerical experiments involving continuous or discrete explanatory features, we present a comparison of the retained methods’ performance in presence of missing variables. 
- continuous, discrete 특성들에 대해서 다양한 실험을 진행하였고, missing variable이 존재하는 상황에서의 다양한 성능을 비교하였다.

> The impact of the distribution of the two classes in the training data is also investigated. 
- 또한, training data에서 two classes의 분포가 미치는 영향에 대해서도 검사하였다. 

> The outcomes of those experiments highlight the fact that artificial neural networks outperforms the discrete choice models, except when the distribution of the classes in the training data is highly unbalanced.
- 실험 결과를 통해, training data에서 class가 unbalance인 상황일 때를 제외하고, ANN이 discrete choice model에 비해서 훨씬 효과적으로 작용하는 것을 알 수 있었다. 

> Finally, this work provides some guidelines for choosing the right classifier with respect to the training data.
- 이 결과는 좋은 분류기를 선정하기 위한 가이드라인으로서 사용될 수 있을 것이다.

## Thoughts of Mine

- 음, 사실 discrete-choice model이라고는 했지만, 그냥 logistic regression과 ANN을 비교한 것 뿐입니다. 몇 가지 데이터 분포등의 차이가 있을 때를 비교했다고 하지만, 사실, 큰 의미가 있어 보이지는 않아요. 
- 그리고, 가장 중요한 것은 ANN이 분류는 더 잘한다고 해도, 설명력이 없다는 것이죠. logistic regression의 경우(정확히는 discrete choice model)의 경우는 설명이 됩니다. 가령, 이 값은 다른 값에 비해서 얼마나 더 중요하고, 가격이 포함되어 있을 경우 WTP 등을 계산하는 데도 사용될 수 있죠. 즉, 이러한 부분을 고려하지 않고, 그냥 'classification' 성능만을 따지는 것은 좀 타당하지 않게 느껴져요. 
- 아무튼, discrete choice model은 logistic regression 정도로 많이 불리지만, 아무튼 큰 차이가 없다라고 생각해도 될것 같아요 호호호.