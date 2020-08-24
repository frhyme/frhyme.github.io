---
title: np.random.choice???
category: python-libs
tags: python numpy random choice error
---

## intro 

- `np.random.choice`를 이용해서, 일정 확률을 이용해서 random하게 sampling할 때가 있습니다. 
- 코드로 표현하면 다음처럼 되겠죠. 

```python
for i in range(0, 3):
    a = np.random.choice(['b', 'c'], 10, [0.9, 0.1])
    print(a)
```

- 어, 근데 결과가 이상합니다. c가 터무니 없이 많이 나오네요. 

```
['c' 'b' 'c' 'c' 'b' 'c' 'b' 'b' 'c' 'b']
['c' 'b' 'b' 'b' 'b' 'b' 'c' 'b' 'c' 'b']
['c' 'b' 'b' 'c' 'c' 'c' 'b' 'c' 'b' 'c']
```

- [공식 문서를 보면 다음과 같이 되어 있습니다](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.choice.html#numpy.random.choice). 

```python
numpy.random.choice(a, size=None, replace=True, p=None)¶
```

- 세번째 오는 값은 p가 아니라, `replace`인 것이죠. 따라서 문제가 발생합니다. 
- 따라서, 다음으로 고치면 잘 됩니다. 

```python
for i in range(0, 3):
    a = np.random.choice(['b', 'c'], 10, p=[0.9, 0.1])
    print(a)
```

```
['b' 'b' 'c' 'b' 'b' 'b' 'b' 'b' 'b' 'b']
['b' 'b' 'b' 'b' 'b' 'b' 'b' 'b' 'b' 'b']
['b' 'b' 'b' 'b' 'b' 'c' 'b' 'b' 'b' 'b']
```

## wrap-up

- 사실 아주 사소한 것이기는 합니다만, 이걸 하나 실수하면 좀 큰 문제가 발생히기 쉬워요. 
- 보통 이정도의 함수는 테스트 없이 그냥 집어넣으니까요, 
- 가능하면 argument를 넘길 때, var_name이랑 함께 넘겨주는 편이 훨씬 좋은 것 같습니다. 

