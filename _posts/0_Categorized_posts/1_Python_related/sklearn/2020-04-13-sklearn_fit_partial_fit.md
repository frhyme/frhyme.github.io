---
title: Python - sklearn - fit, partial_fit
category: python-libs
tags: python python-libs sklearn 
---

## 2-line summary

- `.fit`은 여러 weight fitting을 `max_iter`까지 수행하는 경우를 말하고, `.partial_fit`은 딱 1번의 iteration만을 진행하는 것을 말한다.
- 따라서, 만약 'converge'하지 않는다는 조건 하에서, parameter `max_iter`를 10으로 설정하고, `.fit`을 수행하는 경우와, `.partial_fit`을 10번 수행하는 경우는 결과가 비슷하다.

## Intro

- 일반적인 머신러닝 모델 구축은 그냥 `fit` - `predict`가 다죠. 네, 데이터를 전달하고 학습시키고, 예측합니다. 그리고 `sklearn`의 대부분의 모델들의 메소드도 이렇게 정리되어 있구요.
- 다만, 저처럼 컴퓨터의 메모리가 형편없다거나, 하는 경우에는 데이터를 나누어서 학습하는 것이 필요합니다. 한번에 다 넘기면 컴퓨터가 뭔가 느려터지게 되거든요. 따라서, 필요에 따라서 데이터를 나누어 학습하는 것이 필요하다는 이야기죠.네, 텐서플로우를 공부해보신 분은 빠르게 이해하실 텐데, mini-batch로 학습하는 것을 말합니다.

## sklearn - fitting vs. partial_fitting

- 네 일단은 기본적인 sklearn 모델에 대해서 적용해보겠습니다. 보통 다음과 같은 형태로 코드를 작성해서 사용하죠. 
- 아래 코드에서는 `SGDRegressor`이라고하는, Stochastic Gradient Decent를 사용해서 linear model에 대해 coefficient를 업데이트하는 모델을 사용하였고, `X`, `Y`를 임의로 만들어주었습니다.
- 그리고, `max_iter`는 10으로 매우 작게 세팅했죠. 이 아이는 `epoch`과 동일한데, weight(coefficient)를 업데이트하는 작업을 10번만 하겠다는 말이 되죠. 물론, 이 값만으로는 절대로 converge하지 않습니다만, 우리는 그냥 weight가 어떻게 달라지는지만 볼 꺼니까요.

```python
import numpy as np
from sklearn.linear_model import SGDRegressor

np.random.seed(0)

# X, Y
X = np.linspace(-1, 1, num=50).reshape(-1, 1)
Y = (X*3.3 + 5.6).reshape(50,)

```

### Fitting

- 다음 코드에서는 모델 `SGDRegressor`에 대해서, `max_iter=10`를 설정하였습니다. 즉, 컨버지하지 않는다면 10번 weight를 업데이트하겠다는 이야기죠.

```python
sgd_reg_model_fit = SGDRegressor(
    random_state=0,
    verbose=0,
    max_iter=10,
)
print(f"== First  fitting")
sgd_reg_model_fit.fit(X, Y)
print(f"---- Coefficient: {sgd_reg_model_fit.coef_}")
print("---"*20)
```

```bash
== First  fitting
---- Coefficient: [0.81407501]
```

### partial-Fitting

- 다음 코드에서는 모델 `SGDRegressor`에 대해서, `.fit`가 아닌 `.partial_fit`을 실행합니다.
- 결과를 보시면 이전과 weight 값이 매우 비슷하죠. 완전히 똑같지는 않네요. 뭐 세부적인 설정값이 조금 다른가 봅니다.

```python
sgd_reg_model_partial_fit = SGDRegressor(
    random_state=0,
    verbose=0,
    max_iter=1,
    warm_start=True
)
print(f"== Second fitting")
for iteration_i in range(0, 5):
    sgd_reg_model_partial_fit.partial_fit(X, Y)
print(f"---- Coefficient: {sgd_reg_model_partial_fit.coef_}")
```

```bash
== Second fitting
---- Coefficient: [0.81001236]
```

## wrap-up

- 물론, `.partial_fit`를 사용하지 않고, 그냥 `warmstart`를 True로 설정하여, 이전의 weight를 기억하도록 한 다음 `.fit`을 사용하는 것 또한 방법이죠.
