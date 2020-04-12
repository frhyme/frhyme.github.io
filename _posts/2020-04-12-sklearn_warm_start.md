---
title: Python - sklearn - warm_start.
category: python-libs
tags: python python-libs sklearn 
---

## 2-line summary. 

- `sklearn`에서 model의 `warm_start`의 default는 `False`임. 이는 `.fit`을 실행할 때, 이전에 업데이트된 weight(coefficient)를 초기화하고 다시 fitting한다는 것을 의미한다. 
- 만약 `warm_start`를 True로 설정하고 진행한다면, `.fit`을 실행할 때 이전의 weight를 기억하고 그대로 이어서 업데이트되는 것을 말한다.

## Intro. 

- 일반적인 머신러닝 모델 구축은 그냥 `fit` - `predict`가 다죠. 네, 데이터를 전달하고 학습시키고, 예측합니다. 그리고 `sklearn`의 대부분의 모델들의 메소드도 이렇게 정리되어 있구요. 
- 다만, 저처럼 컴퓨터의 메모리가 형편없다거나, 하는 경우에는 데이터를 나누어서 학습하는 것이 필요합니다. 한번에 다 넘기면 컴퓨터가 뭔가 느려터지게 되거든요. 따라서, 필요에 따라서 데이터를 나누어 학습하는 것이 필요하다는 이야기죠.네, 텐서플로우를 공부해보신 분은 빠르게 이해하실 텐데, mini-batch로 학습하는 것을 말합니다. 

## sklearn - fitting with `warmstart=False`

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

# Define Model 
sgd_reg_model = SGDRegressor(
    random_state=0, 
    verbose=0, 
    max_iter=10, 
)
```

- 그리고, 위에서 정의한 모델에 대해서 fitting을 해줍니다. 
- 아래 코드에서 보시면, fitting을 두번 해준 것을 알수 있죠. 네 이렇게 하면 한번에 iteration 10번씩 총 20번 해주는 것이 아닐까요? 
```python
print(f"== First  fitting")
sgd_reg_model.fit(X, Y)
print(f"---- Coefficient: {sgd_reg_model.coef_}")

print(f"== Second fitting")
sgd_reg_model.fit(X, Y)
print(f"---- Coefficient: {sgd_reg_model.coef_}")
```

- 안타깝게도 그렇지 않습니다. 아래 결과를 보시면, 첫번째 fitting과 두번째 fitting 때의 coefficient가 같은 것을 알 수 있죠.

```
== First  fitting
---- Coefficient: [1.26229792]
== Second fitting
---- Coefficient: [1.26229792]
```

- 이는 `SGDRegressor`를 선언해줄 때, 이 아이의 parameter인 `warm_start`가 `False`로 되어 있기 때문이죠. `warm_start`를 한국말로 번역한다면 "따뜻한 시작"정도가 되겠죠. 즉, 이 값이 True이면, 이전에 학습했던 것을 기억한다는 이야기이고, False이면 이 전에 학습했던 것을 기억하지 않는다는 말이 됩니다. 
- 따라서, 아래 코드와 같이 `warm_start`를 `True`로 바꾸고 진행하면, 첫번째 fitting할 때와 두번째 fitting할 때의 coefficient가 달라지는 것을 알 수 있죠. 

```python
sgd_reg_model = SGDRegressor(
    random_state=0, 
    verbose=0, 
    max_iter=10, 
    warm_start=True
)
print(f"== First  fitting")
sgd_reg_model.fit(X, Y)
print(f"---- Coefficient: {sgd_reg_model.coef_}")

print(f"== Second fitting")
sgd_reg_model.fit(X, Y)
print(f"---- Coefficient: {sgd_reg_model.coef_}")
```

```
== First  fitting
---- Coefficient: [1.26229792]
== Second fitting
---- Coefficient: [2.04389939]
```


## reference

- [stackoverflow - difference between partial-fit and warm-start](https://stackoverflow.com/questions/38052342/what-is-the-difference-between-partial-fit-and-warm-start)