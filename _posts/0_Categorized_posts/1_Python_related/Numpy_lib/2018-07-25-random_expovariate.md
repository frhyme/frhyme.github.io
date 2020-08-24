---
title: random.expovariate == np.random.exponential
category: python-lib
tags: python python-lib numpy random exponential distribution
---

## np.random을 사용합시당. 

- `random.expovariate()`라는 코드를 발견했습니다. 
- exponential 분포를 표현해주는 코드인 것 같은데, `numpy`에 비슷한 코드가 이미 있지 않을까? 하는 생각이 들었습니다. 

- 다음 아래 코드는 동일합니다. 
    - random에서는 `lambda`를 사용하고, np.random에서는 beta, 즉 1/lambda를 사용합니다. 
    - 간단하게 말하면, exponential distribution의 평균은 1/`lambda` 가 평균입니다. 

```python
import random
random.expovariate(1/10)
```

```python
import numpy as np 
np.random.exponential(10)
```

## wrap-up

- 결론은 `numpy`를 사용합시다. 
- 그리고 [이 부분](https://stackoverflow.com/questions/8592048/is-random-expovariate-equivalent-to-a-poisson-process) 도 읽어보면 좋습니다. poisson process와 관계된 부분입니다. 