---
title: regression 결과를 평가해봅시다. 
category: machine-learning
tags: sklearn python python-lib machin-learning regression

---

## continous한 값을 예측하고 잘했는지 어떻게 평가할까요. 

- 그러니까, 내가 예측하려는 것이 집의 가격, 주식의 가격 등 같은 값들이라고 하면, classification과는 다른 식으로 평가해야 합니다. 
- 아주 간단하게는, 내가 예측한 값(`y_pred`)과 실제 값(`y_true`)간의 차이를 계산하고, 그 합(제곱합, 로그합 등)을 보면 될 것 같습니다만, standardization된 값으로 볼 수는 없을까요? 
- 아무튼, 여기서는 regression을 평가할 수 있는 score들을 정리합니다. 모델은 간편하게 `linear-regression`으로 고정하고, 다양한 분포로 그려보면서, 진행해보려 합니다. 


## just do it. 

- linear-regression이 잘 맞는 경우와, 잘 맞지 않는 경우(noise가 큰 경우)를 각각 그리고, `explained_variance_score`, `mean_squared_errors`, `r2_score`이 세 가지에 대해서 scoring을 했습니다. 
    - `explained_variance_score`: y_pred에 의해 설명되는 분산의 정도 
    - `mean_squared_errors`: sum((y_true - y_pred)**2)
    - `r2_score2`: - `explained_variance_score`와 같습니다.
- 결과적으로 보면, `mean_squared_errors`의 경우는 표준화가 되어 있지 않아서 저는 r2_score를 쓰는 것이 더 좋을 것 같네요. 

```python
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import explained_variance_score, mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import MinMaxScaler

def PrintRegScore(y_true, y_pred):
    print('explained_variance_score: {}'.format(explained_variance_score(y_true, y_pred)))
    print('mean_squared_errors: {}'.format(mean_squared_error(y_true, y_pred)))
    print('r2_score: {}'.format(r2_score(y_true, y_pred)))
"""
score가 높도록 데이터를 생성 
"""
x = np.random.normal(0, 1, sample_size)
y_true = x*30 + np.random.normal(0, 10, sample_size)

scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x.reshape(-1, 1))

plt.figure(figsize=(10, 4))
plt.scatter(x_scaled, y_true, alpha=0.5, c='red')
plt.savefig('../../assets/images/markdown_img/180605_1217_linreg_score_well_fit.svg')
plt.show()

y_pred = LinearRegression().fit(x_scaled, y_true).predict(x_scaled)
PrintRegScore(y_true, y_pred)
"""
분산을 확 늘려서, score가 낮도록 데이터를 생성한 경우 
"""
x = np.random.normal(0, 1, sample_size)
y_true = x + np.random.normal(0, 30000, sample_size)

scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x.reshape(-1, 1))

plt.figure(figsize=(8, 3))
plt.scatter(x_scaled, y_true, alpha=0.5, c='red')
plt.savefig('../../assets/images/markdown_img/180605_1217_linreg_score_bad_fit.svg')
plt.show()

y_pred = LinearRegression().fit(x_scaled, y_true).predict(x_scaled)

print('explained_variance_score: {}'.format(explained_variance_score(y_true, y_pred)))
print('mean_squared_errors: {}'.format(mean_squared_error(y_true, y_pred)))
print('r2_score: {}'.format(r2_score(y_true, y_pred)))
```

- 아래에서 보는 것처럼, 잘 맞을때와 잘 맞지 않을때의 값들이 다르고, 특히 mean_squared_erros의 경우는 표준화가 되어 있지 않아서 값 자체가 매우 큰 것을 알 수 있습니다. 

```
explained_variance_score: 0.9060481256881127
mean_squared_errors: 87.48727714048309
r2_score: 0.9060481256881127

explained_variance_score: 0.014843208143344278
mean_squared_errors: 908120920.5647349
r2_score: 0.014843208143344278
```

- 사용한 데이터 scatter plot 

![](/assets/images/markdown_img/180605_1217_linreg_score_well_fit.svg)

![](/assets/images/markdown_img/180605_1217_linreg_score_bad_fit.svg)


## wrap-up

- 뭐 다양한 score들이 있는줄 알았는데 없습니다. 그냥 `r2_score`를 사용합시다. 

## reference

- <http://scikit-learn.org/stable/modules/model_evaluation.html>