---
title: simpy의 process interaction을 알아보자. 
category: python-lib 
tags: python python-lib simpy simulation process generator exception numpy 
---

## process interaction 

- 이전에는 프로세스 간의 상호작용에 대해서는 고려하지 않았습니다만, 사실 하나의 프로세스가 수행되고 있을때, 다른 프로세스와의 상호작용이 있을 수도 있습니다. 
- 간단하게, 하나의 프로세스 수행 중에, subprocess가 있는 경우는 어떻게 표현할 수 있을까요? 

### waiting for process 

- 비교적 간단하게 해줍니다. 우리가 넘긴 generator에서 다시 `env.process()`로 새로운 generator를 넘기면 됩니다. 
- 프로세스를 하나 수행하는데, 프로세스의 모든 activity는 subprocess로 구성되어 있다고 가정합니다. 
    - 즉 개별 activity는 새로운 subprocess generator를 process한 뒤에야 끝낼 수 있죠. 

- 사실 그냥 중요한 건, 일종의 인셉션 같은 개념인데, 하나의 프로세스가 수행중일 때, 그 내부에도 새로운 프로세스를 넣어서 nested, nested 형태로 넘겨도 된다는 것이죠.

- 아래 코드는 결국 프로세스 수행 중에 다시 `env`에 새로운 subprocess를 수행시키고, 다시 subsubprocess를 수행시키는 것을 말합니다. 결과를 보고 보시면 아마 더 이해가 쉬울 것 같습니다. 

```python
import simpy 
import numpy as np 

## 물론 이 아래 부분을 클래스로 구현을 해도 좋지만 일단은 이해를 위해서 다 함수로 표현함 
def subsubprocess(env):
    ## process의 개별 activity는 subprocess로 구성되어 있습니다. 
    print('        subsubprocess start at {:6.2f}'.format(env.now))
    for i in range(0, 2):
        execution_time = np.random.triangular(left=1, right=2, mode=1)
        yield env.timeout(execution_time)
    print('        subsubprocess over  at {:6.2f}'.format(env.now))
def subprocess(env):
    ## process의 개별 activity는 subprocess로 구성되어 있습니다. 
    print('    subprocess start at {:6.2f}'.format(env.now))
    for i in range(0, 2):
        yield env.process(subsubprocess(env))
    print('    subprocess over  at {:6.2f}'.format(env.now))
    
def process(env, activity_lst):
    while True:
        for act in activity_lst:
            print("start {} at {:6.2f}".format(act, env.now))
            execution_time = np.random.triangular(left=3, right=10, mode=6)
            ## 모든 activity는 subprocess라고 생각한다.
            ## subprocess(env)가 종료되어야 다음 스텝으로 넘어감
            ## 즉 일종의 waiting for other process를 구현했다고 보면 됨 
            yield env.process(subprocess(env))
            ##############
            print("end   {} at {:6.2f}".format(act, env.now))
            transfer_time = np.random.triangular(left=1, right=3, mode=2)
            yield env.timeout(transfer_time)
        print('process instance ends')
        print('#'*30)
        return None
###########
env = simpy.Environment()
process1 = process(env, ["act_{}".format(i) for i in range(0, 3)])
env.process(process1)
env.run(50)
```

```
start act_0 at   0.00
    subprocess start at   0.00
        subsubprocess start at   0.00
        subsubprocess over  at   3.24
        subsubprocess start at   3.24
        subsubprocess over  at   6.23
    subprocess over  at   6.23
end   act_0 at   6.23
start act_1 at   8.90
    subprocess start at   8.90
        subsubprocess start at   8.90
        subsubprocess over  at  11.59
        subsubprocess start at  11.59
        subsubprocess over  at  14.48
    subprocess over  at  14.48
end   act_1 at  14.48
start act_2 at  16.68
    subprocess start at  16.68
        subsubprocess start at  16.68
        subsubprocess over  at  19.33
        subsubprocess start at  19.33
        subsubprocess over  at  22.04
    subprocess over  at  22.04
end   act_2 at  22.04
process instance ends
##############################
```

### interrupting another process 

- 기다리기 싫다! 라는 경우도 있습니다. 예를 들어서 이미 어떤 프로세스가 수행중인데, 그 프로세스를 킬해버리고 싶을 때도 있잖아요? 

- 간단하게 같은 여러 가지의 시계가 돌아가는데 2초에 한번씩 시계를 없애는 시뮬레이션을 수행해봅니다. 

