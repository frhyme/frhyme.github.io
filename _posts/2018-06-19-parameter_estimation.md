---
title: 현재 데이터의 모수를 어떻게 추정할 수 있을까요? 
category: python-lib
tags: python python-lib MLE parameter-estimation numpy matplotlib 
---

## 그냥 .std() 같은걸로 하면 안되요?

- 네, 됩니다. `.mean()`으로 평균을 구해도 상관없어요. 요런 방법을 유식하게 **method of moment**라고 한다고들 합니다. 
- 그런데, 여기서는 다른 방법으로 할 거에요. 무엇이냐면, 대략, **가장 그럴법한 놈 찾기**
- 어찌 보면 p-value를 계산하는 방법과 비슷한데, 만약, 평균 추정이라고 한다면, '어떤 평균을 가졌다고 가정해야 현재 데이터와 가장 근접하게 나오느냐'를 찾는 것 같은거요. 이런거를 Maximal Likelihood Estimation 이라고 합니다. 

## 일단은 p-value로 생각해봅시다. 

- 실제 MLE는 좀 다른데, 이해를 돕기 위해서 우리가 이미 알고 있는 p-value로 생각해보려구요.
- p-value: null hypothesis 하에서(기본가설: '평균은 0이다' 등) 이 데이터가 나올 수 있는 가능성. 따라서 p-value가 유의미하게 작으면, 그 값이 해당 분포에서 나올 수 없다고 말해질 수 있다. 
- null hypothesis를 변형해가면서, 가장 큰 p-value를 가지는 null hypothesis의 경우, 해당 데이터를 가장 잘 설명해줄 수 있는 경우라고 말할 수 있지 않을까? 
- 따라서, 간단히 p-value를 사용해서 데이터 분포의 평균을 맞춰보려고 해요. 
- 물론, MLE로도 풀었습니다. 

## do it 

- method of moment와, p-value를 이용하는 경우, 그리고 scipy.optimize를 이용하여, 직접 모수를 추정하였습니다. 
- MLE 시에 `np.log`를 사용하지 않으면, 값이 제대로 예측되지 않는데(특히 분산의 경우), 이 이유에 대해서는 차후에 보충하는 것이 필요할 것 같습니다. 

```python
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import ttest_ind
from scipy.optimize import minimize

# MLE에서 사용하기 위한 gaussian rv X의 pdf
def f_x(mu_sig):
    mu, sig = mu_sig[0], mu_sig[1]
    r = 1/(np.sqrt(2*np.pi*(sig**2))) * np.exp(-(x-mu)**2/(2*sig**2))
    r = np.log(r) 
    #np.log로 변환해주지 않으면, 값이 정확하게 예측되기 어려운데, 왜 그런지는....흠
    return -r.sum() # scipy.optimize에는 maximize밖에 없기 때문에, -를 곱해서 진행해주어야 함

# 랜덤의 평균/분산을 가지는 데이터를 생성합니다. 
x = np.random.normal(np.random.uniform(0, 10), np.random.uniform(0, 10), 500)

print("------------------")
print('method of moment')
print("mean: {:.3f}, std: {:.3f}".format(x.mean(), x.std()))

# 평균 추정하기
ms = np.linspace(x.mean()-x.std()/2, x.mean()+x.std()/2, 100)
ps = [] # p_values
m_by_MLE = 0 # 추정된 mean 값
max_p_value = 0 # 가장 큰 p_value값
for m in ms:
    # 평균을 바꾸어가면서, 두 분포의 평균이 같은지 p-value를 계산함
    p_value = ttest_ind(x, np.random.normal(m, 1, len(x))).pvalue
    ps.append(p_value)
    if p_value > max_p_value:# 더 큰 p_value가 나오면, 그 값을 가장 likelihood가 높은 경우로 고려함. 
        m_by_MLE = m
        max_p_value=p_value

print("------------------")
print('by p-value')
print("mean: {:.3f}".format(m_by_MLE))
print("------------------")

### MLE with numeric optimzation 
result = minimize(f_x, np.array([10, 10]))
mu_sigma = result['x']
print("by MLE, optimization")
print("mu: {:.2f}, sigma: {:.2f}".format(mu_sigma[0], mu_sigma[1]))
print("------------------")
```

- 뭐 대충 비슷비슷하게 나오네요. 

```
------------------
method of moment
mean: 10.155, std: 4.733
------------------
by p-value
mean: 10.179
------------------
by MLE, optimization
mu: 10.15, sigma: 4.73
------------------
```

## wrap-up

- 그냥 MLE를 씁시다 하하하핫 

## reference 

- <https://datascienceschool.net/view-notebook/864a2cc43df44531be32e3fa48769501/>