---
title: 파이썬에서 시뮬레이션을 해봅시다.
category: python-lib
tags: python python-lib simulation simpy generator 
---


## intro

- 연구하다가 간단하게 시뮬레이션을 돌릴 필요성이 있어서, 시뮬레이션을 파이썬에서 어떻게 지원하는지를 알아보았습니다. 
- [simpy](http://simpy.readthedocs.io/en/latest/index.html)라는 라이브러리가 있구요. 일단 이걸 설치합니다. 

```
pip install simpy 
```

## simpy 

> SimPy is a process-based discrete-event simulation framework based on standard Python.

- 라고 합니다. 하나씩 풀어보면 시뮬레이션을 위해서는 process 와 resource를 이해하는 것이 필요한데 

> Processes in SimPy are defined by Python generator functions and may, for example, be used to model active components like customers, vehicles or agents. SimPy also provides various types of shared resources to model limited capacity congestion points (like servers, checkout counters and tunnels).

- 즉 process는 customer, vehicles 등 일반적인 agent를 모델링한다고 할 수 있습니다. 순서가 있는 형태(business process or petri-net)이 프로세스에 해당한다고 할 수 있습니다. 
- resource는 process를 수행하는 수행자 라고 할 수있겠죠. 

## basic case of simpy 

### very basic case - clock

- documentation에 있는 아주 기본적인 예를 들어서 진행해보겠습니다(일단 여기서는 resource는 제외되어 있습니다).
- `clock`이라는 generator를 만들고, 이를 `simpy.environment`에 넘겨 줍니다. 

- 몇 가지 중요한 사항
    - `env.process`에는 generator를 넘겨주어야 합니다. 
    - `env.timeout()`은 일정 시간만큼 멈춰두는 것을 의미합니다. clock의 경우 tick하는 시간이 있기 때문에 일단 tick을 하면 정해진 다음 시간까지는 멈춰두어야 하죠(그래도 전체 시간은 지나갑니다). 그럴때 `env.timeout()`을 사용합니다. 
    - 따라서 generator를 정의할 때, env를 argument로 함께 넘겨 주는 것이 필요합니다. 

```python
import simpy 

## 내부에 loop와 yield가 있는 generator입니다. 
## simpy에서는 generator를 기본적으로 사용하는데, 
## generator는 yield를 포함한 연속된 명령 리스트? 라고 생각해도 상관없습니다. 
## yield: return something and hold 
def clock(env, name, tick):
    while True:
        ## clock generator가 한번 불러지면, 아래 행동을 수행 
        print("{:.2f} sec: {} clock ticks".format(env.now, name))
        ## 넘겨 받는 시간만큼 멈춰둡니다. 
        yield env.timeout(tick)

## Environment: simulation하려는 세계 
env = simpy.Environment()

## 아래 부분에서 함수를 넘겨준다고 생각할 수 있는데, 정확히는 함수가 아니라 generator를 넘겨주는 것임. 
## 0.5초마다 소리치는 클락
fast_clock = clock(env, '     fast', 0.5)
## 1초마다 소리치는 클락 
slow_clock = clock(env, '     slow', 1)
very_fast_clock = clock(env, 'very fast', 0.1)

## 이 두 generator를 앞서 생성한 environment에 넘겨줍니다. 
env.process(fast_clock)
env.process(slow_clock)
env.process(very_fast_clock)

## simulation 수행. 시간이 없으면 무한으로 돌기 때문에 until을 통해 끝나는 시간을 정해두는 것이 필요함. 
env.run(until=2)
```

- 결과는 아래처럼 매 시간마다 clock이 tick하는 것을 찍어줍니다. 

```
0.00 sec:      fast clock ticks
0.00 sec:      slow clock ticks
0.00 sec: very fast clock ticks
0.10 sec: very fast clock ticks
0.20 sec: very fast clock ticks
0.30 sec: very fast clock ticks
0.40 sec: very fast clock ticks
0.50 sec:      fast clock ticks
0.50 sec: very fast clock ticks
0.60 sec: very fast clock ticks
0.70 sec: very fast clock ticks
0.80 sec: very fast clock ticks
0.90 sec: very fast clock ticks
1.00 sec: very fast clock ticks
1.00 sec:      slow clock ticks
1.00 sec:      fast clock ticks
1.10 sec: very fast clock ticks
1.20 sec: very fast clock ticks
1.30 sec: very fast clock ticks
1.40 sec: very fast clock ticks
1.50 sec:      fast clock ticks
1.50 sec: very fast clock ticks
1.60 sec: very fast clock ticks
1.70 sec: very fast clock ticks
1.80 sec: very fast clock ticks
1.90 sec: very fast clock ticks
```

### basic case - car 

- 이번에는 차를 모델링 해보겠습니다(그냥 아주 간단하게 돌리는 거라서 시뮬레이션이라는 말을 붙이기가 좀...) 
- 5초동안 parking하고 2초동안 driving하는 아주 간단한 형태로 시뮬레이션을 돌립니다. 

- `simpy.Environment()`를 argument로 넘겨 받고, `env.timeout`하는 제너레이터를 만들어주는 함수를 정의합니다.
- generator에는 `yield`가 하나만 있어야 하는 것은 아닙니다. 다양한 state를 가지는 agent라면 다양한 yield를 만들어줄 수 있습니다. 

```python
import simpy 
import numpy as np 

## 5초 파킹하고, 2초 운전하는 시뮬레이션 
def car(env):
    while True:
        print('Start parking at %5.1f' % env.now)
        parking_duration = 5
        #parking_duration = np.random.normal(5, 1)
        yield env.timeout(parking_duration)
        print('Stop  parking at %5.1f' % env.now)

        print('Start driving at %5.1f' % env.now)
        driving_duration = 2
        #trip_duration = np.random.normal(2, 1)
        yield env.timeout(driving_duration)
        print('Stop  driving at %5.1f' % env.now)

env = simpy.Environment()
env.process(car(env))
env.run(until=20)
```

### basic case - business process simulation 

- 아주 간단하게 business process instance를 만들고 simulation을 해보겠습니다. 
    - 업무 프로세스 P가 있습니다. P는 여러 가지의 Activity로 구성되는데, 개별 Activity는 수행할 수 있는 Resource가 정해져 있죠. 
    - Process를 generator의 형태로 만듭니다. 그리고 generator 내부에서 특정 activity가 수행될 때 resource에 request를 날려서 resource를 일정 시간 동안 사용합니다(여기서는 일단 resource 부분은 구현하지 않았습니다)

- activity의 execution time은 triangular distribution에 따라 결정된다고 가정합니다. 
- 일단은 resource를 고려하지 않고 모델링했습니다만, 이후에는 resource를 사용해서, 모델링하는 것도 가능할 것 같아요. 그 부분은 나중에 구현하도록 하겠습니다. 
- 또한 기존의 방식과 다르게 generator에 `return`이 포함되어 있습니다. 이는 일정 횟수(여기서는 단 한번)의 비즈니스 프로세스만 수행하고, 제너레이터를 종료시키는 것을 말합니다. 
    - generator에 종료조건이 있으므로, `env.run(until=1000)`에서 until에 넘어가는 값을 무의미해집니다. 

```python
import simpy 
import numpy as np 

def business_process(env, activity_lst):
    while True:
        for act in activity_lst:
            ## activity의 수행 시간은 triangulat dist를 따르며, 
            print('start {} at {:6.2f}'.format(act, env.now))
            activity_time = np.random.triangular(left=3, right=10, mode=7)
            yield env.timeout(activity_time)
            print('end   {} at {:6.2f}'.format(act, env.now))
            
            ## activity를 transfer하는데 일정 시간이 소요된다고 가정함.
            activity_transfer_time = np.random.triangular(left=1, right=3, mode=2)
            yield env.timeout(activity_transfer_time)
        print("#"*30)
        print("process end")
        ## 만약 여기 return 을 넣으면 여기서 generator가 그대로 종료됨 
        ## 만약 n 번 수행하고 싶다면, while True 를 for 문으로 변경하고, 몇 번 종료 후 끝내는 형태로 해도 괜찮을듯. 
        return 'over'

## environment setting
env = simpy.Environment()

bp1 = business_process(env, activity_lst=[ "activity_{}".format(i) for i in range(1, 6)])
env.process(bp1)

env.run(until=100)
```

- 실행 결과는 다음과 같습니다. 

```
start activity_1 at   0.00
end   activity_1 at   7.70
start activity_2 at  10.18
end   activity_2 at  18.64
start activity_3 at  20.33
end   activity_3 at  29.20
start activity_4 at  31.47
end   activity_4 at  37.72
start activity_5 at  39.95
end   activity_5 at  43.88
##############################
process end
```

## wrap-up 

- 쓰다보면 포스트의 내용이 너무 길어져서 요즘에는 post가 200줄을 넘어갈 것 같으면 일단 끊기로 했습니다. 다음 포스트에서 이어서 쓰겠습니다. 