- 개별 시계는 다음처럼 모델링해야 합니다. 기존이랑 다른 방식이라면, `try`, `except`를 활용하여, `simpy.Interrupt`라는 익셉션이 발생했을 때, 어떻게 대응할 것인가가 정리되어 있습니다. 
    - 이렇게 프로세스가 interrupt되었을 때 어떻게 처리되는지를 명확하게 해야 에러없이 수행할 수 있습니다. 

```python
def clock(env, i, tick):
    ## generator에 interrupt 가 발생했을 때 종료하는 조건을 넣어주어야 함 
    while True:
        try: 
            yield env.timeout(tick)
            print('clock {} ticks at {}'.format(i, env.now))
        except simpy.Interrupt:
            print("## the clock {} was interrupted".format(i))
            return None
```

- 아래는 2초에 한번씩 랜덤하게 프로세스를 죽이는 process를 생성했습니다.
- 제일 위에, `current_ps`라는 리스트가 있는데, 여기에는 env에서 돌리는 프로세스의 모든 레퍼런스 값들이 들어가 있습니다. 이상하게도, env에서 현재 모든 프로세스를 확인할 수 있는 방법이 없어요. 그래서 따로 넣어주어야 합니다. 

```python
current_ps = []
def stop_any_process(env):
    ## 2초마다 한번씩 현재 process 중 아무거나 종료시키는 generator
    ## 남아있는 clock이 없을때의 조건도 만들어줌. 
    while True:
        try:
            yield env.timeout(2)
            r = np.random.randint(0, len(current_ps))
            current_ps[r].interrupt()
            current_ps.remove(current_ps[r])
        except:
            print("#"*20)
            print("all process was interrupted at {}".format(env.now))
            return None
```

## raw code 

- 전체 코드를 돌려보면 대략 다음과 같습니다. 

```python
import simpy 
import numpy as np 

## 현재 env에 있는 모든 process를 쭉 접근할 수 있는 방법이 없음.
## 따라서, 매번 프로세스를 따로 리스트의 형태로 저장해주는 것이 필요함. 
current_ps = []

def clock(env, i, tick):
    ## generator에 interrupt 가 발생했을 때 종료하는 조건을 넣어주어야 함 
    while True:
        try: 
            yield env.timeout(tick)
            print('clock {} ticks at {}'.format(i, env.now))
        except simpy.Interrupt:
            print("## the clock {} was interrupted".format(i))
            return None
            
def stop_any_process(env):
    ## 2초마다 한번씩 현재 process 중 아무거나 종료시키는 generator
    ## 남아있는 clock이 없을때의 조건도 만들어줌. 
    while True:
        try:
            yield env.timeout(2)
            r = np.random.randint(0, len(current_ps))
            current_ps[r].interrupt()
            current_ps.remove(current_ps[r])
        except:
            print("#"*20)
            print("all process was interrupted at {}".format(env.now))
            return None
        
## environment setting
env = simpy.Environment()

## 6 개의 중간에 멈출 수 있는 clock을 만들어서 집어넣음
for i in range(0, 5):
    p = env.process(clock(env, i, 2))
    ## 새롭게 만들어진 프로세스에 대해서 외부에서 접근 방법이 없으므로, 따로 저장해두어야 함
    current_ps.append(p)

## 2초마다 process를 멈추는 generator도 넘겨줌
env.process(stop_any_process(env))

env.run(until=20)
```

```
clock 0 ticks at 2
clock 1 ticks at 2
clock 2 ticks at 2
clock 3 ticks at 2
clock 4 ticks at 2
## the clock 3 was interrupted
clock 0 ticks at 4
clock 1 ticks at 4
clock 2 ticks at 4
clock 4 ticks at 4
## the clock 0 was interrupted
clock 1 ticks at 6
clock 2 ticks at 6
clock 4 ticks at 6
## the clock 4 was interrupted
clock 1 ticks at 8
clock 2 ticks at 8
## the clock 1 was interrupted
clock 2 ticks at 10
## the clock 2 was interrupted
####################
all process was interrupted at 12
```



## wrap-up

- 이해하고 보니 별거 아닌데, 사실 이거 이해한다고 조금 헤맸습니다. 그래서 중요한 포인트를 다시 정리했는데 
    1. interrupt되는 프로세스에서 interrupt시에 어떻게 종료되는지 조건 만들 것 
    2. interrupt하는 프로세스도 generator의 형태로 구현되어야 함. 
- 이라고 할 수 있겠네요. 

- 남은 궁금함으로는 nested되는 process의 경우 어떻게 모든 nested process에 대해서 `try, except`구분으로 에러를 처리해주어야 하는지 약간 궁금한데 모른 척하도록 합니다 하하하핫