---
title: simpy에서 resource를 사용해봅시다. 
category: python-lib
tags: python python-lib simpy simulation resource
---

## intro 

> multiple processes want to use a resource of limited capacity. 

- 복수의 프로세스는 제한된 용량을 가진 리소스를 서로 사용하려고 합니다. 아주 많은 경우가 이에 포함되는데, 은행 창구, 주요소 등 을 이를 통해서 모델링할 수 있죠. 
- simpy에서는 세 가지 종류의 resource class를 제공합니다. 
    - resource
    - container
    - store

- 일단은 비교적 간단한 resource부터 시작을 해볼게요. 

## simpy.Resource

- 프로세스처럼 다음으로 정의해서 사용합니다. 한 번에 2명까지 처리할 수 있는 리소스를 정의했습니다. 

```python
import simpy 
resource1 = simpy.Resource(env, capacity=2)
```

- 너무 간단하기 때문에, 조금 복잡한 상황을 표현해보기로 했습니다. 
    - 도서관이 있고 거기에는 2개의 자리만 존재합니다 ==> capacity가 2인 resource를 만들어줍니다. 
    - 학생들이 랜덤하게 도착하고, 도착시에 자리가 없을 경우 그대로 기다린다 ==> student를 generator로 만들어서 process로 넘겨줌. 

- 일단 resource를 사용하는 부분은 두 가지로 표현할 수 있습니다. 

- 다음 구문의 경우는 `with` 내의 구문이 종료되면, 자동으로 resource가 release 됩니다.
    - 이 부분이 좀 더 공식? 혹은 표준적인 방법인 것 같아요. 

```python
with library.request() as req:
    yield req
## with 내의 구문이 종료되면 자동으로 resource release
```

- 다음처럼 사용할 때마다, request를 날리고, release를 해주는 식으로 표현할 수도 있습니다. 
    - logging을 위해서는 아래 표현이 좀 더 편한 것 같기는 합니다. 

```python
## 여기서 해당 resource에 대한 사용권을 얻고 
req = library.request() 
## 사용이 종료되면, 다음을 통해 resource의 사용권을 풀어줌 
library.release(req)
```


### simple code 

- 이를 아주 간단하게 표현하면 다음과 같습니다만, 필요한 log를 추가하여 그 다음 코드로 표현했습니다.

```python
import simpy 
import numpy as np 

def Student(env, num, library, arrive_time):
    ## student마다 도착하는 시간이 다르게 표현
    yield env.timeout(arrive_time)
    ## 아래와 같은 형태로 쓰면 자동으로 get, release가 된다.
    ## 단, 다른 형태로 쓸 경우에는 req = library.request(), library.release(req) 로 해주어야 함. 
    with library.request() as req:
        ## resource를 사용할 수 있을때까지 기다림, 즉시 사용가능하다면 이 부분은 거의 바로 넘어감
        yield req 
        ## 일정 시간 만큼 공부함
        study_time = np.random.triangular(left=5, right=10, mode=8)
        yield env.timeout(study_time)
        ## with as 구문으로 resource를 사용할 경우에는, 끝에 굳이 release를 추가하지 않아도 자동으로 release해줌
        
env = simpy.Environment()
## capacity가 2인 리소스를 선언
library = simpy.Resource(env, capacity=2)

for i in range(0, 5):
    arrive_time = np.random.triangular(left=1, right=8, mode=3)
    stu = Student(env, i, library, arrive_time)
    env.process(stu)

## 50초까지 표현했지만, 남아있는 process가 없을 경우에는 그냥 종료됨. 
env.run(until=50)
```

### better code 

```python
import simpy 
import numpy as np 

def Student(env, num, library, arrive_time):
    ## 학생은 랜덤 시간 이후 도착 
    yield env.timeout(arrive_time)
    print("student {} arrived library at {:6.2f}".format(num, env.now))
    waiting_time = env.now

    ## 아래와 같은 형태로 쓰면 자동으로 get, release가 된다.
    ## 단, 다른 형태로 쓸 경우에는 req = library.request(), library.release(req) 로 해주어야 함. 
    with library.request() as req:
        yield req ## resource를 사용이 가능하면 이 부분이 수행됨 
        waiting_time = env.now - waiting_time
        ## waiting_time이 0이 아닌 경우는 기다린 경우 
        if waiting_time !=0:
            print("student {} is waiting  during {:6.2f}".format(num, waiting_time))
        ## 얼마나 공부할지를 계산 
        study_time = np.random.triangular(left=5, right=10, mode=8)
        print("student {} start to  study at {:6.2f}".format(num, env.now))
        ## 학생이 공부를 시작했고 => 현재 도서관이 꽉 차 있을 경우 꽉 차있다는 것을 표현 
        if library.capacity == library.count:
            print("#### library full at  {:6.2f} ####".format(env.now))
        yield env.timeout(study_time)
        print("student {} end   to  study at {:6.2f}".format(num, env.now))
        print("#### library seat available at {:6.2f} ####".format(env.now))
        
env = simpy.Environment()
library = simpy.Resource(env, capacity=2)

for i in range(0, 5):
    arrive_time = np.random.triangular(left=1, right=8, mode=3)
    stu = Student(env, i, library, arrive_time)
    env.process(stu)

env.run(until=50)
```

- 이 결과는 대략 다음처럼 표현됩니다. 
- 로그를 잘 보시면, resource가 사용불가할 때, 가능할때 등이 자세하게 표현되는 것을 알 수 있습니다. 

```
student 3 arrived library at   2.38
student 3 start to  study at   2.38
student 4 arrived library at   2.77
student 4 start to  study at   2.77
#### library full at    2.77 ####
student 1 arrived library at   4.37
student 0 arrived library at   4.47
student 2 arrived library at   4.83
student 3 end   to  study at  10.73
#### library seat available at  10.73 ####
student 1 is waiting  during   6.36
student 1 start to  study at  10.73
#### library full at   10.73 ####
student 4 end   to  study at  10.87
#### library seat available at  10.87 ####
student 0 is waiting  during   6.40
student 0 start to  study at  10.87
#### library full at   10.87 ####
student 1 end   to  study at  16.08
#### library seat available at  16.08 ####
student 2 is waiting  during  11.25
student 2 start to  study at  16.08
#### library full at   16.08 ####
student 0 end   to  study at  18.80
#### library seat available at  18.80 ####
student 2 end   to  study at  24.33
#### library seat available at  24.33 ####
```

## wrap-up 

- 다만, 아쉬운 부분은 현재 리소스를 어떤 프로세스가 사용하고 있는지 파악하는 것이 조금 어려워요 
- 예를 들어서, `library.queue`나, `library.users`를 사용하면, 다음처럼 표현되는 것을 알 수 있어요. 이것만으로는 어떤 놈이 들어가 있는지를 정확하게 알기가 어렵죠(물론 외부에서 따로 리스트를 만들어서관리해주거나 하는 일도 가능합니다만, 좀 성가시니까요)

```
[<Request() object at 0x10fa1d908>, <Request() object at 0x10fa1da90>]
```

- 하지만 중요한 건, `request`가 아니라, 어떤 process가 사용하고 있는지를 아는 것이잖아요. 요 부분은 조금 다른 식으로 풀어야 하는 것 같아요. `Request()` object 밑에 다른 method가 따로 없어요. 흐으으음. 