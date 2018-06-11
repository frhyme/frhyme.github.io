---
title: sklearn에서 custom metric으로 모델 선정하기
category:
tags: 
---

## custom score 만들기 

- `sklearn.metric`에 이미 좋은 Metric들이 많기는 합니다만, 경우에 따라서 제가 직접 scoring을 하고 싶을때가 있습니다. 
- 뿐만 아니라, 제가 직접 만든 metric을 이용해서, model을 선택하고 싶을때가 있습니다. `GridsearchCV`에서도 해당 scoring을 그대로 이용하도록 하고 싶구요. 그렇다면 어떻게 해야 할까요? 
- 이 포스트에서는 그내용을 정리해보겠습니다. 

## 우선, RMSE or RMSLE

- RMSE: root mean squared error
- RMSLE: root mean squared log error

- 두 가지의 쓰임새가 다른데, [quora의 포스트] (https://www.quora.com/What-is-the-difference-between-an-RMSE-and-RMSLE-logarithmic-error-and-does-a-high-RMSE-imply-low-RMSLE)에 의하면....무슨 말인지 모르겠네요 허허허. 
- 무식한 저는 그냥 metric읇 변형해가면서 보려고 해요 하하핫. 간단하게 보면, 결국 error를 로그화한 것과 안 한 것의 차이인데, 따라서 RMSLE는 큰 error를 약간 무시한다고 볼 수도 있겠네요. 몇 가지 큰 error에서 보는 손해를 무시하더라도, 약간 나머지는 잘 맞추도록 scoring을 한다고 보면 될것 같습니다. 
- 약간 outlier들에 강건한 것과, 그렇지 않은 경우를 구분하는 것이라고 말할 수도 있겠네요. 

## just do it 

- 비교적 간단하게 만들었습니다. y_true, y_pred 를 입력받아서 scoring을 해주는 function을 만들고, 
- `sklearn.metrics.make_score()`에 해당 function을 argument로 넣어주고 
- 그 결과를 GridSearchCV에서 scoring에 넣어주면 됩니다. 
- 그럼 그 scoring에 따라서, 적합한 model을 골라주는 형식입니다. 

```python
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import make_scorer, mean_squared_error

def rmsle(actual_values, predicted_values, convertExp=True):
    """
    - root mean squared log error는 error를 로그화값으로 변환하고, 제곱하고, 평균을 내고, 루트를 씌웁니다.
    - skewness를 해결하기 위해 np.log1p를 했기 때문에, 값을 예측할 때 이를 다시 변환해서 처리해주는 것이 필요합니다. 
    """
    if convertExp==True:
        predicted_values = np.exp(predicted_values),
        actual_values = np.exp(actual_values)
        
    log_predicted_values = np.log(np.array(predicted_values)+1)
    log_actual_values = np.log(np.array(actual_values)+1)

    # 위에서 계산한 예측값에서 실제값을 빼주고 제곱을 해준다.
    difference = np.square(log_predicted_values - log_actual_values)
    return np.sqrt(difference.mean())

sample_size = 100
x = np.random.uniform(0, 10, sample_size)
y = x*3 + np.random.normal(3, 5, sample_size)

reg_rmsle = GridSearchCV(RandomForestRegressor(), {}, 
                   scoring=make_scorer(rmsle, greater_is_better=False))
reg_rmsle.fit(x.reshape(-1, 1), y)

plt.figure(figsize=(12, 4))
plt.scatter(x, y, alpha=0.5, label="norm_0_10")
plt.plot(sorted(x), reg_rmsle.predict(np.array(sorted(x)).reshape(-1, 1)), 
         c='red', label='pred_rmsle', linestyle='--')
plt.legend()
plt.savefig('../../assets/images/markdown_img/180611_makescorer.svg')
plt.show()
```

![](/assets/images/markdown_img/180611_makescorer.svg)

## wrap-up

- 경우에 따라서 적합한 metric을 잘 정의해서 사용합시다. 
- 아무튼 앞으로는 웬만하면 그냥 `GridSearchCV`를 사용하도록 하겠습니다. 

## reference

- <http://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html>
