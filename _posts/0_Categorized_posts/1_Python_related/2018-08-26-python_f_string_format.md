---
title: PEP498 - Literal String Interpolation
category: python-basic
tags: python python-basic string format PEP timeit 
---

## f-string in python

- python3.6에서 [PEP498](https://www.python.org/dev/peps/pep-0498/)이 추가되었습니다. 간단히 말하면 스트링 포매팅에 새로운 방법이 하나 추가되었습니다. 
- 기존의 방식은 원래 다음과 같았죠. 저는 첫번째 방식보다는 두번째 방식을 주로 썼습니다. 첫번째가 old way라고 했던 것 같아요. 

```python
print('%s' %"string1") #string formating1
print("{:^>20s}".format("string2"))#string format2
```

```plaintext
string1
^^^^^^^^^^^^^string2
```

- 아무튼 새로 추가된 방식, PEP498에 의하면 **literal string interpolation**, 해석하면 <원문에 충실한 문자열 삽입> 정도일까요? 는 다음과 같이 씁니다. 
    - 포매팅하려는 스트링 앞에 `f`를 써주고, `{}`안에 변수 이름을 그대로 써줍니다. 
    - 추가하려는 포맷이 있다면 변수 이름 뒤에 `:`과 함께 써주구요. 

```python
a = 'string3'
print(f'{a:^>40s}')
```

```
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^string3
```

- 저는 `.format`의 방식이 좀 더 손에 익기는 했는데, 아무튼 저렇게도 된다고 합니다. 

## is it better??

- 이게 뭐가 좋은가요? 라는 생각이 들 수 있을 것 같아요. 저도 왜 굳이 바꾸어야 하나? 라는 생각이 처음에는 들었죠. 
- 그런데, 파이썬으로 코딩할때 여러분도 비슷하지만, width를 효과적으로 쓰고 싶다는 생각을 할때가 많지 않나요? 쓸데없이 길어지는 일을 줄이고 싶을때가 있죠. 
- 예를 들어서 딕셔너리의 값들을 프린트로 출력하고 싶을 때 다음처럼 코드가 길어지는 경우가 있습니다. 내용은 같은데 약간 쓸데없이 늘어났죠. 

```python
dict1 = {'name':'LSH', 'age':33, 'gender':'male'}
print("name: {}, age: {}, gender: {}".format(dict1['name'], dict1['age'], dict1['gender']))
print(f"name: {dict1['name']}, age: {dict1['age']}, gender: {dict1['gender']}")
```

```
name: LSH, age: 33, gender: male
name: LSH, age: 33, gender: male
```

- 물론 starred expression을 쓰면 더 짧아질 수도 있습니다만...

```python
dict1 = {'name':'LSH', 'age':33, 'gender':'male'}
print("name: {}, age: {}, gender: {}".format(dict1['name'], dict1['age'], dict1['gender']))
print("name: {name}, age: {age}, gender: {gender}".format(**dict1))
print(f"name: {dict1['name']}, age: {dict1['age']}, gender: {dict1['gender']}")
print("name: {name}, age: {age}, gender: {gender}".format(**dict1))
print("name: {}, age: {}, gender: {}".format(*dict1.values()))
```

```
name: LSH, age: 33, gender: male
name: LSH, age: 33, gender: male
name: LSH, age: 33, gender: male
name: LSH, age: 33, gender: male
```

- 에....아무튼 목적은 스트링 포매팅을 할 때 변수가 들어가는 자리에 변수이름과 `{}`를 함께 넣도록 하자 가 목적이 아닌가 싶으요....

## is it faster??

- 그럼 최소한 빠르기는 한지 테스트를 해봅니다. 
- 빠르기는 빠릅니다. 최소 2배에서 2.5배까지 빠르네요. 

```python
import timeit

str_included = """dict1 = {'name':'LSH', 'age':33, 'gender':'male'}\n"""

test_lst = [
    """"name: {}, age: {}, gender: {}".format(dict1['name'], dict1['age'], dict1['gender'])
    """, 
    """"name: {name}, age: {age}, gender: {gender}".format(**dict1)
    """, 
    """f"name: {dict1['name']}, age: {dict1['age']}, gender: {dict1['gender']}"
    """, 
    """"name: {name}, age: {age}, gender: {gender}".format(**dict1)
    """, 
    """"name: {}, age: {}, gender: {}".format(*dict1.values())
    """
]
number = 1000000
for i, t in enumerate(test_lst):
    print(f"code {i:2d}: {t.strip()}")
    print(f"==> {timeit.timeit(str_included + t, number=number)}")
    print("="*30)
```

```
code  0: "name: {}, age: {}, gender: {}".format(dict1['name'], dict1['age'], dict1['gender'])
==> 0.850996766006574
==============================
code  1: "name: {name}, age: {age}, gender: {gender}".format(**dict1)
==> 1.0743701289757155
==============================
code  2: f"name: {dict1['name']}, age: {dict1['age']}, gender: {dict1['gender']}"
==> 0.47520723997149616
==============================
code  3: "name: {name}, age: {age}, gender: {gender}".format(**dict1)
==> 1.004713925998658
==============================
code  4: "name: {}, age: {}, gender: {}".format(*dict1.values())
==> 0.9585023220279254
==============================
```


- 아래가 제일 빠르고 

```python
f"name: {dict1['name']}, age: {dict1['age']}, gender: {dict1['gender']}"
```

- 두번째로는 얘가 빠릅니다. 

```python
"name: {}, age: {}, gender: {}".format(dict1['name'], dict1['age'], dict1['gender'])
```


## wrap-up

- 아직은 `.format`으로 하는게 더 익숙하기는 한데, 뭐 적응될 날이 있겠죠. 
- 앞으로는 가능하면 f-string을 써보려고 합니다. 