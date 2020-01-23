---
title: LP and QP 풀기 
category: optimization 
tags: python optimization python-lib scipy LP QP
---

## LP and QP 

- 다시 최적화시간이 생각납니다 하하핫. LP는 Linear Programming의 약자인데, **간단히 말하면 연립방정식의 해를 찾는 것**라고 해도 아무 문제가 없습니다. 
- LP의 기본적인 형태는 대략 다음과 같습니다. 목적식이 있고, 이 목적식을 만족하는 equality constraint가 있고, 모든 x는 0보다 커야 합니다. 
```
min Wx
Ax = b
x >= 0 
```
- 여기서, x가 정수인 경우에는 Integer programming이 되고, 섞여 있으면 MIP가 됩니다. LP에 비해서 IP는 굉장히 복잡해집니다. 그냥 반올림하면 되는거 아니야? 네 아니에요. 

## solve LP 

- documentation을 보면, 아래처럼 되어 있습니다. `c`, `A_ub`, `b_ub`, `A_eq`, `b_eq` 모두 함수에 넘겨주는 parameter입니다. 각각 upper_bound, equality 죠. 

```
Minimize:     c^T * x

Subject to:   A_ub * x <= b_ub
              A_eq * x == b_eq
```

- 뭐, 간단하게, 그림을 그려주기도 했는데, 별 의미는 없는 것 같아서, 그냥 지웠습니다. 각각 argument에 값을 잘 넘겨주고, `linprog`를 실행하면, 다음처럼 결과가 잘 나옵니다. 끗. 

```python
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import linprog

W =  np.array([-4, -3])
A_eq = np.array([[1, 1],[2, 1],[3, 4]])
b_eq = np.array([2, 4, 6])

A_ub = np.array([[1, 1],[2, 1],[3, 4]])
b_ub = np.array([2, 4, 6])

result = linprog(W, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub= b_ub)
print(result)
```

```
    fun: -8.0
 message: 'Optimization terminated successfully.'
     nit: 2
   slack: array([ 0.,  0.,  0.])
  status: 0
 success: True
       x: array([ 2.,  0.])
```

## wrap-up

- 간단하군요 하하핫. 
- LP 문제의 경우는 위처럼 풀면 되지만, 경우에 따라서, Quadratic Programming(제곱이 있는 경우)을 풀어야 할때는 전에 한 것처럼 `optimize.minimize`를 사용하는 게 제일 좋은 것 같습니다. 


## reference 

- <https://datascienceschool.net/view-notebook/0fca28c71c13460fb7168ee2adb9a8be/>
- <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html>