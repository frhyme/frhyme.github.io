---
title: Python - generator/iterator - Merge.
category: python-basic
tags: python python-basic python-libs itertools
---

## Intro

- 코딩을 하다가, 대용량의 데이터를 가져올 때, 용량이 너무 커서 램에 한번에 올리기가 어려운 경우, generator/iterator를 사용하는 경우들이 있죠(엄밀히 따지면 generator와 iterator는 다르지만 이 글에서는 차이를 두지 않고 쓰기로 합니다).
- 다만, 그때 필요에 따라서 그 서로 다른 generator들을 합쳐서 하나의 generator로 만드는 것이 필요하죠.

## First failure: Can't be merged by `+`

- 리스트들은 합치고 싶을 때 그냥 `+`만으로도 충분하므로, 그냥 아래와 같이 해버리죠.

```python
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1+lst2 # 이렇게 더하면 [1,2,3,4,5,6]이 됩니다.
```

- 하지만 generator는 이렇게 더한다고 합쳐지지 않습니다.

```python
generator1 = (i for i in range(0, 10))
generator2 = (f"str{i}" for i in range(0, 10))

generator1+generator2
```

- 결과를 보면 다음과 같죠. 즉 `generator`간에 `+` 연산하는 것은 불가하다는 이야기죠. 사실, 뭐 이정도는 좀 만들어줘도 괜찮을 텐데요.

```bash
Traceback (most recent call last):
  File "iterator_merge.py", line 11, in <module>
    generator1+generator2
TypeError: unsupported operand type(s) for +: 'generator' and 'generator'
```

## Second failure: to list and merge

- 물론, 다음처럼 필요에 따라서 잠시 list로 만든 다음 이 아이를 합쳐줘도 되기는 합니다.
- 결과로 generator가 생성되기는 했지만, 그 과정에서 모든 generator를 list로 변환할 때 모든 원소를 한번 씩 읽게 됩니다.
- 즉, 나중에는 계산 비용이 적게 사용되는 것 같더라도, 이 과정에서 이미 낭비되는 것들이 있죠.

```python
generator1 = (i for i in range(0, 10))
generator2 = (f"str{i}" for i in range(0, 10))

new_gen = (x for x in (list(generator1) + list(generator2)))
```

## Best: `itertools.chain`

- `itertools`의 `.chain` 메소드를 사용해서 그냥 합쳐주면 끝납니다. 참 쉽죠.

```python
import itertools

generator1 = (i for i in range(0, 10))
generator2 = (f"str{i}" for i in range(0, 10))

for x in itertools.chain(generator1, generator2):
    print(x)
print("=="*30)
```

## reference

- [how to join two generators in python](https://stackoverflow.com/questions/3211041/how-to-join-two-generators-in-python)
