---
title: shallow copy and deep copy in python
category: python-basic
tags: python python-lib copy shallow-copy deep-copy 
---

## 깊게 복사했나요 얕게 복사했나요

- 파이썬에서 가장 많이 쓰이는 컨테이너는 당연히 `[]`와 `{}`입니다. 리스트와 딕셔너리죠. 자주 쓰이는 만큼, 사실 아무렇게나 쓰이는 것일지 몰라요. 
- 제 이름은 '이승훈'입니다. 또 제 아이디는 'frhyme'이죠. 이승훈도 frhyme도 모두 저를 가르키는 말입니다. 이건 shallow copy에요. 이 둘이 가리키는 객체가 서로 다르지 않거든요. 이름만 다를 뿐입니다. 
- 반대로, 누군가, '이승훈'이 가리키는 대상을 그대로 복사해서 미국에 '이승훈1'을 만들었다고 합시다. 이때 원래 이승훈을 바뀌었다고 해서 이승훈1이 바뀌지는 않아요. 이런 경우를 deep copy라고 합니다. 

## type in python 

- 우선 하나 정리해봅시다. 

> everything is object in python

- 파이썬에서는 모든 것이 객체입니다. 심지어 Number(integer, float-point), string까지 모두 객체입니다. 

```python
for x in [1, 1.0, "sdd"]:
    print(f"{x}, Type: {type(x)},  id: {id(x)}, Is instance of object?? {isinstance(x, object)}")
```

```plaintext
1, Type: <class 'int'>,  id: 4422870368, Is instance of object?? True
1.0, Type: <class 'float'>,  id: 4470792984, Is instance of object?? True
sdd, Type: <class 'str'>,  id: 4470763624, Is instance of object?? True
```

