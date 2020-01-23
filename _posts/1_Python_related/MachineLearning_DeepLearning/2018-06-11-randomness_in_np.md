---
title: numpy에서 randomness 이용하기 
category: python-lib
tags: python python-lib random numpy 
---

## numpy에서 randomness 이용하기 

- python numpy에 다양한 random 함수들이 있는데, 이를 어떻게 이용할 수 있을지를 정리합니다. 

## just do it.

- 뭐 쓰고 보니 쓸게 많을줄 알았는데 매우 간단하군요. 

```python
import numpy as np 

## normalization에서 뽑는 경우 
mu=0
sigma = 5
print("random sampling from normal dist.")
print(np.random.normal(mu, sigma, size=(2, 4)))
print("-----")
## uniform하게 float을 뽑는 경우 
print("random sampling from uniform dist.")
print(np.random.rand(10))
print("-----")
## uniform하게 integer를 뽑는 경우 
print("random sampling from integer sets")
print(np.random.randint(low=0, high=10, size=50))
    # high 값은 포함되지 않는다. 
print("-----")
## 특정한 값들에서 뽑는 경우 
print("random sampling from specific set")
print(np.random.choice(['a', 'b', 'c'], size=10, p=[1/3, 1/3, 1/3]))
```

```
random sampling from normal dist.
[[ 3.2369869   2.12594494  6.19852301 -1.26701663]
 [ 4.30959055 -3.53541845 -7.60143385  0.97559074]]
-----
random sampling from uniform dist.
[ 0.0787337   0.84896208  0.81108126  0.25648967  0.0047072   0.03653954
  0.31854997  0.46306836  0.98978169  0.2151292 ]
-----
random sampling from integer sets
[9 6 3 8 7 8 4 0 2 4 5 9 9 0 9 4 1 9 3 9 1 0 5 0 5 9 7 9 5 7 2 6 0 2 8 5 1
 9 2 5 5 8 9 5 4 0 9 3 2 1]
-----
random sampling from specific set
['a' 'b' 'b' 'a' 'a' 'c' 'b' 'a' 'b' 'b']
```

## reference 

- <https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.random.html>