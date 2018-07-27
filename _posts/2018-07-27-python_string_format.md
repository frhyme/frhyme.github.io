---
title: python에서 출력시에 format 에 따라 다르게 출력하기 
category: python-basic
tags: python python-basic string format print dictionary 
---

## intro 

- python에서 변수들을 출력할 때 다양한 형태로 출력하는 방법을 배워봅니다. 

## older formatting

- 과거 python버전에서는 `%`을 이용해서 다음과 같은 형태로 출력했습니다. 다만, [PEP3101](https://www.python.org/dev/peps/pep-3101/#id7)에 의하면, 이는 이후에 없어질 가능성이 있다고 합니다. 참고하시고 가능하면 
다음에 설명할 부분으로 사용하시는 것이 좋을 것 같습니다. 

```python
print("%s, %s" % ('lee', 'seunghoon'))
```

## new formatting without variable_name

- `{}`로 변수의 자리를 만들어두고 
- `:`를 기준으로 오른쪽에 
    - 왼쪽정렬: `<`
    - 오른쪽 정렬: `>`
    - decimal point: `8.2`
- 등을 작성하여 넘깁니다. 

```python
## with format 

import numpy as np 

num = np.random.exponential(10)
print(num)
print("num: {}".format(num))
## 전체 자리수=8, 소수점은 2자리까지만 반올림하여 
print("num: {:8.2f}".format(num))
## 왼쪽 정렬 및 빈 공간 0으로 채우기 
print("num: {:0<8.2f}".format(num))
## 오른쪽 정렬 및 빈 공간 0으로 채우기 
print("num: {:0>8.2f}".format(num))
## 오른쪽 정렬 및 빈 공간 *로 채우기 
print("num: {:*>8.2f}".format(num))
print("="*20)
s = "Lee Seunghoon"
print(s)
## 스트링도 마찬가지, 정렬 값 넣고, 빈 공간 무엇으로 채울지 결정 
print("{:|>30s}".format(s))
print("{:|<30s}".format(s))
```

```
22.521519975341967
num: 22.521519975341967
num:    22.52
num: 22.52000
num: 00022.52
num: ***22.52
====================
Lee Seunghoon
|||||||||||||||||Lee Seunghoon
Lee Seunghoon|||||||||||||||||
```

## new formatting with variable_name

- 다음처럼 `{}`에 변수의 이름을 명시해서 넘길 수도 있습니다. 

```python
## 변수의 형태로 넘길수도 있음. 
formated_s = "{name}, {age:3.2f}".format(name='lee', age=25)
print(formated_s)
```

```
lee, 25.00
```

- 다음처럼 dictionary를 그대로 넘길 수도 있구요. 

```python
## format string with a dictionary 
dict1 = {'name':'lee', 'age':25}
print("{name}, {age:3.2f}".format(**dict1))
```

```
lee, 25.00
```

## reference 

- <https://mkaz.blog/code/python-string-format-cookbook/>