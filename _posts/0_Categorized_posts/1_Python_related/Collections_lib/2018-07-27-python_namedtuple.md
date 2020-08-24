---
title: collections - namedtuple
category: python-lib
tags: python python-lib collections namedtuple tuple dictionary class 
---

## dictionary 보다 인덱싱이 편한 그것

- 솔직히 `dictionary`가 매우 유용한 자료구조이기는 한데, 매우 불편한 것이 값을 indexing할 때죠. 
- 매번 `dict1['name']`과 같이 인덱싱해야 하는데, 이거 너무 귀찮아요. 따옴표 치는 것만 없어도 생산성이 죽 올라간다고!!
- 물론 class를 만들어서 사용할 수도 있습니다만, 이 또한 조금 귀찮아요...
- 미묘하게 조금 쳐야될 게 많고, 또 출력까지 잘 되도록 해주려면 `__repr__`로 정의해주어야 합니다...귀찮...

```python
class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
p1 = Person('lee', 25, 'male')
print(p1)
```

- 출력도 이상해.....

```plaintext
<__main__.Person object at 0x13d6e7ac8>
```

## 그런 여러분을 위해쒀!! namedtuple이 있습니돠

- 아주 쉽습니다!! 매우 간단한 객체를 만든다고 생각히시면 되요. 
- tuple인데, 이름이 붙어있는 tuple이고, 인덱싱은 object처럼 `.###`으로 하면 됩니다. 

```python
from collections import namedtuple
## typename은 만들어진 객체의 타입을 말합니다.
## filed_names는 내부 attribute를 말합니다. 
## 그냥 아래처럼 ',' 이나 ' ' 로 구분해주면 알아서 다른 놈으로 인식합니다. 
## verbose를 True로 세팅하면, 어떤 클래스가 만들어졌는지를 출력합니다. 
Person = namedtuple(typename='Person', field_names='name, age gender', verbose=False)

p1 = Person('lee', 25, 'male')
p2 = Person('lim', 22, 'female')

## 따로 __repr__ 를 정의해주지 않았는데 다음처럼 잘 출력해주고 
print(p1)
## 내부 attribute에 인덱싱하는 것도 dictionary에 비하면 참 쉽고 
print(p1.name)
## 딕셔너리로 변환하는 것도 쉽죠. 
print(p1._asdict())
```

```plaintext
Person(name='lee', age=25, gender='male')
lee
OrderedDict([('name', 'lee'), ('age', 25), ('gender', 'male')])
```

## dictionary to named_tuple

- 그래도 아직 용번 자체는 `dictionary`가 편하기 때문에, 일단 `dictionary`를 만들고 이를 `namedtuple`로 변환하는 방법은 없는지? 알아보도록 합니다 하하핫. 

```python
dict1 = {'name':'lee', 
         'age':25, 
         'gender':'female'
        }
## 그냥 type_name만 정해주고, dictionary를 그대로 넘겨주니까 알아서 잘 되네요 하하핳
Person_by_dict = namedtuple('Person', dict1)
p11 = Person_by_dict('lee', 25, 'male')
print(p11)
```

```plaintext
Person(name='lee', age=25, gender='male')
```

## wrap-up

- 아직까지는 `dictionary`가 편하긴 한데, `namedtuple` 은 .으로 접근이 가능해서 압도적으로 편하긴 하네요. 슬슬 넘어가야 할 것 같아여 하하핫 

## reference 

- [stackoverflow - What are “named tuples” in Python?](https://stackoverflow.com/questions/2970608/what-are-named-tuples-in-python)
