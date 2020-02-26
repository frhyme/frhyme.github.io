---
title: scipy - matrix exponential
category: python-libs
tags: python python-libs numpy matrix exponential
---

## matrix exponential: scipy.linalg.expm(A)

- [matrix exponential](https://en.wikipedia.org/wiki/Matrix_exponential)은 square matrix에 exponential function을 적용하여 도출된 matrix를 말하며, 일반적으로 생각하는 `exp(x)`와 동일합니다. 다만, 적용하는 대상으 1차원의 수가 아니라, matrix라는 것이 다를 뿐이죠. 
- 아래의 간단한 코드를 보시면, 
    - 첫번째는 matrix에 대해서 exponential function을 적용했기 때문에 zero matrix에 대해서 적용했을 때, 정상적인 `identity matrix`가 나오지만, 
    - 두번째 코드의 경우는 `Identity matrix`가 나오지 않습니다. 

```python
A = np.zeros([2, 2])  # zero matrix
# applied matrix exponential function for matrix
assert np.all(
    scipy.linalg.expm(A) == np.identity(2)
)
# applied just exponential function for matrix
assert np.all(
    np.exp(A)== np.array([1, 1, 1, 1]).reshape(2, 2)
)

```

## Use `scipy.linalg.expm`

- `scipy.linalg.expm`를 다음과 같이 사용할 수 있습니다.


```python
import numpy as np
from scipy import linalg as sp_linalg
"""
- 1차원의 값들에 대해서는 np.exp()로 간단하게 exponential을 적용할 수 있다. 
- 그러나, 1차원이 아닌 matrix인 구조일 때는 np.exp()를 matrix의 각 element에 exponential을 처리한다고 해서, 
원하는 결과가 나오지 않는다.
- 이처럼 matrix에 대해서 exponential을 처리하기 위한 함수가 바로 `sp_linalg.expm`를 사용합니다. 
    - check1: 우선, `sp_linalg.expm(zero_matrix)== Identity matrix`를 확인 
    - check2: euler identity 의 matrix form에 적용. 
"""

N = 2
zero_mat = np.zeros([N, N])
print("== zero_mat")
print(zero_mat)
print("--"*20)
# 해당 matrix에 exponential 를 적용함.
# zero에 적용한 것이므로, exp(Zeros) = I 가 나오게 됨.
print("== sp_linalg.expm(zero_mat)")
print(sp_linalg.expm(zero_mat))
print("--" * 20)
# 반대로, 그대로 np.exp를 씌우면 모든 모든 원소가 1이므로, matrix에 맞는 function이 아님
print("== np.exp(zero_mat)")
print(np.exp(zero_mat))
print("--" * 20)

"""
Euler’s identity (exp(i*theta) = cos(theta) + i*sin(theta)) applied to a matrix:
"""
N = 2
X = np.random.normal(0, 1, N**2).reshape(N, N)

# `j` means imaginary parth
LHS = sp_linalg.expm(1j*X) # ij*X 에 exponential function 적용
RHS = sp_linalg.cosm(X) + 1j*sp_linalg.sinm(X)

print("== LHS")
print(LHS)
print("--" * 20)
print("== RHS")
print(RHS)
print("--" * 20)
```


```
== zero_mat
[[0. 0.]
 [0. 0.]]
----------------------------------------
== sp_linalg.expm(zero_mat)
[[1. 0.]
 [0. 1.]]
----------------------------------------
== np.exp(zero_mat)
[[1. 1.]
 [1. 1.]]
----------------------------------------
== LHS
[[-0.87798962+0.62059534j  0.6962854 -0.2663728j ]
 [-0.19544771+0.074771j    1.06801666-0.12387402j]]
----------------------------------------
== RHS
[[-0.87798962+0.62059534j  0.6962854 -0.2663728j ]
 [-0.19544771+0.074771j    1.06801666-0.12387402j]]
----------------------------------------
```


## wrap-up

- 다시 말하지만, 분명히 과거에 다 배웠던 내용일 겁니다. 사실 상식적으로만 생각해도, matrix에 적용할 때는 함수들이 다른 형태여야 한다는 것을 알고 있지만, 이제는 이런것도 다시 복기하는데 시간이 걸리네요. 


## reference

- [Matrix exponential](https://en.wikipedia.org/wiki/Matrix_exponential)
- [scipy.linalg.expm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.expm.html)