---
title: python - logger - logging wisely. 
category: python-libs
tags: python python-libs logger exception
---

## 1-line summary 

- 그냥 `print`를 쓰는 것도 좋지만, `logging`를 사용해서 프로그램의 진행상황을 효과적으로 파악하면 더 좋을 것 같아요.


## 왜 logger를 써야 할까? 

- 사실, 꼭 쓸 필요는 없습니다. 대다수의 경우 `print`로도 충분합니다만, 프로그램의 규모가 커짐에 따라서, command line에 저장하는 것이 복잡하게 느껴질 때가 있습니다. 

### print에서 개발 관련 정보를 분리하자. 

- 어떤 정보는 프로그램의 결과를 출력하는 것이므로 `print`가 맞는데, 어떤 정보는 개발자에게만 필요한 정보이므로 분리하는 것이 필요할 때가 있죠.
- 즉, 원래는 그냥 print라는 함수 안에 섞여 있던 정보를 "개발에 필요한 정보"와 "프로그램의 결과에 대한 정보"를 구분해서 "개발과 관련된 정보"를 다른 방식으로 남기자, 라는 것이 `logging`이라는 라이브러리를 써야하는 이유라고 할 수 있습니다. 
- "그냥 합쳐서 쓰면 안되냐?"라고 생각할 수도 있고 뭐 틀린 말은 아닙니다만, 우리 모두는 결국 더 좋은 프로그래머가 되고 싶은 것이잖아요. 따라서, 좋은 습관을 익혀두는 것이 필요합니다. 따라서, 여기서도 "개발에 대한 정보는 logging을 통해 따로 관리하자, 라는 습관을 일찍 들여두는 것이 좋죠. 

### 시간을 편하게 출력하자.

- 하나 더 추가하자면, 매번 "현새 프로그램이 어떻게 흘러가는지"를 알고 싶을 때, 그 시점에 "시간"도 정확하게 알고 싶을 때가 있습니다. 물론, 그냥 `datetime`과 같은 모듈을 쓰면 쉽게 해결되는 것이기는 한데요, print함수로 시간까지 남기는 걸 만들면, 그거 꽤나 귀찮아지거든요.
- 따라서, `logging` 모듈을 사용해서 맨 위에 세팅해두면, 코드가 꽤 간결해집니다.


## Basic Logging. 

- 사용 방법은 간단합니다. 

### `logging.basicConfig()`

- 우선, `logging.basicConfig()`을 사용해서, logging을 어떤 방식으로 처리할 것인지 설정합니다. 여기서는, 
    - `format`: "어떠한 형태로 로그를 출력할 것인지"
    - `filename`: "log들이 저장되는 파일의 이름은 무엇인지"
    - `filemode`: "write인지, append인지"
    - `level`: 어느 정도의 위험수준을 logging할 것인지 등을 정합니다. 
- 그 다음에는 그냥 `logging.debug('This is a debug message')`와 같은 형식으로 `print` 쓰듯이 쓰면 끝납니다.

### Simple Cdde

- 다음과 같은 간단한 코드를 만들어봤습니다. 조금 아쉬운 것은, 요즘의 python은 "string.format()"이나, "f-string"을 사용해서 string을 표현하는데, `logging`에서는 옛날 방식인 "%-string"을 사용하고 있습니다. 이 부분이 조금 아쉽네요.

```python
import logging 

"""
format: message를 어떤 식으로 표현할지 정의합니다. 
LogRecord attribute라고 하며, 기정의된 다음의 값들을 사용하여 정리해줍니다.
다만, python의 예전 string format을 사용한다는 것이 아쉬운 점.
%(var_name)-<length><type>
%(levelname)-10s
levelname이라는 변수를 10칸 짜리 string으로 출력함. 
----------------------------------
filename: logging되는 값들이 저장되는 파일 이름. 
----------------------------------
filemode: default 값은 'a', append입니다. 
만약, 이전의 실행 기록을 없애고 새롭게 시작하고 싶을 경우에는 'w'로 변경해주면 됩니다
----------------------------------
level: logging할 위험 수준을 말합니다. 
위험이 높은 순으로 critical > error > warning > info > debug 이다. 
만약 logging.error 로 설정하면, 아래의 warning, info, debug는 기록되지 않음.
"""

logging.basicConfig(
    format='%(asctime)s : %(levelname)-10s : %(message)s',
    filename="./log/example.log",
    filemode='w', 
    level=logging.DEBUG # 대문자 
)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

```

- 위의 코드를 실행한 다음, 저장된 파일을 읽어보면 다음과 같은 내용이 담겨 있습니다. 어떤가요? 저는 print보다 훨씬 쉽고 깔끔하게 코드의 실행 결과를 파악할 수 있다는 측면에서 훨씬 마음에 듭니다.

```
2020-03-08 20:47:08,858 : DEBUG      : This is a debug message
2020-03-08 20:47:08,858 : INFO       : This is an info message
2020-03-08 20:47:08,858 : WARNING    : This is a warning message
2020-03-08 20:47:08,858 : ERROR      : This is an error message
2020-03-08 20:47:08,858 : CRITICAL   : This is a critical message
```


## Logging with exception info. 

- 다음과 같이, 코드 실행 중에 발생한 exception에 대해서도 아래처럼 처리해줄 수 있습니다. 

```python
import logging 

logging.error("This is debug")
try:
    5/0
except Exception as e:
    logging.exception("Exception occurred", exc_info=True)
logging.debug("This is debug")
```

```
2020-03-08 20:55:24,826 : ERROR      : This is debug
2020-03-08 20:55:24,826 : ERROR      : Exception occurred
2020-03-08 20:55:24,827 : DEBUG      : This is debug
```


## wrap-up

- 좋은 개발자가 되려면, DEBUG, INFO, WARNING, ERROR, CRITICAL 과 같은 레벨에 대해서도 명확하게 알고 있어야겠죠. 혹은, 발생할 수 있는 예외가 무엇인지 미리 알고, 그 수준이 무엇인지를 정확하게 logging하는 것이 좋겠지만, 뭐 나중에 그렇게 할 수 있는 날이 오겠죠 호호호호호.


## reference

- [realpython - python logging](https://realpython.com/python-logging/)