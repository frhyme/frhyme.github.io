---
title: simpy로 event 이용하기 - 영화관 모델링하기 
category: python-lib
tags: python python-lib simpy numpy simulation event example
---

## intro 

- 영화관에서 티켓을 파는 프로세스를 모델링하려고 합니다. 이전에 모델링한 예시들과 차이점이 있다면, 이 예시에서는 shared event를 이용합니다. 
- 즉, 간단하게 이벤트를 일종의 전역변수로 두고, 이벤트가 succeed가 되면 다른 프로세스에서 참고하여 사용할 수 있습니다. 

## basic example 

- 아래처럼 `shared_event`를 관리하는 프로세스를 만들어줍니다. 
- 일정 확률로 `shared_event.succeed()`가 수행되면, 해당 이벤트를 참고하는 다른 프로세스에서 일종의 인터럽션 개념으로 현재 하고 있는 작업을 중지하고, 다음 단계로 넘어갈 수 있습니다. 
- 즉, 여러 프로세스에서 동시에 참고하는 이벤트를 만들어야 한다면, 다음처럼 세팅해주는 것이 좋을 것 같습니다. 
    - 다만 `succeed`말고도 다른 메소드 들도 여러 가지가 있는 것 같아서, 이를 파악하면 좀 더 좋을 것 같기는 하네요. 

```python
env = simpy.Environment()
## 전역 이벤트 변수 선언
shared_event = env.event()

def global_process(env, shared_event):
    ## 1초에 한번씩 global event가 발생할 것인지 파악함
    while True: 
        yield env.timeout(1)
        if np.random.randint(0, 50)==1:
            ## 이벤트가 성공했음을 표시함 
            shared_event.succeed()
            break

def simple_process(env, shared_event):
    while True:
        ## 다른 프로세스에서 shared_event.succeed()가 실행되면
        ## env.timeout(10.0)이 아직 끝나지 않았더라도, 이 부분이 종료되고 다음으로 넘어감 
        result = yield env.timeout(10.0) | shared_event
        if shared_event in result:
            print("shared event occurs at {}".format(env.now))
            break
        print("shared event didn't occurs during {}".format(env.now))

np.random.seed(21)

env = simpy.Environment()
shared_event = env.event()

env.process(simple_process(env, shared_event))
env.process(global_process(env, shared_event))

env.run(until=100)
```

```
shared event didn't occurs during 10.0
shared event didn't occurs during 20.0
shared event didn't occurs during 30.0
shared event didn't occurs during 40.0
shared event didn't occurs during 50.0
shared event didn't occurs during 60.0
shared event didn't occurs during 70.0
shared event didn't occurs during 80.0
shared event didn't occurs during 90.0
shared event occurs at 91
```

## better example: movie renege 

