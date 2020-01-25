---
title: Q-Q plot을 이용한 normality test 
category: data-science
tags: python python-lib scipy normality qqplot numpy matplotlib boxplot seaborn
---

## 현재 데이터 분포가 가우시안분포를 따르는가? 

- 다양한 확률분포가 있는데, 그중에서, 수치들을 '가우시안 분포'를 따른다고 가정하고 모델링할 때가 많습니다. 그런데, 이건 가정이잖아요. 편하기는 한데, 정말 해당 데이터가 "가우시안 분포"를 정말 따르는지, 그건 어떻게 알 수 있을까요?

## Q-Q plot(Quantile Quantile plot)

- Q-Q plot은 유사공대생의 입장에서 말을 하자면, normal dist를 따를 때, quantile value와 현재 데이터 분포 상에서의 quantile 값을 scattering해주는 것과 비슷합니다. 
- 약간, 헷갈리는 부분이 있는데, 그냥, plotting 결과가 선형 상에서 삐뚤게 나타나면, normal dist를 따르지 않고, 따르면 normal dist라고만 우선을 생각하셔도 아주 문제는 없습니다. 일단 훑어보고 나중에 다시 봅시다 하하핳
- 사실, 그래서, q-q plot을 그리지 않고, 간단히 box-plot만 그려도 대략 비슷하게 알 수있습니다. 

## draw q-q plot

- `scipy.stats.probplot`를 사용해 q-q plot을 그려줍니다. 어떤 값을 받아서 그려주는 것이 아니고, 바로 그려집니다. 그냥 `plt.show()`를 하면 됩니다. 
- normal, exponential, log1p 를 각각 그려줬는데, 당연히, normal dist가 적당히 길쭉하게 잘 나옵니다 하하핫

```python
from scipy.stats import probplot
import matplotlib.pyplot as plt 
import numpy as np 

np.random.seed(0)

n = 100
x1 = np.random.normal(0, 1, n)
x2 = np.random.exponential(2, n)
x3 = np.log1p(x2)

f, axes = plt.subplots(2, 3, figsize=(12, 6))
axes[0][0].boxplot(x1)
probplot(x1, plot=axes[1][0]) #scipy.stats.probplot
axes[0][1].boxplot(x2)
probplot(x2, plot=axes[1][1]) #scipy.stats.probplot
axes[0][2].boxplot(x3)
probplot(x3, plot=axes[1][2]) #scipy.stats.probplot
plt.axis("equal")
plt.savefig('../../assets/images/markdown_img/180619_1347_qqplot.svg')
plt.show()
```

- 아래 그림에서 보는 것처럼, q-q plot에서 알 수 있는 것을 boxplot에서도 대략 알 수 있습니다. 

![](/assets/images/markdown_img/180619_1347_qqplot.svg)

## central limit theorem 

- 학부 2학년때(와 10년 넘었다) central limit theorem을 배운 기억이 나네요. 유사공대생인 저는 이제 와서, 이걸 다시 깨달았습니다....후....ㅠㅠㅠ
- 아무튼, centrali limit theorem이란 다음을 말합니다. 
    - 평균과 분산이 같은 여러 개의 독립변수(X1...Xn)가 있을 때 
    - 이 독립변수의 합으로 만든 새로운 독립변수를 Xsum이라고 하고, 
    - Xsum의 분포를 norm(0, 1)을 따르도록 표준화시켜주었을 때(이건 생략도 가능합니다)
    - Xsum은 n이 커질수록 가우시안분포를 따른다는 것. 
- 예전에는 바보처럼 sample size가 커질수록 좋다는 식으로 이해했네요...ㅠㅠㅠ흑 유사공대생 
- 아무튼, 이 말대로면, 어떤 분포든 n이 커지면 노멀 분포를 따른다는거죠?? 해봅시다. 

```python
"""
central limit theorem
- 평균과 분산이 같은 여러 개의 독립변수(X1...Xn)가 있을 때 
- 이 독립변수의 합인 Xsum이라고 하고 
- Xsum의 분포를 norm(0, 1)을 따르도록 표준화시켜주었을 때, 
- Xsum은 n이 커질수록 가우시안분포를 따른다는 것. 
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import probplot

n = 200
# n의 값이 다른 여러 가지 확률 분포를 가진 X_sum 독립변수를 만들어 줌
xss = np.array([
    np.array([np.random.exponential(2, n) for i in range(0, 1)]).sum(axis=0), 
    np.array([np.random.exponential(2, n) for i in range(0, 5)]+
             [np.random.uniform(2, 4, n)]).sum(axis=0), 
    np.array([np.random.exponential(2, n) for i in range(0, 20)]+
             [np.random.uniform(2, 4, n)]).sum(axis=0)
])
# apply_along_axis는 늘 헷갈리는데....저는 사실 그냥 map을 쓰는게 더 편하기는 합니다 하하핫
xss = np.apply_along_axis(lambda xs: (xs-xs.mean())/xs.std() , 1, xss)
f, axes = plt.subplots(xss.shape[0], 2, figsize=(12, 8))
for i in range(0, xss.shape[0]):
    sns.distplot(xss[i], ax=axes[i][0])
    probplot(xss[i], plot=axes[i][1])
plt.savefig('../../assets/images/markdown_img/180619_1342_central_limit_prove.svg')
plt.show()
```

- 독립분포 여러 개를 합칠 수록 가우시안분포를 따르게 되네요 하하핫

![](/assets/images/markdown_img/180619_1342_central_limit_prove.svg)

## 사실 평균과 분산이 같을 필요는 없어요. 

- 어차피, 평균과 분산을 표준화시켜주면 되거든요. 다음처럼 평균과 분산이 다른 것들을 합쳐도 n이 커지면 알아서 qqplot도, distplot도 모두 잘 나옵니다. 

```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import probplot

n = 200
# n의 값이 다른 여러 가지 확률 분포를 가진 X_sum 독립변수를 만들어 줌
xss = [
    np.random.exponential(np.random.randint(2, 100), n) for i in range(0, 20)
]
xss = list(map(lambda xs: (xs-xs.mean())/xs.std(), xss ))
xss = np.array(xss).sum(axis=0)
#xss = np.apply_along_axis(lambda xs: (xs-xs.mean())/xs.std() , 1, xss).sum(axis=0)

f, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.distplot(xss, ax=axes[0])
probplot(xss, plot=axes[1])
plt.savefig("../../assets/images/markdown_img/180619_1413_different_mean_var.svg")
plt.show()
```

![](/assets/images/markdown_img/180619_1413_different_mean_var.svg)

## wrap-up

- 이제 데이터 분석 전에 해주어야 하는 것이 두 가지로 늘었습니다. -
    - skewness 확인
    - normality test by qqplot(or boxplot)

## reference 

- <https://datascienceschool.net/view-notebook/76acc92d28354e86940001f9fe85c50f/>