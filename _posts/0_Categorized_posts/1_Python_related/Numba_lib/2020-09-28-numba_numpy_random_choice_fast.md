---
title: numba를 사용해서 numpy.random.choice를 빠르게 만들어 봅시다.
category: python-libs
tags: python numba python-libs numpy
---

## np.random.choice with multiple times

- 요즘에는 취미삼아, lotto 시뮬레이션 프로그램을 돌려보고 있습니다. 쓰고보니 거창해보이지만, 사실 로또는 시뮬레이션이랄 것도 없죠. 
- 그냥, 1부터 46번까지의 숫자 중에서, 보너스 번호를 포함하여 총 7개의 숫자를 뽑는 것이 다죠.
- 심지어, 코드는 그냥 다음과 같습니다.

```python
import numpy as np
possible_numbers = [i for i in range(1, 47)]
wining_number = np.random.choice(possible_numbers, size=7)
```

## 다만, N이 매우 크다면?

- 다만, "lotto에 참가하는 사람이 매우 많다"는 가정을 추가해보겠습니다. 단 1번 `np.random.choice()`를 수행하는 것이 아니라, 여러 번 반복적으로 수행해서 그 결과를 고려해야 한다면, 어떻게 될까요?
- 우선, 다음처럼 trial을 약 100,000 개의 로또를 시도한다고 생각하고 실행해봅니다. 이 때, 약 1.4초가 소요되는 것을 알 수 있습니다.

```python
import numpy as np
import time


def lotto_trials_without_jit(trial_n):
    """
    - trial_n 만큼 lotto를 뽑아봄
    """
    possible_numbers = [i for i in range(1, 47)]
    for i in range(0, trial_n):
        np.random.choice(possible_numbers, size=6, replace=False)

TRIAL_N = 100000
start_time = time.time()
lotto_trials_without_jit(TRIAL_N)
print(time.time() - start_time)  # 약 1.4 second.
```

- 현실계에서는, 훨씬 많은 수인 5,940만 게임이 일주일에 실행됩니다. 594억이 일주일에 들어온다는 것이죠.
- 다시, 현재의 100,000개를 돌리는데, 1.4초가 소요된다면, 5,940만 개를 돌리기 위해서는 15분 정도가 소요됩니다. 음, 이거 너무 비효율적인 것 같습니다.

## 어떻게 개선할 수 있을까? 

- 개선할 수 있는 방법은 있쬬. 우선, 각 trial들이 서로 영향을 주고 받지 않습니다. 즉, 병렬적으로 처리를 해도 된다는 것이죠. 병렬적으로 처맇가ㅔ 되면, 속도는 훨씬 빨라지겠죠.

### 그냥 numba로 빠르게 하자

- 하지만, 저는 귀찮으므로 그냥 [Numba](https://numba.pydata.org/numba-doc/latest/user/5minguide.html)를 사용해보기로 합니다.
- numba는 함수 앞에 간단히 `@jit()` decorator를 붙이는 것 만으로도 python 함수의 속도를 배우 빠르게 바꾸어주는 놈이죠. "어떻게 그렇게 되지?"라고 묻는다면, 저도 정확히기 이해하지 못했다고 말씀드리겠습니다 하하하. 
- 간단히 설명하자면, "처음 실행할 때, 기계어로 변경해두고, 다음에는 그 기계어로 바로 실행되도록 처리한다!"라는 방식이라고 말씀드릴 수 있겠네요.

```python
from numba import jit
import numpy as np
import time

# decorator를 다음처럼 한 줄 추가하기만 하면 됩니다.
@jit(nopython=False)
def lotto_trials_without_jit(trial_n):
    # 그리고 np.array()로 바꾸는 것이 더 빠름.
    possible_numbers = np.array([i for i in range(1, 47)])
    for i in range(0, trial_n):
        np.random.choice(possible_numbers, size=6, replace=False)
```

- 이렇게 바꾼 다음 실행을 해보면, 다음과 같습니다. 물론, 함수를 처음 실행할 때는 시간이 조금 걸리지만, 이후에는 아주 빨라지죠. 

```python
TRIAL_N = 100000
lotto_trials_without_jit(TRIAL_N)
start_time = time.time()
lotto_trials_without_jit(TRIAL_N)
print(time.time() - start_time)  # 2.1457672119140625e-06
```

## Wrap-up

- 오늘 글에서 쓴 내용은 딱 두가지입니다. 
  - python native로 짠 경우 `@numba.jit` 데코레이터를 통해서 최적화할 것. 
  - 가능하면 기본 list보다는 `numpy.arra()` 등으로 코딩할 것.
- 다만, 아직 numba는 그 활용도가 넓다고 말하기는 어려워요.