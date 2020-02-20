---
title: np.random.RandomState(seed)를 이용해서 난수를 생성합시다.
category: python-libs
tags: python python-libs numpy random
---

## 2-line summary 

- 일반적으로 numpy를 이용해서 random number(난수)를 생성하는 방법은, `np.random.random()`임. 
- 하지만, `np.random.RandomState(seed)`를 이용해서 관련 method가 정의된 객체를 선언 및 정의하여 사용할 수도 있음. 

## Way 1: `np.random.random()`

- 기존의 방법은 다음과 같습니다. 사실, 이 방법도 딱히 큰 문제는 없긴 하죠 사실.

```python
import numpy as np 
# 일단 seed 값을 지정하고, 
np.random.seed(seed=0) 
# np.random에 있는 함수에 직접 접근 하여 random number를 생성. 
new_random_number = np.random.random(size=3)
```

## Way 2: `np.random.RandomState()`

- 기존의 방법에서는 `numpy`에 존재하는 random generator에 직접 접근하여, 난수를 생성했다면, 여기서는 **난수생성기**라는 object를 새로 만들어준다고 생각하면 됩니다. 
- 즉, 특정 seed를 가지는 `np.random.RandomState()`를 만들어주고, 여기서부터 이 object에 접근하여 난수를 생성해주는 것이죠. 즉 별 차이는 없습니다. 

```python 
RandomGenerator = np.random.RandomState(seed=0)
new_random_number = RandomGenerator.random(size=1)
```

## Difference: Global and local. 

- 이 차이는 오히려, 난수를 생성할 때, 재생산성(reproducibility)를 확인하기 위해서 seed를 어떻게 먹일 것인가? 와 연관이 있습니다(참고: 같은 seed를 세팅하면 같은 값이 순서대로 나옴)
- `np.random.seed(seed=10)`를 사용해서 seed를 세팅할 경우에는 개별적으로 seed를 세팅할 수 없습니다. 
- `numpy`에 있는 global한 seed를 바꾸는 것이기 때문에, 다른 함수에서 다시 `seed`를 새롭게 설정할 경우, 함수 외부에서 생성하는 random에도 영향을 미치게 됩니다. 
- 아래의 코드를 보시면 다음 두 경우에 완전히 똑같은 결과를 보이는 것을 알 수 있습니다. 
    1) 함수 밖에서 Seed를 세팅하고 난수 4개 뽑음: 
    2) 함수 안에서 Seed를 세팅하고 난수 2개 그리고 밖에서 seed를 변경하지 않고 2개 뽑아서 합침.

```python 
import numpy as np
"""
np.random.seed(SEED) 로 random을 생성하게 될 경우, 
"""
def random_int_gen_with_global_seed(size=10, seed=0):
    np.random.seed(seed)
    return np.random.random(size=size)

np.random.seed(3)
# seed를 3으로 세팅하고, random number를 2개 뽑습니다.
A = list(np.random.random(size=4))

# random_int_gen_with_global_seed 내에서
# 같은 seed를 세팅하고, random number를 2개 뽑고.
# 함수 밖에서, seed를 세팅하지 않고, 2개를 더 뽑아서 합칩니다.
# 즉, 함수 안에서 반을, 함수 밖에서 반을 뽑는 것이죠.
B = list(random_int_gen_with_global_seed(2, seed=3))
B+= list(np.random.random(size=2))

# 그리고, A, B를 비교해보면 완전히 같은 것을 알 수 있습니다. 
# 즉, 함수 내에서 np.random.seed() 를 실행하여 seed를 새롭게 설정하면, 
# 함수 밖에서도 seed가 다시 세팅된다는 것이죠.
print("=="*30)
print(f"A: {A}")
print(f"B: {B}")
assert A==B
print("==" * 30)
```

- 아래에서 보시는 것처럼, `np.random.seed()`를 통해 seed를 변경할 경우, 전역변수처럼 모든 코드의 영역에 영향을 끼치게 됩니다. 그리고, 이는 같은 프로젝트에서 다른 코드파일에서 해당 numpy를 사용한다고 해도 딱히 달라지지 않아요.

