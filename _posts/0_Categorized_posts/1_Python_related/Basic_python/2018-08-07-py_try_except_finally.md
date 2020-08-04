---
title: try, except, finally
category: python-basic
tags: python python-basic try except exception-handling
---

## try, except, finally

- 파이썬으로 코딩할 때 코딩을 깔끔하게 해주는 것은 매우 중요합니다. 단 두 줄, 세 줄을 쓴다고 하더라도 개별 두줄이 어떤 의미를 가지는지 구분해서 작성해주면 가독성이 훨씬 높아집니다. 
- 특히, 코딩을 할때 많이 해주는 부분이 바로 `try`, `except`구문입니다. 이는, 일단 코드를 실행하고, 만약 그 내부에서 에러가 발생하면, 그 error를 던져주고, `except`문이 받아먹는 형식을 말합니다. 
- 간단하게 말하면 다음과 같은 형식이죠. 제 기억이 맞다면, java에서는 `raise error`를 해줬어야 했던 것 같은데, 파이썬에서는 알아서 던져줍니다. 

```python
try: 
    f = open("aaaa", 'r')
    # python에서는 자동으로 raise error를 해줌 
except FileNotFoundError as e:
    print(e)

```

- `FileNotFoundError`발생하는 에러이름은 실행한 뒤에 에러코드를 보면 알 수 있습니다. 
  - 아래를 보시면, 에러코드에 에러 코드명이 써있는데, 이 이름을 그대로 `except <errorcode> as e`와 같은 형태로 작성해주면 됩니다. 

```python
open("ddd", 'r') ## raise FileNotFoundError
```

```plaintext
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-46-bdbf46e9e441> in <module>()
----> 1 open("ddd", 'r') ## raise FileNotFoundError

FileNotFoundError: [Errno 2] No such file or directory: 'ddd'
```

## finally

- try, except는 알겠는데, finally는 무엇인가요?. 이는 try, except 구문이 종료되고 나면 항상 실행되는 구문을 말합니다. 
- 다음 두 코드는 서로 같습니다. 그래도, `finally`로 구분을 해주면, 코드를 읽기 전에, 직관적으로 "아 얘는 무조건 실행되는 부분이네" 라고 바로 알 수 있는 것 같아요. 그래서 약간의 가독성을 높여줍니다. 

```python
try:
    [1,2,3,4,5][np.random.randint(0, 9)] ## raise IndexError
    open("ddd", 'r') ## raise FileNotFoundError
    print('try 구문 실행됨')
except IndexError as e1:
    print("error: <{}> 발생했고, except 문 실행됨".format(e1))
finally:
    print('try, except구문 시행후 무조건 시행됨 ')
    print("="*30)
```

```python
try:
    [1,2,3,4,5][np.random.randint(0, 9)] ## raise IndexError
    open("ddd", 'r') ## raise FileNotFoundError
    print('try 구문 실행됨')
except IndexError as e1:
    print("error: <{}> 발생했고, except 문 실행됨".format(e1))
print('try, except구문 시행후 무조건 시행됨 ')
print("="*30)
```

- 아무튼, 그래서 다음처럼 exception handling을 할 수 있습니다. 
- 여러 가지의 exception을 구분해서 처리해주고, `try/except`와 관계없이 항상 수행되는 `finally`구문도 표시해줍니다. 

```python
import numpy as np 

for i in range(0, 5):
    try:
        ## 5칸 짜리 리스트에 리스트의 크기를 넘는 값으로 indexing하므로 
        ## IndexError가 에러가 발생할 수 있음 
        [1,2,3,4,5][np.random.randint(0, 9)] ## raise IndexError
        open("ddd", 'r') ## raise FileNotFoundError
        print('try 구문 실행됨')
    except IndexError as e1:
        print("error: <{}> 발생했고, except 문 실행됨".format(e1))
    except FileNotFoundError as e2:
        print("error: <{}> 발생했고, except 문 실행됨".format(e2))
    finally:
        print('try, except구문 시행후 무조건 시행됨 ')
        print("="*30)
```

```plaintext
error: <[Errno 2] No such file or directory: 'ddd'> 발생했고, except 문 실행됨
try, except구문 시행후 무조건 시행됨 
==============================
error: <[Errno 2] No such file or directory: 'ddd'> 발생했고, except 문 실행됨
try, except구문 시행후 무조건 시행됨 
==============================
error: <[Errno 2] No such file or directory: 'ddd'> 발생했고, except 문 실행됨
try, except구문 시행후 무조건 시행됨 
==============================
error: <list index out of range> 발생했고, except 문 실행됨
try, except구문 시행후 무조건 시행됨 
==============================
error: <[Errno 2] No such file or directory: 'ddd'> 발생했고, except 문 실행됨
try, except구문 시행후 무조건 시행됨 
==============================
```

## wrap-up

- 사소한 부분일 수 있지만, 코딩 협업을 위해서는 조금이라도 가독성을 높여주고, 이처럼 표준에 맞춰서 코드를 작성해주는 것이 매우 중요합니다. 
