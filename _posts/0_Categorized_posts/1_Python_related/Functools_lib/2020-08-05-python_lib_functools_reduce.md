---
title: python-lib) functools - reduce
category: python-lib
tags: python python-lib functools functional-programming iterator
---

## functools.reduce

- `functools.reduce`는 원래 python2에는 built-in으로 있었으나, 지금은 없어진 함수입니다. 
- 동작하는 방식이 약간 특이한데, 만약 우리에게 `[A, B, C]`라는 리스트가 있다면, A와 B에 대해서 특정 연산을 해주고, 그 결과를 다시 C와 해주고, 이런 식으로 연쇄적으로 처리해주는 함수죠. 다음 그림을 보면 대충 어떤 식으로 돌아가는지 알 수 있습니다.

![python_reduce](https://i.stack.imgur.com/OCsJC.png)

- 예를 들어 만약 우리에게 다음과 같이 원소가 리스트인 리스트를 가지고 있다고 하게습니다. 만약, 이 때 모든 원소들을 더해주고 싶다면, `functools.reduce`를 사용해서 처리해줄 수 있습니다.
  - 물론, 엄밀히 따지면 이 경우에는 `itertools.chain.from_iterable`를 사용하는 것이 훨씬 빠릅니다. 그 이유는 [stackoverflow - why functools reduce and itertools chain from itertools had different ~](https://stackoverflow.com/questions/49148342/why-functools-reduce-and-itertools-chain-from-itertools-had-different-comput)에서 확인하는 것이 더 좋구요.

```python
from functools import reduce

lst_of_lst = [[1, 2, 3], [5, 4, 6], [8, 4, 9]]

print(reduce(lambda x, y: x + y, lst_of_lst)) 
print(reduce(list.__add__, lst_of_lst))  # same but more robust code
```

```plaintext
[1, 2, 3, 5, 4, 6, 8, 4, 9]
[1, 2, 3, 5, 4, 6, 8, 4, 9]
```
