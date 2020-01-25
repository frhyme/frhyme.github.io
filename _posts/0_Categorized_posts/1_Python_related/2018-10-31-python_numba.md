---
title: numba를 사용하여 파이썬의 속도를 올려보자. 
category: python-libs
tags: python numba python-libs
---

## numba를 사용하여, 파이썬의 속도를 올려보자. 

- 요즘, 계산을 좀 돌리고 있는데, 속도가 너무 느린거에요. 원래 퓨어 파이썬은 속도 자체가 느리기는 한데, 그래도 나름 속도를 빠르게 만들어보려고 노력을 했는데도, 너무 느립니다.
- 물론 처음부터 그냥 c로 코딩을 하면, 훨씬 빠르기는 하겠지만, c에서 파이썬으로 넘어오는 것은 마치 삼각팬티에서 사각팬티의 길로 넘어가는 것처럼 비가역적인 반응입니다. 돌아갈 수 없습니다. 그냥 파이썬으로 코딩하면서, 빠르게 코딩할 수 있는 방법을 찾는 수 밖에요. 
- 그래서 속도를 좀 빠르게 할 수 있는 방법이 없나? 하고 찾아보다가 [numba](http://numba.pydata.org/)를 발견했습니다. 

## what is numba? 

> Numba is an open source JIT compiler that translates a subset of Python and NumPy code into fast machine code.

- 파이썬과 numpy 코드를 더 빨리 실행될 수 있도록 변환해주는 JIT compiler 라고 합니다. 저는 compiler수업을 듣지 않았기 때문에, 자세히는 모릅니다. 아무튼, 파이썬이 사실 아주 느린데, 이걸 빠르게 변환해주는 무엇인것 같군요. 
- 긴 말하지 않고, 일단 써보겠습니다.

## use it

- 파이썬으로 만든 함수 앞에 데코레이터 `@jit(nopython=True, cache=True)`만 붙이면 됩니다. 
- `nopython`, `cache`가 각각 무엇인지는 나중에 설명드리겠습니다. 

```python
!pip install numba
import numba 
from numba import jit 
import numpy as np 

def sum_to_n_pure_python(n):
    s = 0 
    for i in range(0, n+1):
        s=s+i
    return s
%time print(sum_to_n_pure_python(5000000))
print("==="*20)

@jit(nopython=True, cache=True)
def sum_to_n_numba(n):
    s = 0 
    for i in range(0, n+1):
        s=s+i
    return s
sum_to_n_numba(2) ## 한번 compile이 되어야 해서, 한번 실행함
%time print(sum_to_n_numba(5000000))
print()
```

- 단순히 한 줄만 추가했을 뿐인데, 3000배 빨라지는군요. 

```
12500002500000
CPU times: user 374 ms, sys: 0 ns, total: 374 ms
Wall time: 374 ms
============================================================
12500002500000
CPU times: user 127 µs, sys: 1 µs, total: 128 µs
Wall time: 134 µs
```

## wrap-up

- recursive 함수에서도 빠르게 작동하기는 하지만, 그렇게 빨라지지는 않습니다(피보나치로 테스트). 이 경우에는 오히려 `functool`에 있는 `@lru_cache`를 쓰는 편이 훨씬 좋습니다. 
- pure python과 numpy를 제외한 다른 라이브러리들에서는 아직 잘 작동하지 않습니다. 
    - pandas에서 잘 안되고, 
    - generator에 대해서도 아직 적용이 되지 않습니다. 
- 찾아보니 GPU랑 섞어서 쓰려면 또 어떻게 하는 방법이 있는데, 이걸 추후에 알아보도록 하겠습니다. 

## reference 

- <http://numba.pydata.org/>