---
title: python - statsmodel - ttest independent samples
category: python-libs
tags: python python-libs coursera statsmodels ttest
---

## 서로 다른 두 집단의 평균이 같은지를 테스트하자.

- 두 집단(남성과 여성, 흑인과 백인, 청소년과 노인 등등등) 에 대해서 이 두 집단의 평균이 같은지를 테스트 해봅니다. `scipy.stats.ttest_ind`를 사용해도 되지만, `statsmodels`에도 같은 방식이 있어서, 이 값을 이용해서 정리를 해봅니다.
- `집단1(sample1)`은 고정하고, `집단2(sample2)`에 대해서 평균을 늘리면서 두 집단의 평균이 같은지 다른지를 ttest해봅니다.


```python
import numpy as np 
import statsmodels.api as sm

np.random.seed(0)

print("=="*20)
# sample1은 고정하고, 
sample1 = np.random.normal(0, 1, 100)
for m in [0.1*i for i in range(0, 5)]:
    # sample2의 평균을 증가하면서, p_value의 변화를 예측함.
    print(f"mean: {m:.2f}")
    sample2 = np.random.normal(m, 1, 100)
    t_p_d= sm.stats.ttest_ind(
        x1=sample1, 
        x2=sample2, 
        alternative='two-sided', 
        usevar='pooled' # same variance
    )
    tstat, p_value, degree_of_freedom = t_p_d
    print(f"tstat            : {tstat:.6f}")
    print(f"p_value          : {p_value:.6f}")
    print(f"degree_of_freedom: {degree_of_freedom}")
    print("--"*20)
print("=="*20)
```

```
========================================
mean: 0.00
tstat            : -0.152958
p_value          : 0.878587
degree_of_freedom: 198.0
----------------------------------------
mean: 0.10
tstat            : 0.136647
p_value          : 0.891449
degree_of_freedom: 198.0
----------------------------------------
mean: 0.20
tstat            : 0.410815
p_value          : 0.681653
degree_of_freedom: 198.0
----------------------------------------
mean: 0.30
tstat            : -1.566059
p_value          : 0.118932
degree_of_freedom: 198.0
----------------------------------------
mean: 0.40
tstat            : -0.953851
p_value          : 0.341322
degree_of_freedom: 198.0
----------------------------------------
========================================
```