---
title: python - scipy - 두 집단의 평균이 같은지 파악하는 ttest
category: python-libs
tags: python python-libs statsmodels scipy ttest scipy
---

## 두 집단이 있다고 합시다.

- 남성과 여성이라는 두 집단이 있습니다. 가령 이 두 집단이 같은 성질을 가지는지, 다른 성질을 가지는지 비교를 해보고 싶을 때가 있겠죠. 예를 들어, 이 두 집단의 키 평균은 같다고 할 수 있는지 혹은 다른지 등에 대해서 비교할 수 있고, 이를 위해서 두 집단으로부터 샘플링을 할 수 있겠죠. 
- 즉, 각 집단으로부터 샘플링을 하여 각 집단의 평균을 추정한 다음, 이 평균의 차이가 충분히 유의미한지를 ttest를 통해서 예측할 수 있습니다. 각각의 랜덤변수를 `rv1`, `rv2`라고 한다면, `rv1-rv2`가 새로운 랜덤변수가 되는 것이죠. 그리고 분산이 같을 때 혹은 다를 때에 따라서 서로 다른 기법을 써야 하며, 이는 `scipy.stats.ttest_ind`에 파라미터를 다르게 집어넣어주면 됩니다.


```python
import numpy as np 
from scipy.stats import ttest_ind

np.random.seed(0)
# p1, p2는 모집단에 대한 proportion이며, 
# 어느 정도 차이가 있지만 크지는 않음.
p1 = .36
N1 = 1000
p2 = .39
N2 = 500

print("=="*30)
print("== t-test for two proportion for ind population diff")
# p1의 분포를 가지는 binomial dist에 대해서 n번 시행했을 때의 결과를 size만큼 출력 
# 즉, n이 10이라면, 10번을 시행했을 때의 결과, 즉 0과 10 사이의 값이 적힘.
population1 = np.random.binomial(n=1, p=p1, size=N1)
# p1의 분포를 가지는 binomial dist에 대해서 n번 시행했을 때의 결과를 size만큼 출력 
population2 = np.random.binomial(1, p2, N2)
####
# Parameters
# a, b: 두 집단
# equal_var: 두 집단의 variance가 같은지, 다른지를 측정함. True일 경우는 같다고, False일 경우에는 다르다고 하며, 다른 테스트를 수행함.
# ----------------------
# Returns
# statistic: The calculated t-statistic.
# pvalue   : The two-tailed p-value.
####
statistic, p_value = ttest_ind(
    a=population1, 
    b=population2, 
    equal_var=True # variance equal.
)
print(f"statistic: {statistic:.5f}")
print(f"p_value  : {p_value:.5f}")
print("=="*30)

# 위와 같이 proportion 뿐만 아니라, 다음과 같이 그냥 continuous한 값을 집어넣어도 됩니다.
print("== t-test for two average for ind population diff")
N = 100000
sample1 = np.random.normal(0, 1, N)
sample2 = np.random.normal(0, 1, N)

statistic, p_value = ttest_ind(
    a=sample1, 
    b=sample2, 
    equal_var=True # variance equal.
)
print(f"statistic: {statistic:.5f}")
print(f"p_value  : {p_value:.5f}")
print("=="*30)
```

```
== t-test for two proportion for ind population diff
statistic: -2.72461
p_value  : 0.00651
============================================================
== t-test for two average for ind population diff
statistic: -0.44731
p_value  : 0.65465
============================================================
```


## wrap-up

- 당연하지만, N이 커질수록 더 정확한 값이 나오게 됩니다. 첫번째 실험에서 `p1`, `p2`의 차이가 크지 않으므로 이 때 N을 작게 두면, p-value에서 두 크게 나옵니다. 즉, null hypothesis가 타당할 가능성이 높다는 것이죠. 반대로 N을 키울수록 p-value는 전반적으로 떨어지는 경향을 보입니다. 
- 두번째 실험에서도 마찬가지로, N을 작게 할 경우, 두 분포의 평균이 다르다고 나오곤 합니다. N을 충분히 크게 할 경우, p-value가 충분히 커져서, 귀무가설을 지지할 가능성이 높아지죠. 