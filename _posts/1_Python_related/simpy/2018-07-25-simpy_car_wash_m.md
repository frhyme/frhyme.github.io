---
title: simpy - 세차 프로세스 시뮬레이션
category: python-lib 
tags: python-lib simpy simulation python numpy class generator
---

## 간단한거긴 한데..

- [여기](http://simpy.readthedocs.io/en/latest/examples/carwash.html)에 비슷한 코드가 있습니다. 
- 차가 랜덤하게 세차장에 오고, 세차장에서 세차하고 차를 내보내는 형태의 아주 쉬운 시뮬레이션입니다. 
- 단, resource를 class로 만들어서, 좀 편하게 사용할 수 있게 만들었다는 것이 차이라고 할 수 있겠네요. 

## code 

```python
import simpy 
import numpy as np

## 세차머신
class CarWashMachine(object):
    ## 리소스는 아래처럼 클래스로 만들어서 처리해주는 것이 바람직할 것으로 생각됨 
    def __init__(self, env, capacity):
        self.env = env
        self.machine = simpy.Resource(self.env, capacity = capacity)
        self.users = [] ## 현재 사용중인 프로세스
        self.queue = [] ## 현재 대기열에 있는 프로세스 
    def wash(self, car_name):
        ## 아래처럼 resource 에서 이뤄지는 부분은 여기에서 작성하는 편이 더 좋을 수도 있음.
        print("{:6.2f} users: {}, queue: {}".format(env.now, self.users, self.queue))
        waiting_time = self.env.now
        with self.machine.request() as req:
            ## 바로 resource available 할 때 
            if self.machine.count < self.machine.capacity:
                self.users.append(car_name)
                yield req
            ## resource available 하지 않을 때 
            else:
                self.queue.append(car_name)
                yield req
                self.queue.remove(car_name)
                self.users.append(car_name)
            waiting_time = self.env.now - waiting_time
            if waiting_time!=0:
                print("{:6.2f} {} waited {:6.2f}".format(self.env.now, car_name, waiting_time))
            print("{:6.2f} {} wash start".format(self.env.now, car_name))    
            wash_time = np.random.exponential(30)
            yield self.env.timeout(wash_time)
            print("{:6.2f} {} wash over".format(self.env.now, car_name))
        self.users.remove(car_name)

## 도착했음을 출력하고, 리소스에 사용요청을 보내고, 사용을 끝내면 메세지츨 출력하고 종료하는 제너레이터 
def car(env, name, car_wash_machine):
    ## 도착하고, resource에 넘겨지고 그 다음을 죽 진행함. 
    print("{:6.2f} {} arrived".format(env.now, name))
    yield env.process(car_wash_machine.wash(name))
    print("{:6.2f} {} leaved".format(env.now, name))

## 랜덤으로 car를 생성해내는 제너레이터 
def source(env, car_n, car_wash_machine):
    for i in range(0, car_n):
        arrival_time = np.random.exponential(3)
        yield env.timeout(arrival_time)
        new_car = car(env, "Car{:2d}".format(i), car_wash_machine)
        env.process(new_car)

np.random.seed(42)
env = simpy.Environment()
cwm1 = CarWashMachine(env, capacity=2)

s = source(env, 10, cwm1)
env.process(s)

env.run(until=100)
```

```
  1.41 Car 0 arrived
  1.41 users: [], queue: []
  1.41 Car 0 wash start
 10.44 Car 1 arrived
 10.44 users: ['Car 0'], queue: []
 10.44 Car 1 wash start
 13.18 Car 2 arrived
 13.18 users: ['Car 0', 'Car 1'], queue: []
 13.69 Car 3 arrived
 13.69 users: ['Car 0', 'Car 1'], queue: ['Car 2']
 13.87 Car 4 arrived
 13.87 users: ['Car 0', 'Car 1'], queue: ['Car 2', 'Car 3']
 15.53 Car 1 wash over
 15.53 Car 1 leaved
 15.53 Car 2 waited   2.35
 15.53 Car 2 wash start
 19.90 Car 5 arrived
 19.90 users: ['Car 0', 'Car 2'], queue: ['Car 3', 'Car 4']
 23.59 Car 6 arrived
 23.59 users: ['Car 0', 'Car 2'], queue: ['Car 3', 'Car 4', 'Car 5']
 23.66 Car 7 arrived
 23.66 users: ['Car 0', 'Car 2'], queue: ['Car 3', 'Car 4', 'Car 5', 'Car 6']
 34.17 Car 8 arrived
 34.17 users: ['Car 0', 'Car 2'], queue: ['Car 3', 'Car 4', 'Car 5', 'Car 6', 'Car 7']
 39.53 Car 9 arrived
 39.53 users: ['Car 0', 'Car 2'], queue: ['Car 3', 'Car 4', 'Car 5', 'Car 6', 'Car 7', 'Car 8']
 40.91 Car 0 wash over
 40.91 Car 0 leaved
 40.91 Car 3 waited  27.22
 40.91 Car 3 wash start
 43.10 Car 2 wash over
 43.10 Car 2 leaved
 43.10 Car 4 waited  29.23
 43.10 Car 4 wash start
 48.07 Car 3 wash over
 48.07 Car 3 leaved
 48.07 Car 5 waited  28.17
 48.07 Car 5 wash start
 49.12 Car 4 wash over
 49.12 Car 4 leaved
 49.12 Car 6 waited  25.53
 49.12 Car 6 wash start
 54.15 Car 5 wash over
 54.15 Car 5 leaved
 54.15 Car 7 waited  30.49
 54.15 Car 7 wash start
 60.00 Car 6 wash over
 60.00 Car 6 leaved
 60.00 Car 8 waited  25.84
 60.00 Car 8 wash start
 76.47 Car 7 wash over
 76.47 Car 7 leaved
 76.47 Car 9 waited  36.94
 76.47 Car 9 wash start
 76.97 Car 8 wash over
 76.97 Car 8 leaved
 86.79 Car 9 wash over
 86.79 Car 9 leaved
```

## wrap-up

- 우선 가능하면 resource는 class로 관리하는 것이 좋은 것 같습니다. 
    - 내부에 리소스를 하나 만들어 두고, 
    - 필요한 state의 변화별로 method를 만들어서 관리하는 것이 좋을 것 같아요. wash에 대해서 하나의 method로 만든 것처럼
- 또한 이렇게 class로 만들었을 때, 내부에 `users`, `queue`라는 리스트를 만들고 여기에 