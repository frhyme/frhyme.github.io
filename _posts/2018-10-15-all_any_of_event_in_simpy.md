---
title: simpy에서 (all of) or (any of) event 제어하기 
category: python-libs
tags: python python-libs simpy simulation event 
---

## intro 

- business process, 특히 BPMN을 시뮬레이션할 때, and join, any of it 을 사용해야 하는 일들이 있습니다. 
- 주어진 조건 중에서 무엇이든 만족하면 끝내거나(any of), 주어진 조건을 모두 만족하면 끝내거나(all of) 이렇게 많이 사용하죠. 
- simpy에서 이걸 어떻게 처리할 수 있는지 알아봅시다. 

## event control in simpy 

- 다음의 코드로 간단하게 만들어 봅니다. 
- `AND_events`라는 제너레이터는 argument로 입력받은 모든 이벤트들이 종료되야 끝나고, 
- `ANY_events`라는 제너레이터는 argument로 입력받은 이벤트 중 하나라도 종료되면 끝납니다. 

```python
import simpy ## 시뮬레이션에 사용하기 위한 라이브러리
from simpy.events import AnyOf, AllOf, Event

def AND_events(env, events):
    print("##All event start", env.now)
    ## 결과 result에 저장되는 타입은 <class 'simpy.events.ConditionValue'>
    result = yield AllOf(env, events)
    print("##All event end", env.now)

def ANY_events(env, events):
    print("Any event start", env.now)
    ## 결과 result에 저장되는 타입은 <class 'simpy.events.ConditionValue'>
    result = yield AnyOf(env, events)
    print("Any event end", env.now)
    
env = simpy.Environment()
## AND로 두개를 묶어줬으므로, 0일 때와 10초일때만 프린트됨 
env.process(
    AND_events(env=env, events=[env.timeout(3), env.timeout(10)])
)

## AND로 두개를 묶어줬으므로, 0일 때와 3초일때만 프린트됨 
env.process(
    ANY_events(env=env, events=[env.timeout(3), env.timeout(5)])
)

"""
- 존재하는 모든 프로세스를 끝내고 싶을 때는, 여기에 굳이 값을 넣지 않아도 되지만, 
- 그러다가, 무한으로 돌아가는 경우가 있음(종료조건을 넣지 않았을때)
- 그러므로 가능하면 넣는 것을 습관화하는 것이 좋음. 
"""
env.run(until=30)
```

- 결과는 다음과 같습니다. 
- 말한 바와 같이, 
    - All event는 모두 묶어줘서 모두 끝나야 종료되고, 
    - Any event는 하나라도 끝나면 종료됩니다. 

```
##All event start 0
Any event start 0
Any event end 3
##All event end 10
```

## process(or generator) to event

- 눈썰미가 좋으신 분은 이미 아시겠지만, 위에서는 그냥 event에 대해서 묶어줬습니다. 
- 다시 말하면, `AllOf(event1, event2)`라는 말이죠. `env.timeout()`은 event class에 속합니다. 

- 그렇다면, 몇개의 프로세스(제너레이터)를 만들고, 넘긴 모든 제너레이터들이 종료되면 끝나도록 하려면 어떻게 해야할까요? 
- 이벤트에 대해서 했던 것과 똑같이 generator들을 `AllOf`로 묶어주면 되는 것 아닐까요? 

- 해봅시다. 

```python
import simpy ## 시뮬레이션에 사용하기 위한 라이브러리
from simpy.events import AnyOf, AllOf, Event

def generator1(env): 
    print('generator1 start')
    yield env.timeout(5)
    print('generator1 end')
def generator2(env):
    print("generator2 start")
    yield env.timeout(13)
    print("generator2 end")
    
env = simpy.Environment()
env.process(AllOf(env, [generator1(env), generator2(env)]))
env.run(until=20)
```

- 다음과 같은 오류가 뜹니다. 제너레이터 오브젝트에 env가 없다는 말이군요 뭔소리지. 

> AttributeError: 'generator' object has no attribute 'env'

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-179-a69dfb363172> in <module>()
     12 
     13 env = simpy.Environment()
---> 14 env.process(AllOf(env, [generator1(env), generator2(env)]))
     15 env.run(until=20)

~/anaconda3/lib/python3.6/site-packages/simpy/events.py in __init__(self, env, events)
    585     """
    586     def __init__(self, env, events):
--> 587         super(AllOf, self).__init__(env, Condition.all_events, events)
    588 
    589 

~/anaconda3/lib/python3.6/site-packages/simpy/events.py in __init__(self, env, evaluate, events)
    495         # Check if events belong to the same environment.
    496         for event in self._events:
--> 497             if self.env != event.env:
    498                 raise ValueError('It is not allowed to mix events from '
    499                                  'different environments')

AttributeError: 'generator' object has no attribute 'env'
```

## process to event 

- 이유는 명확하게 모르겠습니다. 
- 하지만 다음처럼 조금 미묘하게 풀기는 했습니다. 

- 이전과의 차이점이 있다면, 이전에는 `env.process(generator)`로 제너레이터를 env에 등록해줬다면 
- 이제는 `simpy.events.Process(env, generator)`를 사용해서 env에 generator를 등록해줍니다. 
- 이 과정을 활용하면 제가 생성해내는 generator(process)는 일종의 이벤트로서, env에 등록됩니다. 
- event로 인식되니까, `AllOf`, `AnyOf`의 방식으로도 묶는 것도 가능합니다. 

```python
import simpy ## 시뮬레이션에 사용하기 위한 라이브러리
from simpy.events import AnyOf, AllOf, Event

def generator1(env): 
    print('##generator1 start', env.now)
    yield env.timeout(5)
    print('##generator1 end', env.now)
def generator2(env):
    print("generator2 start", env.now)
    yield env.timeout(13)
    print("generator2 end", env.now)

def AND_generators(env, generators):
    """
    - generator를 여러 개가 모두 종료되면 끝나는 generator를 만듬
        - 아래에 보면, 일반적으로 하는 방식인 env.process(generator)가 아니라 
        - simpy.events.Process(env, generator)로 처리했음을 알 수 있음. 
        - 두 가지 방식은 동일하나, 지금의 방식의 경우, 해당 프로세스를 이벤트로 고려함. 
        - 따라서 이벤트를 AllOf의 방식으로 묶을 수 있음. 
    """
    yield AllOf(env, 
                [simpy.events.Process(env, g) for g in generators]
               )
    
env = simpy.Environment()
"""
- simpy.events.Process(env, generator1(env)) 는 
- env.process(generator1(env)) 와 의미적으로 같음. 
"""
env.process(AND_generators(env, 
                           [generator1(env), generator2(env), generator2(env)]
                          ))
env.run(until=20)
```

```
##generator1 start 0
generator2 start 0
generator2 start 0
##generator1 end 5
generator2 end 13
generator2 end 13
```


## wrap-up 

- 사실 시간이 없어서 빨리 하려고, 하다보니 대충 이해하고 넘어가는 거긴 한데, 
- 그냥 Process와 Event는 다르다. 여러 프로세스(제너레이터)에 대해서 AllOf, AnyOf 등으로 묶어서 처리해야 한다면 해당 프로세스를 Event처럼 변환해서 활용하는 것이 필요하다. 
- 정도만 이해하면 될 것 같네요. 


## reference

- <https://simpy.readthedocs.io/en/latest/api_reference/simpy.events.html>