---
title: python - class - Math method
category: python-basic
tags: python python-basic OOP math method
---

## python - class - Math method

- python에서 class의 기본 연산자를 지원하는 method를 정의합니다.

```python
class Number(object):
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return f"Number: {self.x}"
    def get(self):
        return self.x
    def set(self, x):
        self.x = x
    # Math Method
    ## Arithmetic Operation
    def __add__(self, x):
        # + 연산자를 정의
        return Number(self.x + x)
    def __sub__(self, x):
        # - 연산자를 정의
        return Number(self.x - x)
    def __mul__(self, x):
        # * 연산자를 정의
        return Number(self.x * x)
    def __truediv__(self, x):
        # / 연산자를 정의
        new_x = self.x / x
        return Number(new_x)
    def __pow__(self, x):
        # ** 연산자를 정의
        return Number(self.x ** x)

    ## Augmented Assignment
    def __iadd__(self, x):
        # += 연산자를 정의
        self.x += x
        return self
    def __isub__(self, x):
        # -= 연산자를 저으이
        self.x -= x
        return self
    def __imul__(self, x):
        # *= 여난자를 정의
        self.x *= x
        return self
    def __itruediv__(self, x):
        # /= 연산자를 정의
        self.x /= x
        return self
    def __ipow__(self, x):
        # **= 연산자를 정의
        self.x **= x
        return self

    ## Comparison Operator
    def __eq__(self, Number_instance):
        # == 연산자를 정의
        if self.get() == Number_instance.get():
            return True
        else:
            return False
    def __ne__(self, Number_instance):
        # != 연산자를 정의
        return not self.__eq__(Number_instance)
    def __lt__(self, Number_instance):
        # < 연산자를 정의
        if self.get() < Number_instance.get():
            return True
        else:
            return False
    def __ge__(self, Number_instance):
        # >= 연산자를 정의
        return not self.__lt__(Number_instance)
    def __gt__(self, Number_instance):
        # > 연산자를 정의
        return (not self.__lt__(Number_instance)) and (not self.__eq__(Number_instance))
    def __le__(self, Number_instance):
        # <= 연산자를 정의
        return not self.__gt__(Number_instance)
```

- 테스트해보면 잘 되는 것을 알 수 있습니다.

```python
x = Number(10)

# Check Arithmetic Operator
assert (Number(1) + 1) == Number(2)
assert (Number(1) - 1) == Number(0)
assert (Number(2) * 5) == Number(10)
assert (Number(2) / 5) == Number(0.4)
assert (Number(2) ** 3) == Number(8)

# Check Augmented Assignment Operator
x = Number(2)
x += 1
assert x == Number(3)
x -= 1
assert x == Number(2)
x *= 2
assert x == Number(4)
x **= 2
assert x == Number(16)
x /= 2
assert x == Number(8.0)
assert x == Number(8)

# Check Comparison Operator
assert Number(1) == Number(1)
assert Number(1) != Number(2)
assert Number(2) >= Number(1)
assert Number(2) >= Number(2)
assert Number(2) <= Number(2)
assert Number(1) < Number(2)
assert Number(2) > Number(1)
```
