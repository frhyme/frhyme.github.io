---
title: python) callback은 무엇인가? 
category: python-lib
tags: python python-lib callback functional-programming
---

## callback 함수란 무엇인가? 

- callback 함수가 무엇인지 모르겠어서 정리해보기로 했습니다. 
- 여전히, higher-order function과의 차이점을 잘 모르겠는데 혹시 아시면 알려주시면 감사하겠습니다. 

### 한글 위키피디아

- 한글 위키피디아에서는 다음으로 정리되어 있습니다. 

> **프로그래밍에서 콜백(callback)은 다른 코드의 인수로서 넘겨주는 실행 가능한 코드**를 말한다. 콜백을 넘겨받는 코드는 이 콜백을 필요에 따라 즉시 실행할 수도 있고, 아니면 나중에 실행할 수도 있다.

- 다른 함수의 argument 로 넘어가는 실행가능한 code라는 말인데, 이거 그냥 functional-programming 에서 first-class function 이랑 뭔가 다른것인지 헷갈리네요. 
    - first-class function: 함수를 특정 변수에 저장할 수도 있고 다른 함수에 argument로 넘길 수도 있는, 함수형 프로그래밍의 핵심적인 조건

- 영문 위키피디아에서도 다르지 않습니다. 단, **call back** 이라는 말보다는, 인자로 넘어가는 시점보다 나중에(after) 수행된다는 의미로 **call-after**가 더 좋은 표현이라는 것처럼 말하기는 합니다. 

> In computer programming, a callback, also known as a "call-after[1]" function, is any executable code that is passed as an argument to other code, which is expected to call back (execute) the argument at a given time.

- 영문 위키피디아에서 python을 활용하여 언급한 예제는 다음과 같아요. 
- 예제를 통해서 보면, callback 함수는 다른 함수에게 일찍 불려서 데려가졌지만, 실제 수행은 나중에, 결정되는 것을 말하는 것 같아요. 
    - 전달받은 즉시 수행될 필요는 없다. 전달 받은 뒤에 전달받아진 함수에서 알아서 수행하면 된다. 

```python
def get_square(val):
    """ the callback """
    return val ** 2

def caller(func, val):
    return func(val)

caller(get_square, 5)
```

- 대부분의 포스트에서 callback 함수와 higher-order function의 개념이 구분되지 않고 사용됩니다. 이 두 개념이 같다고 생각해도 되는걸까요? 

## callback in js

- 검색해보면, [javascript에서 콜백함수를 사용해서 비동기식 처리를 동기화하여 처리하려고 할때 사용한다는 내용이 제일 많습니다](https://hyunseob.github.io/2015/08/09/async-javascript/).


## wrap-up

- higher-order function과 어떤 차이가 있는 것인지 아직 정확히는 모르겠어요. 분명히 뭔가 다른 포인트가 있는 것 같은데 아직은 좀 명확하지 못해요. 
- 함수가 호출되고(call), 그 함수가 종료된 다음에 다시 caller code의 그 시점으로 돌아오니까(back) call-back인 것인가 싶기도 합니다. 
- 그냥 일단은 call-back == higher order function 이라고 생각해도 상관없을 것 같습니다. 

## reference 

- <http://guslabview.tistory.com/214>
- <http://yubylab.tistory.com/entry/자바스크립트의-콜백함수-이해하기>