---
title: python에서 python 코드 바꿔서 다시 읽기
category: python-lib
tags: python python-lib import importlib 
---

## self-modifying code

- [self-modifying code](https://en.wikipedia.org/wiki/Self-modifying_code)라는 개념이 프로그래밍에 있습니다. 
- 간단히 요약하면, 프로그램 중에 프로그램 소스 코드를 바꿔서 프로그램을 변경하는 것을 말하는 것이죠. 
- 예를 들어 기존에 `function A`가 정의되어 있었는데, 이미 정의된 이 코드를 다른 코드로 바꿔서 넘겨버리는 것을 말합니다. 이런쪽을 파고 들어가다보면 lisp와의 관련성, meta-programming 등의 개념이 막 나오기 시작합니다. 저는 julia를 보다가 meta-programming에서 이 부분을 캐치하고 좀 더 파고들어간 케이스에 속합니다. 

## from source file 

- 일단 python 파일을 만듭니다. 그냥 파일을 만들고 스트링으로 코드를 넘겨줍니다. 

```python
f = open("test_lib.py", 'w')
target_str = """
import datetime as dt 
print("function imported at {}".format(dt.datetime.now()))
def test_func(a):
    return a+3
"""
f.write(target_str.strip())
f.close()
```

- 그다음에 해당 파일을 `import` 합니다. 잘 되는 것을 알 수 있네요. 

```python
importlib.import_module('test_lib')
func = test_lib.test_func
print(func(10))
```

```
function imported at 2018-08-29 17:58:42.474089
13
```

- 이제 소스 코드를 바꿔봅니다. 

```python
f = open("test_lib.py", 'w')
target_str = """
import datetime as dt 
print("function imported at {}".format(dt.datetime.now()))
def test_func(a):
    return a**3
"""
f.write(target_str.strip())
f.close()
```

- 그리고 module을 reload하고 실행합니다. 변경되서 실행되는 것을 알 수 있습니다. 

```python
importlib.reload(importlib.import_module('test_lib'))
func = test_lib.test_func
print(func(10))
```

```
function imported at 2018-08-29 18:00:09.729242
1000
```

## from buffer 

- python에는 `exec`라는 명령어가 있습니다. 소스 코드를 그대로 넘기면 알아서 실행해줍니다. 

```python
exec("""
print(12345)
print("ddd")
""")
```

```
12345
ddd
```

- 이걸 이용하면 다음처럼 진행할 수 있습니다. 상황에 따라서 하나의 펑션을 다른 코드로 정의해서 사용할 수 있습니다. 

```python
context_dict = {
    "context_a": """
    def func_a():
        print("hello")
    """, 
    "context_b":"""
    def func_a():
        print("hi")
    """
}
context_dict = {k: context_dict[k].strip() for k in context_dict.keys()}
exec(context_dict['context_a']) 
func_a()
exec(context_dict['context_b']) 
func_a()
```

```
hello
hi
```

## wrap-up

- 사실 이름은 self-modifying code라고 해놓고, 스트링을 그냥 실행했는데, 스트링을 변경하면 코드를 변경해서 실행할 수 있습니다. 
- 이게 의미가 있는 짓인지는 사실 잘 모르겠습니다만, 경우에 따라서 파이썬 함수 자체를 변경해야할 필요성이 있습니다. 그때 상황에 맞춰서 새로운 펑션을 정의하고 이 펑션을 넘겨주는 것이 의미가 있지 않을까? 라는 생각은 합니다. 


## reference

- <https://stackoverflow.com/questions/14191900/pythonimport-module-from-memory>