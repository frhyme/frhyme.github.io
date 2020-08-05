
### functools.partial

- 복잡한 함수를 간단한 함수로 변환해주는 function
    - ex: `functools.partial(function, target_argument=2)`

```python
from functools import partial

def power(base, exponent):
    return base**exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)
print(power(7, 2), square(7))
```

```
    49 49
```

- 다른 방법으로 `closure`를 이용해서 정의할 수 도 있다. 
    - `closure`: 함수 안에 nested-함수를 정의하고, 이 nested-함수를 함수 내에서 리턴하면, 해당 nested-함수는 함수 외부에서도 잘 작동하게 된다. 이러한 것을 `closure`라고 한다. 


```python
def power_func(exponent):
    def r_func(base):
        return base**exponent
    return r_func
square = power_func(2)
cube = power_func(3)
print( square(7))
```

```
    49
```

### comparator completion 

- class를 정의할 때, __eq__, __gt__, __lt__, __le__ 등을 모두 정의하는 것은 굉장히 귀찮은 일임
- 해당 class 앞에 class decorator를 추가하여, 아래처럼 다양한 operator를 쉽게 지원
    - `@functools.total_ordering`
- 아래는 `__ge__`가 정의되어 있지 않기 때문에 에러가 발생함. 


```python
class student():
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
    def __gt__(self, other):
        return self.name > other.name
a = student("111")
b = student("222")
print(a >= b) # not work 
```

```
    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-76-39e47a5a4f23> in <module>()
          8 a = student("111")
          9 b = student("222")
    ---> 10 print(a >= b) # not work
    

    TypeError: unorderable types: student() >= student()
```

- 물론 아래처럼 `__ge__`를 정의하는 것도 방법


```python
class student():
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
    def __gt__(self, other):
        return self.name > other.name
    def __ge__(self, other):
        return self.name >= other.name
a = student("111")
b = student("222")
print(a >= b) # not work 
```

```
    False
```

- 여기서는 `@total_ordering`를 첨부하여 손쉽게 해결함


```python
from functools import total_ordering
@total_ordering# it makes not implemented comp method possible
class student():
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
    def __gt__(self, other):
        return self.name > other.name
a = student("111")
b = student("222")
print( a >= b )
```

```
    False
```
