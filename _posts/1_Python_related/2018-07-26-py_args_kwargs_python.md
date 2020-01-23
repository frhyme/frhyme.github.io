---
title: astericks, args, kwargs in python
category: python-basic
tags: python python-lib args kwargs dictionary tuple decorator
---

## args, kwargs 를 정리해봅시다. 

- 사실 decorator를 쓸 때가 아니면, 아직까지는 반드시 `args`, `kwargs`가 반드시 필요하다고 느낀 적이 없기는 한데, 다른 라이브러리들을 보다보면, `args`, `kwargs` 를 사용하는 일들이 좀 있어요.
- 그래서 이참에 좀 다시 정리해보기로 했습니다. 

- 간단하게 `a`, `b`를 argument로 받아서 합을 계산해주는 함수를 만들었습니다. 
    - 두번째 함수 콜에서는 에러가 발생합니다. 사실 당연하죠. argument의 수가 더 많으니까요. 

```python
def func1(a, b):
    return a+b

print(func1(1, 2)) ## 실행됨 
print(func1(1, 2, 3)) ## argument의 수가 많으므로 실행이 안됨 
```

```
3
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-625-1a02d7b5e7f9> in <module>()
      3 
      4 print(func1(1, 2))
----> 5 print(func1(1, 2,3))

TypeError: func1() takes 2 positional arguments but 3 were given
```

## args: variable-length argument list

- variable-length argument, 한국말로 하면 "가변적 인자 수"라고 표현할 수 있을까요?
- 함수 인자를 미리 정해두지 않고, 들어오는 수에 맞춰서 함수를 돌릴 수 있도록 해봅니다. 
    - 물론 그냥 `list`를 넘기면 되는거 아니냐? 라고 묻는다면 네...사실 그렇죠. 

- 하지만, 자주 쓰는 `print`함수를 생각해봅시다. 아래처럼 여러 개를 한번에 넘겨도 알아서 잘 실행됩니다. `print` 함수가 이렇게 argument의 수가 가변적이라는 것을 알 수 있습니다. 

```python
print("dd")
print("dd", 1, 2)
```

```
dd
dd 1 2
```

- 아래처럼 `*args`로 함수인자를 정의하면, 몇 개가 들어오든 상관없습니다.
    - 그리고 사용할 때는 `args`로 사용하면 되는데 얘는 `tuple`이에요.
    - 또한 혹시나 해서 말하자면, 들어오는 변수의 타입이 같을 필요도 없습니다. 

```python
## 함수 선언부에는 *args 로 써주고 
## 값을 사용할 때는 args 로 사용합니다. 
def func1(*args):
    print(type(args))
    print(sum(args))
    print("="*20)

func1(1, 2)
func1(1, 2, 3)
func1(1, 2, 3, 4)
```

```
<class 'tuple'>
3
====================
<class 'tuple'>
6
====================
<class 'tuple'>
10
====================
```

## kwargs: keyworded, variable-length argument dictionary

- `args`의 경우는 `tuple`로 제공됩니다. 즉 integer indexing을 해야 한다는 이야기인데요.
- integer indexing보다 keyword로 indexing하고 싶을 경우에는 `kwargs`를 사용하면 됩니다. 
- 단 이 아이는 별이 두 개! 붙어야 합니다. 

![별이 다섯개!!](https://pds.joins.com/news/component/newsis/201603/18/NISI20160318_0011479386_web.jpg)

- 아래 보시는 것처럼 알아서 잘 해석해서 넘겨줍니다 하하핫

```python
def func2(**kwargs):
    print(type(kwargs))
    for k in kwargs.keys():
        print("{}: {}".format(k, kwargs[k]))
    print("="*20)

func2(name='Lee', age='25')
func2(name='Kim', age='25', gpa=4.3)
```

```
<class 'dict'>
name: Lee
age: 25
====================
<class 'dict'>
name: Kim
age: 25
gpa: 4.3
====================
```

## hybrid

- 둘 중에 하나만 써야 하는 것이 아니고, 다음처럼 함께 쓸 수 있습니다. 
- 단.
    - `func_hybrid(**kwargs, *args)`와 같은 식으로 순서를 바꿔서 함수를 정의하면 안되고 
    - `func_hybrid(1,2,3, name='Lee', 4)`처럼 `args`, `kwargs` 가 섞여 있는 형태로 함수를 콜하면 안됩니다. 

```python
## hybrid
def func_hybrid(*args, **kwargs):
    print("args")
    for i, v in enumerate(args):
        print("{}: {}".format(i, v))
    print("-"*20)
    for k, v in kwargs.items():
        print("{}: {}".format(k, v))
    print("="*20)

func_hybrid(1,2,3, lambda x:x+10, name='Lee', age=25, gpa=4.3, f = lambda x: x+1)
```

```
args
0: 1
1: 2
2: 3
3: <function <lambda> at 0x11c3ba598>
--------------------
name: Lee
age: 25
gpa: 4.3
f: <function <lambda> at 0x11c3ba7b8>
====================
```

## naming

- 꼭 `args`, `kwargs`로 써야 하는 것은 아닙니다. 
- 이름은 달라도, 별이 하나 인지 두개 인지에 따라서 알아서 `args`, `kwargs`로 인식하게 됩니다. 

```python
## 이름이 똑같지 않아도 됩니다. 
def func_different_name(*input_tuple, **input_dict):
    for i, v in enumerate(input_tuple):
        print("{:2d}: {}".format(i, v))
    print("=== args over ===")
    for k, v in input_dict.items():
        print("{}: {}".format(k, v))
    print("=== kwargs over ===")
func_different_name(1,2,3, name='lee', age=35)
```

```
 0: 1
 1: 2
 2: 3
=== args over ===
name: lee
age: 35
=== kwargs over ===
```

## 별이 붙은 것, 붙지 않은 것 

- 별이 붙은 것을 출력하는 경우와, 별이 붙지 않은 것을 출력하는 경우가 다릅니다. 
- 아래를 보시면 
    - 별 없이 출력하는 경우: 튜플을 출력
    - 별과 함께 출력하는 경우: 연속된 argument를 그대로 출력

```python
def func4(*args):
    print(args)## tuple로 변화된 값을 출력 
    print(*args)## 연속된 값을 그대로 출력 함 
func4(1,2,3)
```

```
(1, 2, 3)
1 2 3
```

- print가 아니라 이를 함수에 넘긴다고 생각하면, 
    - 별이 없는 경우는 단 하나의 argument가 tuple로 넘어가는 것이고
    - 별이 있는 경우는 여러 개의 argument가 넘어가는 형태입니다.

```python
def func4(*args):
    def print_func(*args):
        for i, v in enumerate(args):
            print("{}: {}".format(i, v))
        print("#"*20)
    ## 아래의 경우 단 하나의 argument가 넘어가는 것이고 
    print_func(args)
    ## 아래의 경우는 여러 개의 argument가 넘어오는 것 
    print_func(*args)
func4(1,2,3)
```

```
0: (1, 2, 3)
####################
0: 1
1: 2
2: 3
####################
```


## wrap-up

- decorator를 쓸 때는 이 구분이 유의미할 것 같은데, 음....반드시 알아야 하는것인가? 잘 모르겠습니다 허허헛


## reference

- <https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3>
- <https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters>