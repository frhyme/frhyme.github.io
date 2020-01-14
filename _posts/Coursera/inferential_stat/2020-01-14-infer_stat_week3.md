---
title: Inferential Statistical Analysis with Python - WEEK 3
category: python-libs
tags: python python-libs coursera statsmodel
---


## WEEK 3 - HYPOTHESIS TESTING

- 이 단계에서는 가설 검정에 대한 부분을 배웁니다. 즉, WEEK 2에 배웠던 5가지 기법을 사용하여, hypothesis testing에 대해서 배우고, 이를 해석합니다.

## Introduction to Hypothesis Testing in Python

### One population hypothesis

- normal distribution을 따르는 `proportion`에 대해서, null hypothesis가 맞다고 가정했을 때, 현재의 추정 값 혹은 이 값보다 크게 나올 수 있는 확률은 무엇인가? 를 추정하는 것을 hypothesis라고 합니다. 
- 아래 코드에서는 200개의 관측에서 100, 110, 120, 130개로 성공의 수를 변경합니다. 즉, `proportion_hat`이 커질수록 현재의 null hypothesis에서 p-value가 어떻게 변하는지를 정리하였습니다. 

```python
import statsmodels.api as sm
#from statsmodels.stats.proportion import proportions_ztest

####################################
# params
# -----------------------------------
## count      : the number of successes in nobs, <nobs
## nobs       : the numbrer of trials
## value      : null hypothesis(ex: p=0.54)
## alternative: [‘two-sided’, ‘smaller’, ‘larger’]
# -----------------------------------
# return 
# -----------------------------------
## zstat : test statistic for the z-test
## p-value 
####################################
# 당연하지만, number of trial가 커질 수록 p-value가 작아지며,
# 즉 null hypothesis가 위배될 가능성이 커짐.
for count in [100, 110, 120, 130]:
    zstat, p_value = sm.stats.proportions_ztest(
        count = count, 
        nobs  = 200, 
        value =0.50,
        alternative = 'larger'
    )
    print(f"count: {count}")
    print(f"zstat  : {zstat:.5f}, p_value: {p_value:.5f}")
    print("--"*30)
```

- 당연하지만, number of trial가 커질 수록 p-value가 작아지며, 즉 null hypothesis가 위배될 가능성이 커집니다.

```
count: 100
zstat  : 0.00000, p_value: 0.50000
------------------------------------------------------------
count: 110
zstat  : 1.42134, p_value: 0.07761
------------------------------------------------------------
count: 120
zstat  : 2.88675, p_value: 0.00195
------------------------------------------------------------
count: 130
zstat  : 4.44750, p_value: 0.00000
------------------------------------------------------------
```

### Difference in Population Proportions.

- 집단 A와 집단 B가 있다고 합시다. 이 때, 이 두 집단의 분산은 동일할 때, 두 집단의 '평균'이 같은지 아닌지를 판단하려면 어떻게 해야 할까요? 우선, 당연히 null hypothesis는 `p1=p2`가 됩니다. 다시, 이를 `p1-p2=0`으로 변경할 수 있겠죠. 우리는 랜덤 변수 `p1-p2`에 대한 분포를 보는 것이니까요. 또한, 분산이 같다고 가정할 것인지, 다르다고 가정할 것인지에 따라서 조금씩 parameter와 테스트 방식이 달라집니다.
- 다음의 코드와 같이 실행하여 그 차이를 테스트할 수 있습니다.


```python
import numpy as np 
import statsmodels.api as sm

np.random.seed(0)

print("=="*20)
# sample1은 고정하고, 
sample1 = np.random.normal(0, 1, 100)
# sample2의 평균을 증가하면서, p_value의 변화를 예측함.
sample2 = np.random.normal(0.5, 1, 100)
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
```





## wrap-up

- WEEK 2에서는 confidence interval을 배웠고, WEEK 3에서는 hypothesis testing을 배웠습니다. 
- 아주 간단히 말하자면, 어떤 random variable이 특정한 분포(가령, normal dist(1.0, 3.0))을 따른다고 하고(null hypothesis) 표본으로 부터 추정한 추정값 `p_hat`이 이 분포대로 라면 나올 수 있는 가능성이 어떻게 되느냐?(p_value)를 평가해서, 충분히 작으면, null hypothesis를 무시하는 과정으로 전개되죠. 
- 물론 사이사이에 one-sided test로 할 것인가, two-sided로 할 것인가, 한 집단이 아니라, 두 집단에 대해서 비교한다면, 분산은 같은가 아닌가 등을 정리하게 되는데, 
- 또한, 이 주차에서는 보다 본격적으로 `statsmodels`를 사용하게 됩니다. 