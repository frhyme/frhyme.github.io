---
title: `np.random.seed()`는 정확히 무엇을 의미하는가? 
category: python-libs
tags: python python-libs numpy random seed
---

## 2-line summary. 

- `np.random.seed(seed=3)`를 사용해서 난수(random number)가 발생하는 동작을 제어하지만, 난수를 생성하게 되는 624개의 모수 세트의 첫번째 값을 변경해줄 뿐임. 
- 좀더 세밀하게 random성을 제어하고 싶을 경우, `np.random.get_state()`로 특정한 상황의 random성을 저장하고, `np.random.set_state()`로 특정한 상황의 state를 지정해준다.

## What is `np.random.seed()`?

- 코딩을 하다 보면 적절하게 random성을 제어해야 할 때가 있습니다. 
- 가령, 어떤 알고리즘을 개발했다고 할 때, 다음 두 가지가 혼동될 때가 있거든요. 
    1) "내 알고리즘이 좋아서 지표가 개선된 것인지?" 
    2) "random성이 뛰어나서 지표가 개선된 것처럼 보이는 것인지?"
- 물론, random성을 제어할 수 없을 때는 그냥 여러 샘플을 뽑은 다음에, 검정해도 되는 것이기는 한데, 굳이 그럴 필요는 없죠. 
- 아무튼, 보통 우리는 다음처럼 `np.random.seed()`를 고정한 상태로 알고리즘을 실행하여, 난수의 생성 패턴을 동일하게 관리할 수 있습니다. 
- 다음 코드를 실행해보면, seed가 같을 때는 같은 값이, 다를 때는 다른 값들이 순서대로 생겨나는 것을 알 수 있죠.

```python
# seed를 같게 세팅하면 같은 난수가 순서대로 생겨남.
np.random.seed(0)
print(np.random.random(3))
np.random.seed(2)
print(np.random.random(3))
np.random.seed(0)
print(np.random.random(3))
```

```
[0.5488135  0.71518937 0.60276338]
[0.4359949  0.02592623 0.54966248]
[0.5488135  0.71518937 0.60276338]
```

## `np.random.seed()`는 실제로 무엇을 하나? 

- 사실 `np.random.seed(seed=SEED)`를 통해 넘기는 `SEED`라는 값은 그냥 난수를 뽑아내는 알고리즘인 [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister)에서 참고하는 '하나의 값'에 불과합니다.

### Mersenne Twister Algorithm 

- 이를 이해하려면, 간단하게 나마, [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister) 알고리즘을 이해하는 것이 필요한데요, 간단하게 요약하면 다음과 같습니다. 
    1) `SEED`를 첫번재 항으로 하여(`MT[0]`) 점화식을 통해 624개의 길이를 가진 배열(`MT`)을 생성합니다. 이 MT가 일종의 모수 세트 라고 생각하면 됩니다.
    2) "random number를 만들어달라"라는 요청이 들어오면, 이미 생성된 624개의 배열의 첫번째 항(`MT[0]`)으로부터 값을 마구 변형하여(Black BOX) 난수를 리턴한다(실제로는 Black Box 가 아니지만, 그냥 "복잡한 공정"이라고만 이해하셔도 됩니다)
    3) MT의 마지막 모수인 `MT[623]`까지 모두 사용하였으면, `twist`로 새로운 `MT`를 만든다. 즉, 모수 세트가 다시 만들어졌으므로, `MT[0]`로부터 Black BOX를 사용하여 새로운 난수를 생성한다.
- 즉, 다시 정리하자면, `SEED`는 메르센-트위스터 알고리즘에서 난수를 생성하기 위해 필요한 624개의 모수 세트를 만들기 위한 "초기 설정값"일 뿐인 것이죠.

### np.random.get_state()

