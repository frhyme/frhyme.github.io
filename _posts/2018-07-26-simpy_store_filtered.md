---
title: simpy - Resource, Store 이용하기 
category: python-lib
tags: python python-lib simpy numpy filter simulation 
---

## simpy.Resource - store

- 앞서 말씀드린 바와 같이 `simpy`에서는 Resource, Container, Store 라는 세 가지 종류의 리소스가 있습니다. 
    - `Resources`
    > Resources that can be used by a limited number of processes at a time (e.g., a gas station with a limited number of fuel pumps).

    - `Containers` 
    > Resources that model the production and consumption of a homogeneous, undifferentiated bulk. It may either be continuous (like water) or discrete (like apples).

    - `Stores` 
    > Resources that allow the production and consumption of Python objects.

- 즉 `Stores`는 내부에 있는 개체들이 python object이기만 하면 되고, 마음대로 소비하고, 채워넣는 형태의 창고라고 생각하면 될 것 같습니다. `Containers`처럼 같은 형태의 개체들만 있어야 할 필요는 없습니다. 
    - 대신, `Container`는 물 과 같이 `amount`를 측정할 수 있고, `Store`에서는 discrete한 것들을 다룬다고 보면 됩니다. 

```python
store = simpy.Store(env, capacity=2)
store.items ## 창고에 있는 아이템들 
store.put() ## 창고에 아이템 넣기, 하나씩 넣어야 함 리스트를 넣으면 리스트 하나를 아이템 하나로 인식
store.get() 
## 창고에서 아이템 꺼내기. resource에 request 하는 것과 마찬가지로, 만약 아이템이 없으면 나올때까지 기다림. 
```

## basic example - just store 

- 간단하게, producer와 consumer를 모델링해보겠습니다. 
    - `producer`: 일정 간격에 한번씩 제품을 store에 `put`
    - `consumer`: 일정 간격에 한번씩 제품을 store로부터 `get`
    - `consuemrs`: 일정 간격마다 consumer 프로세스를 추가 

```python
import numpy as np 
import simpy 

def producer(env, store):
    ## 무한으로 진행되는 generator
    ## 1초에 제품을 하나씩 생성해냄. 
    i = 1
    while True:
        yield env.timeout(1)
        product_name = "spam{:2d}".format(i)
        ## store method: items, put, get 
        yield store.put(product_name)
        ## 현재 창고에 있는 제품들 출력 
        print("{:6.2f}: Produced {}, items: {}".format(env.now, product_name, store.items))
        i+=1

def consumer(name, env, store):
    ## 고객 한명이 스팸을 요구하고, 
    ## 한번 사간 다음에는 한동안 안 사감 
    while True:
        yield env.timeout(1)
        print("{:6.2f}: {} requesting spam".format(env.now, name))
        ## 아래도 request와 마찬가지로 획득할때까지 기다렸다가 생기면 가져감 
        waiting_time = env.now
        item = yield store.get()
        waiting_time = env.now - waiting_time
        #print("{} was waiting during {:6.2f}".format(name, waiting_time))
        print("{:6.2f}: {} got {}".format(env.now, name, item))
        ## 물건을 사갔으니 한동안 안 사감 
        yield env.timeout(np.random.exponential(5))

def consumers(env, store, n):
    ## 총 n 명의 고객을 프로세스로 등록함  
    for i in range(0, n):
        yield env.timeout(2)
        new_consumer = consumer("consumer{:2d}".format(i), env, store)
        env.process(new_consumer)

np.random.seed(42)
env = simpy.Environment()
store = simpy.Store(env, capacity=2)

prod = env.process(producer(env, store))
#consumers = [env.process(consumer("consumer{:2d}".format(i), env, store)) for i in range(0, 2)]
env.process(consumers(env, store, 5))

env.run(until=10)
```

- 실행 결과 

```
  1.00: Produced spam 1, items: ['spam 1']
  2.00: Produced spam 2, items: ['spam 1', 'spam 2']
  3.00: consumer 0 requesting spam
  3.00: consumer 0 got spam 1
  3.00: Produced spam 3, items: ['spam 2', 'spam 3']
  5.00: consumer 1 requesting spam
  5.00: consumer 1 got spam 2
  5.00: Produced spam 4, items: ['spam 3', 'spam 4']
  6.35: consumer 0 requesting spam
  6.35: consumer 0 got spam 3
  6.35: Produced spam 5, items: ['spam 4', 'spam 5']
  7.00: consumer 2 requesting spam
  7.00: consumer 2 got spam 4
  7.35: Produced spam 6, items: ['spam 5', 'spam 6']
  9.00: consumer 3 requesting spam
  9.00: consumer 3 got spam 5
  9.00: Produced spam 7, items: ['spam 6', 'spam 7']
```

