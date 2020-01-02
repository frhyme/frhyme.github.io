---
title: simpy - PriorityStore
category: python-lib
tags: python python-lib simpy numpy simulation generator 
---

## intro 

- simpy의 `PriorityStore`를 파보겠습니다. 
- 어떤 일을 수행할 때, 모든 일에는 우선순위가 있습니다. 마찬가지로 `Store`에서 값을 빼낼 때도, 우선순위에 맞춰서 빼낼 수 있으면 좋을 것 같습니다. 
- `PriorityStore`는 `Store`에서 `get` 할 때, 내부 item의 우선순위에 따라서 빼내는 `store`를 말합니다. 

```python
PStore = simpy.PriorityStore(env) ## capacity => inf
## 그냥 item이 아니라 PriorityItem을 넣어주어야 합니다. 
## 또한 priority, item을 각각 넣어줍니다. 
## get, put은 Store와 동일합니다. 
new_item = simpy.PriorityItem(priority=round(env.now, 2), item="PDT{:2d}".format(i))
PStore.put(new_item)
```

## do it

- 간단하게 코딩합니다. 

- 만들어지는 제품(`PriorityItem`)에 `env.now`를 `priority`로 줍니다. 이렇게 하면 가장 먼저 만들어진 물건이 제일 먼저 나가게 됩니다. 
- 그리고 exponential time에 따라서 n명의 사람이 도착합니다. 

```python
import simpy 
import numpy as np 

def Producer(_env, _PStore):
    ## 최대 100개의 제품을 0.2초마다 만들어내는 제너레이터 
    ## 가장 먼저 만들어진 제품에 우선순위를 높게 둬서 빠르게 내보내는 작업을 수행 
    for i in range(0, 1000):
        yield _env.timeout(0.2)
        new_item = simpy.PriorityItem(priority=round(_env.now, 2), item="PDT{:2d}".format(i))
        yield _PStore.put(new_item)

def consumer(_env, _name, _PStore):
    ## 도착 ==> 제품 획득 => 2초 기다림 ==> 출력 및 종료 
    print("{:6.2f}: {} arrived".format(_env.now, _name))
    #print("{:6.2f}: {} items remained".format(_env.now, _PStore.items))
    get_item = yield _PStore.get()
    yield _env.timeout(2)
    print("{:6.2f}: {} get {}".format(_env.now, _name, get_item))
    
def consumers(_env, _PStore):
    ## 일정 시간 간격으로 고객을 도착
    ## 도착 시간 간격은 exponential time, 사람 수는 poisson dist
    i = 0
    while True:
        ## 도착 시간은 exponential time
        yield env.timeout(np.random.exponential(3))
        ## 도착하는 사람 수는 poisson dist 
        customers_count = np.random.poisson(3)
        if customers_count != 0:
            print("{:6.2f}: {} customer arrived".format(_env.now, customers_count))
            for j in range(0, customers_count):
                ## 아래처럼 포맷팅을 할 경우 zero-padding이 됨 
                _env.process(consumer(_env, "consumer({:0>2d}_{:0>2d})".format(i, j), _PStore))
            i+=1

np.random.seed(42)
env = simpy.Environment()
PStore = simpy.PriorityStore(env) ## capacity => inf

env.process(Producer(env, PStore))
env.process(consumers(env, PStore))

env.run(until=20)
```

```
  1.41: 4 customer arrived
  1.41: consumer(00_00) arrived
  1.41: consumer(00_01) arrived
  1.41: consumer(00_02) arrived
  1.41: consumer(00_03) arrived
  1.59: 3 customer arrived
  1.59: consumer(01_00) arrived
  1.59: consumer(01_01) arrived
  1.59: consumer(01_02) arrived
  3.41: consumer(00_00) get PriorityItem(priority=0.2, item='PDT 0')
  3.41: consumer(00_01) get PriorityItem(priority=0.4, item='PDT 1')
  3.41: consumer(00_02) get PriorityItem(priority=0.6, item='PDT 2')
  3.41: consumer(00_03) get PriorityItem(priority=0.8, item='PDT 3')
  3.59: consumer(01_00) get PriorityItem(priority=1.0, item='PDT 4')
  3.59: consumer(01_01) get PriorityItem(priority=1.2, item='PDT 5')
  3.59: consumer(01_02) get PriorityItem(priority=1.4, item='PDT 6')
 12.10: 2 customer arrived
 12.10: consumer(02_00) arrived
 12.10: consumer(02_01) arrived
 12.71: 3 customer arrived
 12.71: consumer(03_00) arrived
 12.71: consumer(03_01) arrived
 12.71: consumer(03_02) arrived
 14.10: consumer(02_00) get PriorityItem(priority=1.6, item='PDT 7')
 14.10: consumer(02_01) get PriorityItem(priority=1.8, item='PDT 8')
 14.71: consumer(03_00) get PriorityItem(priority=2.0, item='PDT 9')
 14.71: consumer(03_01) get PriorityItem(priority=2.2, item='PDT10')
 14.71: consumer(03_02) get PriorityItem(priority=2.4, item='PDT11')
 15.54: 1 customer arrived
 15.54: consumer(04_00) arrived
 16.91: 3 customer arrived
 16.91: consumer(05_00) arrived
 16.91: consumer(05_01) arrived
 16.91: consumer(05_02) arrived
 17.54: consumer(04_00) get PriorityItem(priority=2.6, item='PDT12')
 18.91: consumer(05_00) get PriorityItem(priority=2.8, item='PDT13')
 18.91: consumer(05_01) get PriorityItem(priority=3.0, item='PDT14')
 18.91: consumer(05_02) get PriorityItem(priority=3.2, item='PDT15')
```

## wrap-up

- 사소하지만, simpy에서 제너레이터를 만들 때 `while`문을 사용하는 것이 더 좋을 것 같아요. `for`문의 경우는 시작값과, 종료값을 모두 입력해줘야 해서 제한적인 개수만 돌릴 수있는 반면, `while`은 종료조건을 따로 명시해주지 않을 경우 무한으로 돌아갈 수 있거든요. 
    - 어차피 `env.run(until=50)`의 종료 시각이 되면 종료되니까, 개별 프로세스는 무한으로 돌아가게 만들어도 될것 같구요. 

- 다만, 그래도, `while` 내부에서 일종의 `index integer`는 필요한데(customer_num 같은 것을 넘기기 위해서라도) 그럼 약간 코드가 지저분해져요. 다음처럼 위 아래에 쓸데없는 줄이 몇 개 더 가있으니까 별로 예쁘지 않네요. 
- 어떻게 하면 좀 더 깔끔하게 만들 수 있을지 고민이 필요할 것 같습니다. 

```python
def while_gen():
    i=0
    while True:
        ...
        i+=1
```


