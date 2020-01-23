---
title: simpy - process communication 
category: python-lib 
tags: python simpy numpy simulation dictionary 
---

## example illustration 

- 다수의 프로세스가 동시에 수행되고 있을 때를 생각해봅시다. 
    - Process A는 수행 중에 message1를 Process B에 보냅니다. 
    - Process B는 알아서 수행하고 있다가, Process A가 보낸 message에 따라서 서로 다른 동작을 하게 됩니다. 
- 이렇게 프로세스 간의 interconnection을 어떤 식으로 표현할 수 있을까요? 
- [simpy - example: Process communication](http://simpy.readthedocs.io/en/latest/examples/process_communication.html) 을 고려하여 만들었습니다. 

## ex1) process communication: one to one

- 서로 다른 process A, B를 각각 만들고 
- A의 경우 B가 던진 msg에 따라서 컨트롤 플로우를 변경하여 사용한다고 합시다. 

- 아래처럼 서로 다른 프로세스에서 하나의 pipe(정확히는 store)를 공유하도록 하고, 한쪽에서는 일방적으로 보내고, 다른쪽에서는 일반적으로 받는 형태로 진행하면 되죠. 

```python
import simpy 
import numpy

## one to one communication
def processA(env, pipe_out):
    ## processA sending msg to processB
    for i in range(0, 10):
        p_name = "PA{:2d}".format(i)
        yield env.timeout(3)
        print("{:8.2f}: {} executed a1".format(env.now, p_name))
        yield env.timeout(5)
        print("{:8.2f}: {} executed a2".format(env.now, p_name))
        ## 상황에 따라서 메세지를 보냄 
        if np.random.normal(0, 1)< 0.5:
            pipe_out.put("msg1")
        else:
            pipe_out.put("msg2")
        yield env.timeout(5)
        print("{:8.2f}: {} executed a3".format(env.now, p_name))
        print("{:8.2f}: {} completed".format(env.now, p_name))
def processB(env, pipe_in):
    for i in range(0, 10):
        p_name = "PB{:2d}".format(i)
        yield env.timeout(3)
        print("{:8.2f}: {} executed a1".format(env.now, p_name))
        print("{:8.2f}: {} is waiting for msg".format(env.now, p_name))
        ## 메세지를 받음. 
        msg = yield pipe_in.get()
        ## 받은 메세지에 따라서 다른 행동을 취함
        if msg=='msg1':
            print("{:8.2f}: {} get {}".format(env.now, p_name, msg))
            yield env.timeout(5)
            print("{:8.2f}: {} executed exc_a1".format(env.now, p_name))
        elif msg=='msg2':
            print("{:8.2f}: {} get {}".format(env.now, p_name, msg))
            yield env.timeout(5)
            print("{:8.2f}: {} executed exc_a2".format(env.now, p_name))
        print("{:8.2f}: {} completed".format(env.now, p_name))
            
np.random.seed(42)
env = simpy.Environment()
pipe = simpy.Store(env)
env.process(processA(env, pipe_out=pipe))
env.process(processB(env, pipe_in=pipe))

env.run(until=50)

```

- 실행 결과 

```
    3.00: PA 0 executed a1
    3.00: PB 0 executed a1
    3.00: PB 0 is waiting for msg
    8.00: PA 0 executed a2
    8.00: PB 0 get msg1
   13.00: PA 0 executed a3
   13.00: PA 0 completed
   13.00: PB 0 executed exc_a1
   13.00: PB 0 completed
   16.00: PA 1 executed a1
   16.00: PB 1 executed a1
   16.00: PB 1 is waiting for msg
   21.00: PA 1 executed a2
   21.00: PB 1 get msg1
   26.00: PA 1 executed a3
   26.00: PA 1 completed
   26.00: PB 1 executed exc_a1
   26.00: PB 1 completed
   29.00: PA 2 executed a1
   29.00: PB 2 executed a1
   29.00: PB 2 is waiting for msg
   34.00: PA 2 executed a2
   34.00: PB 2 get msg2
   39.00: PA 2 executed a3
   39.00: PA 2 completed
   39.00: PB 2 executed exc_a2
   39.00: PB 2 completed
   42.00: PA 3 executed a1
   42.00: PB 3 executed a1
   42.00: PB 3 is waiting for msg
   47.00: PA 3 executed a2
   47.00: PB 3 get msg2
```

## ex2) process communication: many to one

- 두 개 이상의 프로세스에서 모두 메세지를 보내고 그 메세지가 모두 전달된 뒤에야 프로세스에서 특정 액티비티를 수행할 수 있다고 하고, 그런 형태로 진행해봅시다. 

- 이 경우에는 메세지를 보내는 프로세스 별로 서로 다른 `pipe`를 세팅해줘야 합니다. 이 파이프는 그냥 일단 리스트로 넣어두고(편하게 하려면 클래스로 해도 되고요), 개별 파이프별로 `put` method 를 사용해서 메세지를 죽죽 넣어줍니다. 

- 메세지를 받는 쪽에서는, 아래처럼 이벤트를 `env.all_of()`로 묶어줘야 합니다. 이렇게 해야, 모든 이벤트가 실행된 다음에 다음 스텝으로 넘어갈 수 있죠. 
    - 또한, `compound_events`에 저장된 msg를 보려면, 일단 이 형태를 `dictionary`로 변형한 다음 사용해야 합니다. 

```python
compound_events = yield env.all_of([pipe_in.get() for pipe_in in pipe_ins])
```

```python
import numpy as np 
import simpy

## n to 1 communication 
def processA(env, pipe_out):
    ## processA sending msg to processB
    for i in range(0, 10):
        p_name = "PA{:2d}".format(i)
        yield env.timeout(3)
        print("{:8.2f}: {} executed a1".format(env.now, p_name))
        yield env.timeout(np.random.exponential(10))
        print("{:8.2f}: {} sending msg".format(env.now, p_name))
        if np.random.normal(0, 1)< 0.5:
            pipe_out.put("msg1")
        else:
            pipe_out.put("msg2")
        yield env.timeout(5)
        print("{:8.2f}: {} executed a3".format(env.now, p_name))
        print("{:8.2f}: {} completed".format(env.now, p_name))
def processB(env, pipe_ins):
    ## process
    for i in range(0, 10):
        p_name = "PB{:2d}".format(i)
        yield env.timeout(3)
        print("{:8.2f}: {} executed a1".format(env.now, p_name))
        print("{:8.2f}: {} is waiting for msgs".format(env.now, p_name))
        ## 아래처럼 env.all_of 로 묶어주면 여기서 발생하는 모든 이벤트가 종료되어야 넘어감
        compound_events = yield env.all_of([pipe_in.get() for pipe_in in pipe_ins])
        ## 값을 indexing하는 것이 어려운데, 아래처럼 딕셔너리로 바꿔주고 value로 접근하면 넘겨받은 msg를 알 수 있음. 
        compound_events_dict = dict(compound_events)
        print("{:8.2f}: {} get {}".format(env.now, p_name, compound_events_dict.values()))
        yield env.timeout(5)
        print("{:8.2f}: {} completed".format(env.now, p_name))
            
        
np.random.seed(1)
env = simpy.Environment()
## ProcessA가 두 개 돌아가는데, 두 ProcessA가 모두 메세지를 보낸 뒤에만 ProcessB가 운영할 수 있음
## 즉, ProcessA는 2개 ProcessB는 1개 이므로 communication channel을 두 개 만들어야 함
pipes = [simpy.Store(env) for i in range(0, 2)]

## 개별 process에 메세지를 보내는 채널을 연결해 주고 
env.process(processA(env, pipe_out=pipes[0]))
env.process(processA(env, pipe_out=pipes[1]))
## 여기서는 전체 파이프를 모두 넘겨줌 
env.process(processB(env, pipe_ins=pipes))

env.run(until=25)
```

```
    3.00: PA 0 executed a1
    3.00: PA 0 executed a1
    3.00: PB 0 executed a1
    3.00: PB 0 is waiting for msgs
    8.40: PA 0 sending msg
   13.40: PA 0 executed a3
   13.40: PA 0 completed
   15.74: PA 0 sending msg
   15.74: PB 0 get dict_values(['msg1', 'msg1'])
   16.40: PA 1 executed a1
   20.74: PA 0 executed a3
   20.74: PA 0 completed
   20.74: PB 0 completed
   21.45: PA 1 sending msg
   23.74: PA 1 executed a1
   23.74: PB 1 executed a1
   23.74: PB 1 is waiting for msgs
```

## wrap-up

- `simpy`의 `Store`를 pipe의 형태로 사용해서 프로세스 간의 간단한 통신을 가능하도록 한다는 것이 좋네요. 