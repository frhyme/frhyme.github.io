---
title: data preprocessing 잘하기 
category: data-preprocessing
tags: python python-lib scipy skewness
---

## data preprocessing 을 잘해보려고 합니다. 

- skewness 해결, MinMaxScaler, robustScaler 등을 처리합니다. 
- missing value도 다루어야 하는데, missing value의 경우는 상황에 따라 달라지는 면들이 있는 것 같아요. 그래서 일단은 제외하였습니다. 
- 본 포스트에서는 skewness를 조절하는 방법과, scaling, 그리고 skewness에 따라서 r2_score가 어떻게 달라지는지를 보려고 합니다. 

## data generation 

- 일단 임의의 데이터를 만들어봅시다. 

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, RobustScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import scipy

import itertools 
import seaborn as sns 
from matplotlib import gridspec

sample_size = 500
x1 = np.exp(np.random.normal(0, 1, sample_size)) # numerical value
x2 = np.array(list(itertools.chain.from_iterable([[i for j in range(0, sample_size//4)] for i in range(0, 4)])))

# skewness를 높이기 위해서, 거듭제곱한다. 
y = (x1 * 1 + x2*5 + np.random.normal(0, 1, sample_size))**5

df = pd.DataFrame({'x1':x1, 'x2':x2, 'y':y})
X = df[['x1', 'x2']]
Y = df['y']

for col in df.columns:
    print("skewness of column({}): {}".format(col, scipy.stats.skew(df[col])))

reg = LinearRegression()
reg.fit(df[['x1', 'x2']], df['y'])
print("r2_score: {}".format(r2_score(Y, reg.predict(X))))

# 그림을 그려줍니다. 
f, axes = plt.subplots(1, 3, figsize=(12, 4))
for i, col in enumerate(df.columns):
    #axes[i].scatter(df[col], y, alpha=0.5)
    sns.distplot(df[col], ax=axes[i])
    axes[i].set_title("skewness: {}".format(scipy.stats.skew(df[col])))
    axes[i].set_xlabel(col)
plt.savefig('../../assets/images/markdown_img/180606_2107_data_preprocess.svg')
plt.show()
```

- 만들어진 데이터의 `skewness`를 보면, 매우 높은 편입니다. `x1`, `y` 모두, 높은 편인데 이로 인해서 `r2_score` 또한 매우 높게 나오는 것을 알 수 있습니다. 
- 우선 이러한 skewness를 없애는 것이 매우 중요합니다. 

```
skewness of column(x1): 4.290130622189554
skewness of column(x2): 0.0
skewness of column(y): 10.355241349505134
r2_score: 0.498353813401178
```

![](/assets/images/markdown_img/180606_2107_data_preprocess.svg)


## scaling and resolving skewness 

- scaling을 하고, skewness를 없애 줍니다. 
    - skewness의 경우 box-cox transformation을 쓰는 것도 방법이지만, 간단히 `np.log1p` 만으로도 괜찮은 결과를 얻을 수 있습니다. 
    - `np.log1p`를 적용하기 위해서는 값들이 0 이상이어야 하고, 이를 위해서 scaling을 일괄적으로 적용해줍니다. 

```python

"""
- 사실 scaling 자체는 r2_score 자체를 변화시키지는 않습니다. 
- 하지만, 향후 np.log1p를 할때나, 등등에 현재 값들에 모두 양수만 있고, 또 outlier에 대해서 강건하게 처리해주는 것이 좋기 때문에 
일단 이 두가지에 대해서 모두 scaling을 해줍니다. 
"""
scaler1 = MinMaxScaler()
scaler2 = RobustScaler()
X_scaled = scaler1.fit_transform(scaler2.fit_transform(X.values.reshape(-1, 2)))
Y_scaled = scaler1.fit_transform(scaler2.fit_transform(Y.values.reshape(-1, 1)))

Y_scaled_log = Y_scaled

skew_lst = []
r2_score_lst = []
for i in range(0, 40):
    Y_scaled_log = np.log1p(Y_scaled_log)
    #print("np log {}, skewness: {}".format(i, scipy.stats.skew(Y_scaled_log)))
    skew_lst.append(scipy.stats.skew(Y_scaled_log))
    
    reg = LinearRegression()
    reg.fit(X_scaled, Y_scaled_log)
    Y_scaled_pred = reg.predict(X_scaled)
    for j in range(0, i+1):
        Y_scaled_pred = np.exp(Y_scaled_pred) - 1
    #print("r2_score: {}".format(r2_score(Y_scaled, Y_scaled_pred)))
    r2_score_lst.append(r2_score(Y_scaled, Y_scaled_pred))


fig = plt.figure(figsize=(12, 3)) 
gs = gridspec.GridSpec(nrows=1, # row 몇 개 
                       ncols=2, # col 몇 개 
                       width_ratios=[9, 3]
                      )

#print(max(r2_score_lst)), 0.81
ax0 = plt.subplot(gs[0])
ax0.plot(skew_lst, 'b*', label='skewness')
ax0.plot(r2_score_lst, 'go-', label='r2_score')
#ax0.set_ylim(min(r2_score_lst), max(skew_lst))
plt.legend()

ax1 = plt.subplot(gs[1])
ax1.plot(r2_score_lst, 'g-o', label='r2_score')
ax1.set_ylim(0, 1)
plt.legend()
plt.savefig('../../assets/images/markdown_img/180606_2114_skewness_r2_score_change.svg')
plt.show()
```

- skewness가 높을 경우, 얼마나 낮춰줘야 하는가? 라는 생각이 들 수 있는데, 이 때는 이 값의 변화에 따라서, `r2_score`가 얼마나 변하는지를 확인하면서 조절하는 것이 좋습니다. 
- 그림에서 보는 것처럼 일반적으로 2 아래면 `r2_score` 또한 일정 값으로 수렴하는데, 2의 어떤 지점을 넘어서면 data간에 명확한 구분이 없어져서, `r2_score`가 음의 값으로 떨어지게 됩니다. 즉, 알아서 잘 조절하셔야 합니다. 

![](/assets/images/markdown_img/180606_2114_skewness_r2_score_change.svg)


## filling missing values

- 빈 칸을 채울 때는 보통, 그냥 해당 column의 평균으로 채운다. missing value가 너무 많을 때는 문제가 될 수 있지만, 많지 않을때는 그정도로는 큰 문제가 되지 않을 수 있다. 
- 해당 missing value를 다른 값들을 이용해서 적합한 값으로, 예측하는 것도 하나의 방법이 될 수 있는데, 이건 나중에 한번 해보면 좋겠다. 
- `fillna(col.mean())`이나, `fillna(col.mode()[0])`으로 웬만한 것들을 다 할 수 있다. 

```python
import numpy as np 
import pandas as pd

numericCol = pd.Series([1, 1, 1, 2, 3, 4, 5, np.nan, 7, np.nan])
print("missing value: {}".format(numericCol.isnull().sum()))
print("-------")
print(a.fillna(numericCol.mean()))
print("-------")
nonNumericCol = pd.Series(['a', 'b', 'c', 'b', 'a', np.nan])
# 가장 많은 걸로 채우기 
print(nonNumericCol.fillna( nonNumericCol.mode()[0]))
print("-------")
```

## wrap-up

- 으어 missing value 극혐. 


