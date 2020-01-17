---
title: Fitting Statistical Models to Data with Python - WEEK 2 - Part 2
category: python-libs
tags: python python-libs coursera statsmodel statistics
---

## Logistic regression

- 이제, binary outcome을 예측하는 모델을 만든다. 여기서는 `SMQ020`라고 하는, '흡연 유무(정확히는, "인생에서 최소 100개의 담배를 피웠는가"라는 질문에 대한 응답)'을 response varible로, 이를 예측하는 모델을 만들어본다.
- logistic regression은 event가 발생할 'odds'를 계산하는데, 만약 event가 `p`의 확률을 가지고 있다면, 이 event의 odd는 `p/(1-p)`가 된다. 
- 멀쩡히 잘 있는 probability를 무시하고, `Odds`를 사용하고, 그리고 거기에 log를 붙여서 `log-Odds`까지 붙이는 이유는, probability의 경우 0과 1사이의 값만을 가지는 반면, Odds의 경우 range(0, inf) 그리고 log-Odds의 경우는 range(-inf, inf)의 범위를 가진다. 
- 정리를 하자면, binary regression에서는 0과 1을 바로 나타낼 수 없기 때문에 우선 확률적인 값인 `P(E)`등을 이용하여 `P(E) = b0 + b1x1 + ... + bnxn` 형태로 표현합니다. 하지만, 이렇게 표현하게 될 경우, 좌변과 우변의 range가 다릅니다. 좌변은 proability이므로 range(0, 1)인 반면, 오늘쪽의 경우는 range(-inf, inf)를 가지죠. 따라서 이를 똑같이 mapping할 수 있도록 해주기 위해, Odds로 변경하고, 다시 Log-Odds로 변경해줍니다. 


### Odds and log odds

Logistic regression provides a model for the *odds* of an event
happening.  Recall that if an event has probability `p`, then the odds
for this event is `p/(1-p)`.  The odds is a mathematical
transformation of the probability onto a different scale.  For
example, if the probability is 1/2, then the odds is 1.

To begin, we look at the odds of alcohol use for women and men separately.