## filterStore

- 여기서는 선택적으로 필요한 리소스를 찾는 작업을 지원한다. 
    - 랜덤하게 task가 발생하는데 해당 task는 required activity가 존재함
    - filterstore 에 들어있는 resource들은 각자 activity들을 가지고 있음
    - filtersotre에 있는 resource중에서 task의 required activity를 수행할 수 있는 놈들을 찾아서 수행하도록 함

```python
import simpy 
import numpy as np 

skill_set = ["skill{:2d}".format(i) for i in range(0, 3)]

class Human(object):
    def __init__(self, name):
        self.name = name
        ## 몇 개의 skill을 가지게 될지 정함 
        self.skill_num = np.random.randint(1, 3)
        ## 가지고 있는 skill은 중복될 수 없으며, 따라서 set로 관리해야 편한
        ## 특히, 이렇게 해야 skill set이 subset인지 아닌지를 더 잘 알 수 있음. 
        self.skills = set(np.random.choice(skill_set, self.skill_num, replace=False))
    def __repr__(self):
        ## 프린트할때는 여기서 리턴되는 스트링을 참고하여 만들어짐 
        return "{}".format(self.skills)
        #return "{} have skills: {}\n".format(self.name, self.skills)
        
def task(env, name, human_resources):
    skill_num = np.random.randint(1, 3)## 해당 태스크는 몇 가지의 스킬을 필요로 하는가 
    required_skills = set(np.random.choice(skill_set, skill_num, replace=False))
    ## 현재 사용가능한 사람 수 
    print("{:6.2f}: available humans count: {}".format(env.now, len(human_resources.items)))
    ## 태스크 대기열 수 
    print("{:6.2f}: task queue count: {}".format(env.now, len(human_resources.get_queue)))
    ## 해당 태스크가 필요로 하는 스킬 
    print("{:6.2f}: {} required skills: {}".format(env.now, name, required_skills))
    ## 사용하는 시간동안은 뺐다가, 사용이 끝나면 다시 store에 넣어줌 
    ## 아래처럼 원하는 조건을 넘기면, 그 조건에 맞는 resource를 찾아서 정리해줌. 
    ## 여러 가지의 리소스가 있을때는 어떤 것이 되는지 모르겠지만, 어떤 것이 되어도 상관없지 않은가.
    human = yield human_resources.get(lambda x: required_skills.issubset(x.skills))
    print("{:6.2f}: {} start to handle {}".format(env.now, human.name, name))
    yield env.timeout(30)
    print("{:6.2f}: {} completed".format(env.now, name))
    yield human_resources.put(human)
    

def task_generator(env, human_resources):
    for i in range(0, 100):
        yield env.timeout(3)
        env.process(task(env, "task{:2d}".format(i), human_resources))
        
np.random.seed(42)
env = simpy.Environment()

human_resources = simpy.FilterStore(env)## capacity를 명시하지 않으면 inf로 인식함. 즉 존나 마음껏 할수 있다는 이야기. 
human_resources.items = [Human("human{:2d}".format(i)) for i in range(0, 5)]

env.process( task_generator(env, human_resources) )
env.run(until=20)
```

- 실행 결과 

```
  3.00: available humans count: 5
  3.00: task queue count: 0
  3.00: task 0 required skills: {'skill 0', 'skill 1'}
  6.00: available humans count: 5
  6.00: task queue count: 1
  6.00: task 1 required skills: {'skill 0'}
  9.00: available humans count: 5
  9.00: task queue count: 2
  9.00: task 2 required skills: {'skill 0', 'skill 2'}
 12.00: available humans count: 5
 12.00: task queue count: 3
 12.00: task 3 required skills: {'skill 1', 'skill 2'}
 12.00: human 4 start to handle task 3
 15.00: available humans count: 4
 15.00: task queue count: 3
 15.00: task 4 required skills: {'skill 0', 'skill 2'}
 18.00: available humans count: 4
 18.00: task queue count: 4
 18.00: task 5 required skills: {'skill 1'}
 18.00: human 0 start to handle task 5
```


## wrap-up

- `simpy.FilterStore(env)`를 이용하면, 프로세스를 정의하고, 리소스를 정의한 다음 시뮬레이션 돌릴 때 유용하게 사용할 수 있을 것 같음. 최소한 벤치마크기준으로라도 잘 사용할 수 있을 것 같은데. 
