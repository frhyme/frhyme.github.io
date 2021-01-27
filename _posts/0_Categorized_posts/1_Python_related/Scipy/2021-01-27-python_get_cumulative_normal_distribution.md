---
title: python - Cumulative normal distribution
category: python-lib
tags: python python-basic scipy
---

## python - Cumulative normal distribution function

- python에서 누적 정규 분포 함수(CDF, Cumulative normal Distribution Function)을 계산하는 방법을 정리했습니다.
- `scipy`를 이용하면 다음과 같습니다.

```python
from scipy.stats import norm

mu = 0
sigma = 1
# P(z < 1.96)
print(norm.cdf(1.96, mu, sigma))
# 0.9750021048517795
print(norm.cdf(2.58, mu, sigma))
# 0.9950599842422293

mu = 10
sigma = 20
x = 61.6
# X ~ norm(10, 20)
# Z ~ norm(0, 1)
z = (x - mu) / sigma
print(norm.cdf(z, 0, 1))
# 0.9950599842422293
```

- `scipy`를 사용하지 않고 직접 만들어서 처리하는 경우에는 다음과 같죠.
- `math.erf`는 [Error Function](https://en.wikipedia.org/wiki/Error_function)을 의미하는데 일단은 sigmoid function라고 생각하면 됩니다. 기본적으로 normal dist.의 CDF와 errof function는 같은 성질을 가지기 때문에, Normal CDF를 구할 때는 erf를 사용하죠.

```python
def cumulative_norm_dist(x, mu, sigma):
    from math import erf, sqrt
    # erf: Gauss Error functino
    # 그냥 sigmoid function이라고 이해하고 있어도 상관없습니다.
    r = (x - mu) / (sigma * sqrt(2))
    r = 1 + erf(r)
    return r * 0.5

print(cumulative_norm_dist(1.96, 0, 1))
# 0.9750021048517796
print(cumulative_norm_dist(2.58, 0, 1))
# 0.9950599842422294
```

## Reference

- [Stackoverflow - How to calculate cumulative normal distribution](https://stackoverflow.com/questions/809362/how-to-calculate-cumulative-normal-distribution)
