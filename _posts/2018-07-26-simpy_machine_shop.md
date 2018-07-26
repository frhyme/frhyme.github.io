---
title: simpy.PreemptiveResource로 우선순위 이용하기 - 머신 샵 모델링
category: python-lib
tags: python-lib python simpy numpy class generator
---

## 우선순위에 따라 업무 처리하기 

- 모든 업무에는 우선순위가 있습니다. priority가 2인 일을 하는 중에 priority가 1인 일이 들어오면, 1인 일을 우선 처리하고 다시 2로 돌아가야 하죠. 
- simpy에서도 이를 지원하며, 이를 어떻게 활용할 수 있는지 알아보겠습니다. 

## simpy.PreemptiveResource

- 일단 다음으로 간단하게 선언합니다. 

```python
repairman = simpy.PreemptiveResource(env, capacity=1)
```

- resource에 사용 요청을 할때가 좀 달라지는데, 다음과 같습니다. 
    - priority를 argument로 넣어서 request를 날려줍니다. 

- 또한 기존 resource와 다르게 generator에 try, except 구문이 있는데, 이것은 우선순위가 높은 업무가 들어왔을때 어떻게 반응하는지가 정의되어 있는 부분입니다. 
    - 우선순위가 높은 업무가 들어오면 자동으로 해당 process가 인터럽트되고, 그 예외상황에 어떻게 반응할지가 프로세스 상에서 정의되어 있어야 합니다. 
- 또한 우선순위가 높다는 말은 priority 값이 적다는 말입니다. (priority가 2보다 priority가 1인 업무가 더 중요함)

```python
def other_jobs(env, repairman):
    while True:
        do_time = 30.0
        while True:
            with repairman.request(priority=2) as req:
                ## repairman의 경우 그냥 Resource가 아닌 PreemptiveResource
                ## 따라서 현재 하고 있는 일보다 priority가 높은 request가 들어왔는데 capacity가 부족할 경우, 
                ## priority가 우선인 것을 먼저 한다. 따라서 그때는 simpy.Interrupt가 발생하게 됨. 
                yield req
                try:
                    start = env.now
                    yield env.timeout(do_time)
                    do_time = 0
                    break
                except simpy.Interrupt:
                    do_time -= (env.now - start)
```

## Process with class

- 이번에는 Process들도 모두 class에 넣어서 설계했습니다. 
- 기계를 모델링하는데 이 기계는 'working'과 'break', 'repair'라는 세 가지 프로세스를 가집니다. 
    - working: 제품을 계속 만드는 프로세스.
        - break에서 인터럽션이 전달되면, repair 프로세스를 수행하고, repair 프로세스가 종료되면, 다시 break프로세스를 수행함
    - break: 랜덤한 일정 시간 이후 working에 interruptiong을 발생시킴
    - repair: 머신을 고치는 프로세스 priority가 높은 업무를 수행

```python
class Machine(object):
    def __init__(self, env, name, repairman):
        self.env = env
        self.name = name
        self.parts_made = 0
        self.broken = False 
        
        self.process = self.env.process(self.working(repairman))
        self.env.process(self.break_machine())
        
    def working(self, repairman):
        while True:
            time_per_part = np.random.normal(20, 2)
            while True:
                start = self.env.now
                try:
                    ## 문제없이 부품을 생산한 경우 
                    yield self.env.timeout(time_per_part)
                    break
                except simpy.Interrupt:
                    ## 부품 생산중에 장비가 고장난 경우 
                    ## 이미 조립한 부분은 남기고, 추가로 조립해야 하는 시간만 계산함 
                    time_per_part -= (self.env.now - start)## remain time to part
                    ## 고장 났기 때문에 repairman에게 우선순위 높게 요청한다. 
                    self.env.process(self.repair_machine(repairman))
                    ## 고침 완료
                    ## 고쳐졌으므로 다시 고장 프로세스 가동
                    self.env.process(self.break_machine())
            self.parts_made += 1
            
    def repair_machine(self, repairman):
        with repairman.request(priority=1) as req:
            yield req ## 사용 요청 
            repair_time = np.random.uniform(30, 40)
            yield self.env.timeout(repair_time) ## 고침 
            print("{} is repaired at {:8.2f}".format(self.name, env.now))
            self.broken = False
            
    def break_machine(self):
        ## 랜덤한 시간 뒤에 현재 broken이 아니면 인터럽트를 발생시킴. 
        time_to_failure = np.random.exponential(300) 
        if self.broken == True:
            time_to_failure += np.random.uniform(30, 40)
        yield self.env.timeout(time_to_failure)
        if self.broken == False:
            print("{} is broken   at {:8.2f}".format(self.name, env.now))
            self.broken = True
            self.process.interrupt()
```


