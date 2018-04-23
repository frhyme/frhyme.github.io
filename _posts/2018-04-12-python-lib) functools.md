---
title: python-lib) `functools` 
category: python-lib
tags: python python-lib functools functional-programming iterator

---

## intro 

- python 에서 유용하게 쓰이는 functools의 주요 함수를 정리함. 
- 몇 가지 정리가 더 필요한 메소드 들이 있지만, 지금은 중요하다고 생각되지 않아서 제외하였음. 
- 추후에 functional programming의 관점에서 또 하나 올릴 예정입니다. 


```python
import numpy as np # random한 값을 가진 리스트를 만들기 위해서 numpy를 import 
```

- 보통 하나의 데이터(int, float, string 등)만으로 존재하는 경우에는 sort할 때 문제가 없지만, 리스트 안에 tuple, list가 존재하고 이를 비교해야 할 때는 customized comparator를 정의해줘야 하는 경우가 발생함. 
- unary comparator의 경우는 `key`를 사용해서 정의하면 되는데, binary comparator의 경우는 python3에서는 정의할 수 없음. 
    - python2의 경우는 sort할 때 cmp로 값을 넘기면 되는데, python3에서는 이 부분이 functools로 넘어감. 
        - python2: `sorted(target_lst, cmp=lambda x, y: x[1]>y[1] )`
        - python3: `sorted(target_lst, key= functools.cmp_to_key(lambda x, y: x[1]>y[1]))`
    - 자세한 내용은 아래 코드에서 설명함

### unary comparator를 정의하는 경우 

- 비교되어야 하는 데이터가 tuple, list 등이고, 특정 데이터만을 가지고 비교하는 경우

```python
test_lst = [(np.random.randint(1, 10), chr(np.random.randint(ord("a"), ord("z")))) for i in range(0, 5)]
print(test_lst)
print(sorted(test_lst, key=lambda x: x[0]))
print(sorted(test_lst, key=lambda x: x[1]))
```

```
    [(5, 'd'), (5, 'n'), (7, 'h'), (1, 'd'), (8, 's')]
    [(1, 'd'), (5, 'd'), (5, 'n'), (7, 'h'), (8, 's')]
    [(5, 'd'), (1, 'd'), (7, 'h'), (5, 'n'), (8, 's')]
```

### binary comparator를 정의하는 경우 

- 비교되어야 하는 데이터가 tuple, list 등인데, 둘 간의 관계를 고려하여 좀 더 복잡한 comparator를 설계하는 것이 필요한 경우
    - sort 함수에 key로 넘기는 것은 똑같지만, 해당 함수를 `functools.cmp_to_key`로 변환하여 넘겨야 함. 


```python
from functools import cmp_to_key
test_lst = [(np.random.randint(1, 4), chr(np.random.randint(ord("a"), ord("f")))) for i in range(0, 5)]
print(test_lst)

# first one decreasing, second one increasing
def cmp_func(a, b):
    if a[0]>b[0]:
        return -1
    elif a[0]==b[0]:
        if a[1]>b[1]:
            return 1
        elif a[1]==b[1]:
            return 0
        else:
            return -1
    else:
        return 1
sorted(test_lst, key=cmp_to_key(cmp_func))# first one decreasing, second one increasing
```

```
    [(3, 'd'), (3, 'b'), (3, 'c'), (1, 'c'), (2, 'c')]





    [(3, 'b'), (3, 'c'), (3, 'd'), (2, 'c'), (1, 'c')]
```


### functools.reduce

- 이것도 원래 python2에는 built-in으로 있었지만 지금은 없는 함수 
- list의 앞 원소부터 시작하여, 연쇄적으로 함수를 수행하는 것.
- 아래 예는 리스트 안에 리스트들이 있을 때, 각 원소 리스트를 모두 통합해주는 경우
  - [이 방법은 `functols.reduce`보다는 `itertools.chain.from_iterable`를 쓰는 경우 훨씬 빠릅니다.](https://stackoverflow.com/questions/49148342/why-functools-reduce-and-itertools-chain-from-itertools-had-different-comput)

```python
from functools import reduce
test_lst_lst = [ [np.random.randint(1, 10) for i in range(0, 3)]for i in range(0, 5)]
print(test_lst_lst)
print( reduce(lambda x, y: x+y, test_lst_lst) ) 
print( reduce(list.__add__, test_lst_lst) )# same but more robust code
```

```
    [[4, 7, 5], [1, 4, 5], [7, 1, 1], [9, 2, 3], [7, 3, 1]]
    [4, 7, 5, 1, 4, 5, 7, 1, 1, 9, 2, 3, 7, 3, 1]
    [4, 7, 5, 1, 4, 5, 7, 1, 1, 9, 2, 3, 7, 3, 1]
```

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