- 정말 그런지, 아래의 코드를 통해 확인해봅니다. 
- `np.random.get_state()`는 현재 random의 상황을 더 정확하게 파악해보는 함수를 말합니다. 즉 위에서 언급한 메르센-트위스터 알고리즘의 '모수'가 무엇인지 확인해볼 수 있죠. 
    - 이 함수를 실행하면 5개의 값이 리턴되지만, 저는 그냥 2번째 값만 확인하겠습니다. 
- 결과를 보시면, 624개의 모수 세트에서 첫번째 값이 바뀌는 것을 알 수 있습니다. 624개의 모수는 첫번재 값으로부터 이후의 값을 일종의 점화식을 통해서 만듭니다. 따라서, 첫번째 값이 바뀌면 다 바뀌게 되는 것이죠.

```python
import numpy as np

def print_current_random_state():
    current_random_state = np.random.get_state()
    a, b, c, d, e = current_random_state
    # 1st element: 'MT19937'
    # `MT19937`은 numpy에서 사용하는 난수생성알고리즘의 이름을 말합니다.
    print(f"1st element: {a}")
    print("2nd element: 624개의 모수, 즉 MT")
    print(f"2nd element[:10]: {b[:5]}")
    print("--"*30)

print("--" * 30)
print("== seed doesn't changed")
print_current_random_state()
np.random.seed(1)
print("== seed changed to 1")
print_current_random_state()
np.random.seed(2)
print("== seed changed to 2")
print_current_random_state()

```

```
------------------------------------------------------------
== seed doesn't changed
1st element: MT19937
2nd element: 624개의 모수, 즉 MT
2nd element[:10]: [2147483648 3663476462 2253056295  218075282 2236494591]
------------------------------------------------------------
== seed changed to 1
1st element: MT19937
2nd element: 624개의 모수, 즉 MT
2nd element[:10]: [         1 1812433254 3713160357 3109174145   64984499]
------------------------------------------------------------
== seed changed to 2
1st element: MT19937
2nd element: 624개의 모수, 즉 MT
2nd element[:10]: [         2 3624866507  846688490 2733819477 1447939927]
------------------------------------------------------------
```

### np.random.set_state()

- 이를 확장하여, 단지, `np.random.seed()`뿐만 아니라, 더 세부적으로 random성을 조절할 수 있습니다. 즉, 만약 624개의 모수로부터 난수가 결정된다면, 난수 624개를 넘겨버린다면 좀 더 세부적인 제어가 가능하게 되는 것이죠.
- 즉, 일반적으로는 `np.random.seed(seed=3)`으로 랜덤성을 조절하지만, 가령, 
> "<1000개의 random number>를 뽑은 다음의 상태를 저장하고, 이 때 생성되는 난수 패턴을 계속 이용하고 싶다"
- 와 같은 변태적인 마음이 있다면, 이 부분을 `np.random.set_state()`를 통해 해결할 수 있습니다. 

```python
import numpy as np
"""
- <1000개의 random number>를 뽑고 
- 그 다음의 state를 저장하고 
- 그 state를 세팅하여 다시 값을 뽑음.
"""


print("--" * 30)
print("== Extact 1000 random number(integer)")
# 1000개의 값을 뽑고,
temp = np.random.random(size=1000)

# 이 때의 state를 저장해두고, 5개의 값을 뽑아서 출력하고
State1 = np.random.get_state()
print("== Save current state to `State1`")
print(np.random.random(size=5))

# 이전의 state로 돌아가고, 다시 5개의 값을 출력한다.
np.random.set_state(State1)
print("== Revert state to `State1`")
print(np.random.random(size=5))
print("--" * 30)
```

```
------------------------------------------------------------
== Extact 1000 random number(integer)
== Save current state to `State1`
[0.41059295 0.92839617 0.21698743 0.08751889 0.33477266]
== Revert state to `State1`
[0.41059295 0.92839617 0.21698743 0.08751889 0.33477266]
------------------------------------------------------------
```


## wrap-up

- 사실, 정리하는 김에 정리하기는 했지만, `np.random.seed()`가 더 편하죠. 아니면 그냥 `np.random.RandomState()`를 쓰는게 더 편해요.