- simpy documentation에 있는 예제인 [movie renege](http://simpy.readthedocs.io/en/latest/examples/movie_renege.html)를 참고하여 작성하였습니다. 

```python
import simpy 
import numpy as np 

def movie_goer(env, movie, num_tickets, theater):
    ## 영화보러 온 사람 프로세스 
    ## 카운터에 리소스를 요청하고 기다리는 중에 
    ## sold_out이라는 전역 이벤트가 발생하면 renege, 
    ## 그렇찌 않을때는 다른 프로세스를 따름. 
    with theater['counter'].request() as req:
        ## sold_out은 env.event(), 만약 다른 프로세스에서 succeed를 처리하면 아래에서 먼저 실행됨 
        sold_out = theater['sold_out'][movie]
        result = yield req | sold_out
        if sold_out in result:
            ## 티켓이 다 팔렸음.
            theater['num_renegers'][movie]+=1
            ## 프로세스 종료 
            env.exit()
        elif req in result:
            if num_tickets > theater['available'][movie]:
                ## 티켓이 있는데 부족할 경우에는 그냥 감 
                print("{:7.1f}: we don't have enough tickets".format(env.now))
                yield env.timeout(0.5)
                env.exit()
            else:
                theater['available'][movie] -= num_tickets
                if theater['available'][movie] < 1:
                    ## 아래 보면 이벤트를 succeed로 변경함. 
                    ## 따라서 만약 다른 프로세스에서 yield req | theater['sold_out'][movie] 등으로 참고하고 있을 경우 
                    ## 아래 부분이 수행되는 즉시, yield 구문을 빠져오게 됨. 
                    theater['sold_out'][movie].succeed()
                    theater['when_sold_out'][movie] = env.now
                    theater['available'][movie] = 0
                    print('{} is sold out'.format(movie))
                yield env.timeout(1)
    
def customer_arrivals(env, theater):
    ## exponential time마다 사람이 도착함 
    ## 영화, 사람 수 등을 랜덤하게 고르고, 티켓이 남아있을 경우 이를 프로세스로 env에 넘겨줌
    while True:
        yield env.timeout(np.random.exponential(2))
        movie = np.random.choice(theater['movies'])
        num_tickets = np.random.randint(1, 6)
        ## 티켓이 남아지 않으면 새로운 사람이 프로세스로 넘어가지 않는다. 
        if theater['available'][movie]!=0:
            print("{:7.1f}: {} customer arrived to see {}".format(env.now, num_tickets, movie))
            env.process(movie_goer(env, movie, num_tickets, theater))

np.random.seed(42)
env = simpy.Environment()

print("Movie renege")
## 이전에는 모두 class, process등으로 처리했는데 여기서는 딕셔너리로 데이터를 관리함. 
## 딕셔너리에 Resource, event 등이 포함되어 있음. 
## 경우에 따라 클래스로 만들지 않고, 아래처럼 딕셔너리로 관리하는 것이 편할 수도 있음. 
movies = ['Die hard 2', "Kill bill", 'Resevoir Dogs']
theater = {
    'counter' : simpy.Resource(env, capacity=1),
    'movies' : movies, 
    'available' : {movie: 20 for movie in movies}, 
    'sold_out' : {movie: env.event() for movie in movies}, 
    'when_sold_out' : {movie: None for movie in movies}, 
    'num_renegers' : {movie: 0 for movie in movies}
}

env.process(customer_arrivals(env, theater))
env.run(until=100)
```

- 로그는 다음처럼 생성됩니다. 

```
Movie renege
    0.9: 3 customer arrived to see Die hard 2
    4.0: 2 customer arrived to see Die hard 2
    4.3: 3 customer arrived to see Resevoir Dogs
    8.3: 5 customer arrived to see Resevoir Dogs
   15.3: 2 customer arrived to see Kill bill
   15.7: 1 customer arrived to see Die hard 2
   16.5: 5 customer arrived to see Kill bill
   17.6: 3 customer arrived to see Die hard 2
   19.5: 4 customer arrived to see Kill bill
   26.8: 3 customer arrived to see Resevoir Dogs
   27.7: 3 customer arrived to see Die hard 2
   31.7: 5 customer arrived to see Resevoir Dogs
   32.9: 4 customer arrived to see Kill bill
   38.6: 2 customer arrived to see Kill bill
   39.5: 5 customer arrived to see Kill bill
   39.6: we don't have enough tickets
   40.1: 4 customer arrived to see Resevoir Dogs
Resevoir Dogs is sold out
   40.3: 3 customer arrived to see Die hard 2
   45.1: 4 customer arrived to see Kill bill
   45.1: we don't have enough tickets
   45.9: 2 customer arrived to see Kill bill
   47.5: 2 customer arrived to see Die hard 2
   50.5: 2 customer arrived to see Kill bill
   50.5: we don't have enough tickets
   55.0: 4 customer arrived to see Kill bill
   55.0: we don't have enough tickets
   55.1: 5 customer arrived to see Die hard 2
   55.5: we don't have enough tickets
   55.8: 2 customer arrived to see Die hard 2
   62.5: 1 customer arrived to see Die hard 2
Die hard 2 is sold out
   71.9: 1 customer arrived to see Kill bill
Kill bill is sold out
```

## wrap-up

- 여기서 배운 것은 `env.event`를 전역 변수로 설정하고, 특정한 조건을 만족했을때, `succeed()`를 전달하면, 해당 이벤트를 참고하고 있는 다른 프로세스들에게 모두 영향을 줄 수 있다는 것입니다. 
- 하나를 더 추가하자면, succeed를 한 다음, 다시 원래 상태로 돌아갈 수 있는지(예를 들어서 영화관의 경우 환불 취소 같은 상황)이 발생하면, 이를 어떻게 모델링할 수 있는가? 가 이후에 고민해야 할 부분이 아닐까 싶습니다. 