## 전체 코드 와 결과 

- 전체 코드와 결과는 다음과 같습니다. 

```python
import simpy 
import numpy as np 

class Machine(object):
    def __init__(self, env, name, repairman):
        self.env = env
        self.name = name
        self.parts_made = 0
        self.broken = False 
        
        self.process = self.env.process(self.working(repairman))
        self.env.process(self.break_machine())
        
    def working(self, repairman):
        while True:
            time_per_part = np.random.normal(20, 2)
            while True:
                start = self.env.now
                try:
                    ## 문제없이 부품을 생산한 경우 
                    yield self.env.timeout(time_per_part)
                    break
                except simpy.Interrupt:
                    ## 부품 생산중에 장비가 고장난 경우 
                    ## 이미 조립한 부분은 남기고, 추가로 조립해야 하는 시간만 계산함 
                    time_per_part -= (self.env.now - start)## remain time to part
                    ## 고장 났기 때문에 repairman에게 우선순위 높게 요청한다. 
                    self.env.process(self.repair_machine(repairman))
                    ## 고침 완료
                    ## 고쳐졌으므로 다시 고장 프로세스 가동
                    self.env.process(self.break_machine())
            self.parts_made += 1
            
    def repair_machine(self, repairman):
        with repairman.request(priority=1) as req:
            yield req ## 사용 요청 
            repair_time = np.random.uniform(30, 40)
            yield self.env.timeout(repair_time) ## 고침 
            print("{} is repaired at {:8.2f}".format(self.name, env.now))
            self.broken = False
            
    def break_machine(self):
        ## 랜덤한 시간 뒤에 현재 broken이 아니면 인터럽트를 발생시킴. 
        time_to_failure = np.random.exponential(300) 
        if self.broken == True:
            time_to_failure += np.random.uniform(30, 40)
        yield self.env.timeout(time_to_failure)
        if self.broken == False:
            print("{} is broken   at {:8.2f}".format(self.name, env.now))
            self.broken = True
            self.process.interrupt()
                
def other_jobs(env, repairman):
    ## repairman은 고치는 일 이외에도 우선순위가 낮은 다른 일들을 계속 수행하고 있음. 
    while True:
        do_time = 30.0
        while True:
            with repairman.request(priority=2) as req:
                yield req
                ## repairman의 경우 그냥 Resource가 아닌 PreemptiveResource
                ## 따라서 현재 하고 있는 일보다 priority가 높은 request가 들어왔는데 capacity가 부족할 경우, 
                ## priority가 우선인 것을 먼저 한다. 따라서 그때는 simpy.Interrupt가 발생하게 됨. 
                try:
                    start = env.now
                    yield env.timeout(do_time)
                    do_time = 0
                    break
                except simpy.Interrupt:
                    do_time -= (env.now - start)
        
####################
np.random.seed(42)
print("Machine shop")

env = simpy.Environment()
repairman = simpy.PreemptiveResource(env, capacity=1)

machines = [Machine(env, 'Machine %d' % i, repairman) for i in range(0, 10)]
env.process(other_jobs(env, repairman))
env.run(until=60*5)

print("#"*31)
print('Machine shop results after %s weeks' % 4)
sum_parts = 0
for machine in machines:
    print('%s made %d parts.' % (machine.name, machine.parts_made))
    sum_parts += machine.parts_made
print("#"*31)
print("{} parts produced".format(sum_parts))
```

- 시뮬레이션 수행 결과.

```
Machine shop
Machine 4 is broken   at     6.24
Machine 2 is broken   at    17.95
Machine 4 is repaired at    39.16
Machine 6 is broken   at    60.20
Machine 7 is broken   at    60.78
Machine 2 is repaired at    74.11
Machine 9 is broken   at   103.27
Machine 6 is repaired at   107.42
Machine 7 is repaired at   138.50
Machine 7 is broken   at   144.37
Machine 8 is broken   at   169.66
Machine 9 is repaired at   176.58
Machine 6 is broken   at   194.57
Machine 7 is repaired at   211.60
Machine 8 is repaired at   250.97
Machine 1 is broken   at   273.88
Machine 6 is repaired at   287.89
###############################
Machine shop results after 4 weeks
Machine 0 made 14 parts.
Machine 1 made 14 parts.
Machine 2 made 14 parts.
Machine 3 made 16 parts.
Machine 4 made 14 parts.
Machine 5 made 14 parts.
Machine 6 made 15 parts.
Machine 7 made 14 parts.
Machine 8 made 15 parts.
Machine 9 made 15 parts.
###############################
145 parts produced
```

## wrap-up

- 이제는 Resource도, Process도 모두 class로 정리해서 사용하는 것이 좋은 것 같습니다. 

