---
title: python-basic) Decorator in python
category: python-basic
tags: python python-basic decorator functools

--- 

## Intro - decorator는 무엇인가?

- OOP(Object-Oriented Programming)을 들어본 사람이라면, '상속'이라는 개념을 이미 알고 있을 겁니다. 엄밀히 따지면, 다르지만, 제가 볼 때는 비슷한데, 상황에 따라서, function의 기능을 확장해야 할 때가 있습니다. 보통 이럴 때 decorator를 사용합니다.

## AOP in java and Decorator in python

- 최근에 java의 스프링 프레잌워크를 공부하고 있습니다. java에는 AOP(Aspect Orieted Programming)이라는 것이 나오는데, 이는 "거대 프로그램을 만들어야 할때, 공통기능, 특수기능을 구분하고, 특수기능에서 특정 시점에 공통 기능이 필요할 경우 정의해놓은 공통 기능을 가져와서 사용하는 것을 말합니다.
- 이렇게 말하면 어려우므로, 예를 들어 설명하면, "물을 받는 것"은 공통 기능, "특정 요리를 만드는 것"은 특수 기능이 됩니다. 특수기능을 수행할 때, "물을 받는 것"은 매우 반복적으로 일어납니다. 즉, 이렇게 공통기능을 정의하고 이를 통해 특수기능을 새롭게 정의하는, 약간 모듈 기반 설계에 가까운 것이, 바로 AOP의 개념이죠.
- 실제로 AOP 에서 예시로 드는 것 중 하나가, 특수기능의 앞뒤로 해당 함수의 시작 시간 및 종료 시간을 출력해주는 공통 기능을 설계하는 것입니다. 이는 오늘 설명하 python에서의 decorator와 매우 유사하죠. 따라서, AOP를 공부하는 중에 python의 decorator도 함께 공부해봤습니다.

## Simple Decorator - 함수 실행 앞뒤로 시간 기록

- 아래의 python code는 함수를 input으로 받아서, 함수의 기능을 확장하여 확장된 함수를 리턴해주는 코드입니다.
- `time_logger`함수는 외부에서 전달 받은 함수를 input으로 받아서, 새로운 함수를 정의하고, 이 함수를 리턴해줍니다. 
- 문득 보기에는 이상해보일 수 잇지만, 됩니다. 잘 됩니다.

```python
def time_logger(raw_func):
    """
    - 이 함수는 decorator로서, raw_func를 확장하여 정의한다
    - 확장하여 정의된 함수인 decorated_func를 리턴한다.
    - raw_func 함수의 실행전, 후에 현재 시각을 출력해준다.
    """
    import time

    def decorated_func(*args, **kwargs): 
        """
        - *args, **kwargs 는 각각 함수에 넘어오는 모든 arguments를 의미합니다.
        - 이 argument들이 아래 에서 그대로 raw_func로 들어가게 됩니다. 
        - 즉 약간 wild-card의 느낌으로 쓰였다고 보셔도 되죠.
        """
        print("--" * 20)
        print(f"Raw func start at {time.time()}")
        return_value = raw_func(*args, **kwargs)
        print(f"Raw func ends at {time.time()}")
        print("--" * 20)
        return return_value
    return decorated_func
```

## Decorator를 어떻게 쓸 수 있는가?

- 좋습니다. 앞서 말한 것처럼 decorator는 원래 주어진 하나의 함수에 대해서 이 함수의 기능 자체를 확장해주는 것이죠.
- 우리가 만든 `time_logger`라는 함수는 input으로 함수를 받아서, 앞 뒤로 현재 시간을 출력해주는 기능을 수행하도록 함수를 확장하여 확장된 함수를 리턴하는 기능을 수행합니다.
- 이 기능을 만든 이유는, 매번 모든 함수마다 앞에 `time.time()`을 붙여서 출력해주는 것이 매우 귀찮기 때문이죠.
- 아래처럼 간단하게 쓸 수 있고, 확장될 함수의 앞에 `@time_logger`를 붙여주면 됩니다.

