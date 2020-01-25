---
title: boolean을 잘 다뤄야 pandas도 잘 쓸 수 있숩니돠
category: python-lib
tags: python python-lib pandas boolean logic

---

## boolean vector 다루기 

- pandas를 쓸때는 boolean vector를 많이 다루게 됩니다. 예를 들어서, 특정 칼럼 Age를 20대 이상으로 필터링하고 싶다면, `df[df['Age']> 20]]`로 표현을 합니다. 여기서 `df['Age']>20`은 boolean vector가 됩니다. 
- 하나의 조건에 대해서 이렇게 필터링하는 경우가 아니라, 여러 복합적인 경우일 때, 이럴때는 and, or, not 등의 오퍼레이터도 쓰게 되죠. 그래서 간단하게 무엇무엇들이 파이썬에 있는지 정리를 해보았습니다. 

## 사실, 매우 쉽습니다. 

- `~` or `np.logical_not`: T-> F, F->T operator
- `&` or `np.logical_and`: and 
- `|` or `np.logical_or`: or
- `np.logical_xor`: exclusive or
- `np.any()`: 2개 이상에 대해서 or operator를 연속으로 적용해주는 것 
    - `np.any(, axis=0)`: 첫번째 축 원소에 대해서 적용함. 예를 들어, shape(10, 2)인 경우, 결과는 (2,)로 변화된다. 
    - `np.any(, axis=1)`: 두번째 축 원소에 대해서 적용함. 예를 들어, shape(10, 2)인 경우, 결과는 (10,)로 변화된다. 
- `np.all()`: 2개 이상에 대해서 and operator를 연속으로 적용해주는 것 

```python
"""
2개의 어레이에 대해서 해주는 경우 
"""
bool_lst = np.array([False, False, False, False, False, False, True, True, True, True])
r_bool_lst = ~np.array([False, False, False, False, False, False, True, True, True, True])
print(r_bool_lst) # tilde operator를 사용하여, T->F, F->T 로 변환해줌 
print("---")
print(np.logical_and(bool_lst, r_bool_lst))
print(np.logical_or(bool_lst, r_bool_lst))
print(np.logical_xor(bool_lst, r_bool_lst))
print('---')
"""2차원의 어레이에서 모든 칼럼에 대해서 한꺼번에 적용하고 싶을 때, 
"""
df = pd.DataFrame({"booLst":bool_lst, 'r_boolLst':r_bool_lst, 'T':True, 'F':False})
print(type(df.values))
print(df.values)
print("---")
"""함수 를 해당 cell의 
"""
print("shape: {}".format(df.values.shape))
print("---")
print("axis 0: column을 하나의 원소로 보고 함수를 적용함, 다르게 표현하자면, shape가 (10, 4)이므로 첫번째 shape 길이의 원소에 대해서 적용")
print(np.any(df, axis=0)) 

print("---")
print("axis 1: row를 하나의 원소로 보고 함수를 적용함, 다르게 표현하자면, shape가 (10, 4)이므로 두번째 shape 길이의 원소에 대해서 적용")
print(np.any(df, axis=1))
```

```
[ True  True  True  True  True  True False False False False]
---
[False False False False False False False False False False]
[ True  True  True  True  True  True  True  True  True  True]
[ True  True  True  True  True  True  True  True  True  True]
---
<class 'numpy.ndarray'>
[[False  True False  True]
 [False  True False  True]
 [False  True False  True]
 [False  True False  True]
 [False  True False  True]
 [False  True False  True]
 [False  True  True False]
 [False  True  True False]
 [False  True  True False]
 [False  True  True False]]
---
shape: (10, 4)
---
axis 0: column을 하나의 원소로 보고 함수를 적용함, 다르게 표현하자면, shape가 (10, 4)이므로 첫번째 shape 길이의 원소에 대해서 적용
[False  True  True  True]
---
axis 1: row를 하나의 원소로 보고 함수를 적용함, 다르게 표현하자면, shape가 (10, 4)이므로 두번째 shape 길이의 원소에 대해서 적용
[ True  True  True  True  True  True  True  True  True  True]
```

## reference 

- <http://joergdietrich.github.io/python-numpy-bool-types.html>