---
title: asyncio - coroutine
category: python-lib
tags: python python-lib coroutine asyncio concurrency parallelism 
---

## concurrency vs. parallelism 

- 우선 늘 헷갈리는 정보부터 정리하고 가겠습니다. 예전에 안다고 생각했는데 뒤돌아서면 또 잊어버려요. 
- Concurrency(동시성)과 parallelism(병렬성)은 다른 개념입니다. 그림으로 이해하시는 게 더 편할 것 같은데, 아래 그림에서 병렬성의 경우는 실제로 서로 다른 두 가지 쓰레드가 동시에 돌아가는 것을 말합니다. 그에 반해서 동시성은, 실제로 동타임에 두 쓰레드가 동시에 구현되는 것이 아니고, 짧은 시간에 연속적으로 switch되면서 두 쓰레드가 동시에 실행되는 것처럼 보이는 것, 을 말합니다. 

![concurr vs. parellel](https://www.google.co.kr/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiGkYuz-4ndAhXZEXAKHWMxCOwQjRx6BAgBEAU&url=https%3A%2F%2Fbrianchan.us%2F2017%2F05%2F27%2Fconcurrency-vs-parallelism%2F&psig=AOvVaw2bKIxy18oDiyfGOaUbTzcY&ust=1535346964218575)

- 어쩌면 위 그림보다는 이 그림이 더 이해에 도움이 될 수도 있어요.
    - 대기열: 처리해야 하는 프로세스 
    - 벤딩 머신: CPU

![](https://www.google.co.kr/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjUo8qO_IndAhUOUN4KHTRJCzAQjRx6BAgBEAU&url=https%3A%2F%2Fmedium.com%2F%40deepshig%2Fconcurrency-vs-parallelism-4a99abe9efb8&psig=AOvVaw2bKIxy18oDiyfGOaUbTzcY&ust=1535346964218575)

- 즉 일반적으로 싱글코어인 컴퓨터에서 동시에 여러 개의 프로그램을 수행하고 있을때 보통은 이 것은 concurrency를 수행하고 있는 것이죠. 

## coroutine

- 간단하게 '함수'라는 개념부터 잡고 들어갑시다. '함수'는 보통 시작되는 지점이 하나 있고 보통 `return`이 수행되면 함수는 그대로 종료되죠. 함수 내 코드의 특정 지점으로 다시 들어갈 수 없습니다. 이러한 함수를 보통 sub-routine이라고 하기도 하죠. 
- 그에 반해 coroutine의 경우는 함수 실행 중에 밖으로 잠깐 나왔다가 다시 들어갈 수 있습니다. entry point가 여러 개라는 이야기죠. 즉, coroutine은 subroutine의 일반화된 형태라고 말할 수 있습니다. 

- 여기서 잠깐 [wikipedia의 정의](https://en.wikipedia.org/wiki/Coroutine#Comparison_with_subroutines)를 보면 다음과 같아요. 

> Coroutines are computer-program components that generalize subroutines for non-preemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations.

- subroutine의 일반화된 형태고, non-preemptive multitasking에 적합하고, 특정 지점에서 작업을 멈추고 다시 시작할 수 있는 다양한 entry-point를 허용하는 컴퓨터 프로그램 구성요소, 라고 한다고 하네요. 
    - non-preemptive scheduling: 비선점 스케쥴링이라고도 하며 현재 수행중인 프로세스가 자원을 할당받았을 경우 프로세스 내부에서 자원을 반납하기 전까지는 프로세스가 중단되지 않는 것
    - preemptive scheduling: 선점 스케쥴링이라고도 하며 현재 다른 프로세스가 이미 수행중이더라도, 우선순위가 높은 다른 프로세스가 들어왔을 경우 이미 수행중인 프로세스를 멈출 수 있는 스케쥴링

### generator??

- 이전에 파이썬으로 코딩할 때 generator를 사용해본 적이 있으신 분들은 generator와 coroution이 꽤 유사하다고 느낄 수 있습니다. 저도 꽤 유사한 부분이 많다고 느껴지는데 위키피디아에서는 차이점을 다음과 같이 말하고 있어요.

> they differ in coroutines' ability to control where execution continues immediately after they yield, while generators cannot, instead transferring control back to the generator's caller.

- 뭐 대부분 같은데, generator는 `yield`를 통해 중간에 빠져 나와도 바로 다른 coroutin이 자원을 할당받지 않는 반면, coroutine은 다른 코루틴이 suspend되면 바로 자원을 할당받는다. 이게 가장 큰 차이다, 뭐 그렇게 말하고 있네요. 


## coroutine and concurrency 

- 정리를 해보면, Concurrency의 경우 실제로는 자원이 1개고, 따라서 한번에 하나의 프로세스밖에 수행할 수 없지만, 프로세스를 빠르게 switching하여 마치 여러 프로세스를 동시에 수행하는 것이 가능한 것처럼 보이게 하는 것을 말합니다. 
- 그리고 이를 위해서는 하나의 프로세스가 멈추면, 자동으로 다른 프로세스에서 해당 남겨진 자원을 자동으로 획득하여 이용하는 것이 필요하죠. 
- 즉 여기서 제가 말한 프로세스 가 바로 **코루틴**을 말하는 것이 됩니다. 
- 파이썬에서 이 코루틴 부분을 지원해주는 라이브러리는 asyncio가 있죠. 

## asyncio

- 아마 pip install로 설치하지 않아도 될 거에요. 기본으로 깔려 잇는 것 같습니다. 
- 아무튼. 코드는 대략 다음과 같아요. 

- 간단하게 하나의 리스트를 반으로 나눠서 concurrent하게 양쪽에서 처리해줄 수 있도록 했습니다. 
    - 이벤트 루프를 만들고 
    - 이벤트 루프에 코루틴을 각각 등록하고 
    - 각각의 코루틴은 입력받은 리스트를 100개 처리하고, 1초씩 쉬는 식으로 진행됨 
        - 당연히 하나의 코루틴에서 1초를 쉬면, 다른 코루틴에서 자원을 자동으로 할당받음 

```python
import asyncio
from datetime import datetime

## async def 는 코루틴을 정의할 때 사용됨 
async def async_sum(cr_name, input_lst):
    r = 0 
    comp_unit = 100 ##100개를 더하고, 1초 쉼     
    for i in range(0, len(input_lst)//comp_unit+1):
        print("{} start at {}".format(cr_name, datetime.now()))
        r = r + sum(input_lst[i*comp_unit:(i+1)*comp_unit])
        print("{} stops at {}".format(cr_name, datetime.now()))
        await asyncio.sleep(0.1)
        ## 100개를 더하고 1초쉼, 1초 쉬면 다른 coroutin이 알아서 자원을 획득함 
    return r

target_lst = [i for i in range(0, 200)]
loop = asyncio.get_event_loop()
## 아래에서 두가지 코루틴을 각각 생성하고, 
tasks = [  
    asyncio.ensure_future( async_sum('A', target_lst[:len(target_lst)//2]) ), 
    asyncio.ensure_future( async_sum('B', target_lst[len(target_lst)//2:]) ),
]

# tasks[0].result() 로 결과값에 접근할 수 있음. 
## 이를 모두 이벤트 루프에 등록해줌
loop.run_until_complete(asyncio.wait(tasks))  
loop.close()
```

```
A start at 2018-08-26 14:59:50.108779
A stops at 2018-08-26 14:59:50.108918
B start at 2018-08-26 14:59:50.109040
B stops at 2018-08-26 14:59:50.109082
A start at 2018-08-26 14:59:50.209368
A stops at 2018-08-26 14:59:50.209514
B start at 2018-08-26 14:59:50.209649
B stops at 2018-08-26 14:59:50.209693
```

- 결과를 읽을 때는 다음처럼 읽습니다. 

```python
for i, t in enumerate(tasks):
    print("task{:2d}, result: {}".format(i, t.result()))
```

```
task 0, result: 4950
task 1, result: 14950
```

## wrap-up

- 조금 더 알고 싶으신 분은 pyconkr2018에서 발표한 [Deep Dive into Coroutine](https://www.slideshare.net/daykim7/pyconkr-2018-deep-dive-into-coroutine-110194978/1)를 참고하셔도 좋습니다. 
- 그래도 쭉 보고 나니까 이제는 어느 정도 이해가 되네요 하하핫