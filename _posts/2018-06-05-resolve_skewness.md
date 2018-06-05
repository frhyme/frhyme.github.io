---
title: data의 skewness를 삭제합시다. 
category: data-science
tags: python skewness python-lib scipy matplotlib pandas numpy 
---

## skewed data를 어떻게 해결할까요. 

- 예측 문제라는 것은 결국 "A로부터 B를 추론하는 것"인데, A의 분포와 B의 분포가 다를 수 있습니다. 아니, 다르게 표현하면, A의 어떤 부분이 B를 매우 예측하는데, 그것이 A라는 변수 혹은 데이터의 어떤 부분인지 맞추는 것은 매우 어렵죠. 
- 이런 종류의 문제를 data-preprocessing이라고도 하고, feature engineering이라고도 합니다. 
- 아무튼, A를 잘 정리하면, B를 훨씬 잘 예측할 수 있는데, A를 잘 정리하지 못해서, 실패하는 경우가 많습니다. 그중 하나로 `skewness`를 해결하는 것이 하나의 방법이 됩니다. 

## skewness는 무엇인가?

- 데이터의 분포가 한쪽으로 치우쳐여 있는 정도를 의미합니다. [d1, d2, ... , dn]의 값이 있을 때 이를 histogram의 형태로 만들어서 그려보면, 대충 왼쪽 오른쪽이 비슷하게 존재하는 경우가 있고, 한쪽으로만 치우쳐져서 그려지는 경우가 있습니다. 
- 이를 그림으로 표현하면 대략 다음과 같죠. 
    - 선형적인 관계를 가지는 `X`, `Y`를 각각 그린 다음 
    - `X`를 여러 가지 값들로 제곱하여, `sns.distplot`을 그리고 skewness를 계산해봅니다. 
- 왼쪽으로 치우쳐져 있을 때는 skewness가 음수, 오른쪽으로 치우쳐져 있을때는 skewness가 양수가 나오는 것을 알 수 있습니다. 

```python
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew

sample_size = 500

X = np.random.normal(0, 5, sample_size)
X = X + abs(X.min())
r = np.random.normal(0, 2, sample_size)
Y = X * 1.0 + r + abs(r.min())

df = pd.DataFrame({'X':X, 'Y':Y})
print(df.head())

sns.jointplot(x='X', y='Y', data=df, alpha=0.5)
plt.savefig('../../assets/images/markdown_img/180605_1519_resolve_skewness_scatter_plot.svg')
plt.show()

sqr_vs = [0.2, 0.5, 1.0, 2.0, 3.0]

f, axes = plt.subplots(1, 5, figsize=(15, 3))
for i, j in enumerate(sqr_vs):
    axes[i].set_title('X ** {} \nskewness = {:.2f}'.format(j, skew(df['X']**j)))
    sns.distplot(df['X']**j, ax=axes[i])
plt.savefig('../../assets/images/markdown_img/180605_1517_resolve_skewness_compare.svg')
plt.show()
```

```
           X          Y
0  14.495827  20.286481
1  10.530516  14.640092
2  13.954999  22.221570
3  15.537182  21.114477
4  11.702983  18.348981
```

![](/assets/images/markdown_img/180605_1519_resolve_skewness_scatter_plot.svg)

![](/assets/images/markdown_img/180605_1517_resolve_skewness_compare.svg)


## skewness에 따른 pearson_r 의 변화

- 선형적인 관련성을 파악하기 위해서는 보통 `pearson_r`을 많이 이용한다. 자세히는 귀찮고, 그냥 단순히 similarity 라고 생각해도 일단은 아무 문제가 없다
- 지금 해보려는 것은, 과연 skewness가 달라짐에 따라서 pearson_r이 달라지는가? 를 확인하고, 얼마나 달라지는가 를 확인하려 한다. 
    - 변수 `X`를 값을 변화시켜 가면서 제곱해보고, 각각의 `skewness`에 따라서, `pearson_r`이 어떻게 변하는지를 확인해보려고 한다. 

```python
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, pearsonr

df = pd.DataFrame({'X':X, 'Y':Y})
skew_lst = []
pearson_lst = []
for i, v in enumerate([0.1*j for j in range(1, 60)]):
    skew_lst.append(skew(df['X']**v))
    pearson_lst.append(pearsonr(df['X']**v, df['Y'])[0])

plt.figure(figsize=(12, 4))
plt.scatter(skew_lst, pearson_lst, marker='^', s=50, alpha=0.8)
plt.xlabel("skewness", fontsize='x-large')
plt.ylabel("pearson_r", fontsize='x-large')
plt.savefig('../../assets/images/markdown_img/180605_1536_skewness_pearsonr_v.svg')
plt.show()
```

- 아래에서 보는 것처럼, skewness가 대략 -1과 1 사이를 벗어나면 pearson_r이 급격하게 변하는 것을 알 수 있다. 
- 따라서, 미리 데이터의 skewness를 확인해보고, 값이 일정 범위를 넘어설 경우, `np.log`등으로 변경해주는 것이 필요하다. 

![](/assets/images/markdown_img/180605_1536_skewness_pearsonr_v.svg)


## wrap-up

- 음수가 있을 경우, 최소값을 빼서, 모든 값을 0보다 크게 바꿔주고
- `skewness`를 확인해서, 쏠림정도를 변경해주자!

## reference

- <http://hamelg.blogspot.com/2015/11/python-for-data-analysis-part-16.html>