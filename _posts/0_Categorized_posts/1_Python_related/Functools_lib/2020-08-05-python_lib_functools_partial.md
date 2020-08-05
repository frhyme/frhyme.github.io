---
title: python-lib) functools - partial
category: python-lib
tags: python python-lib functools functional-programming iterator
---

## functools.partial

- `functools.partial`은 다양한 argument를 가지는 함수에 대해서, 특정한 argument를 제한하여, 좁은 기능의 function을 리턴해주는 함수를 말합니다.
- 가령, `func(a, b, c)`라는 함수가 있을 때, a의 값을 특정 값으로 고정하고, b, c만 input으로 받아들이는 함수를 만든다는 것이죠.
- 매우 간단한 예를 들어보겠습니다. 우리에게는 다음과 같이 `base^exponent`를 리턴해주는 함수가 있습니다.

```python
def power(base, exponent):
    return base**exponent
```

- `power` 함수의 기능을 줄여서, `base`를 3으로 한정하여, 3의 제곱수만을 리턴하는 함수를 생성하고 싶다고 하겠습니다.
- 이 때, `functools.partial`를 사용해서 다음과 같이 새로운 함수를 만들어 줄 수 있습니다.

```python
from functools import partial

def power(base, exponent):
    return base**exponent

# 3의 제곱수를 리턴하는 함수
power_three = partial(power, base=3)
# 4의 제곱수를 리턴하는 함수
power_four = partial(power, base=4)

print(power_three(exponent=2)) # 9 
print(power_three(exponent=3)) # 27
```

### by closure

- 사실, 위에서는 `functools.partial`를 사용하기는 했지만, 그냥 직접 제한된 함수를 만들어서 사용할 수도 있죠.
- `closure`는 "함수 안에서 새로운 함수를 정의하고, 이 함수를 리턴해서 main함수에서 사용할 수 있도록 하는것"을 말합니다. 어려워보이지만 아래 코드를 보면 쉽게 이해될 거에요.

```python
def power_func(exponent):
    def r_func(base):
        return base**exponent
    return r_func
square = power_func(2)
cube = power_func(3)
print(square(7))
```
