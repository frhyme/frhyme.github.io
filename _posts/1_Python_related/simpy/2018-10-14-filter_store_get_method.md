---
title: simpy의 FilterStore get, set 잘 이해하기 
category: python-libs
tags: python simpy filterstore python-libs simulation 
---

## intro

- 다들 simulation을 무엇을 이용해서 하시는지 모르겠네요. 물론 잘하는 사람은 excel만 가지고도 잘 할 수 있습니다. 물론 그럴 필요가 있나? 싶기는 합니다만. 
- 저는 `simpy`를 이용해서 시뮬레이션을 돌립니다. 물론 제가 하는 시뮬레이션이 대부분 현실 세계를 매우 간단하게 모델링하는 방법들이고, 다라서 그냥 `simpy`의 resource만 가지고도 꽤 비슷하게 할 수 있기 때문이겠죠. 
- 또한, 시뮬레이션을 돌리는 모델이 상황에 따라서 달라질 수 있기 때문에, 모델을 계속 변경해주는 작업이 필요합니다. ARENA나 AuthoMod등에서 이를 자동으로 하는 건 좀 성가시죠(되긴 될겁니다만).

## 아무튼 간에. 

- 원하는 resoure를 선택하기 위해서 저는 `simpy.FilterStore`를 사용합니다. 
- 그냥 `get` 메소드를 사용하면 적합한 리소스 하나가 리턴되고, 해당 리소스가 일을 다 끝내면 리소스 하나를 더 `put`메소드로 리턴하면 끝나는 일이기는 합니다. 
- 그런데, 만약 여러 개의 리소스가 모두 가능한 상태라면 어떤 resource가 리턴되는 걸까요? 

## do it

- 아주 간단한 코드를 만들었습니다. 
- 연속으로 `simpy.FilterStore(env)`에서 리소스를 get and put 합니다. 
- 그 get을 할때 항상 제일 앞에 있는 놈만 나오면 맨 뒤의 놈은 영영 쓰이지 않을 수도 있는 거니까요.

```python
import simpy 

env = simpy.Environment()

human_resources = simpy.FilterStore(env)
human_resources.items = ['s1', 's2', 's3', 's4']

def test_process():
    """
    - 그냥 resource를 주기적으로 get and put 
    """
    for i in range(0, 5):
        selected_r = yield human_resources.get(lambda x: True if 's' in x else False)
        print(selected_r)
        human_resources.put(selected_r)
        print(human_resources.items)
        print("==="*10)
env.process(test_process())
env.run()
```

- 결과를 보면, 일종의 round-robin 방식으로 진행됩니다. 이미 쓰인 적 있는 놈은 대기열의 맨 뒤로 돌아가서 가장 나중에 돌아오게 되겠죠. 이렇게 사용하면 리소스간이 나름 평균적으로 업무가 분배될 것 같습니다. 

```
s1
['s2', 's3', 's4', 's1']
==============================
s2
['s3', 's4', 's1', 's2']
==============================
s3
['s4', 's1', 's2', 's3']
==============================
s4
['s1', 's2', 's3', 's4']
==============================
s1
['s2', 's3', 's4', 's1']
==============================
```

## resource selection with randomness

- 뭐 round-robin 방식이 아니더라도 random하게 처리할 수도 있습니다. 
- 다음처럼 `human_resource.items`에 shuffle을 먹이면 알아서 잘됩니다. 

```python
import simpy 
import numpy as np 

np.random.seed(40)

env = simpy.Environment()

human_resources = simpy.FilterStore(env)
human_resources.items = ['s1', 's2', 's3', 's4']

def test_process():
    """
    - 그냥 resource를 주기적으로 get and put 
    """
    for i in range(0, 5):
        selected_r = yield human_resources.get(lambda x: True if 's' in x else False)
        print(selected_r)
        human_resources.put(selected_r)
        np.random.shuffle(human_resources.items)
        print(human_resources.items)
        print("==="*10)
env.process(test_process())
env.run()
```

## wrap-up

- 늘 느끼지만, 남이 만든 라이브러리들은 너무 좋아요. 그냥 쓰면 됩니다 낄낄낄. 