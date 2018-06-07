---
title: sklearn.mlpregressor는 쓸만한가요? 
category: python-lib
tags: python python-lib sklearn regression neural-network matplotlib 
---

## sklearn.mlpregressor는 쓸만한가요? 

- classification시에 neural network이 좋다는 것은 너무 당연하고도 명백한 사실인데, neural network는 쓸만한건지 사실 잘 모르겠습니다. 
- regression을 할때, 한번씩 `sklearn.mlpregressor`를 사용하는데, 이게 정확도가 지나치게 떨어지는 것을 볼 수 있습니다. 
- 그래서, 제가 hyperparameter tuning을 잘못하는 것인지도 궁금하고, 어떻게 써야 좋은지도 궁금해서 포스팅을 해보려고 합니다. 

## data geneneration and regression 

- x의 값에 의해서 polynomial하게 변하는 y를 만들었습니다. 

```python
import warnings
warnings.filterwarnings("ignore")

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

sample_size = 500

x = np.random.uniform(-20, 20, sample_size).reshape(-1, 1)
y = x**4 + x**3 + x**2 + x + np.random.normal(0, 10, sample_size).reshape(-1, 1)

print(x.shape, y.shape)

plt.figure(figsize=(12, 4))
plt.scatter(x, y, marker='o', s=20, alpha=0.4, c='red')
#plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size =0.7, test_size=0.3)


models = [
    LinearRegression(), 
    MLPRegressor(hidden_layer_sizes=[512, 4], alpha=0.005, random_state=42),
    MLPRegressor(hidden_layer_sizes=[48, 4], max_iter=5000, alpha=0.005, random_state=42), 
    MLPRegressor(hidden_layer_sizes=[512, 4], max_iter=5000, alpha=0.005, random_state=42), 
    MLPRegressor(hidden_layer_sizes=[1024, 4], max_iter=5000, alpha=0.005, random_state=42),
    MLPRegressor(hidden_layer_sizes=[1024, 512, 4], max_iter=5000, alpha=0.005, random_state=42),
]

for m in models:
    m.fit(x_train, y_train)
    print(m.__class__)
    print(r2_score(y_train, m.predict(x_train)))
    print(r2_score(y_test, m.predict(x_test)))

plt.figure(figsize=(12, 6))

plt.scatter(x, y, marker='^', s=50, alpha=0.7, label='y_true')
for i, m in enumerate(models):
    plt.scatter(x, m.predict(x), marker='o', s=10, alpha=0.7, label='nn_{}'.format(i))
plt.legend()
plt.savefig('../../assets/images/markdown_img/180607_1614_nn_scatter.svg')
plt.show()
```

- 해당 데이터의 분포가 포물선의 형태로 되어 있어서, linear regression의 경우, r2_score가 매우 떨어지는 것을 알 수 있습니다. 
- neural_network의 경우도 마찬가지인데, 단, `max_iter`를 조절하니까 압도적으로 좋아지는 것을 알 수 있습니다. 

```
<class 'sklearn.linear_model.base.LinearRegression'>
0.0283777235436
-0.0617858892415
<class 'sklearn.neural_network.multilayer_perceptron.MLPRegressor'>
-0.392900747866
-0.30431829499
<class 'sklearn.neural_network.multilayer_perceptron.MLPRegressor'>
0.660804204872
0.59980194264
<class 'sklearn.neural_network.multilayer_perceptron.MLPRegressor'>
0.92684929777
0.920185192685
<class 'sklearn.neural_network.multilayer_perceptron.MLPRegressor'>
0.991719741159
0.993990888503
```

- 그림을 그려 보면, `max_iter`와 `hidden_layer_sizes`를 함께 높여야 의미가 잇는 것을 알 수 있습니다. 

![](/assets/images/markdown_img/180607_1614_nn_scatter.svg)


## max_iter!!! 

- 늘 생각없이 돌리다보니, hyper parameter tuninng을 잘하지 않습니다만, `sklearn`과 같은 것들을 돌릴 때는 몇 번이나, backpropagation을 할지를 정확히 알아야 합니다. 여기서 그 값을 의미하는 것이 바로 `max_iter`입니다. 
    - 보통 `mlpregressor`를 돌릴 때, 쓸데없이 warning이 막 뜬다! 라고 생각하실 때가 있는데 이는 아직 optimization이 제대로 되지 않았다는 것을 의미합니다. 
    - 따라서 이렇게 warning이 뜰 때는 max_iter를 조절하면서 결과를 보시면 좋습니다. 

## wrap-up

- 결론은 결국 **니가 병신이지 라이브러리가 병신이 아니란다** 라고 말할 수 있겠네요....ㅠㅠ
- 앞으로는 hidden_layer_size를 올릴 거면, `max_iter`도 같이 많이 올립시다....
- 그리고, mlpregressor의 경우는 overfitting이 되기 쉽습니다. train set에는 잘 맞는데, test set에는 안 맞는 경우가 많으니, 반드시 cross validation을 하는 것이 중요합니다. 

## reference 

- <http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html>