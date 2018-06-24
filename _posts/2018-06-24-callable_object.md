---
title: callable object? callable 객체?
category: others
tags: python object-orietned-programming OOP
---

## callable object? callable 객체?

- keras로 코딩을 하다가, `model`와 `Sequential`의 차이가 궁금해서 찾아보고 있었습니다. 그런데 [제가 참고한 포스트](https://datascienceschool.net/view-notebook/1bde49133d7d40c0806e78b70513040b/)에서 다음을 언급하더군요. 

> Keras의 Model 클래스 객체와 레이어(Tensor) 객체는 callable 객체.

- 이게 무슨 말인가? 싶어서 간단히 찾아본 내용을 정리합니다. 

## definition in wikipedia

> A callable object, in computer programming, is any object that can be called like a function

- 컴퓨터 프로그래밍 에서, **callable object**란 함수처럼 호출될 수 있는 객체를 말한다고 합니다. 
- 파이썬에서는 간단히 다음처럼 표현할 수 있는 것 같아요. 

```python
"""
- class를 생성했으나, 내부에 __init__는 없고 __call__만 있음
- 객체로 표현했으나, 실제는 함수처럼 사용되는 경우, 이러한 경우를 callable object라고 하는 듯.
"""
class Foo(object):
    def __call__(self):
        print("Called.")
foo_instance = Foo()
print(type(foo_instance))
foo_instance()
```

```
<class '__main__.Foo'>
Called.
```

- 위의 예제는 무척 간단했습니다만, `__init__`을 넣어서 좀 더 다양한 함수를 만들 수 있게 사용할 수 있을 것 같아요. 
- 상황에 따라 다른 함수를 만들 수 있도록, 객체에서 일정 정보를 저장해 두고 알아서 새로운 함수를 생성해주는 형태로 사용할 수 있는 것 같습니다. 약간 **함수적 다형성을 확보하려는 시도**인 것 같기도 하구요. 

- 아래처럼 해주면, `from_1`과 `from_10`에는 각각 다른 함수가 들어가게 됩니다. 함수를 콜하면(정확히는 callable object) 다른 함수가 되죠. 

```python
class Accumulator(object):
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        self.n += x
        return self.n

from_1 = Accumulator(1)
from_10 = Accumulator(10)

print(from_1(10))
print(from_10(200))
```

```
11
210
```

## wrap-up

- 필요에 따라서 함수적 다양성을 확보해야 할때는, callable object로 표현하는게 괜찮을 것 같기도 합니다.


## reference 
- <https://stackoverflow.com/questions/111234/what-is-a-callable-in-python/111255#111255>