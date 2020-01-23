---
title: python - statsmodel - proportion ztest.
category: python-libs
tags: python python-libs coursera statsmodels ztest
---

## normal dist.를 따르는 proportion에 대한 test. 

- 우리가 표본 집단으로부터 `p`라는 비율을 측정했습니다. 충분히 많은 `N`에 대해서 측정했고, 따라서, `p` 또한, normal distribution을 따르겠죠. 그리고, 우리가 랜덤변수 `p`에 대해 측정한 결과 `p_hat`이 0.56이 나왔다고 합시다. 
- 그리고 귀무가설(Null hypothesis)에서는 `p`가 0.54라고 하겠습니다. 즉, `p`라는 랜덤변수는 평균이 0.54인 분포를 가지게 된다는 것이죠. 
- 이 때, 0.54의 정규분포에서 0.56보다 큰 값이 나올 수 있는 확률, 이것이 p-value죠. 
- 아주 쉽게 극단적인 예를 들어보겠습니다. 우리의 null hypothesis에서는 `p`가 0.54의 평균을 가지는 분포라고 정의하였는데, `p_hat`이 0.9가 나왔다고 해보죠(물론 N도 충분히 크구요). 그렇다면, 우리의 null hypothesis가 틀릴 것은 당연해 보이지 않나요? 0.54의 평균을 가지는 분포가 맞다면, p_hat이 저렇게 나오는 게 거의 로또에 가까운 것이 되니까요. 
- 반대로, `p_hat`이 0.60 정도가 나왔다고 해봅시다. 그렇다면, 이 값이 타당한지 아닌지 조금 아리까리해지죠. 그래서, 이 아리까리한 정도를 파악하기 위해서 null hypothesis가 맞다고 놓고, 그 때의 p-value를 측정합니다. 그 값이 어느 정도 크면, null hypothesis가 틀리다고 할 수 있는 것이죠. 

## do it with statsmodel. 

- 따라서, 그 값을 측정하기 위해 `statsmodels`을 이용합니다. 

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

## wrap-up

- 즉, null hypothesis는 기본적인 가정을 말합니다. '그래, null hypothesis가 맞다고 가정하고, 이 랜덤변수를 그 가정에 맞춰서 돌려보자. 그런데 그게 맞다고 하면, 이 결과가 나오면 안되는거 아냐?'를 파악하기 위한 것이 hypothesis testing이죠.