```python
import numpy as np
@time_logger
def test1(n):
    print("number: {:,}".format(n))
    return sum([ i for i in range(0, n)])
@time_logger
def test2(n):
    print("number: {:,}".format(n))
    return sum(( i for i in range(0, n)))
test1(10000000)
test2(10000000)
```

- 결과는 다음과 같이, 앞뒤로 함수의 기능이 확장되어 출력됩니다.

```plaintext
----------------------------------------
Raw func start at 1596542093.4091032
number: 10,000,000
Raw func ends at 1596542093.9842172
----------------------------------------
----------------------------------------
Raw func start at 1596542093.984328
number: 10,000,000
Raw func ends at 1596542094.386215
----------------------------------------
```

### args, kwargs

- 앞서 주석에도 설명했지만, 이 둘은 그냥 매우 generic하게 쓰이는 argument라고 보시면 됩니다.
- 아래 코드를 보시면 더 명확해지실텐데, 제가 아래 코드에서 새롭게 정의한 `func`라는 함수는 그냥 args와 kwargs를 출력해주는 기능만을 수행합니다.

```python
def func(*args, **kwargs):
    print("== func START")
    print(f"  args: {args}")
    print(f"kwargs: {kwargs}")
    print("== func OVER")
    print("--" * 20)


func(1, 2, 3, 4, 5) 
func(1, 2, 3, 4, 5, a=10, b=1, c=3)
```

- 다만 위 코드의 수행 결과를 보시면, argument의 값만 넘길때는 `args`에 들어가고, argument의 label와 value를 함께 넘기는 경우에는 `kwargs`에 들어감을 알 수 있습니다. 각각 tuple과 dictionary로 넘어가죠.
- 다시 말하지만, 이는 일종의 와일드 카드고, "어떤 값들이 함수로 넘어올지는 모를 경우"에 대해서, 일종의 template처럼 정의해줄 수 있습니다.

```plaintext
== func START
  args: (1, 2, 3, 4, 5)
kwargs: {}
== func OVER
----------------------------------------
== func START
  args: (1, 2, 3, 4, 5)
kwargs: {'a': 10, 'b': 1, 'c': 3}
== func OVER
----------------------------------------
```

### functools - lru_cache

- 이처럼, decorator는 함수의 정의를 확장할 수 있는데, functools에서는 이미 매우 유용한 decorator를 지원합니다.
- `functools.lru_cache`는 memozing을 지원합니다. 이 아이는 간단하게, recursion시에 계산을 빠르게 하기 위해서 최근에 발생한 값을 recent cache에 박아두는 것을 말합니다. 물론, 최근에 call된 값들을 몇 개까지 읽어들일지 또한 매우 중요하긴 합니다만.
- 실제로, memoization이 없는 경우, 피보나치 수를 33까지 돌리는데 꽤 많은 시간이 소요되는 반면, memoization이 되는 경우 피보나치 수를 더 많이 돌려도 큰 문제가 없습니다.

```python
# memoization 없는 경우, 
import time

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

a = time.time()
print( fib(33) )
b = time.time()
print(b-a)
```

```plaintext
3524578
2.2419958114624023
```
   
- `functools.lru_cache`을 사용하는 경우 훨씬 짧은 시간이 소요된다.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
# least recently used caches
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

a = time.time()
print( fib(200) )
b = time.time()
print(b-a)
```

```plaintext
280571172992510140037611932413038677189525
0.0
```

## wrap-up

- 여러 모로 설명이 좀 부족했던 것 같기도 하지만, 대략 decorator에 대한 설명을 정리했습니다.
- 함수를 input으로 받아서 함수의 기능을 앞 뒤로 확장해서 리턴해주는 기능이 바로 decorator이고, 함수 정의 앞에 `@decorator_name`를 붙임으로써 수월하게 정의할 수 있습니다.
- 또한, 이미 다른 많은 라이브러리 들에서 괜찮은 decorator들을 정의하고 있으므로 참고해서 편하게 사용할 수도 있죠.
