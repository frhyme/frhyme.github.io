---
title: Python - TypeError - Object of type 'int64' is not JSON serializable
category: python-libs
tags: python python-libs json numpy int64 TypeError
---

## Intro

- python으로 코딩을 하다가, `numpy`를 사용해서 뭘 좀 처리하고(보통은 ML 모델에 넘기죠), 이 결과를 json 파일로 저장하려고 할 때 다음과 같은 오류가 뜰 때가 있습니다. 
- 대충 "Type"이 문제고, int64의 변수 타입은 json으로 저장할 수 없다, 라는 말인 것이죠. 

```plaintext
TypeError: Object of type 'int64' is not JSON serializable
```

## What is PROBLEM?? 

- 이 문제는 다음 코드를 보면 좀 더 명확해지는데요.
- 아래 코드를 보면 그냥 list에 python 기본 변수 타입인 `int`를 집어넣었습니다. 이때, 각 원소의 변수 타입은 `int`입니다.

```python
import numpy as np 

integer_lst = [1, 2, 3]
print(integer_lst)
print(type(integer_lst[0]))
```

```plaintext
[1, 2, 3]
<class 'int'>
```

- 잠시 처리할 일이 있어서 이 아이를 `np.array()`로 변경해주기로 합니다. 
- 이렇게 변경되면, 각 원소의 변수 타입은 `<class 'numpy.int64'>`가 됩니다. 

```python
np_int_lst = np.array(integer_lst)
print(type(np_int_lst[0]))
```

```plaintext
<class 'numpy.int64'>
```

- 이제 다시, 처리하기 편하게 list로 변환을 합니다. 
- 그런데, 여기서 다시 list로 변환을 해도, 내부 원소는 여전히 `<class 'numpy.int64'>`로 존재합니다. 
- 이 상태에서 그대로 다음처럼 `json`을 이용해 변환할 경우, `json`은 `numpy.int64`를 이해하지 못하여 에러를 발생시키게 됩니다. 

```python
np_int_lst = list(np_int_lst)
print(type(np_int_lst[0]))

with open("temp.json", 'w') as f: 
    json.dump(list(np_int_lst), f)
```

```plaintext
<class 'numpy.int64'>
TypeError: Object of type 'int64' is not JSON serializable
```

- 따라서, 이 때는 내부 원소까지 모두 `int`형으로 변환한 다음 진행해야 하죠. 

```python
np_int_lst = list([int(x) for x in np_int_lst])
print(type(np_int_lst[0]))

with open("temp.json", 'w') as f: 
    json.dump(list(np_int_lst), f)
```

## reference

- [Python - TypeError: Object of type 'int64' is not JSON serializable](https://stackoverflow.com/questions/50916422/python-typeerror-object-of-type-int64-is-not-json-serializable/50916741)