```
============================================================
A: [0.5507979025745755, 0.7081478226181048, 0.2909047389129443, 0.510827605197663]
B: [0.5507979025745755, 0.7081478226181048, 0.2909047389129443, 0.510827605197663]
============================================================
```

- 사실, 어떻게 생각하면 "별 문제 아니야"라고 생각할 수도 있는데, 약간의 불안함이 남아있게 되죠. 

### Better with `np.random.RandomState`

- 따라서, 저는 `np.random.RandomState()`를 사용해서, seed를 localization하여 사용하는 것이 훨씬 효과적인 것 같아요. 개별적으로 seed를 localization하여 사용하므로, 외부의 seed에 영향을 미치지 않습니다. 
- 이렇게 설정할 경우, seed를 개별적으로 두고, 필요에 따라서 분리하여 사용할 수 있다는 것을 의미하죠.
- 아래의 코드에서는 다음 두 가지 경우를 비교하였으며, 결과가 같은 것을 알 수 있습니다. 
    1) 함수 밖에서 gloabl Seed를 세팅하고 난수 4개 뽑고, 함수 실행 후에 난수 2개를 뽑아서 합침: 
    2) 함수 안에서 local Seed를 세팅하고 난수 6개를 뽑음.

```python
import numpy as np
"""
np.random.seed(SEED) 로 random을 생성하게 될 경우, 
"""
def random_int_gen_with_local_seed(size=10, seed=0):
    # 내부에 같은 seed를 지정해준 random generator object를 만들고
    # 이 객체의 method를 통해 난수를 생성한다.
    # 이렇게 할 경우, 전체 seed에 영향을 미치지 않으므로 효과적으로 random number를 뽑을 수있다.
    Rand = np.random.RandomState(seed=seed)
    return Rand.random(size=size)

# global seed를 3으로 설정하고
# 4개의 수를 뽑습니다.
np.random.seed(3)
global_seed3_num1234 = np.random.random(size=4)

# 함수내에서 사용하는 local seed도 seed를 동일하게 설정하고, 6개의 수를 뽑습니다.
local_seed3_num123456 = random_int_gen_with_local_seed(6, seed=3)

# global seed에서 수를 2개 더 뽑습니다.
global_seed3_num56 = np.random.random(size=2)

global_seed3_num123456 = list(global_seed3_num1234) + list(global_seed3_num56)
global_seed3_num123456 = np.array(global_seed3_num123456)

# 결과를 보면, global seed에서 4개, 2개를 뽑아서 합친 값과 
# local seed에서 6개를 뽑아낸 값이 같은 것을 알 수 있습니다. 
# 즉, local에서의 seed 변화가, 외부에 영향을 끼치지 않은 것이죠.
print("=="*30)
print(f"global seed num: {global_seed3_num123456}")
print(f"local  seed num: {local_seed3_num123456}")
print("=="*30)
```

- global seed에서 4개, 2개를 뽑아서 합친 값과 local seed에서 6개를 뽑아낸 값이 같은 것을 알 수 있습니다. 즉, local에서의 seed 변화가, 외부에 영향을 끼치지 않은 것이죠.

```
============================================================
global seed num: [0.5507979  0.70814782 0.29090474 0.51082761 0.89294695 0.89629309]
local  seed num: [0.5507979  0.70814782 0.29090474 0.51082761 0.89294695 0.89629309]
============================================================
```

## wrap-up

- 이전에 제가 박사졸업을 위해서 시뮬레이션 분석을 수행했는데, 그 당시에, random 생성을 위한 seed를 global하게 세팅하여 꽤 어려움을 겪었습니다. 이걸 알았다면, 사실 좀 더 쉽게 함수들을 디자인해서, random을 효율적으로 컨트롤했을텐데, 라는 아쉬움이 있네요. 
- 또한, 이 난수 생성에 대해서 더 자세하게 알기 위해서는 `seed`가 뭐고 어떻게 영향을 미치는뎨? 라는 것을 아시는 것이 좋습니다만, 정신건강을 위해, 일단은 그걸 모르시는게 더 편할 수 있습니다. 호호. 이거는 제가 다음에 시간이 조금 있을 때 추가작성하도록 할게요.

## reference

- [numpy.random.RandomState](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.RandomState.html)
