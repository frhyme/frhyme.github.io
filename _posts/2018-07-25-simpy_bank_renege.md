---
title: 예제를 통해 simpy 더 잘 이해하기(conditional event)
category: python-lib
tags: python python-lib simpy numpy simulation condition
---

## example을 풀어봅시다.

- 정확히는 푸는 것은 아니고, [simpy - example](http://simpy.readthedocs.io/en/latest/examples/index.html)를 보면 다양한 예제가 있습니다. documentation을 읽어보는 것도 좋지만, 제 기준으로는 예제를 몇 번 풀어보면 더 잘 이해할 수 있을 것 같아요. 또 시뮬레이션 스킬도 조금 늘 거라는 생각도 조금 해봅니다. 

- 여기서는 `simpy.Resource`를 사용하고, 어떤 event가 발생했느냐에 따라서 다른 동작을 하도록 만드는 것을 배웁니다. 

## bank example - basic 

- 다음의 조건 하에서 시뮬레이션합니다. 
    - 고객이 exponential distribution에 한 번씩 은행에 도착합니다. 
    - 고객이 resource를 이용하는 시간도 exp dist를 따릅니다.

```python
import simpy 
import numpy as np 

def customer(env, name, counter, mean_service_time):
    ## counter: 사용하는 리소스 
    ## mean_service_time: 서비스 시간 평균 
    arrive_time = env.now
    print('%7.4f %s: Here I am' % (arrive_time, name))
    
    with counter.request() as req:
        yield req 
        wait_time = env.now - arrive_time
        print('%7.4f %s: Waited %6.3f' % (env.now, name, wait_time))
        service_time = np.random.exponential(mean_service_time)
        yield env.timeout(service_time)
        print('%7.4f %s: Finished' % (env.now, name))

def source(env, customer_n, interval, counter):
    ## exponential time 마다 customer를 추가해줍니다
    for i in range(customer_n):
        c = customer(env, 'Customer%02d' % i, counter, mean_service_time=5.0)
        env.process(c)
        t = np.random.exponential(interval)
        yield env.timeout(t)
        
np.random.seed(42)
env = simpy.Environment()

## 우선 counter generator를 만들어주고 
counter = simpy.Resource(env, capacity=1)
## 5명의 고객이, 평균적으로 3초에 한번씩 생기고, counter resource를 이용합니다. 
bank = source(env, 5, 3.0, counter)

env.process(bank)
env.run(until=90)
```

```
 0.0000 Customer00: Here I am
 0.0000 Customer00: Waited  0.000
 1.4078 Customer01: Here I am
 5.3580 Customer02: Here I am
 8.0969 Customer03: Here I am
 8.6057 Customer04: Here I am
15.0506 Customer00: Finished
15.0506 Customer01: Waited 13.643
15.3498 Customer01: Finished
15.3498 Customer02: Waited  9.992
25.4060 Customer02: Finished
25.4060 Customer03: Waited 17.309
30.0014 Customer03: Finished
30.0014 Customer04: Waited 21.396
36.1576 Customer04: Finished
```

## bank example - complex 

- 이제 새로운 조건을 추가해보겠습니다. 
    - 고객은 너무 많이 기다릴 경우 서비스를 받지 않고 은행을 떠난다. 
    - 고객의 인내심은 uniform한 분포에 따라 결정된다. 

- 따라서 총 다음 조건을 만족합니다. 
    - 고객이 exponential distribution에 한 번씩 은행에 도착합니다. 
    - 고객이 resource를 이용하는 시간도 exp dist를 따릅니다.
    - 고객은 너무 많이 기다릴 경우 서비스를 받지 않고 은행을 떠난다. 
    - 고객의 인내심은 uniform한 분포에 따라 결정된다. 

- 다음 부분으로 표현해주면, `req` 와 `env.timeout(patience_time)` 둘 중에서 일찍 끝나는 값이 `result`에 들어가게 됩니다. 
    - `env.timeout()`이 `yield` 다음에 들어가지 않으면 수행되지 않습니다. 다음처럼 사용해도 문제가 없죠. 

```python
## | 로 묶어주면 or  종료조건
## & 로 묶어주면 and 종료조건으로 인식함 
with counter.request() as req:
    patience_over = env.timeout(patience_time) 
    result = yield req | patience_over
```

```python
import simpy 
import numpy as np 

def customer(env, name, counter, mean_service_time):
    ## counter: 사용하는 리소스 
    ## mean_service_time: 서비스 시간 평균 
    arrive_time = env.now
    patience_time = np.random.uniform(2, 5)
    print('%7.4f %s: Here I am' % (arrive_time, name))
    
    with counter.request() as req:
        ## | 로 묶어주면 or  종료조건
        ## & 로 묶어주면 and 종료조건으로 인식함 
        patience_over = env.timeout(patience_time) 
        result = yield req | patience_over
        ## wait time 게산 
        wait_time = env.now - arrive_time
        ## is 가 아니라 in인 것에 유의
        if patience_over in result:
            print('%7.4f %s: RENEGED after %6.3f' % (env.now, name, wait_time))
        elif req in result:
            print('%7.4f %s: Waited %6.3f' % (env.now, name, wait_time))
            service_time = np.random.exponential(mean_service_time)
            yield env.timeout(service_time)
            print('%7.4f %s: Finished' % (env.now, name))

def source(env, customer_n, interval, counter):
    ## exponential time 마다 customer를 추가해줍니다
    for i in range(customer_n):
        c = customer(env, 'Customer%02d' % i, counter, mean_service_time=8.0)
        env.process(c)
        t = np.random.exponential(interval)
        yield env.timeout(t)
        
np.random.seed(42)
env = simpy.Environment()

## 우선 counter generator를 만들어주고 
counter = simpy.Resource(env, capacity=1)
bank = source(env, 5, 3.0, counter)

env.process(bank)
env.run(until=90)
```

- 다음처럼 시뮬레이션 됩니다. 

```
 0.0000 Customer00: Here I am
 0.0000 Customer00: Waited  0.000
 1.4078 Customer01: Here I am
 3.8759 Customer01: RENEGED after  2.468
 4.1466 Customer02: Here I am
 4.6554 Customer03: Here I am
 6.3209 Customer02: RENEGED after  2.174
 8.4588 Customer03: RENEGED after  3.803
10.5340 Customer00: Finished
10.6891 Customer04: Here I am
10.6891 Customer04: Waited  0.000
38.7176 Customer04: Finished
```