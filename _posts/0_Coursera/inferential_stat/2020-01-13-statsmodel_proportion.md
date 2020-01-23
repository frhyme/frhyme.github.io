---
title: statsmodel - proportion confidence interval.
category: python-libs
tags: python python-libs coursera statsmodel confidence-interval 
---

## statsmodel로 binomial proportion에 대한 신뢰구간 구하기. 

- binomial proportion에 대해서 신뢰 구간을 계산하기 위하여, python의 통계 패키지인 `statsmodel`을 사용합니다.
- 예를 들어, 대한민국 남성들의 흡연율(proportion)을 추정한다고 합시다. N명에 대해서, p를 추정했을 때, 이 `p`라는 값이 90% 혹은 95%의 가능성으로 어느 구간 내에 존재하는지 계산하려면 statsmodel을 사용하여 다음과 같이 계산할 수 있습니다. 

```python
!pip install statsmodels
import statsmodels.api as sm

ci_low, ci_upp = sm.stats.proportion_confint(
    count = n*p, # number of success
    nobs = n, # number observations
    alpha = 0.05, # significance level
    method='normal' # default
)
print(f"n: {n}")
print(f"p: {p}")
print(f"Confidence interval low: {ci_low}")
print(f"Confidence interval upp: {ci_upp}")
```

- 위 코드의 실행 결과는 다음과 같죠.

```
n: 1000
p: 0.85
Confidence interval low: 0.8278688906821529
Confidence interval upp: 0.8721311093178471
```