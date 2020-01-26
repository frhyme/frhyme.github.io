---
title: python - static type checking - mypy more.
category: python
tags: python static-type type-checking mypy python-libs typing
---

## intro.

- 이전의 post에서, `mypy`를 사용하여 비교적 간단한 static type checking을 하는 짓을 해봤습니다. 
- 이 post에서는 `mypy`에 대한 개괄적이 설명과, 무엇을 더 할 수 있는지에 대해서 알아보겠습니다.

## What is mypy?

- `mypy`는 python3를 위한 static type check입니다. 즉, 변수들의 타입들에 맞게 코드가 진행되는지, run-time(코드 실행) 전에 확인해준다는 이야기죠. 
- 다만, 이를 위해서는 아래와 같이, type-annotation의 형태로 각 변수들의 type이 선언되어 있어야 합니다.

```python
def func1(param1: int) -> int:
    return param1+1
```

- 설치는 아래와 같이 해줍니다. 

```
pip install mypy
```

## basic usage

- 앞서 말한것과 같이, 다음과 같은 코드를 만들었다고 합시다. 

```python
def func1(param1: int) -> int:
    return param1+1
# int가 들어가야 하는 자리에 string이 들어감. 
# 하지만, python으로 실행하면 아무 문제가 없음. 
func1("sss") 
```

- static type checking을 해줍시다. 그러면 다음과 같이 어디가 잘못되었는지를 알려주죠.

```
mypy test.py
```
```
aaaaa.py:5: error: Argument 1 to "func1" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
```

## usage more type: with `typing` module

- 기본적으로는 int, float, str, list, dict, tuple 와 같은 type을 모두 인지합니다.
- 하지만, 그 외로, `list of int`와 같이 좀 더 복잡한 type들을 지정할 수는 없을까요? 물론, 당연히 됩니다. 다만 이를 위해서는 `typing`이라는 모듈이 필요하죠. 

- 다음과 같이 `List[str]`이라는 type을 받아들이고 `None`을 리턴(즉, 아무것도 리턴하지 않는)하는 함수를 만들고, `mypy test.py`를 실행해봅시다. 

```python
from typing import List
# List 대신, Iterable을 사용할 수도 있습니다 
# Iterable[str]

def print_elements_in_lst(input_lst: List[str]) -> None:
    for x in input_lst:
        print(x)
    return 0

print_elements_in_lst([1, 2, "3"])
```

```
test.py:26: error: Argument 2 to "greeting" has incompatible type "float"; expected "int"
test.py:34: error: No return value expected
test.py:36: error: List item 0 has incompatible type "int"; expected "str"
test.py:36: error: List item 1 has incompatible type "int"; expected "str"
Found 4 errors in 1 file (checked 1 source file)
```


## wrap-up

- 저는 앞으로, type-hinting을 가급적 쓸 계획입니다. 코드의 가독성이 훨씬 높아지는 것 같아요.


## reference

- <https://mypy.readthedocs.io/en/stable/introduction.html>