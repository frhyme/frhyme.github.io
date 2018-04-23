
## Decorator in python

### intro

- 과거에 object-oriented programming을 들어본 사람들의 경우는 '상속'의 개념을 이미 알고 있을 것이다. 
- 유사하다고 볼 수 있는데, function을 필요에 따라서 확장해야 할 때가 있다. 이 때, decorator를 사용한다. 

### AOP in java and Decorator in python 

- 최근 `java` 스프링 프레임웤을 공부하고 있는데, java에서 AOP(Aspect oriented Programming)이라는 것이 나온다. 
- 간단하게 설명하면, 거대 프로그램을 만들어야 할 때, 공통기능, 특수 기능을 구분하고, 특수기능에서 앞/뒤/혹은 수행 상 특정 시점에서 공통 기능이 필요할 경우, 정의해놓은 공통기능에서 불러와서 조립하는 식으로 운영하는 것을 말한다. 
- 예를 들어 말하자면, '물을 받는 것'은 공통 기능이고, '특정 요리를 만드는 것'은 특수기능일 때, 특수기능 수행시에는 물을 받는 것이 반복적으로 수행되지 않나? 이것을 지원하는 것이 AOP, 시점 지향적인 프로그래밍이라는 것이다. 
- 강의에서는 예시로 특수기능마다 앞뒤로 수행시간을 로깅해주는 함수를 만들었는데, 이게 파이썬에서의 decorator와 너무도 유사한 것이다. 그래서 aop공부하다가 decorator도 함께 공부해봄


### code

- 아래 코드는 함수를 입력받아서, 함수의 기능을 확장하여 새로운 함수를 다시 리턴해주는 함수다. 

```python
# simple time logger
def time_logger(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        print('time logging start: {}'.format(start))
        return_value = func(*args, **kwargs)
        end = time.time()
        print('time logging end: {}'.format(end))
        print('compuation time is {}'.format(end-start))
        return return_value
    return wrapper
```

- 그래 좋은데 저걸 언제 쓰냐? 
- 내가 함수를 만들고 나서, 얘가 정말, 빨리 돌아가는게 맞는지, 확인하고 싶을 때가 있다. 
- 그런데, 매번 모두 함수마다, 앞에 time.time()를 넣어주는게 엄청나게 귀찮고, 그렇다면, 함수의 앞 뒤로 필요한 기능을 추가하는게 좋다 


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

    time logging start: 1508915382.4293952
    number: 10,000,000
    time logging end: 1508915383.690395
    compuation time is 1.2609999179840088
    time logging start: 1508915383.690395
    number: 10,000,000
    time logging end: 1508915384.8143945
    compuation time is 1.1239993572235107
    




    49999995000000



- args, kwargs는 무엇인가? 
- 각각 값으로 넘겨 받은 인자들, key:value로 넘겨 받은 인자들을 말한다. 
- 예를 들면 아래와 같다.
    - 단 decorator가 아닐 때는 그다지 쓸 일이 없다. 일종의 generic


```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print("over")
func(1,2,3,4,5)
func(1,2,3,4,5, a=10, b=1, c=3)
```

    (1, 2, 3, 4, 5)
    {}
    over
    (1, 2, 3, 4, 5)
    {'c': 3, 'b': 1, 'a': 10}
    over
    

- 또, functools에서 꽤 유용한 decorator를 지원한다. 

- lru_cache의 경우는 memozing을 지원하는데 ~~~~ 최근 값을 recnet cache에 박아두고 활용하는 것을 의미하는 듯
"Decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls. It can save time when an expensive or I/O bound function is periodically called with the same arguments."
- memoization: 
    - In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again.

- memoization이 없는 경우 에는 피보나치 수를 33 돌리는데, 2초 넘게 수행되는 반면
    - 이 경우, 피보나치 수를 40이상 계산하면 시간이 기하급수적으로 증가한다.
- memoization이 있는 경우, 피보나치 수를 200까지 돌려도, 문제가 없다. 


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

    3524578
    2.2419958114624023
    


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

    280571172992510140037611932413038677189525
    0.0
    
