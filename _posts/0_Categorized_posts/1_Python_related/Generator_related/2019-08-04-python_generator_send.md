---
title: generator의 send 이용하기. 
category: python-basic
tags: python python-basic generator send yield 
---

## generator의 send 이해하기

- 아마도 이 글을 보시는 분들은 대충 generator가 무엇인지는 아실테고, 당연히 `yield`도 명확하게 이해하고 있을 것 같습니다. 
- 오늘은 `send`라는 저도 처음 보는 메소드를 설명할 것인데요. 

- 대충 아래와 같은 코드입니다. 
  - `x = yield`라는 이상한 코드가 있씁니다. 이건 사실 x에 대해서 일종의 placeholder를 박아두는 것이라고 보시면 됩니다. 원래 `yield`는 값을 넘겨주는 형식인데, 그렇지 않고, "언젠가 들어올 값을 미리 placeholder에 박아둠"이라고 생각하시면 됩니다.
  - `next(gen)`은 실제로 placeholder를 박아두는 것을 의미하고, 
  - `gen.send(x)`는 제너레이터로 값을 보내는 것을 의미하죠. 즉, 이 때, `gen.send(x)`를 통해 보내지는 값이, 함수의 내부로 들어가서 `x = yield`에서 값을 넘겨받는다고 보시면 됩니다.

```python
def generator_for_send():
    """
    - 외부로부터 값을 전달받아서, 그 값을 다시 출력함.
    """
    while True:
        # get_value는 일종의 placeholder
        get_value = yield  # exactly yield nothing
        print(f"value {get_value} get")
        yield get_value

gen = generator_for_send()
values = [1, 2, 3, 4]
for send_value in values:
    next(gen)
    gen.send(send_value)  # send_value를 보냄
```

- 아래에서 보시는 것처럼, 외부 main 함수에서 generator에 값을 전달해줄 수 있는 것이죠. 일종의 message 전달방식이라고 보시면 됩니다.

```plaintext
value 1 get
value 2 get
value 3 get
value 4 get
```

- 사실, 이것만으로는 크게 유의미한 배움이 없습니다만, 사실 이후에 좀 쓸모가 있다고 합니다. 
- generator는 결국, 일종의 쓰레드, 혹은 코루틴과 같은 개념으로 사용될 수 있는데, 그렇게 고려해보면 이건 결국 서로 다른 제너레이터간의 통신을 위한 수단인 것이죠. 즉, 여기서 yield는 원래대로라면 값을 전달하기 위해서 사용되었다면, 반대로 값을 다른 제너레이터로부터 전달받을수도 있는 것이니까요. 

## yield from 

- 필요에 따라서, generator내에서 새로운 generator를 불러야 할때가 있습니다. 
- 그럴때, 다음과 같이 사용하면 됩니다. 
- 중요한 것은 `yield`가 아니고, `return`도 아니고, `yield from`이라는 것이죠. 
- 여기서는 매우 간단한 형태로 만들어서 보여줬지만, 조금만 잘 만든다면, 우리가 흔히 말하는 recursion과 유사하게 만들어낼 수 있습니다. 

```python
def infinity(start):
    yield start
    yield from infinity(start + 1)

gen = infinity(0)
for i in range(0, 5):
    print(next(gen))
```

## reference

- [Stackoverflow - python generator “send” function purpose?](https://stackoverflow.com/questions/19302530/python-generator-send-function-purpose)
- [flowdas - 파이썬제너레이터](https://www.flowdas.com/blog/generators-in-python/index.html)
