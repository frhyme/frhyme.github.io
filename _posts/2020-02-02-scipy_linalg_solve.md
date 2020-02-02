---
title: scipy - Solve a linear matrix equation
category: python-libs
tags: python python-libs networkx centrality eigenvector linear-algebra
---

## 간단한 선형 방정식 풀기. 

- 간단한 선형방정식(`ax = b`)을 풉니다. 단, a는 diagonal matrix(rectangular matrix)여야 하죠. 
- `np.linalg.solve(A, b)`를 사용해야 하죠.

```python
import numpy as np 

A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
# 
x = np.linalg.solve(A, b)
print("== constraints")
for A_coef, b_coef in zip(A, b):
    LHS = " + ".join([f"{a}x{i+1}" for i, a in enumerate(A_coef)])
    RHS = b_coef
    print(f"{LHS} = {RHS}")
print("== solution")
for i in range(0, len(x)):
    print(f"x{i+1} = {x[i]}")
```

```
== constraints
3x1 + 1x2 = 9
1x1 + 2x2 = 8
== solution
x1 = 2.0
x2 = 3.0
```