- **'python에서는 모든 것이 객체다'**라는 말을 다시 곱씹어봅시다. 객체는 보통 여러 기본형(primitive data type)을 참고하여 만드는 혼합형 데이터죠. 여러 데이터를 복잡하게 참고하고 있기 때문에 대부분의 경우 메모리에 값을 저장하는 것이 아니라, 값이 저장된 메모리주소가 저장됩니다. 
- 이 말인 즉슨 `=`(assignment operator)를 사용해서 복사를 해주면, 값이 복사되는 것이 아니라, 메모리주소가 복사된다는 이야깁니다. 두 놈이 같은 실체를 가리키고 있는 상황(shallow copy)가 발생하기 쉽다는 것이죠. 
- 모든것이 객체인 파이썬에서는 오히려 default가 shallow copy라고 할 수 있습니다. [여기서는 value type과 reference type에 대한 개념을 잡고 가는 것이 필요할 수 있습니다](https://en.wikipedia.org/wiki/Value_type_and_reference_type).

## shallow copy and deep copy in python 

- 일반적으로 어떤 변수에 값을 넣을때 우리는 `=`(assignment operator)를 사용합니다. 이 operator는 container나 객체를 넣을 때는 기본적으로 항상 shallow copy를 지원한다고 보면 되요. 
- 다음 코드처럼 리스트에 대해서 `=`를 넣어주면 shallow copy, `.copy`로 넣어주면 deep copy가 됩니다. 딕셔너리로, 리스트도 모두 마찬가지에요. 
  - python의 built-in object들은 모두 기본적으로 `.copy`를 지원합니다.
  - 뿐만 아니라. `pandas`, `numpy`등 주요 라이브러리들도 `.copy`를 통해서 deep copy를 지원합니다.

```python
print("lst case:")
lst_a = [i for i in range(0, 10)]
lst_b = lst_a
print(f"shallow copy: {id(lst_a)}, {id(lst_b)}")## id가 같으므로 shallow copy
lst_b = lst_a.copy()
print(f"   deep copy: {id(lst_a)}, {id(lst_b)}")## .copy를 이용했으므로 deep copy
print("="*21)
print("dictionary case:")
dict_a = {i:chr(i) for i in range(0, 10)}
dict_b = dict_a
print(f"shallow copy: {id(dict_a)}, {id(dict_b)}")
dict_b = dict_a.copy()
print(f"   deep copy: {id(dict_a)}, {id(dict_b)}")
print("="*21)
```

```plaintext
lst case:
shallow copy: 4470666248, 4470666248
   deep copy: 4470666248, 4470013192
=====================
dictionary case:
shallow copy: 4470570368, 4470570368
   deep copy: 4470570368, 4470870952
=====================
```

## customized class deep copy

- 그렇다면, 제가 직접 만든, class에서는 어떻게 deep copy를 지원할 수 있을까요? 
- 기본적으로, 앞에서 다 한 이야기들이지만 `=` assignment operator를 사용하면, shallow copy가 됩니다. 
  - 클래스는 물론이고, 클래스의 attribute들인 객체들도 마찬가지죠. 

```python
class AA(object):
    def __init__(self, lst, dct):
        self.lst = lst
        self.dct = dct

lst1 = [i for i in range(0, 10)]
dct1 = {i:chr(i) for i in range(0, 10)}
a1 = AA(lst1, dct1)
a2 = a1
a3 = AA(lst1, dct1)
## a1과 a2가 같은 객체와 binding됨. 
print(id(a1), id(a2), id(a3))
## 또한, a1과 a3가 메모리 주소가 달라서 다를 것으로 알기 쉽지만, 내부 변수의 메모리 주소는 같음 
## 즉, shallow copy된 것 
print(id(a1.lst), id(a2.lst), id(a3.lst))
```

```plaintext
4470976864 4470976864 4470976920
4470748424 4470748424 4470748424
```

### create method 'copy'

- 내부에 copy method를 만들어줍니다. 저는 python에서 기본적으로 모든 Object에 대해서 deepcopy method를 만들고 이를 기본 object에 포함하여, 만약 python의 클래스가 `object`라는 클래스를 상속받는다면 모든 경우에 대해서 deep copy method를 사용할 수 있도록 해줄 수 있을 것 같은데요. 왜 포함되어 있지 않은지 잘 모르겠습니다. 흠. 

```python
## 자 이제 어떻게 deep copy할까? 
## 1) 내부에 copy method를 만들어주자. 

class AA(object):
    def __init__(self, lst, dct):
        self.lst = lst
        self.dct = dct
    def copy(self):
        ## 모든 attribute에 대해서 copy해줘야 함
        return AA(self.lst.copy(), 
                  self.dct.copy())

a1 = AA(lst1, dct1)
a2 = a1.copy()
a3 = a1.copy()
print(id(a1), id(a2), id(a3))
print(id(a1.lst), id(a2.lst), id(a3.lst))
```

```plaintext
4470979160 4470979048 4470978320
4470748424 4470922440 4470968840
```

### with copy module

- 뭐, 이미 `copy` 라는 모듈이 있습니다. `copy.deepcopy()`를 사용하면 객체와 내부에 있는 모든 attribute들이 deep copy되기는 합니다. 

```python
import copy

class AA(object):
    def __init__(self, lst, dct):
        self.lst = lst
        self.dct = dct
    
a1 = AA(lst1, dct1)
## 그냥 아래처럼 copy.deepcopy를 사용하면 다 해결되긴 합니다. 
## shallow copy: copy.copy()
a2 = copy.deepcopy(a1)
a3 = copy.deepcopy(a2)
print(id(a1), id(a2), id(a3))
print(id(a1.lst), id(a2.lst), id(a3.lst))
```

```plaintext
4470978320 4470977312 4470977928
4470748424 4470067336 4470972296
```

### create copy method with copy module

- copy module의 deepcopy를 사용해서 해당 클래스의 상위 클래스에 `copy`를 새롭게 정의해줍시다. 상속받는 형태로 상위 클래스에 정의해줘서 다른 모든 클래스들이 다 copy를 사용할 수 있도록 해보죠. 

```python
import copy
import numpy as np 

class obj(object):
    ## 이렇게 basic class를 만들고 모두 상속받는 식으로 처리해도 좋습니다. 
    def copy1(self):
        ## __class__(): 마치 cls를 넘겨받는 것처럼 해당 클래스를 생성해줄 수 있습니다. 
        ## self__dict: 내부의 attribute과 각 값ㅇ 접근할 수 있습니다. 
        ## **dict: dictionary 앞에 **를 붙이면, key=value의 형태로 함수에 바로 넘겨줄 수 있습니다. 
        ## 하지만 이 경우에도 해당 class의 내부 attribute에 대해서는 deep copy가 안됩니다. 
        return self.__class__(**self.__dict__)

    def copy2(self):
        ## 이렇게 해당 딕셔너리의 각 v에 deepcopy를 해서 복제해줘도 됩니다. 
        return self.__class__(**{k: copy.deepcopy(v) for k, v in self.__dict__.items()})
        
    def copy3(self):
        ## 근데..그냥 copy module을 사용합시다. 
        return copy.deepcopy(self)
    
class AA(obj):
    def __init__(self, lst):
        self.lst = lst
lst = [1,2 , 3, 4, 5]
a1 = AA(lst)
a2 = a1.copy1()
print(id(a1), id(a2))
print(id(a1.lst), id(a2.lst))
print("="*21)
a2 = a1.copy2()
print(id(a1), id(a2))
print(id(a1.lst), id(a2.lst))
print("="*21)
a2 = a1.copy3()
print(id(a1), id(a2))
print(id(a1.lst), id(a2.lst))
print("="*21)
```

## wrap-up

- 막상, 다 만들고 나니 굳이 이렇게 할 필요가 있나, 라는 생각이 들기는 하네요. 
- 뭐, 그래도 다음과 같은 대략의 배움이 있는 것 같습니다. 
  - shallow copy와 deep copy를 늘 명확하게 인지하자. 
  - `self.__dir__`를 사용하면, 내부의 모든 attribute에 접근할 수 있음. 
  - `self.__cls__`는 마치 `cls`를 넘겨받는 classmethod에서처럼 class의 변수들에 접근할 수 있다. 또한 `self.__cls__()`는 해당 클래스의 `__init__`메소드를 실행시키는 것과 동일함. 

## reference

- [programiz - python programming - shallow deep copy](https://www.programiz.com/python-programming/shallow-deep-copy)
- [Wikipedia - value type and reference type](https://en.wikipedia.org/wiki/Value_type_and_reference_type)
- [Scaler Topics - Understanding Objects in Python](https://www.scaler.com/topics/python/what-is-object-in-python/)
